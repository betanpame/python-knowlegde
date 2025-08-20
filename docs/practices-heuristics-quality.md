<!-- COPILOT_CONTEXT_TAGS: heuristics, quality, warnings, promotion -->
# Practice Heuristics & Quality Signals (Quick)

Core warnings emitted by `scripts/generate_progress.py`.

## Warning Codes

| Code | Trigger | Fix |
|------|--------|-----|
| `low_implementation_loc` | <3 meaningful LOC in RESOLVED/VALIDATED | Flesh out logic |
| `todo_leftover` | "TODO" appears beyond first line | Remove or convert to comment rationale |
| `pass_leftover` | Stray `pass` after implementation | Remove / replace with logic |
| `missing_status` | No leading status line | Add `# TODO:` / promote appropriately |
| `multi_status_conflict` | Multiple .py files with differing statuses | Consolidate or align |
| `runtime_error:<msg>` | Smoke run raised exception | Fix failure cause |
| `missing_docstring:<fn>` | (optional flag) public fn lacks docstring | Add concise docstring |
| `high_complexity:<fn>:<score>` | Complexity > threshold | Refactor / justify |

## Clean File Criteria (VALIDATED)

- Status `# VALIDATED:` on first line
- Zero warnings
- Docstring on main function(s)
- Edge cases handled (empty, None, invalid type, boundary size)

## Promotion Snapshot

| From | To | Conditions |
|------|----|------------|
| TODO | RESOLVED | ≥3 LOC, at least one def/class, no leftover pass/TODO |
| RESOLVED | VALIDATED | All edge cases covered, zero warnings, clarity pass |

> See full guide: `COPILOT_IMPLEMENT_PRACTICE.md` for deep validation flow.

---

### Related

- Structure basics: `practices-structure-basics.md`
- Full structure spec: `PRACTICES_STRUCTURE.md`
- Creation guide: `COPILOT_CREATE_PRACTICE.md`
- Implementation guide: `COPILOT_IMPLEMENT_PRACTICE.md`
- Inline prompts: `COPILOT_INLINE_PROMPTS.md`
