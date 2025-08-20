# List Slicing Basics - Practice 6

**Difficulty:** ⭐ (Very Easy)

**Related Topics:** List Slicing, Subsequences, Range Operations

## Objectives

- Master basic list slicing operations
- Learn to extract parts of lists
- Understand slice notation and step values

## Description

Learn to extract portions of lists using Python's slicing notation. Slicing allows you to get subsequences without modifying the original list.

## Examples

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_first_n_items(numbers, 3))     # [0, 1, 2]
print(get_last_n_items(numbers, 3))      # [7, 8, 9]
print(get_middle_items(numbers, 2, 5))   # [2, 3, 4]
```

## Your Tasks

1. **get_first_n_items(my_list, n)** - Get first n elements
2. **get_last_n_items(my_list, n)** - Get last n elements
3. **get_middle_items(my_list, start, end)** - Get elements from start to end
4. **get_every_second_item(my_list)** - Get every second element
5. **reverse_list(my_list)** - Get reversed copy of list
6. **get_odd_positioned_items(my_list)** - Get elements at odd indices
7. **get_even_positioned_items(my_list)** - Get elements at even indices
8. **skip_first_and_last(my_list)** - Get all elements except first and last

## Hints

- Use `my_list[:n]` for first n items
- Use `my_list[-n:]` for last n items
- Use `my_list[start:end]` for range
- Use `my_list[::2]` for every second item
- Use `my_list[::-1]` for reverse
- Use `my_list[1::2]` for odd positions
- Use `my_list[1:-1]` to skip first and last

## Practice Cases

```python
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected results:
# get_first_n_items(test_list, 3) -> [1, 2, 3]
# get_every_second_item(test_list) -> [1, 3, 5, 7, 9]
# reverse_list(test_list) -> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

Remember: Slicing creates new lists - it doesn't modify the original!