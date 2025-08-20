# Python Knowledge Curriculum

> Guided, AI‑accelerated Python practice set with structured progress tracking and Copilot‑centric workflows.

## 📚 Overview

Topic‑based practice folders under `practices/` progress through statuses (`# TODO:` → `# RESOLVED:` → `# VALIDATED:`). GitHub Copilot Chat (Agent + Ask + Inline) accelerates scaffold creation, implementation, validation, refactoring, and reflective comparison.

## 🗂 Directory Highlights

| Path | Purpose |
|------|---------|
| `practices/` | Topic folders each containing numbered practice slots (markdown + Python) |
| `docs/` | Workflow & reference documentation (see map) |
| `progress/` | Auto-generated dated progress dashboards & deltas |
| `badges/` | JSON endpoints for Shields.io progress badges |
| `plan/` | Curriculum syllabus and planning assets |
| `scripts/` | Automation (`generate_progress.py`) + future helpers |

## 🔑 Status Keywords

Place as first non-empty line of each primary practice `.py` file:

| Keyword | Meaning |
|---------|---------|
| `# TODO:` | Scaffold / not yet implemented |
| `# RESOLVED:` | Working implementation (meets objectives) |
| `# VALIDATED:` | Fully reviewed, heuristic-clean, educational completeness achieved |

## 🚀 Quick Start

```powershell
# Generate current progress dashboard
python scripts/generate_progress.py --stdout

# (Agent) Scaffold a new practice (see NEW_PRACTICE_SCAFFOLD macro)

# Implement logic, then promote when ready
# (Inline) use PROMOTE_TODO macro for readiness review

# Deep validation & edge cases
# (Agent) run DEEP_VALIDATE macro → consider ALT_STRATEGY

# Re-run progress with smoke tests for that topic
python scripts/generate_progress.py --only-topic Functions --stdout --smoke
```

## 🧠 Copilot-First Learning Flow

1. Scaffold markdown (`COPILOT_CREATE_PRACTICE.md`).
2. Implement minimal solution → promote to `# RESOLVED:`.
3. Deep validation + edge cases + docstring + alternative solutions → promote to `# VALIDATED:` (`COPILOT_IMPLEMENT_PRACTICE.md`).
4. Compare alternative strategies (performance, clarity, idioms).
5. Iterate heuristics to zero warnings; track funnel metrics via progress scripts.

## 🏷 Copilot Context Tagging

All major docs begin with a hidden HTML comment `<!-- COPILOT_CONTEXT_TAGS: ... -->`. Include one or more tag keywords in a prompt (e.g., `inline-prompts`, `validate`, `structure`) to bias retrieval toward those documents.

## 🔗 Core Documentation Map

### Full Guides

| Doc | Focus |
|-----|-------|
| `PRACTICES_STRUCTURE.md` | Canonical structure & detailed heuristics rationale |
| `COPILOT_CREATE_PRACTICE.md` | Scaffolding new practices (Agent flow) |
| `COPILOT_IMPLEMENT_PRACTICE.md` | Implementation → deep validation pipeline |
| `COPILOT_CHAT_USAGE.md` | Agent vs Ask vs Inline; context layering strategy |
| `COPILOT_INLINE_PROMPTS.md` | Prompt & macro catalog (inline & agent) |

### Quick References

| Doc | Focus |
|-----|-------|
| `practices-structure-basics.md` | Minimal structure cheat sheet |
| `practices-heuristics-quality.md` | Heuristic codes & promotion snapshot |
| `validation-promotion-flow-quick.md` | Condensed validation & promotion flow |
| `copilot-macros-quick.md` | Macro names & usage boosters |
| `chat-usage-quick.md` | Agent vs Ask + context packets |
| `inline-prompts-top10-quick.md` | Top 10 inline prompts |
| `create-practice-quick.md` | New practice checklist |

### Supporting / Legacy

| Doc | Focus |
|-----|-------|
| `ci_progress.md` | CI automation & badge endpoints |
| `progressBase.md` | Legacy snapshot example |

## 🧩 Common Copilot Macros (Inline / Agent)

| Macro | Purpose |
|-------|---------|
| `NEW_PRACTICE_SCAFFOLD` | Structured markdown creation |
| `PROMOTE_TODO` | Readiness checklist for TODO → RESOLVED |
| `DEEP_VALIDATE` | Multi-stage edge case & quality sweep |
| `ALT_STRATEGY` | Generate + compare alternative approach |
| `FIX_WARNINGS` | Resolve heuristic warnings with minimal diff |

## 🔄 Validation Funnel Targets

Track and improve these transitions:

1. Markdown created → Python file exists
2. Python file → `# RESOLVED:` (functional correctness baseline)
3. `# RESOLVED:` → `# VALIDATED:` (edge cases + clarity + docs)
4. Post-validation improvement: alternative strategies + refactors

## 🧪 Heuristic Cleanliness Checklist

Before promoting to `# VALIDATED:` ensure:

- No `low_implementation_loc` on RESOLVED/VALIDATED files
- No `todo_leftover` / `pass_leftover`
- Single status line present (`missing_status` cleared)
- No conflicting statuses (`multi_status_conflict`)
- Any `runtime_error:*` fixed
- Complexity warnings justified or refactored
- Docstring(s) on primary public function(s)

## 🛠 Progress Badges (Add After First CI Run)

```markdown
![Validated](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/<USER>/<REPO>/main/badges/validated.json)
![Resolved](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/<USER>/<REPO>/main/badges/resolved.json)
```

## ✨ Roadmap Ideas

- Add automated lightweight tests per practice
- Integrate complexity metrics into progress report
- Auto-suggest promotions when heuristics all clean
- Difficulty tiers & tagging taxonomy
- Visual topic heatmap (coverage vs validation %)

## 🙌 Contributing

Fork → branch → focused PR. Keep docs modular & small. Retain hidden tag blocks. Follow markdown lint basics (blank lines around headings, lists, tables; fenced blocks labeled; no tabs). Use descriptive commit messages (e.g., `feat(practices): add recursion practice 05 scaffold`, `chore(practices): promote strings 03 to VALIDATED`).

---

Happy learning — let Copilot accelerate *understanding*, not replace it.
