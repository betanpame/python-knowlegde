# Tuple Slicing and Access - Test 4

**Difficulty:** ⭐ (Very Easy)

**Related Topics:** Slicing, Subsequences, Index Operations

## Objectives

- Master tuple slicing operations
- Learn to extract parts of tuples
- Understand slice notation with tuples

## Description

Learn to extract portions of tuples using Python's slicing notation. Since tuples are immutable, slicing creates new tuples.

## Examples

```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(get_first_n_elements(numbers, 3))     # (0, 1, 2)
print(get_last_n_elements(numbers, 3))      # (7, 8, 9)
print(get_range_elements(numbers, 2, 5))    # (2, 3, 4)
```

## Your Tasks

1. **get_first_n_elements(my_tuple, n)** - Get first n elements
2. **get_last_n_elements(my_tuple, n)** - Get last n elements  
3. **get_range_elements(my_tuple, start, end)** - Get elements from start to end
4. **get_every_second_element(my_tuple)** - Get every second element
5. **reverse_tuple(my_tuple)** - Get reversed tuple
6. **skip_first_and_last(my_tuple)** - Get all elements except first and last
7. **get_odd_positioned_elements(my_tuple)** - Get elements at odd indices
8. **get_even_positioned_elements(my_tuple)** - Get elements at even indices

Remember: Tuple slicing creates new tuples!
