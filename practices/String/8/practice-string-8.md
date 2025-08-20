# Practice String 8: String Indexing and Character Access

**Difficulty:** ⭐☆☆☆☆ (Very Easy)

**Related Topics:** String indexing, character access, negative indexing

## Objective

Learn to access individual characters in strings using indexing.

## Requirements

Create functions that access characters at specific positions in strings.

## Example

```python
text = "Python"
first_char = get_first_character(text)  # "P"
last_char = get_last_character(text)    # "n"
char_at_index = get_character_at_index(text, 2)  # "t"
```

## Hints

- Use square brackets `[]` for indexing
- Remember that indexing starts at 0
- Use negative indices to access from the end: `[-1]` for last character
- Handle index out of range errors

## Practice Cases

Your functions should handle:

1. `"Python"` first character → `"P"`
2. `"Python"` last character → `"n"`
3. `"Python"` character at index 2 → `"t"`
4. `"Hello"` character at index 0 → `"H"`
5. Empty string should handle gracefully