<!-- COPILOT_CONTEXT_TAGS: inline-prompts, prompts, validation, refactor, explanation -->
# GitHub Copilot Inline & Quick Chat Prompt Library

> Fast version: `inline-prompts-top10-quick.md` lists the highest‑leverage prompts.

This document lists **concise, copyable prompts** optimized for **Inline Chat** (in-editor) and **Quick Chat** to accelerate everyday study & implementation tasks. Each prompt is tagged with discoverable keywords for context injection.

---
## 1. Usage Guidelines

Keep inline prompts SHORT + DIRECT. Reference file paths or symbols explicitly if outside the current buffer.

Format patterns:

 
* Action + Target + Constraint
* "Review", "Refactor", "Explain", "List", "Compare", "Validate"

Add `//` or `#` comment prefix when invoking from inside code for some editors, else just type in Inline Chat box.

---
## 2. Status & Heuristic Focus

| Scenario | Prompt | Tags |
|----------|--------|------|
| Promote TODO → RESOLVED | Review this file for promotion criteria (≥3 meaningful LOC, no stray pass/TODO) and output minimal diff only. | promote, status |
| Promote RESOLVED → VALIDATED | Apply VALIDATION CHECKLIST (objectives, edge cases, no warnings). If satisfied, diff changing header + add rationale comment. | validate, status |
| List Warnings Causes | Explain root causes of each heuristic warning listed in progress report excerpt (paste excerpt). | heuristics, warnings |
 
| Fix Warnings | Clear these warnings (list them) with minimal code changes, return unified diff. | heuristics, fix |

---
## 3. Explanation & Learning

| Goal | Prompt | Tags |
|------|--------|------|
| Concept Map | List core Python concepts used here and line anchors. | explain, concepts |
| Edge Case Table | Build table with columns: Case; Expected; Handled?; Patch Plan. | edge-cases, validate |
| Algorithm Narration | Narrate the transformation (input→output) in ≤8 sentences; omit code paraphrase. | narration, explain |
| Misconceptions | List 3 beginner misconceptions this code helps clarify with mini examples. | pedagogy, explain |
 
---
### Related Docs

* Chat usage strategies: `COPILOT_CHAT_USAGE.md` (tags: chat-usage)
* Practice creation: `COPILOT_CREATE_PRACTICE.md` (tags: create)
* Implementation & validation: `COPILOT_IMPLEMENT_PRACTICE.md` (tags: implement, validate)
* Structure & heuristics: `PRACTICES_STRUCTURE.md` (tags: structure, heuristics)
* Progress automation & CI: `ci_progress.md` (tags: progress, ci)
| Flashcards | Produce 3 Q/A flashcards reinforcing key ideas. | flashcards, retention |

---
## 4. Refactoring & Quality

| Goal | Prompt | Tags |
|------|--------|------|
| Simplify Function | Refactor solve() to reduce branching; keep behavior + signature identical; diff only. | refactor, simplify |
| Extract Helper | Identify logical subtask worth extracting; propose name + diff. | refactor, helpers |
| Complexity Control | Estimate cyclomatic complexity of solve(); if >10 propose 2-step split plan. | complexity, refactor |
| Naming Review | Suggest improved variable/function names (reason per change) without modifying code yet. | naming, review |
| Intent Comments | Insert comments explaining rationale (not mechanics) for non-trivial steps; diff only. | comments, pedagogy |
 

---
## 5. Alternative Solutions

| Goal | Prompt | Tags |
|------|--------|------|
| List Strategies | Enumerate 2 alternative strategies with Time/Space/Tradeoffs table. | alternatives, compare |
| Implement Alt | Add solve_alt() implementing the most contrasting feasible approach; docstring + example. | alternatives, implement |
| Compare Solutions | Compare solve vs solve_alt focusing on readability + complexity + extensibility. | compare, analysis |

---
## 5. Alternative Solutions

| Goal | Prompt | Tags |
|------|--------|------|
| List Strategies | Enumerate 2 alternative strategies with Time/Space/Tradeoffs table. | alternatives, compare |
| Implement Alt | Add solve_alt() implementing the most contrasting feasible approach; docstring + example. | alternatives, implement |
| Compare Solutions | Compare solve vs solve_alt focusing on readability + complexity + extensibility. | compare, analysis |

---

## 6. Defensive & Edge Handling
 

| Goal | Prompt | Tags |
|------|--------|------|
| Validate Inputs | Add input validation raising ValueError for invalid types described in spec; diff only. | validation, inputs |
| Robustness Gaps | List potential runtime failure points and propose guards; no code changes yet. | robustness, review |
| Add Edge Tests | Suggest 4 assert statements covering uncovered branches; no rewrites. | tests, edge-cases |

---
## 7. Performance & Optimization

 
| Goal | Prompt | Tags |
|------|--------|------|
| Big-O Summary | State time & space complexity; justify key operations. | performance, complexity |
| Micro-Optimization | Suggest one micro-optimization with measurable benefit; skip if negligible. | performance, optimize |
| Data Structure Choice | Evaluate current data structures; propose replacements if cost/benefit positive. | performance, structures |

---
## 8. Documentation & Pedagogy

| Goal | Prompt | Tags |
 
|------|--------|------|
| Improve Docstring | Enhance docstring: clearer Args/Returns + 2 Examples + Edge Cases list; diff only. | docstring, docs |
| Educational Block | Generate educational markdown comment with sections (Concepts, Pitfalls, Strategy). | pedagogy, docs |
| Remove Redundant Comments | Remove comments that simply restate code; preserve rationale comments. | cleanup, comments |

---
## 9. Progress-Driven Prompts

| Goal | Prompt | Tags |
|------|--------|------|
 
| Topic Gap Plan | From progress excerpt (paste table rows), recommend next 3 practices with rationale. | planning, gaps |
| Prioritize Validation | Given low validated %, select 2 candidate TODO files in this topic to implement first (give reason). | planning, validation |

---
## 10. Multi-Step Inline Sequence (Copy/Paste)

```text
Step 1: List unhandled edge cases.
Step 2: Provide minimal patch to address them.
 
Step 3: Add brief complexity comment.
(Pause for confirmation after each step.)
```

Invoke: "Execute the 3-step sequence toward validation readiness." (Tags: sequence, validation)

---
## 11. Tag Glossary (for Copilot Context)

`inline-prompts`, `promote`, `validate`, `heuristics`, `warnings`, `explain`, `concepts`, `edge-cases`, `narration`, `flashcards`, `refactor`, `simplify`, `helpers`, `complexity`, `naming`, `comments`, `alternatives`, `compare`, `analysis`, `validation`, `inputs`, `robustness`, `tests`, `performance`, `optimize`, `structures`, `docstring`, `docs`, `pedagogy`, `cleanup`, `planning`, `gaps`, `sequence`.

Use any combination when referencing this file to boost retrieval.

 
---
## 12. Quick Copy Block

```text
PROMOTE: Review for RESOLVED readiness (≥3 LOC, no pass/TODO) → diff.
VALIDATE: Apply checklist; if clean promote to VALIDATED with rationale comment.
EDGE TABLE: Build Case|Expected|Handled?|Fix rows.
ALT STRATEGIES: Table + implement most contrasting as solve_alt().
 
REFINE DOCSTRING: Improve structure + examples; diff only.
```

---
**Outcome:** Keep this file open for fast contextual injections—short prompts produce higher quality focused results via Inline Chat.

---
### Related Docs
* Chat usage strategies: `COPILOT_CHAT_USAGE.md` (tags: chat-usage)
* Practice creation: `COPILOT_CREATE_PRACTICE.md` (tags: create)
* Implementation & validation: `COPILOT_IMPLEMENT_PRACTICE.md` (tags: implement, validate)
* Structure & heuristics: `PRACTICES_STRUCTURE.md` (tags: structure, heuristics)
* Progress & CI automation: `ci_progress.md` (tags: progress, ci)
