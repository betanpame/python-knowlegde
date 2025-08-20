<!-- COPILOT_CONTEXT_TAGS: validation, deep-dive, checklist, edge-cases -->
# Validation Deep Dive

Structured multi‑stage process to upgrade `# RESOLVED:` → `# VALIDATED:` deliberately.

## Stages

1. Structure Audit: required functions, return shapes, error handling policy.
2. Edge Case Table: Case | Expected | Covered? | Fix Plan.
3. Apply Minimal Fix Patch.
4. Readability & Naming: reduce branching, clarify intent, extract helpers.
5. Complexity Check: split if cyclomatic > target (≤10 ideal, justify if >10).
6. Alternative Strategy (optional): outline or implement `solve_alt()`.
7. Heuristic Sweep: ensure zero warnings.
8. Promote with Rationale comment.

## Edge Case Table Prompt

```text
Build table: Case | Expected | Covered? | Fix. Do not change code yet.
```

## Promotion Rationale Template

```text
Validation Rationale:
- Objectives satisfied: <summary>
- Edge cases covered: <list>
- Complexity: O(...)
- Alternative considered: <yes/no + brief>
- No heuristic warnings outstanding.
```

## Diff Guardrails

- Avoid large rewrites
- Behavior parity required (add asserts to check if uncertain)
- Keep docstring updated with examples & edge notes

---
### Related Docs

- Skeleton quick: `implementation-skeleton-quick.md` (tags: implement)
- Promotion flow quick: `validation-promotion-flow-quick.md` (tags: validation)
- Alternative strategies: `alternative-strategies-learning.md` (tags: alternatives)
- Full guide index: `COPILOT_IMPLEMENT_PRACTICE.md` (tags: implement, validate)
