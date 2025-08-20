<!-- COPILOT_CONTEXT_TAGS: inline-prompts, top-prompts, refactor, validation -->
# Inline Prompts Top 10 (Quick)

Highest leverage copy/paste prompts.

| # | Purpose | Prompt Core |
|---|---------|-------------|
| 1 | Promote TODO | Review readiness (≥3 LOC, no pass/TODO) → unified diff only |
| 2 | Edge Table | Build Case | Expected | Handled? | Fix rows (no code yet) |
| 3 | Apply Edge Fixes | Patch only for uncovered cases; diff |
| 4 | Validate | Apply validation checklist → if clean promote & add rationale comment |
| 5 | Alt Strategies | Enumerate 2 strategies (Time/Space/Tradeoffs) |
| 6 | Implement Alt | Add solve_alt() w/ docstring + example |
| 7 | Refactor Simplify | Reduce branching, keep behavior & signature; diff only |
| 8 | Complexity Split | If complexity >10 propose 2-function split plan then diff |
| 9 | Fix Warnings | Given warnings (<paste>), clear minimally; diff |
| 10 | Docstring Enhance | Improve docstring (Args, Returns, 2 Examples, Edge Cases) diff only |

Tip: Add suffixes: "Return unified diff only" / "List issues first" for precision.

---
### Related Docs

- Full prompt library: `COPILOT_INLINE_PROMPTS.md` (tags: inline-prompts)
- Macros quick: `copilot-macros-quick.md` (tags: macros)
- Validation flow: `validation-promotion-flow-quick.md` (tags: validation)
