<!-- COPILOT_CONTEXT_TAGS: implement, validate, promotion-flow, alternative-solutions -->
# Implementing a Practice Python File with GitHub Copilot Chat (Agent Mode)

This companion guide covers turning a newly created practice markdown into a high‑quality Python implementation using GitHub Copilot Chat **agent mode**, while respecting repository progress heuristics.

---

## 1. Goal & Constraints

The resulting Python file must:

- Live at: `practices/<Topic>/<N>/practice-<slug>-<N>.py`
- Begin with one of the status lines (start at `# TODO:` → later promote)
- Contain ≥ 3 meaningful (non-comment, non-blank) lines before promotion to `# RESOLVED:`
- Have no stray `pass` or extra `TODO` once promoted
- Optionally include type hints & docstrings (recommended)

---

## 2. Initial Copilot Prompt (Generate Skeleton)

Open the practice markdown to give Copilot context (having the file open helps). In Chat:

> Using the open markdown practice for \<Topic\> index \<N\>, create the starter Python file `practice-<slug>-<N>.py` with first non-empty line `# TODO:`. Include a `solve()` (or appropriately named) function stub matching the tasks. Add a docstring listing Args, Returns, and at least 2 edge cases from the Practice Cases section.

If multiple functions are implied:

> Derive clear function boundaries (core solver + helpers) and propose them. Then implement only the interface + docstrings without logic yet.

---

## 3. Request Testable Logic Incrementally

Prompt for iterative construction (prevents over-generation):

> Implement the minimal working logic for the main function based on Objectives, but keep status `# TODO:`. Avoid advanced optimizations yet.

Review the diff. If it already satisfies the TODO→RESOLVED criteria (≥ 3 meaningful LOC, no placeholder `pass`), you can promote.

Promotion step (either manual edit or via prompt):

> Update the first line to `# RESOLVED:` now that core logic is implemented, and remove any remaining placeholder code.

---

## 4. Enforce Heuristic Cleanliness

Ask Copilot to self-audit:

> Inspect this file for: leftover `pass`, stray `TODO`, missing docstrings on public functions, or opportunities to simplify. Provide a concise diff fixing issues.

Optional complexity check direction:

> Refactor to keep cyclomatic complexity below 10 by extracting helpers where logical.

---

## 5. Introduce Validation & Edge Cases

Prompt ideas:

- *"List edge cases from the markdown and confirm each is handled; patch code if any are missing."*
- *"Add input validation raising ValueError for invalid types described in the practice cases."*
- *"Improve docstring with a clear Examples section matching the markdown's Examples block."*

Then re-run (topic-only) progress report:

```powershell
python scripts/generate_progress.py --only-topic <Topic> --stdout --smoke
```
If runtime errors appear, iterate until clear.

---

## 6. Moving to VALIDATED

Your criteria to promote to `# VALIDATED:`:

1. All described tasks & edge cases implemented.
2. No heuristic warnings (`low_implementation_loc`, `pass_leftover`, etc.).
3. Docstring present for main function(s).
4. Smoke run (optional `--smoke`) passes.

Promotion prompt:

> Review the implementation for completeness vs the markdown specification. If complete, change the status to `# VALIDATED:` and ensure style/readability improvements (naming, small functions) without altering externally visible behavior.

### 6.1 Deep Validation Pass with Copilot

Use a structured, multi‑stage prompt to drive richer validation instead of a single broad ask:

1. Structural conformance
	> Audit this file ONLY for structural conformance to the markdown spec (required functions, return shapes, error handling). List discrepancies; do not change code yet.

2. Edge case replay
	> For each Practice Case + any implicit edge case (empty input, None, large size), build a small table: Case | Expected Behavior (in plain language) | Whether current code handles it | If not, fix plan.

3. Implementation refinement
	> Apply the previously described fix plan as a minimal, focused patch. Avoid unrelated refactors.

4. Readability & naming
	> Suggest renames or micro‑refactors that reduce cognitive load (short function length, clear variable purpose). Provide a diff; keep behavior identical.

5. Status promotion
	> If ALL prior issues are resolved and no heuristic warnings would trigger (assume progress script heuristics), promote header to `# VALIDATED:` and add a brief summary comment block explaining why it's validated.

### 6.2 Validation Criteria Checklist (Copy/Paste for Chat)

> VALIDATION CHECKLIST:
>
> - All objectives satisfied
> - All listed Practice Cases addressed
> - Edge cases handled (empty / invalid types / boundary sizes)
> - No heuristic triggers: low_implementation_loc, pass_leftover, todo_leftover, missing_status
> - Clear docstring & inline educational comments
> - Cyclomatic complexity within threshold OR justified comment
> - Deterministic behavior & idempotent where expected

### 6.3 Generating an Educational Validation Report

Prompt:
> Produce an "Educational Validation Report" summarizing: (1) Problem restatement, (2) Key concepts learned, (3) Walkthrough of algorithm, (4) Edge case handling strategy, (5) Potential future optimizations, (6) Common beginner pitfalls avoided here. Output as a markdown comment block I can paste above the code (wrapped inside triple quotes or a multiline comment style), concise but instructive.

You can keep this block temporarily for learners then prune later when confident.

### 6.4 Auto‑Generating Lightweight Test Snippets (Optional)

Prompt:
> Generate a minimal self‑contained test snippet (no external libs) exercising all branches. Use assert statements. Place it under an `if __name__ == "__main__":` guard so smoke execution remains fast.

Integrate only if it improves understanding; keep noise low.

### 6.5 Ensuring Pedagogical Comments

Ask Copilot:
> Insert inline comments that explain WHY each non‑trivial step exists (avoid obvious comments). Focus on intent, invariants, and complexity tradeoffs. Do not restate the code literally.

Then optionally trim verbosity:
> Remove any comments that merely paraphrase code; keep conceptual / rationale comments.

### 6.6 Promoting with Rationale Summary

Final promotion prompt combining quality signals:
> If this implementation meets the VALIDATION CHECKLIST, upgrade status and append a trailing block comment labeled "Validation Rationale" summarizing coverage, complexity, and any deliberate tradeoffs.

---

## 7. Adding a Lightweight Harness (Optional)

You can generate a harness for quick manual invocation:

```powershell
python scripts/generate_progress.py --generate-harness <Topic>
```
Open `.progress_state/harness_<Topic>.txt` and manually test functions in a REPL if desired.

---

## 8. Typical Prompt Sequence (Cheat Sheet)

1. Scaffold skeleton: *starter file with # TODO:*.
2. Implement minimal logic: *core algorithm only*.
3. Promote: *change to # RESOLVED:*.
4. Audit & refine: *remove warnings, handle edge cases*.
5. Final polish & promote: *set # VALIDATED:*.

---

## 9. Handling Multi-File Practices

If you need helper modules (rare early on):

> Create an additional helper file for reusable utilities, but DO NOT include a status keyword in the helper—only in the primary file.

Keep helpers small; complexity still accumulates.

---

## 10. Common Issues & Fixes

| Issue | Symptom | Resolution |
|-------|---------|------------|
| Missing status | Warning `missing_status` | Add `# TODO:` at top |
| Forgot promotion | File still `# TODO:` though complete | Change to `# RESOLVED:` (or `# VALIDATED:` if fully vetted) |
| Stray TODO text | `todo_leftover` warning | Remove internal TODO comments (convert to clarifying comments) |
| Over-complex function | Hard-to-read, potential `high_complexity` | Extract helpers, early returns |
| Placeholder pass | `pass_leftover` warning | Replace with real logic or remove |

---

## 11. Commit Example

```powershell
git add practices/<Topic>/<N>/practice-<slug>-<N>.py
git commit -m "feat(practices): implement <Topic> practice <N> (initial resolved solution)"
```

Later (after validation):

```powershell
git commit -am "chore(practices): promote <Topic> practice <N> to VALIDATED"
```

---

## 12. Continuous Improvement Prompts

- *"Suggest micro-optimizations with clear complexity rationale (avoid premature changes)."*
- *"Add one more challenging Practice Case and adapt code if needed."*
- *"Generate a brief performance note (Big-O) and embed it as a comment."*

---
## 13. Alternative Solutions & Comparative Review


Encourage deeper learning by contrasting different approaches. Prompts:

1. Enumerate solution strategies
	> List 2–3 distinct solution strategies (e.g., iterative, recursive, data structure optimized) for this problem. Provide pros/cons table: Approach | Time | Space | Readability | When Prefer.

2. Provide alternative implementation
	> Implement the most contrasting alternative (different paradigm) in a separate function `solve_alt()` with full docstring; comment key differences.

3. Comparative analysis
	> Compare `solve` vs `solve_alt` focusing on asymptotic complexity, constant factors, clarity, extensibility. Identify which scenarios favor each.

4. Educational commentary
	> Insert a top-level multiline comment titled "Alternative Strategy Notes" summarizing how a learner can decide which approach to choose in real projects.

Optional follow-up:
> If both solutions are equally performant for typical input sizes, suggest a micro-benchmark harness stub without implementing timing logic.

### Pros/Cons Prompt Template

> Build a markdown table for the alternative plus current solution with columns: Approach, Core Idea, Best For, Tradeoffs, Cognitive Load (Low/Med/High).

### Guard Against Bloat

After adding an alternative, prune unused helpers and ensure the main path (`solve`) is still the primary validated implementation. You may keep `solve_alt` with a `# TODO:` header initially until validated separately.

---
## 14. Deep Dive Prompt Patterns (Learning Focus)


Use these to extract more conceptual value:

- Concept extraction:
	> List core Python concepts exercised here (e.g., list slicing, closures, recursion, error handling). For each: brief explanation & where in code it appears (line references optional).
- Misconception highlight:
	> Identify 3 plausible beginner misconceptions about this problem and clarify them with short examples.
- Incremental refactor path:
	> Suggest a 3-step refactoring journey from naive to production-grade, with intent for each step (readability, performance, extensibility).
- Data flow narration:
	> Narrate input → output transformation in 6–10 sentences focusing on state changes.

---
## 15. Incorporating Feedback Loops


Add a retrospective prompt after validation:
> Provide a Retrospective: What was improved from initial draft to validated version? Categorize changes: correctness, performance, readability, pedagogy.

Archive this in a comment or a separate `NOTES.md` if it becomes long.

---
## 16. Minimizing Overfitting to AI Suggestions

Prompt to avoid blindly trusting generated code:
> Critically review this solution: point out any assumptions the code makes about input shape or types that aren't enforced; propose guard clauses or clarify docstring wording.

---
## 17. Summary: Validation Promotion Flow (Condensed)

1. Draft (# TODO)
2. Minimal working logic (# RESOLVED)
3. Structured validation (checklist + edge tables)
4. Educational augmentation (comments + report)
5. (Optional) Alternative solution & comparative notes
6. Final refinement & heuristics clean
7. Promote (# VALIDATED) with rationale

Copyable compact prompt:
> Perform steps 3–7 of the Validation Promotion Flow sequentially, pausing after each with a brief summary and awaiting confirmation before continuing. Stop if any step reveals a failing case.

---
**Outcome:** Using structured prompts keeps each promotion deliberate, ensures repository heuristics stay green, and avoids silent status inflation.

---
### Related Docs

- Creation workflow: `COPILOT_CREATE_PRACTICE.md` (tags: create)
- Chat usage strategies: `COPILOT_CHAT_USAGE.md` (tags: chat-usage)
- Inline prompt library: `COPILOT_INLINE_PROMPTS.md` (tags: inline-prompts)
- Structure & heuristics: `PRACTICES_STRUCTURE.md` (tags: structure, heuristics)
- Progress & CI: `ci_progress.md` (tags: progress, ci)
