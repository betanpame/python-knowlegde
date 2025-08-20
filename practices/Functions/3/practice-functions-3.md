# Basic Function Definition - Practice 3

**Difficulty:** ⭐ (Very Easy)

**Related Topics:** Function Definition, Parameters, Return Values

## Objectives

- Learn basic function definition syntax
- Practice creating functions with parameters
- Understand return values and function calls

## Description

Master the fundamental concepts of creating and using functions in Python. Functions allow you to organize code into reusable blocks.

## Examples

```python
def greet_person(name):
    return f"Hello, {name}!"

result = greet_person("Alice")
print(result)  # "Hello, Alice!"

def add_numbers(a, b):
    return a + b

sum_result = add_numbers(5, 3)
print(sum_result)  # 8
```

## Your Tasks

1. **create_greeting(name)** - Return personalized greeting
2. **add_two_numbers(a, b)** - Add two numbers and return result
3. **multiply_by_two(number)** - Multiply number by 2
4. **get_string_length(text)** - Return length of string
5. **is_even_number(number)** - Return True if number is even
6. **get_absolute_value(number)** - Return absolute value
7. **concatenate_strings(str1, str2)** - Join two strings
8. **calculate_area_rectangle(length, width)** - Calculate rectangle area

## Hints

- Use `def` keyword to define functions
- Functions can have zero or more parameters
- Use `return` to send values back to caller
- Function names should be descriptive
- Practice your functions with different inputs

## Practice Cases

```python
# Practice your functions
test_cases = [
    (create_greeting("Bob"), "Hello, Bob!"),
    (add_two_numbers(10, 5), 15),
    (multiply_by_two(7), 14),
    (is_even_number(4), True),
    (is_even_number(5), False)
]
```

Remember: Functions make code more organized and reusable!