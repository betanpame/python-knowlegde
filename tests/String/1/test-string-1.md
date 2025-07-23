# Test String 1: String Reversal

**Difficulty:** ⭐☆☆☆☆ (Very Easy)

**Related Topics:** String indexing, slicing, basic string operations

## Objective

Learn basic string manipulation by reversing the order of characters in a string.

## Requirements

Given a variable with a string, create another variable with all the content reversed.

## Example

```python
myStr = 'Pamela'
# Your code here
res = 'alemaP'
```

## Hints

- Use string slicing with negative step: `string[::-1]`
- Alternative: use `reversed()` function with `join()`
- Remember that strings are immutable in Python

## Test Cases

Your solution should handle:

1. `"Pamela"` → `"alemaP"`
2. `"Python"` → `"nohtyP"`
3. `""` → `""` (empty string)
4. `"a"` → `"a"` (single character)
5. `"12345"` → `"54321"` (numbers as string)
