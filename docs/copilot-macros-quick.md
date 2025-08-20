<!-- COPILOT_CONTEXT_TAGS: macros, prompts, quick-reference, inline-prompts -->
# Copilot Macros (Quick)

Short macro names you can paste into Chat/Inline prompts. Pair them with a file selection for best results.

| Macro | Purpose | Typical Mode |
|-------|---------|--------------|
| `NEW_PRACTICE_SCAFFOLD` | Create markdown scaffold for new practice | Agent |
| `PROMOTE_TODO` | Check readiness & promote TODO → RESOLVED | Ask/Inline |
| `DEEP_VALIDATE` | Multi-stage validation → VALIDATED | Agent |
| `ALT_STRATEGY` | Generate + compare alternative solution | Ask |
| `FIX_WARNINGS` | Clear listed heuristic warnings with minimal diff | Inline |
| `EDGE_TABLE` | Produce edge case coverage table | Inline |
| `SAFE_REFACTOR` | Refactor with signature & behavior constraints | Inline |
| `GAP_ANALYSIS` | Recommend next practices from syllabus + progress | Agent |

## Usage Pattern

```text
<MACRO>: <optional context refinement>

Example:
DEEP_VALIDATE: apply full validation flow; pause after each stage for approval.
```

## Prompt Suffix Boosters

- "Return unified diff only"
- "List issues first; wait for confirmation"
- "Do not alter validated functions"
- "Keep complexity class unchanged"

---

### Related Docs

- Inline prompt library: `COPILOT_INLINE_PROMPTS.md` (tags: inline-prompts)
- Chat usage strategies: `COPILOT_CHAT_USAGE.md` (tags: chat-usage)
- Validation flow quick ref: `validation-promotion-flow-quick.md` (tags: validation)
- Heuristics quick ref: `practices-heuristics-quality.md` (tags: heuristics)
