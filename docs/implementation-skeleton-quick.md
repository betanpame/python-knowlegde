<!-- COPILOT_CONTEXT_TAGS: implement, skeleton, todo-to-resolved, starter -->
# Implementation Skeleton (Quick)

Focused steps to go from fresh scaffold to `# RESOLVED:`.

## Objectives

- Create starter `.py` with first line `# TODO:`
- Add minimal working logic (≥3 meaningful LOC)
- Remove placeholder `pass` / stray internal TODOs
- Decide public function names (usually `solve()`)

## Minimal Prompt Sequence

1. "Generate starter Python file for practice <topic>/<n> with # TODO: header and solve() stub (docstring: Args, Returns, 2 edge cases)."
2. "Implement minimal logic only; keep status # TODO:." (prevents premature promotion)
3. "Review readiness for RESOLVED (≥3 LOC, no pass/TODO leftover, at least one def); if ready produce diff updating header to # RESOLVED:."

## Skeleton Quality Hints

- Keep logic linear first; avoid early optimizations
- Add docstring early (easier to evolve than write later)
- Edge case placeholders: comment or docstring note (not TODO keywords)

## Promotion Criteria (Copy)

```text
READY FOR RESOLVED IF:
- ≥3 meaningful LOC
- Contains at least one def or class
- No 'pass' or stray TODO below first line
```

---
### Related Docs

- Deep validation: `validation-deep-dive.md` (tags: validation)
- Full implementation flow: `COPILOT_IMPLEMENT_PRACTICE.md` (tags: implement, validate)
- Promotion flow quick: `validation-promotion-flow-quick.md` (tags: validation)
- Heuristics: `practices-heuristics-quality.md` (tags: heuristics)
