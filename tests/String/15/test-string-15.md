# Test String 15: String Formatting and Templates

**Difficulty:** ⭐⭐☆☆☆ (Easy-Medium)

**Related Topics:** String formatting, f-strings, format method

## Objective

Learn different string formatting techniques including f-strings, .format(), and % formatting.

## Requirements

Create functions that format strings using different methods.

## Example

```python
name = "Alice"
age = 25
result = format_with_f_string(name, age)  # "Hello Alice, you are 25 years old"
```

## Hints

- Use f-strings: `f"Hello {name}"`
- Use .format(): `"Hello {}".format(name)`
- Use % formatting: `"Hello %s" % name`
- f-strings are the most modern and preferred method

## Test Cases

1. Format person info: name="Alice", age=25
2. Format numbers with decimals: value=3.14159, precision=2
3. Format with multiple variables
4. Format with expressions inside f-strings
5. Handle different data types
