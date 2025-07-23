# Test String 5: String Uppercase and Lowercase

**Difficulty:** ⭐☆☆☆☆ (Very Easy)

**Related Topics:** String methods, case conversion

## Objective

Learn to convert strings between uppercase and lowercase using built-in methods.

## Requirements

Create functions that convert strings to uppercase and lowercase.

## Example

```python
text = "Hello World"
upper_text = to_uppercase(text)  # "HELLO WORLD"
lower_text = to_lowercase(text)  # "hello world"
```

## Hints

- Use `.upper()` method for uppercase conversion
- Use `.lower()` method for lowercase conversion
- These methods return new strings (strings are immutable)

## Test Cases

Your functions should handle:

1. `"Hello World"` → upper: `"HELLO WORLD"`, lower: `"hello world"`
2. `"PYTHON"` → upper: `"PYTHON"`, lower: `"python"`
3. `"MiXeD cAsE"` → upper: `"MIXED CASE"`, lower: `"mixed case"`
4. `"123"` → upper: `"123"`, lower: `"123"`
5. `""` → upper: `""`, lower: `""`
