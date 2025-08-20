<!-- COPILOT_CONTEXT_TAGS: structure, basics, files, status-keywords -->
# Practices Structure (Basics)

Goal: Quick reference for how a practice is laid out.

## Essentials

- Path: `practices/<Topic>/<Number>/`
- Markdown: `practice-<slug>-<Number>.md`
- Python (optional initially): `practice-<slug>-<Number>.py`
- Slug = kebab-case of Topic (ControlFlow → control-flow)

## Status Keywords (First Non‑Empty Line)

| Keyword | Meaning |
|---------|---------|
| `# TODO:` | Scaffold / not implemented |
| `# RESOLVED:` | Working but not fully validated |
| `# VALIDATED:` | Clean, reviewed, edge cases handled |

## Promotion Rules (Condensed)

- Promote TODO→RESOLVED when ≥3 meaningful LOC & no stray `pass`/`TODO`.
- Promote RESOLVED→VALIDATED only after edge cases + zero warnings.

## Folder Ready Checklist

- [ ] Correct names
- [ ] Markdown sections: Description, Objectives, Tasks, Examples, Hints, Practice Cases, Bonus
- [ ] Status keyword at top of `.py`

> For heuristics & warnings see: `practices-heuristics-quality.md`.

---

### Related

- Extended structure & rationale: `PRACTICES_STRUCTURE.md`
- Heuristics & warnings: `practices-heuristics-quality.md`
- Create workflow: `COPILOT_CREATE_PRACTICE.md`
- Implement & validate: `COPILOT_IMPLEMENT_PRACTICE.md`
