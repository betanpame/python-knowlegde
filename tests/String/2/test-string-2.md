# Test String 2: String Manipulation Methods

**Difficulty:** ⭐⭐☆☆☆ (Easy-Medium)

**Related Topics:** String methods, text processing

## Objective
Create a function that cleans and formats user input text by applying multiple string methods.

## Requirements
Given a messy user input string, create a function `clean_text(text)` that:
1. Removes leading and trailing whitespace
2. Converts to title case
3. Removes extra spaces between words (only single spaces allowed)
4. Replaces all occurrences of "bad" with "good"

## Example
```python
messy_input = "  hello   world  this is bad  text bad  "
result = clean_text(messy_input)
# Expected output: "Hello World This Is Good Text Good"
```

## Hints
- Use `.strip()` for removing leading/trailing whitespace
- Use `.title()` for title case conversion
- Use `.split()` and `.join()` to handle multiple spaces
- Use `.replace()` for word substitution

## Test Cases
Your function should handle these cases:
1. `"  python   programming  "` → `"Python Programming"`
2. `"bad code is bad"` → `"Good Code Is Good"`
4. `"   single   "` → `"Single"`
