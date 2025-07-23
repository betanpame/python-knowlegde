# List Comparison Operations - Test 9

**Difficulty:** ⭐ (Very Easy)

**Related Topics:** List Comparison, Equality, Boolean Logic

## Objectives

- Learn to compare lists
- Understand list equality and differences
- Practice set operations with lists

## Description

Master comparing lists and finding relationships between them. These operations are essential for data analysis and validation.

## Examples

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]

print(are_lists_equal(list1, list2))     # True
print(have_same_elements(list1, list3))  # True
print(find_common_elements(list1, [2, 3, 4]))  # [2, 3]
```

## Your Tasks

1. **are_lists_equal(list1, list2)** - Check if lists are exactly equal
2. **have_same_elements(list1, list2)** - Check if lists contain same elements (any order)
3. **find_common_elements(list1, list2)** - Find elements in both lists
4. **find_different_elements(list1, list2)** - Find elements only in first list
5. **are_lists_same_length(list1, list2)** - Check if lists have same length
6. **is_list_subset(list1, list2)** - Check if list1 is subset of list2
7. **combine_unique_elements(list1, list2)** - Combine lists without duplicates
8. **find_missing_elements(list1, list2)** - Find what's in list2 but not list1

Remember: Compare contents, not just references!
