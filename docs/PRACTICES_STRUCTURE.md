<!-- COPILOT_CONTEXT_TAGS: structure, practices, heuristics -->
# Practices Structure & Conventions

This document defines the canonical structure for all learning **practices** in this repository, how files are named, how progress keywords work, and the quality heuristics used by `scripts/generate_progress.py`.

---

## 1. Directory Layout

Each topic (e.g. `Lists`, `ControlFlow`, `Functions`) lives directly under the `practices/` root:

```text
practices/
    TopicName/
        1/
            practice-<slug>-1.md
            practice-<slug>-1.py   (optional until you start coding)
        2/
            practice-<slug>-2.md
            practice-<slug>-2.py
        ...
        20/
```

Rules:

1. Exactly (up to) 20 numbered subfolders (`1` → `20`) per topic (`TOTAL_PER_TOPIC = 20`).
2. A folder is considered a **Created Practice** once its numbered directory exists and contains the markdown file.
3. A practice is considered to have **Python File Coverage** once at least one `*.py` file is present in that numbered folder.
4. Multiple `*.py` files are allowed, but the progress engine selects the one with the highest status keyword as the **primary** implementation. Conflicting statuses across files trigger a `multi_status_conflict` warning.

> Tip: Prefer a single Python file per practice unless you have a clear reason to split (e.g. helper module). If you do add helpers, keep the status keyword only in the main file and omit leading status lines in helper modules (they will otherwise appear as `UNCATEGORIZED`).

---

## 2. File Naming Convention

Markdown + Python file names follow this pattern:

```text
practice-<slug>-<index>.md
practice-<slug>-<index>.py
```

Where `<slug>` is the kebab‑case of the topic name:
* CamelCase boundary: `ControlFlow` → `control-flow`
* Acronyms stay lowercase: `OOP` → `oop`, `NumPy` → `numpy`

Algorithm (as used in tooling): insert a hyphen before a capital letter that follows a lowercase/digit, then lowercase the whole string. Regex: `re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', name).lower()`.

Consistency Matters:

* Avoid accidental duplicates like `practice-file-operations-1.md` vs `practice-fileoperations-1.md` — the normalization script (`scripts/normalize_practices.py`) flags duplicates or slug drift.
* Run: `python scripts/normalize_practices.py` (dry run) or add `--fix --apply` to auto-correct slugs and report anomalies.

---

## 3. Markdown File Structure

Recommended sections (starter template the creation script uses):

```markdown
# <Topic> Practice <N>

## Description
<short narrative of the problem domain>

## Objectives
* Clear, testable objective 1
* Objective 2

## Tasks
1. Primary task
2. Secondary / extension task

## Examples
```python
# Illustrative examples (inputs/expected outputs)
```

## Hints

* Optional nudge without giving the full solution

## Practice Cases

* Case 1 description
* Case 2 description

## Bonus

* Stretch idea (performance, extra feature, refactor suggestion)

```

Guidelines:
* Keep examples runnable and minimal.
* The heading text **Practice Cases** must remain exactly that (the migration tooling preserves this phrase intentionally).
* Include edge cases to encourage robust solutions (empty inputs, large sizes, error conditions).

---

## 4. Python File Structure & Progress Keywords

The **first non-empty line** of the primary `.py` file must be one of:

```text
# TODO:
# RESOLVED:
# VALIDATED:
```

Meaning:

* `# TODO:` – Scaffold or placeholder; implementation not started or incomplete.
* `# RESOLVED:` – A working solution is present (meets the basic objectives), but not yet fully validated.
* `# VALIDATED:` – Solution is complete, tested mentally or via usage, and meets quality guidelines (no warnings ideally).

Example skeletons:

```python
# TODO:

def solve(data):
    """Return processed result (describe parameters succinctly)."""
    # Outline approach / pseudocode
    pass
```

```python
# RESOLVED:

def solve(data):
    """Compute the transformed structure from `data`.

    Steps:
    1. Validate input
    2. Transform
    3. Return result
    """
    if not data:
        return []
    return [x * 2 for x in data]
```

```python
# VALIDATED:

from __future__ import annotations

def solve(data):
    """Double each numeric element.

    Args:
        data: Iterable of numbers (int/float).
    Returns:
        List of doubled numbers.
    Edge Cases:
        - Empty input → empty list
        - Non-numeric element → ValueError
    """
    if data is None:
        return []
    out = []
    for x in data:
        if not isinstance(x, (int, float)):
            raise ValueError(f"Non-numeric element: {x!r}")
        out.append(x * 2)
    return out

if __name__ == "__main__":  # Optional manual smoke
    print(solve([1, 2, 3]))
```

Rules:

1. The keyword must be flush with line start (no leading spaces) and end with a colon.
2. Only the first non-empty line counts; extra status markers later are ignored (but may produce `todo_leftover`).
3. Keep only one status keyword per file.
4. Transition path: TODO → (auto or manual) RESOLVED → (manual or auto) VALIDATED.

---

## 5. Heuristic Warnings (Quality Signals)

When a file is `RESOLVED` or `VALIDATED`, the progress script analyzes it and can attach warnings:

| Warning | Trigger | Mitigation |
|---------|---------|------------|
| `low_implementation_loc` | < 3 meaningful (non-comment, non-blank) lines | Flesh out code / remove placeholder pass-only bodies |
| `todo_leftover` | The string `TODO` appears beyond header | Remove stray TODOs once resolved |
| `pass_leftover` | Standalone `pass` statements remain | Remove or replace with logic |
| `missing_status` | No recognized leading keyword | Add `# TODO:` (or higher) as first non-empty line |
| `multi_status_conflict` | Multiple `.py` files under one practice differ in status | Consolidate / align statuses |
| `runtime_error:<...>` | Smoke execution (when `--smoke` enabled) raised an exception | Fix runtime issue |
| `missing_docstring:<fn>` | (Only if `--enforce-docstrings`) function lacks docstring | Add concise docstring |
| `high_complexity:<fn>:<score>` | Cyclomatic complexity > threshold (default 15) | Refactor into smaller functions |

Meaningful LOC definition: Non-empty, non-comment lines.

Goal for VALIDATED: **Zero warnings** (unless complexity is intentionally high and justified in comments).

---

## 6. Promotion Workflow

Two promotion modes:

1. Manual: You edit the first line, changing `# TODO:` → `# RESOLVED:` or `# RESOLVED:` → `# VALIDATED:` once you are confident.
2. Automated (`--promote` flag): The script upgrades eligible `# TODO:` files to `# RESOLVED:` when ALL are true:
    * Meaningful LOC ≥ threshold (`--promote-threshold`, default 3)
    * `pass` lines ≤ allowance (`--promote-allow-pass`, default 0)
    * Contains at least one `def` or `class`
    * No additional `TODO` occurrences beyond the header

After auto promotion it re-scans so metrics reflect new statuses.

VALIDATED is always a deliberate, manual step (no auto promote to VALIDATED is implemented today).

---

## 7. Adding / Creating Missing Practices

Use the generator to scaffold any absent numbered folders and markdown files (optionally the Python files):

```bash
python scripts/generate_progress.py --create-missing --create-with-py
```

Options:

* Limit to a single topic: `--only-topic Lists`
* Skip writing reports during creation (if you just want scaffolds): add `--no-md --no-json --no-badges --no-history`

---

## 8. Harness Generation

You can generate a harness enumerating functions/classes across a topic for quick review:

```bash
python scripts/generate_progress.py --generate-harness Lists
```

Output file: `.progress_state/harness_Lists.txt`

---

## 9. Badges & Reports

Running the generator (default) creates:

* `progress/progressDD_MM_YYYY.md` – Markdown dashboard
* `progress/progressDD_MM_YYYY.json` – Machine-readable summary
* `progress/progressDD_MM_YYYY.csv` – (if `--export-csv`)
* `progress/completed_all.md` – Cumulative resolved/validated practices
* `progress/completed_delta_DD_MM_YYYY.md` – Newly resolved on this run
* `badges/validated.json`, `badges/resolved.json` – Shields.io style badges

---

## 10. Validation Quality Targets

For a practice to be confidently VALIDATED, aim for:

* Clear, self-documenting code + docstring(s)
* Edge cases handled (empty inputs, invalid types, boundary values)
* No heuristic warnings
* Readable, small functions (complexity ≤ 10 preferred; ≤ 15 enforced unless overridden)
* Defensive checks only where meaningful (avoid over-validating trivial internal helpers)

Optional Future Enhancements (not yet automated but good practice):

* Inline complexity notes for non-trivial algorithms.
* Micro benchmarks or time complexity comment for performance-sensitive tasks.
* Type hints (`from __future__ import annotations`) for clarity.

---

## 11. Dealing With Duplicates / Normalization

If you see two markdown files for the same slot (e.g. `practice-datascience-1.md` and `practice-numpy-1.md` in the same `1/` folder), consolidate them:

1. Decide canonical slug (most consistent with topic folder name).
2. Merge distinct content sections.
3. Delete the redundant file (or archive it outside the practices tree).
4. Rerun the progress script.

The normalization script helps detect these situations early.

---

## 12. Legacy Compatibility

The tooling still supports a legacy `tests/` root for backward compatibility. New contributions must target `practices/`. Migration and rollback scripts exist but should not be necessary for standard daily work.

---

## 13. Quick Reference Checklist

* [ ] Folder path: `practices/<Topic>/<N>/`
* [ ] Markdown: `practice-<slug>-<N>.md` present
* [ ] Python file started (optional early): `practice-<slug>-<N>.py`
* [ ] First non-empty line is status keyword
* [ ] At least 3 meaningful LOC before promoting to RESOLVED
* [ ] No leftover `TODO` or stray `pass` after resolution
* [ ] Docstrings (if enforcing or for clarity) added
* [ ] Edge cases considered & documented
* [ ] Zero heuristic warnings before marking VALIDATED

---

## 14. Example: From TODO to VALIDATED (Diff Summary)

```diff
# TODO:

def fizzbuzz(n):
    pass
```

↓ Implement logic, remove pass, upgrade status when confident:

```diff
# RESOLVED:

def fizzbuzz(n):
    """Return list of fizz/buzz strings up to n inclusive."""
    out = []
    for i in range(1, n + 1):
        token = ""
        if i % 3 == 0: token += "Fizz"
        if i % 5 == 0: token += "Buzz"
        out.append(token or str(i))
    return out
```

↓ After manual validation (edge cases n=0, negative, large values) and maybe refactor:

```diff
# VALIDATED:

def fizzbuzz(n: int) -> list[str]:
    """Return FizzBuzz sequence 1..n.

    n <= 0 -> returns empty list.
    """
    if n <= 0:
        return []
    words = []
    for i in range(1, n + 1):
        label = ("Fizz" if i % 3 == 0 else "") + ("Buzz" if i % 5 == 0 else "")
        words.append(label or str(i))
    return words
```

---

## 15. Getting Help

If something looks off (unexpected warnings, missing counts, duplicate detection):

1. Run with `--stdout` to inspect live markdown report without opening file.
2. Run with `--smoke` to catch runtime issues early.
3. Use normalization script for structural issues.
4. Check the first line of the Python file for status formatting.

---

## 16. Current Observed Issues Snapshot

From the latest normalization / inspection of the existing repository state:

* Duplicate markdown in `practices/DataScience/1/`: both a `practice-datascience-1.md` and a `practice-numpy-1.md` (choose one slug, merge content).
* Duplicate markdown in `practices/FileOperations/1/`: `practice-file-operations-1.md` vs `practice-fileoperations-1.md` (retain the hyphenated form).
* Mixed slug styles in early FileOperations slots (normalize to `file-operations`).

Address these to avoid ambiguity in reports and future automated scaffolding.

---

Maintained automatically & manually — feel free to extend with new quality practices as the curriculum evolves.

---

### Related Docs

* Creation workflow: `COPILOT_CREATE_PRACTICE.md` (tags: create)
* Implementation & validation: `COPILOT_IMPLEMENT_PRACTICE.md` (tags: implement)
* Chat usage strategies: `COPILOT_CHAT_USAGE.md` (tags: chat-usage)
* Inline prompt library: `COPILOT_INLINE_PROMPTS.md` (tags: inline-prompts)
* Progress automation & CI: `ci_progress.md` (tags: progress, ci)
