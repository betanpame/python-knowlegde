# List Modification Basics - Practice 4

**Difficulty:** ⭐ (Very Easy)

**Related Topics:** List Methods, Adding Elements, Removing Elements

## Objectives

- Learn basic list modification methods
- Practice adding and removing elements
- Understand list mutability

## Description

Learn how to modify lists by adding and removing elements using built-in list methods. Lists are mutable, meaning you can change them after creation.

## Examples

```python
# Adding elements
fruits = ["apple", "banana"]
add_to_end(fruits, "cherry")
print(fruits)  # ["apple", "banana", "cherry"]

# Removing elements
numbers = [1, 2, 3, 2, 4]
remove_first_occurrence(numbers, 2)
print(numbers)  # [1, 3, 2, 4]
```

## Your Tasks

1. **add_to_end(my_list, item)** - Add item to end of list
2. **add_to_beginning(my_list, item)** - Add item to beginning of list
3. **remove_first_occurrence(my_list, item)** - Remove first occurrence of item
4. **remove_last_element(my_list)** - Remove and return last element
5. **clear_list(my_list)** - Remove all elements from list
6. **add_multiple_items(my_list, items)** - Add multiple items to end
7. **insert_at_position(my_list, index, item)** - Insert item at specific position
8. **remove_at_position(my_list, index)** - Remove item at specific position

## Hints

- Use `.append()` to add to end
- Use `.insert(0, item)` to add to beginning
- Use `.remove()` to remove first occurrence
- Use `.pop()` to remove and return last element
- Use `.clear()` to empty list
- Use `.extend()` to add multiple items
- Handle cases where item doesn't exist

## Practice Cases

```python
# Practice scenarios
original = [1, 2, 3]
after_append = [1, 2, 3, 4]
after_insert = [0, 1, 2, 3, 4]
after_remove = [0, 2, 3, 4]
after_clear = []
```

## Bonus Challenges

- Add error handling for invalid operations
- Create a function to remove all occurrences of an item
- Implement safe removal that doesn't error if item missing

Remember: List methods modify the original list - they don't create a new list!