# Practice String 14: String Split and Join Operations

**Difficulty:** ⭐⭐☆☆☆ (Easy-Medium)

**Related Topics:** String methods, list operations, text processing

## Objective

Master string splitting and joining operations for text processing tasks.

## Requirements

Create functions that split strings into lists and join lists into strings.

## Example

```python
text = "apple,banana,cherry"
fruits = split_by_delimiter(text, ",")  # ["apple", "banana", "cherry"]
rejoined = join_with_delimiter(fruits, " | ")  # "apple | banana | cherry"
```

## Hints

- Use `.split()` method to split strings
- Use `.join()` method to join lists into strings
- `.split()` without arguments splits on any whitespace
- Handle edge cases like empty strings and single words

## Practice Cases

1. `"apple,banana,cherry"` split by `","` → `["apple", "banana", "cherry"]`
2. `"Hello World Python"` split by space → `["Hello", "World", "Python"]`
3. `["a", "b", "c"]` joined with `"-"` → `"a-b-c"`
4. `"single"` split → `["single"]`
5. `""` split → `[]`