<!-- COPILOT_CONTEXT_TAGS: chat-usage, agent-mode, ask-mode, context, prompts -->
# Chat Usage (Quick)

Agent vs Ask at a glance + minimal context strategy.

## Mode Selection

| Mode | Use When | Strength | Guardrail |
|------|----------|----------|-----------|
| Ask | Single fact, tiny refactor, clarify concept | Fast | Keep scope to 1 intent |
| Agent | Multi-file edits, scaffold, validation flow, alt strategies | Structured steps | Provide explicit plan steps |

## Minimal Context Packets

| Goal | Key Files |
|------|-----------|
| Create practice | `PRACTICES_STRUCTURE.md`, target topic folder, syllabus excerpt |
| Implement | Practice `.md` + similar validated `.py` + `COPILOT_IMPLEMENT_PRACTICE.md` |
| Validate | Practice `.py` + `validation-promotion-flow-quick.md` + heuristics quick ref |
| Clear warnings | Target `.py` + warning lines copied from progress report |

## High-Value Prompt Starters

- "List structural gaps vs markdown spec; no code yet."
- "Edge case table (Case | Expected | Covered? | Fix)."
- "Promote readiness TODO→RESOLVED (criteria...) diff only."
- "Deep validate steps 1–3 then pause."
- "Produce alt strategy table; choose one to implement as solve_alt()."

## Guardrail Suffixes

- "Return unified diff only"
- "List issues first; await confirm"
- "Do not change public signature"
- "Keep complexity class"

---
### Related Docs

- Full chat guide: `COPILOT_CHAT_USAGE.md` (tags: chat-usage)
- Macro list: `copilot-macros-quick.md` (tags: macros)
- Validation flow: `validation-promotion-flow-quick.md` (tags: validation)
- Inline prompts: `COPILOT_INLINE_PROMPTS.md` (tags: inline-prompts)
