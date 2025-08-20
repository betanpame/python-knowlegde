# Practice String 12: String Replace Basic

**Difficulty:** ⭐☆☆☆☆ (Very Easy)

**Related Topics:** String methods, text replacement

## Objective

Learn to replace characters or substrings in text using the replace method.

## Requirements

Create functions that replace text in strings.

## Example

```python
text = "Hello World"
result = replace_text(text, "World", "Python")  # "Hello Python"
```

## Hints

- Use `.replace(old, new)` method
- The method replaces ALL occurrences by default
- Use `.replace(old, new, count)` to limit replacements
- Original string is not modified (strings are immutable)

## Practice Cases

1. `"Hello World", "World", "Python"` → `"Hello Python"`
2. `"test test test", "test", "demo"` → `"demo demo demo"`
3. `"Python", "Java", "C++"` → `"Python"` (no change)
4. `"aaa", "a", "b"` → `"bbb"`
5. `"Hello", "l", "L"` → `"HeLLo"`