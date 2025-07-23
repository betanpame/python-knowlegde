# Basic List Operations - Test 3

**Difficulty:** ⭐ (Very Easy)

**Related Topics:** List Basics, Indexing, Length

## Objectives

- Learn fundamental list operations
- Practice basic list access and manipulation
- Understand list indexing and length

## Description

Master the most basic list operations including creating lists, accessing elements, and getting list information. These are the foundation skills for all list programming.

## Examples

```python
# Creating and accessing lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])        # "apple"
print(len(fruits))      # 3

# Basic list operations
numbers = [1, 2, 3, 4, 5]
first = get_first_element(numbers)    # 1
last = get_last_element(numbers)      # 5
length = get_list_length(numbers)     # 5
```

## Your Tasks

1. **get_first_element(my_list)** - Return the first element of a list
2. **get_last_element(my_list)** - Return the last element of a list
3. **get_list_length(my_list)** - Return the number of elements in a list
4. **get_middle_element(my_list)** - Return the middle element (for odd-length lists)
5. **is_list_empty(my_list)** - Check if a list is empty
6. **get_element_at_position(my_list, index)** - Get element at specific index
7. **create_number_list(start, end)** - Create list of numbers from start to end
8. **combine_two_lists(list1, list2)** - Combine two lists into one

## Hints

- Use square brackets `[]` for indexing
- Index `-1` refers to the last element
- `len()` function gives you the list length
- Empty lists have length 0
- Handle edge cases like empty lists
- Use `+` operator to combine lists
- `range()` can help create number sequences

## Test Cases

```python
# Test data for validation
test_cases = [
    ([1, 2, 3], 1, 3, 3),           # first, last, length
    (["a", "b", "c", "d", "e"], "a", "e", 5),
    ([42], 42, 42, 1),              # single element
    ([], None, None, 0),            # empty list
    ([1, 2, 3, 4, 5], 3),          # middle element
    (([1, 2], [3, 4]), [1, 2, 3, 4])  # combined
]
```

## Bonus Challenges

- Handle negative indices properly
- Add error handling for invalid indices
- Create lists with different data types
- Practice with nested lists

Remember: Lists are ordered collections that can contain any type of data, including other lists!
