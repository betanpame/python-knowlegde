<!-- COPILOT_CONTEXT_TAGS: chat-usage, workflows, patterns -->
# Chat Workflow Blueprints

Copy + adapt these minimal scaffolds.

## 1. Bug Reproduction & Fix

```text
Goal: reproduce & patch
Symptom: <error/log>
Env: <python version / OS>
Suspect Areas: <files>
Steps Attempted: <bullets>
Need: root cause hypothesis list + next probe
Return: table(hypothesis, evidence, probe)
```

## 2. Feature Spike → Implementation

```text
Goal: explore feasibility for <feature>
Constraints: <perf / security / deadline>
Success: <measurable criteria>
Deliver: risk list + recommended minimal slice
Then: request implementation plan (agent mode)
```

## 3. Refactor Safely

```text
Goal: improve structure of <target>
Drivers: <duplication / complexity / clarity>
Risks: <regression domains>
Safety Nets: existing tests? yes/no
Return: ordered refactor steps + per-step risk note
```

## 4. Validation Pass

```text
Goal: validate implementation of <feature>
Artifacts: <PR link / file list>
Checklist Source: validation-promotion-flow-quick.md
Flags: <heuristics>
Return: findings categorized (bug, improvement, nit)
```

## 5. Guided Learning Drill

```text
Topic: <concept>
Level: <self-assessed>
Goal: reach ability to <apply/implement X>
Provide: spaced micro-exercises sequence (increasing difficulty)
Check: ask for answer only after attempt
```

---
 
## Related Docs

- Modes: `chat-agent-vs-ask.md`
- Context techniques: `chat-context-techniques.md`
- Quick usage: `chat-usage-quick.md`
