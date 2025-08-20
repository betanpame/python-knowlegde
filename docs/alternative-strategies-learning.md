<!-- COPILOT_CONTEXT_TAGS: alternatives, comparative, learning, refactor -->
# Alternative Strategies & Comparative Learning

Use after a stable validated baseline exists.

## Purposes

- Contrast paradigms (iterative vs recursive, comprehension vs loops, data structure choices)
- Explore performance tradeoffs
- Reinforce conceptual breadth

## Prompt Core

```text
List 2–3 distinct solution strategies: table (Approach | Core Idea | Time | Space | Tradeoffs | When Prefer). Then implement most contrasting as solve_alt() with full docstring & example. Keep original solve() unchanged.
```

## Comparative Analysis Prompt

```text
Compare solve vs solve_alt: readability, asymptotic complexity, constant factors, extensibility, cognitive load. Output markdown bullet list.
```

## Refactoring Caution

- Do not inflate codebase; remove alt if redundant
- Keep solve_alt() under similar complexity budget
- Document decision; learners should see why choose one

## Micro-Benchmark Stub (Optional)

```python
import time
data = ...  # representative input
for fn in (solve, solve_alt):
    start = time.perf_counter(); fn(data); dur = (time.perf_counter()-start)*1e6
    print(fn.__name__, f"{dur:.1f}µs")
```

---
### Related Docs

- Deep validation: `validation-deep-dive.md` (tags: validation)
- Implementation index: `COPILOT_IMPLEMENT_PRACTICE.md` (tags: implement)
- Prompt library: `COPILOT_INLINE_PROMPTS.md` (tags: inline-prompts)
