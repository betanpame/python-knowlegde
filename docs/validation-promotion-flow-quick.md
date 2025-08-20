<!-- COPILOT_CONTEXT_TAGS: validation, promotion, checklist, flow -->
# Validation & Promotion Flow (Quick)

Ultra‑concise reference for moving a practice `.py` file through statuses.

## Status Path

`# TODO:` → `# RESOLVED:` → `# VALIDATED:`

## Promote TODO → RESOLVED

- ≥3 meaningful LOC (non-blank, non-comment)
- At least one `def` or `class`
- No stray `pass` left as placeholder
- No extra `TODO` beyond first line

## Promote RESOLVED → VALIDATED

- All objectives implemented
- All Practice Cases & edge cases handled (empty, None, invalid type, boundary size)
- Zero heuristic warnings (`low_implementation_loc`, `todo_leftover`, `pass_leftover`, `missing_status`, `multi_status_conflict`)
- Docstring(s) on main function(s)
- Complexity reasonable or justified

## Deep Validation Micro-Steps

1. Structural audit (functions, returns, errors)
2. Edge case table (Case | Expected | Covered? | Fix)
3. Apply minimal fixes
4. Readability & naming pass
5. Alternative strategy (optional) compare
6. Final heuristic check → promote

## Copyable Macro

```text
VALIDATE FLOW:
1) Structure gaps?
2) Edge table & fixes
3) Readability + complexity
4) (Optional) alt strategy summary
5) If clean: promote to # VALIDATED: + rationale comment
```

## Heuristic Zero Checklist

- No leftover TODO/pass
- No duplicate/conflicting statuses
- Meaningful LOC ≥ threshold
- Runtime smoke passes (if used)
- Complexity < threshold OR commented rationale

---

### Related Docs

- Implementation guide: `COPILOT_IMPLEMENT_PRACTICE.md` (tags: implement, validate)
- Heuristics quick ref: `practices-heuristics-quality.md` (tags: heuristics)
- Structure basics: `practices-structure-basics.md` (tags: structure)
- Inline prompts: `COPILOT_INLINE_PROMPTS.md` (tags: inline-prompts)
