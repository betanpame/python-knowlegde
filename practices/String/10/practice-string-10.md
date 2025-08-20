# Practice String 10: String Comparison

**Difficulty:** ⭐☆☆☆☆ (Very Easy)

**Related Topics:** Comparison operators, string equality

## Objective

Learn to compare strings using comparison operators.

## Requirements

Create functions that compare strings in different ways.

## Example

```python
result = strings_equal("Hello", "Hello")  # True
result = strings_equal("Hello", "hello")  # False
```

## Hints

- Use `==` for equality comparison
- Use `!=` for inequality comparison
- String comparison is case-sensitive by default
- Use `.lower()` or `.upper()` for case-insensitive comparison

## Practice Cases

1. `"Hello", "Hello"` → `True`
2. `"Hello", "hello"` → `False` (case-sensitive)
3. `"Python", "Java"` → `False`
4. `"", ""` → `True`
5. Case-insensitive: `"HELLO", "hello"` → `True`