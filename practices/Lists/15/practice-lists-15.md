# Nested Lists and 2D Operations - Practice 15

**Difficulty:** ⭐⭐⭐ (Easy-Medium)

**Related Topics:** Nested Lists, 2D Arrays, Matrix Operations

## Objectives

- Work with lists containing other lists
- Perform operations on 2D data structures
- Navigate and manipulate nested data

## Description

Master working with nested lists (lists of lists) which represent 2D data like matrices, tables, or grids. Learn to access, modify, and analyze 2D structures.

## Examples

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(get_element(matrix, 1, 2))        # 6
print(sum_all_elements(matrix))         # 45
print(transpose_matrix(matrix))         # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

## Your Tasks

1. **get_element(matrix, row, col)** - Get element at specific position
2. **set_element(matrix, row, col, value)** - Set element at position
3. **sum_all_elements(matrix)** - Sum all numbers in 2D list
4. **transpose_matrix(matrix)** - Swap rows and columns
5. **get_row(matrix, row_index)** - Extract specific row
6. **get_column(matrix, col_index)** - Extract specific column
7. **flatten_2d_list(matrix)** - Convert 2D list to 1D
8. **create_identity_matrix(size)** - Create identity matrix of given size

Remember: Nested lists allow you to work with table-like data structures!