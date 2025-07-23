# Tuple vs List Differences - Test 3

**Difficulty:** ⭐ (Very Easy)

**Related Topics:** Immutability, Performance, Data Types

## Objectives

- Understand key differences between tuples and lists
- Learn when to use tuples vs lists
- Practice converting between tuples and lists

## Description

Learn the fundamental differences between tuples and lists, focusing on immutability, performance, and appropriate use cases.

## Examples

```python
# Converting between types
my_list = [1, 2, 3]
my_tuple = convert_list_to_tuple(my_list)     # (1, 2, 3)
back_to_list = convert_tuple_to_list(my_tuple)  # [1, 2, 3]

# Testing immutability
result = can_modify_tuple((1, 2, 3))  # False
result = can_modify_list([1, 2, 3])   # True
```

## Your Tasks

1. **convert_list_to_tuple(my_list)** - Convert list to tuple
2. **convert_tuple_to_list(my_tuple)** - Convert tuple to list
3. **can_modify_tuple(my_tuple)** - Test if tuple can be modified (should return False)
4. **can_modify_list(my_list)** - Test if list can be modified (should return True)
5. **compare_access_speed(data)** - Compare tuple vs list access (conceptual)
6. **find_hashable_items(items)** - Identify which items can be used as dict keys
7. **create_coordinate_tuple(x, y)** - Create coordinate tuple
8. **extract_coordinates(coord_tuple)** - Extract x, y from coordinate tuple

Remember: Tuples are immutable and hashable, lists are mutable but not hashable!
