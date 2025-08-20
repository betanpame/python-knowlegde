# CI Integration for Progress Reports

This guide explains how to automate generation of the progress report, JSON summary, and Shields.io badges via GitHub Actions.

## 1. Files Generated

The script `scripts/generate_progress.py` produces:

- `doc/progressDD_MM_YYYY.md` – Markdown snapshot
- `doc/progressDD_MM_YYYY.json` – Machine‑readable summary
- `badges/resolved.json` – Shields endpoint for resolved progress
- `badges/validated.json` – Shields endpoint for validated progress

## 2. Badge Embedding (README example)

```markdown
![Validated](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/<USER>/<REPO>/main/badges/validated.json)
![Resolved](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/<USER>/<REPO>/main/badges/resolved.json)
```

Replace `<USER>` and `<REPO>` appropriately.

## 3. Example GitHub Actions Workflow

Create `.github/workflows/progress.yml`:

```yaml
name: Progress Snapshot

on:
  push:
    paths:
  - 'tests/**'
      - 'scripts/generate_progress.py'
  workflow_dispatch: {}
  schedule:
    - cron: '0 6 * * *'   # Daily at 06:00 UTC

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Generate progress artifacts
        run: |
          python scripts/generate_progress.py --smoke --export-csv

      - name: Commit & push if changed
        run: |
          git config user.name 'progress-bot'
          git config user.email 'progress-bot@users.noreply.github.com'
          if git diff --quiet; then
            echo 'No changes.'
          else
            git add doc/progress*.md doc/progress*.json badges/*.json
            git commit -m 'chore: automated progress snapshot'
            git push
          fi
```

## 4. Optional: Fail on Warnings

Add `--smoke` already triggers runtime checks. To fail the workflow if warnings are present, add a post step:

```yaml
      - name: Fail on heuristic warnings
        run: |
          python scripts/generate_progress.py --no-md --no-json --no-badges --smoke --stdout > /tmp/report.md
          if grep -q 'Heuristic Warnings' /tmp/report.md; then
            echo 'Heuristic warnings detected'; exit 1; fi
```

## 5. Local Pre-Commit Hook (Optional)

Create `.git/hooks/pre-commit` (Unix environments):

```bash
#!/usr/bin/env bash
python scripts/generate_progress.py --no-badges --stdout > /dev/null
if ! git diff --quiet doc/progress*.md; then
  git add doc/progress*.md doc/progress*.json
fi
```

Make executable:

```bash
chmod +x .git/hooks/pre-commit
```

## 6. Extending Heuristics

Add or refine heuristics inside `determine_file_status` or after smoke execution (e.g., detect cyclomatic complexity, enforce docstring presence, or run lightweight unit tests).

## 7. Troubleshooting

- Empty badge values? Ensure the script was run at least once in CI.
- UNCATEGORIZED status: Add a leading `# TODO:` / `# RESOLVED:` / `# VALIDATED:` line.
- High `low_implementation_loc`: Add meaningful logic lines (comments don’t count).

---

Automate early to keep momentum—manual status drift is the enemy of accuracy.

---

## 8. Script Usage Cheat Sheet

Core generation (markdown + json + badges):

```bash
python scripts/generate_progress.py
```

Include smoke runtime checks & CSV export:

```bash
python scripts/generate_progress.py --smoke --export-csv
```

Limit to a single topic (faster incremental iteration):

```bash
python scripts/generate_progress.py --only-topic String --stdout
```

List all topics:

```bash
python scripts/generate_progress.py --list-topics
```

Promote eligible TODO files to RESOLVED automatically (heuristic threshold 5 meaningful LOC):

```bash
python scripts/generate_progress.py --promote --promote-threshold 5
```

Skip history/delta creation (useful in quick local runs):

```bash
python scripts/generate_progress.py --no-history --no-badges --stdout
```

Generate a harness (function/class summary) for a topic:

```bash
python scripts/generate_progress.py --generate-harness String
```

Inspect cumulative resolved/validated list:

```bash
type doc/completed_all.md
```

View delta (newly completed this run) if present:

```bash
type doc/completed_delta_$(Get-Date -Format 'dd_MM_yyyy').md
```

---

## 9. Promotion Logic Summary

When `--promote` is used, a file with a leading `# TODO:` is upgraded to `# RESOLVED:` iff:

1. Meaningful (non-comment, non-blank) LOC ≥ threshold.
2. No lingering `TODO` occurrences beyond the header line.
3. No standalone `pass` statements remain.
4. At least one `def` or `class` is defined.

Upgrade is conservative by design to avoid false progress inflation.

---

## 10. CSV Columns

`progressDD_MM_YYYY.csv` includes:

| Column | Meaning |
|--------|---------|
| Topic | Topic name |
| Created | Count of created practice folders |
| PythonFiles | Count with at least one .py file |
| Resolved | Practices RESOLVED or VALIDATED |
| Validated | Practices VALIDATED only |
| Remaining | 20 - Created |
| Created% | % created out of 20 |
| PythonFile% | % with .py out of 20 |
| Resolved% | % resolved out of 20 |
| Validated% | % validated out of 20 |

---

Stay intentional: use delta files to direct daily focus; celebrate each VALIDATED increment.
