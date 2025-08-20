# Practice String 9: Basic String Repetition

**Difficulty:** ⭐☆☆☆☆ (Very Easy)

**Related Topics:** String operators, multiplication operator

## Objective

Learn to repeat strings using the multiplication operator.

## Requirements

Create functions that repeat strings a specified number of times.

## Example

```python
text = "Hi"
repeated = repeat_string(text, 3)  # "HiHiHi"
```

## Hints

- Use the `*` operator with strings: `"text" * 3`
- Handle edge cases like 0 repetitions
- Negative numbers should return empty string

## Practice Cases

1. `"Hi", 3` → `"HiHiHi"`
2. `"Python", 2` → `"PythonPython"`
3. `"Practice", 0` → `""`
4. `"A", 5` → `"AAAAA"`
5. `"Hello", 1` → `"Hello"`