# Practice Lists 2: List Comprehensions and Advanced Operations

**Difficulty:** ⭐⭐⭐☆☆ (Medium)

**Related Topics:** List comprehensions, filtering, mapping, nested lists

## Objective

Create functions that use list comprehensions to process and transform data efficiently.

## Requirements

Implement the following functions using list comprehensions:

1. `filter_even_squares(numbers)` - Return squares of even numbers only
2. `extract_initials(names)` - Extract first letter of each word in each name
3. `flatten_matrix(matrix)` - Flatten a 2D list into 1D
4. `filter_long_words(sentences, min_length)` - Get words longer than min_length from all sentences
5. `create_multiplication_table(n)` - Create an n×n multiplication table

## Examples

```python
numbers = [1, 2, 3, 4, 5, 6]
result = filter_even_squares(numbers)  # [4, 16, 36]

names = ["John Doe", "Jane Smith", "Bob Wilson"]
initials = extract_initials(names)  # [["J", "D"], ["J", "S"], ["B", "W"]]

matrix = [[1, 2], [3, 4], [5, 6]]
flat = flatten_matrix(matrix)  # [1, 2, 3, 4, 5, 6]
```

## Hints

- Use `if` conditions in list comprehensions for filtering
- Use nested list comprehensions for 2D operations
- Use `.split()` with list comprehensions for word processing
- Use `range()` with list comprehensions for generating sequences

## Practice Cases

Your functions should handle:

1. Empty lists and edge cases
2. Lists with mixed data types where applicable
3. Single-element lists
4. Large datasets efficiently