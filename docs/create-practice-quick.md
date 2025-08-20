<!-- COPILOT_CONTEXT_TAGS: create, scaffold, practice, checklist -->
# Create Practice (Quick)

One-screen checklist for new practice scaffolds.

## Steps

1. Identify topic + next index (fill gaps allowed).
2. Derive slug (camel → kebab).
3. Create folder `practices/<Topic>/<N>/`.
4. Create markdown with sections: Description, Objectives, Tasks, Examples, Hints, Practice Cases, Bonus.
5. (Optional) Add `.py` with first line `# TODO:` + `solve()` stub.
6. Run progress generator (topic-only) to confirm detection.

## Macro Prompt Core

```text
NEW_PRACTICE_SCAFFOLD: Topic=<Topic> Index=<N> Focus=<concepts>; generate markdown with required sections; concise instructional tone; no solution code.
```

## Quality Quick Checks

- Objectives actionable (start with verb)
- ≥4 Practice Cases (incl. one edge case)
- Bonus is stretch/extension, not duplicate task
- Examples runnable & minimal

---
### Related Docs

- Full creation guide: `COPILOT_CREATE_PRACTICE.md` (tags: create)
- Structure basics: `practices-structure-basics.md` (tags: structure)
- Heuristics quick: `practices-heuristics-quality.md` (tags: heuristics)
- Implementation guide: `COPILOT_IMPLEMENT_PRACTICE.md` (tags: implement, validate)
