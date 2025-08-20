# List Searching and Counting - Practice 5

**Difficulty:** ⭐ (Very Easy)

**Related Topics:** List Search, Counting, Boolean Operations

## Objectives

- Learn to search for elements in lists
- Practice counting occurrences
- Understand membership testing

## Description

Master the ability to find and count elements in lists. These operations help you analyze list contents without modifying the list.

## Examples

```python
numbers = [1, 2, 3, 2, 4, 2]
print(count_occurrences(numbers, 2))  # 3
print(is_item_in_list(numbers, 5))    # False
print(find_first_index(numbers, 3))   # 2
```

## Your Tasks

1. **is_item_in_list(my_list, item)** - Check if item exists in list
2. **count_occurrences(my_list, item)** - Count how many times item appears
3. **find_first_index(my_list, item)** - Find index of first occurrence
4. **find_all_indices(my_list, item)** - Find all indices where item appears
5. **get_unique_items(my_list)** - Get list without duplicates
6. **has_duplicates(my_list)** - Check if list contains duplicate values
7. **find_max_value(my_list)** - Find largest value in list
8. **find_min_value(my_list)** - Find smallest value in list

## Hints

- Use `in` operator for membership testing
- Use `.count()` method for counting
- Use `.index()` method for finding position
- Loop through list to find all indices
- Convert to set and back for unique items
- Compare original length with unique length for duplicates

## Practice Cases

```python
test_data = [1, 2, 3, 2, 4, 2, 5]
# Expected results:
# count_occurrences(test_data, 2) -> 3
# find_all_indices(test_data, 2) -> [1, 3, 5]
# get_unique_items(test_data) -> [1, 2, 3, 4, 5]
# has_duplicates(test_data) -> True
```

Remember: These operations don't change the original list!