<!-- COPILOT_CONTEXT_TAGS: chat-usage, context-injection, retrieval -->
# Chat Context Techniques

Goal: maximize answer relevance while minimizing tokens.

## Core Patterns

| Pattern | When | Snippet Template |
|---------|------|------------------|
| File List | Multi-file change summary | `Files: a.py (add func), b.py (fix bug)` |
| Inline Excerpt | Need model to see specific block | ```Excerpt (foo.py lines 10-34):``` then paste |
| Structural Map | Large module orientation | `Structure: class A→methods; utils/helpers: parse(), format()` |
| Status Summary | Track lifecycle states | `Status: foo (#RESOLVED), bar (#TODO)` |
| Heuristic Flags | Drive targeted fixes | `Flags: low_implementation_loc:foo, missing_docstring:bar` |

## Injection Heuristics

1. Prefer smallest artifact that makes ambiguity zero
2. Replace narratives with enumerated facts
3. Strip comments unless clarifying intent
4. Collapse sequential unchanged lines into ranges
5. Keep < 30 lines raw excerpt whenever possible

## Anti-Patterns

- Dumping entire files without justification
- Repeating unchanged context every turn
- Mixing planning + execution requests in one blob

## Micro-Prompts (Paste Friendly)

```text
Context Pack v1
Files: <short list>
Goal: <succinct objective>
Constraints: <strict limits>
Open Questions: <bullets>
Return: <format>
```

```text
Delta Focus
Changed: <files>
New Flags: <heuristics>
Need: identify regression risk areas only
```

---
 
## Related Docs

- Modes: `chat-agent-vs-ask.md`
- Workflows: `chat-workflow-blueprints.md`
- Quick usage: `chat-usage-quick.md`
