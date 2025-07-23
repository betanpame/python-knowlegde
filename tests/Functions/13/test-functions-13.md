# Advanced Function Parameters - Test 13

**Difficulty:** ⭐⭐⭐ (Easy-Medium)

**Related Topics:** *args, **kwargs, Flexible Parameters, Advanced Arguments

## Objectives

- Master *args and **kwargs for flexible function parameters
- Handle variable numbers of arguments efficiently
- Create highly flexible and reusable functions

## Description

Learn advanced parameter techniques that allow functions to accept varying numbers of arguments, making them more flexible and powerful.

## Examples

```python
def flexible_calculator(operation, *args, **kwargs):
    # Can handle any number of arguments
    if operation == "sum":
        return sum(args)
    elif operation == "product":
        result = 1
        for num in args:
            result *= num
        return result

result1 = flexible_calculator("sum", 1, 2, 3, 4)  # 10
result2 = flexible_calculator("product", 2, 3, 4)  # 24
```

## Your Tasks

1. **flexible_calculator(operation, *numbers, **options)** - Calculator with flexible args
2. **create_formatted_message(template, *args, **kwargs)** - Message formatter
3. **data_processor(*datasets, operation="merge", **config)** - Process multiple datasets
4. **flexible_validator(*values, strict=False, **validation_rules)** - Flexible validation
5. **advanced_logger(message, *tags, level="INFO", **metadata)** - Advanced logging
6. **dynamic_query_builder(table, *fields, **conditions)** - Build database queries
7. **flexible_api_call(endpoint, *path_parts, method="GET", **params)** - API call builder
8. **configurable_processor(*inputs, **processing_options)** - Configurable processing

## Hints

- `*args` collects positional arguments into a tuple
- `**kwargs` collects keyword arguments into a dictionary
- Order: positional, *args, keyword, **kwargs
- Use meaningful parameter names for clarity
- Document the expected arguments clearly

## Test Cases

```python
# Test flexible calculator
test_cases = [
    (flexible_calculator("sum", 1, 2, 3), 6),
    (flexible_calculator("product", 2, 3, 4), 24),
    (flexible_calculator("average", 10, 20, 30, return_float=True), 20.0)
]
```

Remember: *args and **kwargs make functions incredibly flexible!
