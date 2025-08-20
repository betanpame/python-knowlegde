# Advanced List Comprehensions - Practice 16

**Difficulty:** ⭐⭐⭐ (Easy-Medium)

**Related Topics:** List Comprehensions, Functional Programming, Advanced Filtering

## Objectives

- Master complex list comprehensions
- Combine multiple conditions and transformations
- Write concise and efficient list processing code

## Description

Advance your list comprehension skills by working with complex filtering, nested comprehensions, and multiple transformations in single expressions.

## Examples

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Squares of even numbers
result = [x**2 for x in numbers if x % 2 == 0]  # [4, 16, 36, 64, 100]

# Nested comprehension for matrix
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

## Your Tasks

1. **squares_of_evens(numbers)** - Squares of even numbers only
2. **words_with_vowels(words)** - Words containing vowels
3. **nested_multiplication_table(size)** - Create multiplication table
4. **conditional_transformations(numbers)** - Different operations based on conditions
5. **filter_and_transform_strings(strings)** - Complex string processing
6. **extract_numbers_from_mixed(mixed_list)** - Extract only numbers from mixed data
7. **create_coordinate_pairs(x_range, y_range)** - Generate coordinate combinations
8. **process_nested_data(nested_list)** - Work with complex nested structures

Remember: List comprehensions can replace many loops and make code more readable!