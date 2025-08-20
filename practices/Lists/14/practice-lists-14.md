# List Algorithms and Patterns - Practice 14

**Difficulty:** ⭐⭐⭐ (Easy-Medium)

**Related Topics:** Algorithms, Pattern Recognition, Problem Solving

## Objectives

- Implement common list algorithms
- Recognize and work with patterns in data
- Apply algorithmic thinking to list problems

## Description

Develop algorithmic solutions for common list processing tasks. Learn to recognize patterns and implement efficient solutions for data manipulation.

## Examples

```python
numbers = [1, 3, 2, 4, 3, 5, 3]
print(find_mode(numbers))              # 3 (most frequent)
print(remove_duplicates_preserve_order(numbers))  # [1, 3, 2, 4, 5]

data = [1, 2, 3, 4, 5]
print(rotate_list_left(data, 2))       # [3, 4, 5, 1, 2]
```

## Your Tasks

1. **find_mode(numbers)** - Find most frequently occurring number
2. **remove_duplicates_preserve_order(my_list)** - Remove duplicates keeping first occurrence
3. **rotate_list_left(my_list, positions)** - Rotate list left by n positions
4. **rotate_list_right(my_list, positions)** - Rotate list right by n positions
5. **find_missing_number(numbers, max_num)** - Find missing number in sequence
6. **partition_list(my_list, pivot)** - Split list around pivot value
7. **merge_sorted_lists(list1, list2)** - Merge two sorted lists maintaining order
8. **find_intersection_ordered(list1, list2)** - Find common elements preserving order

## Hints

- Use dictionaries to count frequencies for mode
- Use sets to track seen elements for duplicate removal
- List slicing can help with rotation operations
- Missing number can be found using mathematical properties
- Partition means elements < pivot, then pivot, then elements > pivot
- Merge sorted lists using two pointers technique
- Consider time complexity for large lists

## Practice Cases

```python
test_cases = [
    ([1, 2, 2, 3, 2], 2),  # mode
    ([1, 2, 1, 3, 2], [1, 2, 3]),  # remove duplicates
    ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),  # rotate left
    ([1, 2, 4, 5], 6, 3),  # missing number
    ([3, 1, 4, 1, 5], 3, [[1, 1], [3], [4, 5]])  # partition
]
```

## Bonus Challenges

- Implement efficient rotation without creating new lists
- Handle edge cases like empty lists or single elements
- Optimize for very large lists
- Add support for rotating by negative numbers

Remember: Focus on both correctness and efficiency!