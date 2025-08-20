# Simple List Sorting - Practice 7

**Difficulty:** ⭐ (Very Easy)

**Related Topics:** Sorting, List Organization, Comparison

## Objectives

- Learn basic list sorting operations
- Understand ascending and descending order
- Practice with different data types

## Description

Master the fundamental sorting operations for lists. Sorting helps organize data for easier processing and analysis.

## Examples

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(sort_ascending(numbers))    # [1, 1, 2, 3, 4, 5, 6, 9]
print(sort_descending(numbers))   # [9, 6, 5, 4, 3, 2, 1, 1]

words = ["banana", "apple", "cherry"]
print(sort_words(words))          # ["apple", "banana", "cherry"]
```

## Your Tasks

1. **sort_ascending(my_list)** - Sort list in ascending order
2. **sort_descending(my_list)** - Sort list in descending order
3. **sort_words(my_list)** - Sort list of strings alphabetically
4. **sort_by_length(my_list)** - Sort strings by length
5. **is_sorted(my_list)** - Check if list is already sorted
6. **find_smallest(my_list)** - Find smallest value
7. **find_largest(my_list)** - Find largest value
8. **get_sorted_copy(my_list)** - Get sorted copy without changing original

## Hints

- Use `sorted()` function to create sorted copy
- Use `.sort()` method to sort in-place
- Use `reverse=True` parameter for descending order
- Use `key=len` for sorting by length
- Compare list with sorted version to check if sorted
- Use `min()` and `max()` functions for smallest/largest

## Practice Cases

```python
test_numbers = [5, 2, 8, 1, 9, 3]
test_words = ["dog", "cat", "elephant", "ant"]
# Expected results:
# sort_ascending(test_numbers) -> [1, 2, 3, 5, 8, 9]
# sort_by_length(test_words) -> ["dog", "cat", "ant", "elephant"]
```

Remember: `sorted()` creates a new list, `.sort()` modifies the original!