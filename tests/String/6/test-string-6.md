# Test String 6: String Concatenation

**Difficulty:** ⭐☆☆☆☆ (Very Easy)

**Related Topics:** String operations, concatenation

## Objective

Learn different ways to combine strings together.

## Requirements

Create functions that concatenate strings using different methods.

## Example

```python
str1 = "Hello"
str2 = "World"
result = concatenate_strings(str1, str2)  # "HelloWorld"
result_with_space = concatenate_with_separator(str1, str2, " ")  # "Hello World"
```

## Hints

- Use the `+` operator for simple concatenation
- Use `join()` method for multiple strings
- Consider using f-strings for formatted concatenation

## Test Cases

Your functions should handle:

1. `"Hello", "World"` → `"HelloWorld"`
2. `"Python", "Programming"` → `"PythonProgramming"`
3. `"", "Test"` → `"Test"`
4. `"Test", ""` → `"Test"`
5. With separator `" "`: `"Hello", "World"` → `"Hello World"`
