# Test Functions 1: Basic Function Definition and Usage

**Difficulty:** ⭐⭐☆☆☆ (Easy-Medium)

**Related Topics:** Function definition, return statements, function scope, docstrings

## Objective

Master the fundamentals of function definition, documentation, and scope management.

## Requirements

Create well-documented functions that demonstrate proper function design:

1. `calculate_area(shape, **dimensions)` - Calculate area of different shapes with docstring
2. `temperature_converter(temp, from_unit, to_unit)` - Convert between temperature units
3. `scope_demonstration()` - Demonstrate local vs global scope
4. `fibonacci_recursive(n)` - Recursive function with proper base case
5. `input_validator(value, data_type, constraints=None)` - Validate input with default parameters

## Examples

```python
# Area calculation with docstring
area = calculate_area("rectangle", length=5, width=3)  # Returns 15

# Temperature conversion
celsius = temperature_converter(32, "fahrenheit", "celsius")  # Returns 0.0

# Fibonacci
fib_5 = fibonacci_recursive(5)  # Returns 5 (1, 1, 2, 3, 5)
```

## Requirements for Docstrings

Each function must include:
- Brief description of what the function does
- Args section with parameter descriptions and types
- Returns section with return type and description
- Raises section if applicable

## Hints

- Use triple quotes `"""` for docstrings
- Follow PEP 257 for docstring conventions
- Use `global` keyword carefully for scope demonstration
- Consider edge cases and input validation
- Recursive functions need base cases to avoid infinite recursion

## Test Cases

Your functions should handle:

1. Valid inputs with expected outputs
2. Invalid inputs with appropriate error handling
3. Edge cases (zero, negative numbers, empty strings)
4. Different parameter combinations
5. Scope conflicts and variable shadowing
