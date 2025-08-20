# Practice String 13: String Strip and Clean

**Difficulty:** ⭐☆☆☆☆ (Very Easy)

**Related Topics:** String methods, whitespace removal

## Objective

Learn to remove whitespace and unwanted characters from strings.

## Requirements

Create functions that clean strings by removing whitespace and specific characters.

## Example

```python
text = "  Hello World  "
clean = strip_whitespace(text)  # "Hello World"
```

## Hints

- Use `.strip()` to remove leading and trailing whitespace
- Use `.lstrip()` to remove only leading whitespace
- Use `.rstrip()` to remove only trailing whitespace
- `.strip(chars)` can remove specific characters

## Practice Cases

1. `"  Hello World  "` → `"Hello World"`
2. `"   Python   "` → `"Python"`
3. `"...Hello..."` with dots → `"Hello"`
4. `"Practice"` (no whitespace) → `"Practice"`
5. `"   "` (only spaces) → `""`