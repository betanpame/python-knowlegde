# Practice Functions 2: Advanced Function Parameters (*args, **kwargs)

**Difficulty:** ⭐⭐⭐☆☆ (Medium)

**Related Topics:** *args, **kwargs, variable-length arguments, parameter ordering

## Objective

Master advanced function parameter techniques for flexible and reusable functions.

## Requirements

Create functions that effectively use *args and **kwargs:

1. `flexible_calculator(operation, *args, **kwargs)` - Calculator with variable arguments
2. `log_function_call(func, *args, **kwargs)` - Function decorator-like logger
3. `merge_configurations(*config_dicts, **override_options)` - Merge multiple configs
4. `create_formatted_string(template, *values, **formatting_options)` - String formatter
5. `statistical_analysis(*datasets, **analysis_options)` - Analyze multiple datasets

## Examples

```python
# Flexible calculator
result = flexible_calculator("add", 1, 2, 3, 4, 5)  # Sum: 15
result = flexible_calculator("multiply", 2, 3, 4, precision=2)  # Product: 24

# Configuration merger
config = merge_configurations(
    {"db_host": "localhost", "port": 5432},
    {"db_name": "test", "port": 3306},
    username="admin",
    password="secret"
)
```

## Parameter Order Rules

Remember the correct parameter order:
1. Regular positional parameters
2. *args (variable positional)
3. Keyword-only parameters
4. **kwargs (variable keyword)

## Hints

- *args collects extra positional arguments into a tuple
- **kwargs collects extra keyword arguments into a dictionary
- Use unpacking (*list, **dict) when calling functions
- Default parameters should come before *args
- Keyword-only parameters come after *args

## Practice Cases

Your functions should handle:

1. Functions called with only positional arguments
2. Functions called with only keyword arguments
3. Mixed positional and keyword arguments
4. Empty *args and **kwargs
5. Argument unpacking scenarios