# Basic Tuple Operations - Test 2

**Difficulty:** ⭐ (Very Easy)

**Related Topics:** Tuple Basics, Indexing, Access

## Objectives

- Learn fundamental tuple operations
- Practice basic tuple access and information retrieval
- Understand tuple indexing and length

## Description

Master the most basic tuple operations including creating tuples, accessing elements, and getting tuple information. Tuples are immutable sequences that store ordered data.

## Examples

```python
# Creating and accessing tuples
colors = ("red", "green", "blue")
print(get_first_element(colors))     # "red"
print(get_tuple_length(colors))      # 3

# Basic tuple operations
numbers = (1, 2, 3, 4, 5)
first = get_first_element(numbers)   # 1
last = get_last_element(numbers)     # 5
length = get_tuple_length(numbers)   # 5
```

## Your Tasks

1. **get_first_element(my_tuple)** - Return the first element of a tuple
2. **get_last_element(my_tuple)** - Return the last element of a tuple
3. **get_tuple_length(my_tuple)** - Return the number of elements in a tuple
4. **get_middle_element(my_tuple)** - Return middle element (for odd-length tuples)
5. **is_tuple_empty(my_tuple)** - Check if a tuple is empty
6. **get_element_at_position(my_tuple, index)** - Get element at specific index
7. **create_number_tuple(start, end)** - Create tuple of numbers from start to end
8. **combine_two_tuples(tuple1, tuple2)** - Combine two tuples into one

## Hints

- Use square brackets `[]` for indexing (same as lists)
- Index `-1` refers to the last element
- `len()` function gives you the tuple length
- Empty tuples have length 0
- Handle edge cases like empty tuples
- Use `+` operator to combine tuples
- `tuple(range())` can help create number sequences

## Test Cases

```python
# Test data for validation
test_cases = [
    ((1, 2, 3), 1, 3, 3),              # first, last, length
    (("a", "b", "c", "d", "e"), "a", "e", 5),
    ((42,), 42, 42, 1),                # single element
    ((), None, None, 0),               # empty tuple
    ((1, 2, 3, 4, 5), 3),             # middle element
    (((1, 2), (3, 4)), (1, 2, 3, 4))  # combined
]
```

## Bonus Challenges

- Handle negative indices properly
- Add error handling for invalid indices
- Create tuples with different data types
- Practice with nested tuples

Remember: Tuples are immutable sequences - you cannot change them after creation!
