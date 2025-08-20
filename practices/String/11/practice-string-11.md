# Practice String 11: String Startswith and Endswith

**Difficulty:** ⭐☆☆☆☆ (Very Easy)

**Related Topics:** String methods, prefix and suffix checking

## Objective

Learn to check if strings start or end with specific text.

## Requirements

Create functions that check string prefixes and suffixes.

## Example

```python
text = "Python Programming"
starts = starts_with(text, "Python")  # True
ends = ends_with(text, "ing")  # True
```

## Hints

- Use `.startswith()` method to check prefixes
- Use `.endswith()` method to check suffixes
- These methods are case-sensitive
- They can accept tuples of strings to check multiple options

## Practice Cases

1. `"Python Programming", "Python"` → `True` (starts with)
2. `"Python Programming", "Java"` → `False` (starts with)
3. `"Python Programming", "ing"` → `True` (ends with)
4. `"Hello World", "World"` → `True` (ends with)
5. `"Hello World", "world"` → `False` (case-sensitive)