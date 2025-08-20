<!-- COPILOT_CONTEXT_TAGS: create, scaffold, practice-generation -->
# Creating a New Practice with GitHub Copilot Chat (Agent Mode)

> Short form: `create-practice-quick.md` (step checklist + macro prompt).

This guide shows a repeatable workflow to add a brand‑new practice (markdown scaffold + optional starter `.py`) using GitHub Copilot Chat *agent mode* so that the repository conventions and progress automation pick it up immediately.

---

## 1. Pre‑Flight Checklist

Ensure you know:

- Topic folder name (e.g. `Functions`, `DataScience`).
- Next available numeric index inside that topic (dynamic capacity; not capped at 20 anymore).
- Slug form of the topic (camel case boundaries replaced with hyphen + lowercase). Example: `ControlFlow` → `control-flow`.

Quickly list existing indices (PowerShell example):

```powershell
Get-ChildItem practices/Functions -Directory | Where-Object { $_.Name -match '^[0-9]+$' } | Select-Object -Expand Name
```
Choose the smallest missing positive integer (gap filling is fine; order is not strictly enforced but keeping contiguous blocks helps readability).

---

## 2. Folder & File Naming Rules (Recap)

Inside `practices/<Topic>/<N>/` you will create:

- `practice-<slug>-<N>.md`
- `practice-<slug>-<N>.py` (optional now; can add later)

Example for `Functions` topic, index 21:

```text
practices/Functions/21/
  practice-functions-21.md
  practice-functions-21.py  (optional at creation)
```

---

## 3. Copilot Chat: Prompt to Scaffold a New Practice

Open Copilot Chat (agent mode). Use a **concrete, directive prompt**:

> Create a new practice in `practices/Functions/21/` named `practice-functions-21.md`. Follow the repository structure. Provide sections: Description, Objectives, Tasks (ordered list), Examples (Python fenced), Hints, Practice Cases (bullet list), Bonus. Topic focus: Higher-order function patterns (closures and decorators). Do not generate the `.py` yet. Use concise, instructional language.

If the directory does not yet exist, ask the agent to create it explicitly:

> Ensure the folder `practices/Functions/21/` exists before writing the file.

### Quality Guidance for the Practice Markdown

Ask Copilot to self‑review:

> Review the created markdown for: clarity of objectives, at least 2 practice cases, one stretch Bonus, and an example that is runnable. Provide a diff improving any weak sections and then apply it.

### Optional: Add Starter Python File

If you also want a starter `.py` (with the required first status line):

> Add `practice-functions-21.py` in the same folder. First non-empty line must be `# TODO:`. Include a placeholder `solve()` function signature aligned to the tasks, plus a docstring skeleton with Args/Returns sections.

---

## 4. Validating the Addition

Run the progress generator (limit to topic for speed):

```powershell
python scripts/generate_progress.py --only-topic Functions --stdout
```

Check the markdown table:

- Created count increments for `Functions`.
- Python Files count increments only if you added the `.py`.

If you forgot the status keyword, the file will show a `missing_status` warning—fix by adding `# TODO:` at the top.

---

## 5. Iterative Refinement with Copilot

Prompt examples:

- Improve clarity: *"Refine the Objectives in `practice-functions-21.md` to be testable and begin each with an imperative verb."*
- Add edge cases: *"Append two additional Practice Cases covering decorator ordering and metadata preservation."*
- Enforce conciseness: *"Shorten the Description to ≤ 4 sentences without losing intent."*

After each refinement, re-run (optional):

```powershell
python scripts/generate_progress.py --only-topic Functions --stdout --no-json --no-badges --no-history
```

---
## 6. Common Pitfalls & Fixes

| Issue | Symptom | Fix |
|-------|---------|-----|
| Wrong slug | File named `practice-Function-21.md` | Rename to kebab case `practice-functions-21.md` |
| Missing status | Warning `missing_status` | Add `# TODO:` as first non-empty line in `.py` |
| Duplicate index | Two folders with same number | Remove / merge one, keep canonical content |
| Out-of-order creation | Large gap (e.g. jump from 10 → 25) | Acceptable but consider filling gaps for continuity |

---
## 7. Commit Strategy
Stage and commit together:

```powershell
git add practices/Functions/21/
git commit -m "feat(practices): add Functions practice 21 (closures & decorators)"
```

---
 
## 8. Suggested Copilot Macro Prompt (Reusable)

You can store a reusable prompt snippet:

> New practice scaffold: Topic=\<TopicName\>, Index=\<N\>, Focus=\<focus summary\>. Create folder and markdown with sections: Description, Objectives (3–6), Tasks (ordered list), Examples (Python), Hints (1–3 bullets), Practice Cases (4–8 bullets), Bonus (1–2 stretch ideas). Use active voice, concise sentences. Avoid implementation details; focus on learning outcomes.

---
 
## 9. Next Steps

After creation:

1. Implement `.py` (see companion guide `COPILOT_IMPLEMENT_PRACTICE.md`).
2. Promote from `# TODO:` to `# RESOLVED:` when logic exists (≥ 3 meaningful LOC, no stray `pass`).
3. Eventually mark as `# VALIDATED:` after manual review / smoke.

---
**Outcome:** You now have a reproducible, AI-assisted workflow to add high-quality practice scaffolds consistently with minimal manual boilerplate.

---
### Related Docs
* Implementation & validation: `COPILOT_IMPLEMENT_PRACTICE.md` (tags: implement, validate)
* Chat usage strategies: `COPILOT_CHAT_USAGE.md` (tags: chat-usage)
* Inline prompts: `COPILOT_INLINE_PROMPTS.md` (tags: inline-prompts)
* Structure & heuristics: `PRACTICES_STRUCTURE.md` (tags: structure)
* Progress automation: `ci_progress.md` (tags: progress, ci)
