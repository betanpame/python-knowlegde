# Test String 7: String Contains Check

**Difficulty:** ⭐☆☆☆☆ (Very Easy)

**Related Topics:** Membership operators, string searching

## Objective

Learn to check if a string contains specific characters or substrings.

## Requirements

Create functions that check if strings contain specific text.

## Example

```python
text = "Python Programming"
contains_python = check_contains(text, "Python")  # True
contains_java = check_contains(text, "Java")  # False
```

## Hints

- Use the `in` operator to check membership
- Remember that string searches are case-sensitive
- Consider using `.lower()` for case-insensitive searches

## Test Cases

Your functions should handle:

1. `"Python Programming", "Python"` → `True`
2. `"Python Programming", "Java"` → `False`
3. `"Hello World", "o"` → `True`
4. `"Hello World", "xyz"` → `False`
5. Case-insensitive: `"HELLO", "hello"` → `True`
