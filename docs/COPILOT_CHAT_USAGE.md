<!-- COPILOT_CONTEXT_TAGS: chat-usage, prompts, agent-mode, ask-mode, context-strategy -->
# Using GitHub Copilot Chat (Agent Mode & Ask Mode) with This Repository

> Need the TL;DR? See `chat-usage-quick.md` for a one‑screen summary.

This guide explains how to get the most out of GitHub Copilot Chat in BOTH:

- **Agent Mode** (multi‑step, stateful, iterative plans)
- **Ask Mode** (single, focused questions)

…while leveraging the repository’s structured context:

- `practices/` (individual learning practices)
- `progress/` (automated progress outputs)
- `docs/` (meta documentation & workflows)
- `plan/syllabus.md` (curriculum map)
- `scripts/generate_progress.py` (progress + heuristics engine)

> Treat this document as a *prompt design playbook* specialized for this project.

---

## 1. Core Concepts: Agent vs Ask

| Mode | When to Use | Strengths | Caution |
|------|-------------|-----------|---------|
| Ask | Quick fact, definition, tiny refactor, syntax, “what does X mean?” | Fast, low overhead | Easy to lose broader intent |
| Agent | Creating/editing multiple files, scaffolding practices, validation workflows, comparative solutions, multi-step refinement | Maintains context & plan; structured | Can drift; keep it grounded with explicit anchors |

**Rule of Thumb:** Start with Ask for clarification; escalate to Agent when the task spans more than one change, file, or conceptual step.

---

## 2. Supplying Context to Copilot

Copilot’s responses improve dramatically when it sees the *right slices* of this repo.

### 2.1 Minimal Context Packets

| Goal | Recommended Context Files |
|------|---------------------------|
| Create new practice | `docs/PRACTICES_STRUCTURE.md`, nearby practice folder, `plan/syllabus.md` section for topic |
| Implement solution | The target practice `.md`, existing similar validated `.py` files, `docs/COPILOT_IMPLEMENT_PRACTICE.md` |
| Improve status → VALIDATED | Practice `.py` + `docs/COPILOT_IMPLEMENT_PRACTICE.md` + heuristics section in `scripts/generate_progress.py` |
| Generate alt strategies | Current implementation + at least one other practice in same topic |
| Curriculum planning | `plan/syllabus.md` + `progress/progressDD_MM_YYYY.md` |
| Heuristic debugging | Target `.py` + `scripts/generate_progress.py` (search for warnings keywords) |

### 2.2 Practical Context Techniques

1. **Open Files**: Open the key practice markdown + implementation file before prompting.
2. **Select Region**: Highlight just the relevant function or spec and then ask a refinement question.
3. **Reference Paths**: Explicitly mention file paths in your prompt (Copilot indexes open/changed first).
4. **Quote Excerpts**: Paste small spec excerpts instead of “see above”.
5. **Use Directives**: "Only modify the function body of `solve`—do not rename functions or change I/O signature." helps prevent overreach.

### 2.3 Context Anti‑Patterns

| Anti‑Pattern | Impact | Fix |
|-------------|--------|-----|
| Dumping whole syllabus + all code | Token noise; diluted focus | Provide only current topic section |
| Vague “optimize this” | Random micro-churn | State objective: readability / complexity / memory |
| Asking for validation w/o heuristics reminder | Missed quality gates | Include: “Respect repository heuristics (no leftover TODO/pass; ≥3 meaningful LOC).” |

---

## 3. Reusable Prompt Snippets

Below are *fill‑in* templates you can reuse (copy → adapt → run). Keep a library of your best variants.

### 3.1 New Practice (Agent Mode)

```text
You are acting as a curriculum assistant.
Topic: <TopicName>
Index: <N>
Learning Focus: <concepts>
Use rules in docs/PRACTICES_STRUCTURE.md.
Create folder + practice-<slug>-<N>.md with sections:
Description, Objectives (actionable), Tasks (ordered), Examples (Python), Hints, Practice Cases, Bonus.
Tone: concise, instructional.
Report a short checklist after generation.
```

### 3.2 Implement Practice Skeleton (Agent Mode)

```text
Create practice-<slug>-<N>.py for the open markdown.
Add first line: # TODO:
Add solve() stub + docstring with Args, Returns, 2 edge cases.
No full logic yet.
```

### 3.3 Promote TODO → RESOLVED (Ask or Agent)

```text
Review this file for readiness to promote to RESOLVED.
Criteria: >=3 meaningful LOC, no placeholder pass beyond necessary, at least one def or class.
Return: a patch (diff-style). If not ready, list blockers.
```

### 3.4 Deep Validation (Agent Mode)

```text
Run a multi-stage validation on practice-<slug>-<N>.py:
1) Structural gaps vs practice markdown.
2) Edge case table (Case | Expected | Covered? | Fix).
3) Apply minimal fixes.
4) Complexity & naming refinement.
5) If clean, promote to # VALIDATED: and append Validation Rationale comment.
Stop early if a blocking issue is found.
```

### 3.5 Alternative Solution Exploration

```text
Given current solve(), propose two distinct alternative strategies.
Produce table: Approach | Core Idea | Time | Space | Tradeoffs | When Prefer.
Implement ONLY the most contrasting as solve_alt() (with docstring) unless constraints equal.
```

### 3.6 Curriculum Gap Analysis

```text
Using plan/syllabus.md and latest progress/progress<date>.md:
Identify underdeveloped areas (low created % or low python file %).
Propose next 5 practices (Topic/Index + short goal).
```

### 3.7 Refactor with Safety Constraints

```text
Refactor solve() for readability.
Must keep:
- Public signature
- Behavior (prove with 3 example input/output pairs)
- Complexity class
Add intent comments (not code-rephrasing) for non-trivial steps only.
Return unified diff.
```

### 3.8 Heuristic Warning Remediation

```text
File has warnings: <list>.
Explain cause of each warning relative to repository heuristic definitions.
Generate minimal changes to clear them all.
```

---

## 4. Leveraging Syllabus (`plan/syllabus.md`)

The syllabus is your concept lattice. Use it to:

- **Pre-seed learning goals**: "From section 3.2 Advanced Function Parameters, generate 3 micro-practices building toward decorators."
- **Progress alignment**: Cross-check implemented practices vs missing syllabus items.
- **Spiral reinforcement**: Ask for a follow-up practice revisiting earlier foundational concepts with a twist.

**Prompt Pattern:**

```text
From syllabus sections <numbers>, generate a progression of 4 practices that increase difficulty, referencing already implemented topics where possible (list existing from progress markdown summary if needed).
```

---

## 5. Integrating Progress Metrics

Use `scripts/generate_progress.py` output (JSON + markdown) to steer focus.

**Ask Mode Example:**

```text
Given this summary snippet:
<excerpt table row(s) from progress markdown>
Recommend focus priorities ranked by: (1) lowest Python File %, (2) strategic breadth (core fundamentals earlier), (3) synergy with upcoming syllabus sections.
```

**Agent Mode Sequence:**

1. Parse summary.
2. Choose target topic.
3. Generate new practice scaffold.
4. Implement skeleton.
5. (Optionally) auto-promote.
6. Suggest alt strategies.

---

## 6. Educational Layer & Meta-Learning

Use Copilot to *explain why*, not just *what*.

| Objective | Prompt Add‑On |
|-----------|---------------|
| Extract underlying concept | "Explain the key Python concepts this solution exercises and how they map to code regions." |
| Reduce cognitive load | "Suggest a mental model or analogy for this algorithm for beginners." |
| Reinforce retention | "Generate 3 spaced repetition flashcard Q/A pairs based on this practice." |
| Encourage transfer | "How does this pattern translate to data science / web / OOP contexts?" |

---

## 7. Prompt Quality Principles

| Principle | Description | Example Suffix |
|-----------|-------------|----------------|
| Anchor Source | Point at real files | "Use docs/PRACTICES_STRUCTURE.md as policy authority." |
| Single Intent | One operation per request | Avoid mixing create + validate + refactor simultaneously |
| Bounded Output | Limit form | "Return a markdown table only." |
| Delta Not Dump | Prefer diffs | "Produce unified diff instead of full file." |
| Explain THEN Act | Ask for reasoning before patch | "List issues first; wait for confirm before changes." |
| Guardrails | Declare no-go zones | "Do not alter existing validated functions." |

---

## 8. Common Failure Modes & Corrections

| Symptom | Likely Cause | Correction Prompt |
|---------|--------------|------------------|
| Overwritten good code | Vague refactor request | "Refactor only inside solve(); keep other functions verbatim." |
| Missing sections in new practice | Omitted structural doc | "Re-read PRACTICES_STRUCTURE.md and regenerate missing sections only." |
| Bloated alternative solutions | Non-scoped exploration | "Limit alt strategy to ≤25 LOC; focus on different data structure." |
| Shallow validation | Skipped checklist | "Apply VALIDATION CHECKLIST from section 6.2 before promoting." |
| Infinite improvement loop | Non-terminating refinement | "Stop after 2 improvement iterations and summarize residual risks." |

---

## 9. Progressive Workflow Blueprint (Agent Mode)

```text
PLAN:
1. Identify weakest topic (low Python File %)
2. Propose next practice (gap aligned to syllabus)
3. Generate markdown scaffold
4. Create TODO Python skeleton
5. Implement minimal logic → RESOLVED
6. Run deep validation flow → VALIDATED
7. Generate alternative solution summary
8. Produce educational validation report + flashcards
9. Output concise recap + next recommended practice
```

Use: "Execute the PLAN step-by-step. After each step, pause and show a one-line status; await 'continue'."

---

## 10. Combining Ask & Agent Efficiently

1. Use **Ask** to clarify / reduce ambiguity *before* kicking off a long agent plan.
2. Use **Agent** to orchestrate multi-file edits—otherwise you risk losing continuity.
3. Bounce back to **Ask** for tiny tactical queries mid-plan (e.g., "What is time complexity now?") without derailing the agent.
4. Resume agent with explicit state reminder: "Resume at step 5 (implement minimal logic)."

---

## 11. Safety & Quality Guidelines

- Always *skim diffs* before accepting large agent-applied patches.
- Reject code that removes status keywords inadvertently.
- Re-run `python scripts/generate_progress.py --only-topic <Topic> --stdout` after major changes to confirm heuristics remain clean.
- Use alt solutions for learning—not mandatory to keep both long-term.

---

## 12. Quick Reference: Copy/Paste Macros

| Scenario | Macro Name | Reference |
|----------|------------|-----------|
| New Practice | `NEW_PRACTICE_SCAFFOLD` | Section 3.1 |
| Promote TODO→RESOLVED | `PROMOTE_TODO` | Section 3.3 |
| Deep Validation | `DEEP_VALIDATE` | Section 3.4 + 6.1 |
| Alt Strategy | `ALT_STRATEGY` | Section 3.5 + 13 |
| Gap Analysis | `GAP_ANALYSIS` | Section 3.6 |
| Refactor Safely | `SAFE_REFACTOR` | Section 3.7 |
| Heuristic Fix | `FIX_WARNINGS` | Section 3.8 |

Store these in a local snippet file or a scratch markdown for fast reuse.

---

## 13. Evolving the Workflow

As the repository matures:

- Add a **Test Harness Layer**: ask Agent to generate parametric tests once enough practices are VALIDATED.
- Introduce **Difficulty Metadata** in practice headers and have Agent auto-suggest a learning path gradient.
- Build a **Topic Complexity Heatmap** (derive from number of practices + validation ratio) and ask Copilot to focus on cold spots.

Prompt to bootstrap these:

```text
Using progress JSON and syllabus, propose a difficulty calibration rubric (1–5) and assign provisional difficulty scores to each existing practice title.
```

---

**Outcome:** You now have a structured, repeatable approach to harness Copilot Chat’s modes for *creation*, *implementation*, *validation*, *alternative reasoning*, and *curriculum navigation*—while staying aligned to the repository’s quality heuristics and syllabus.

---
### Related Docs
* Practice structure & heuristics: `PRACTICES_STRUCTURE.md` (tags: structure, heuristics)
* Creating practices: `COPILOT_CREATE_PRACTICE.md` (tags: create)
* Implementing & validating: `COPILOT_IMPLEMENT_PRACTICE.md` (tags: implement, validate)
* Inline prompt library: `COPILOT_INLINE_PROMPTS.md` (tags: inline-prompts)
* Progress & CI automation: `ci_progress.md` (tags: progress, ci)
