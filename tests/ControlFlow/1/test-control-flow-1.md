# Test Control Flow 1: Conditional Operators

**Difficulty:** ⭐⭐☆☆☆ (Easy-Medium)

**Related Topics:** Identity operators (is, is not), membership operators (in, not in), logical operators

## Objective

Master the use of Python's conditional operators in practical scenarios.

## Requirements

Implement functions that demonstrate proper use of different conditional operators:

1. `check_identity(obj1, obj2)` - Use `is` and `is not` to check object identity
2. `validate_membership(item, container)` - Use `in` and `not in` for membership testing
3. `analyze_data_types(data_list)` - Categorize data using type checking and operators
4. `security_check(user_permissions, required_permissions)` - Check access rights
5. `smart_comparison(value1, value2)` - Compare values using appropriate operators

## Examples

```python
# Identity checking
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(check_identity(list1, list2))  # False (different objects)
print(check_identity(list1, list3))  # True (same object)

# Membership testing
fruits = ['apple', 'banana', 'orange']
print(validate_membership('apple', fruits))  # True
print(validate_membership('grape', fruits))  # False
```

## Hints

- `is` checks object identity, not equality
- `==` checks value equality, `is` checks if same object in memory
- Use `in` for checking if element exists in sequence
- Combine operators with `and`, `or`, `not` for complex conditions
- `None` should always be checked with `is` or `is not`

## Test Cases

Your functions should handle:

1. Comparing different data types (int, str, list, None)
2. Checking membership in different containers (list, tuple, set, dict)
3. Complex logical conditions with multiple operators
4. Edge cases like empty containers and None values
