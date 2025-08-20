<!-- COPILOT_CONTEXT_TAGS: chat-usage, modes, agent-mode, ask-mode -->
# Chat Modes: Agent vs Ask

Concise distinction to select the right mode fast.

| Mode | Use For | Strengths | Risks | Guardrail Prompt Add‑On |
|------|---------|-----------|-------|-------------------------|
| Ask | Clarify concept, tiny refactor, single diff | Fast, focused | Shallow context | "Return unified diff only" |
| Agent | Multi-step plan, multi-file edits, validation flow | Structured, retains steps | Drift / scope creep | "List plan steps; pause after each" |

Decision Heuristic:

```text
If task >1 file OR >1 conceptual step → Agent else Ask.
```

Escalation Pattern:

1. Start in Ask to clarify ambiguity
2. Escalate to Agent with explicit plan & success criteria
3. Drop back to Ask for micro-queries mid plan

---
 
## Related Docs

- Context techniques: `chat-context-techniques.md` (tags: chat-usage)
- Workflow blueprints: `chat-workflow-blueprints.md` (tags: chat-usage)
- Quick usage summary: `chat-usage-quick.md` (tags: chat-usage)
