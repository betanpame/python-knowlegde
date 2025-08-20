# Practice Modules 1: Built-in Modules and Import Statements

**Difficulty:** ⭐⭐☆☆☆ (Easy-Medium)

**Related Topics:** Import statements, built-in modules, module aliases

## Objective

Master working with Python's built-in modules and different import techniques.

## Requirements

Create functions that demonstrate effective use of built-in modules:

1. `math_operations_demo()` - Use math module for advanced calculations
2. `datetime_utilities()` - Work with dates, times, and calendars
3. `random_data_generator()` - Generate various types of random data
4. `json_data_processor()` - Process JSON data with proper error handling
5. `system_information()` - Get system information using os and sys modules

## Import Techniques to Demonstrate

Show different import styles:
- `import module`
- `from module import function`
- `import module as alias`
- `from module import *` (explain why to avoid)

## Examples

```python
# Math operations
import math
result = math_operations_demo()
# Should include: sqrt, sin, cos, log, factorial, etc.

# DateTime utilities
from datetime import datetime, timedelta
schedule = datetime_utilities()
# Should work with dates, formatting, arithmetic
```

## Hints

- Use `math` for mathematical functions and constants
- Use `datetime` for date/time operations and formatting
- Use `random` for generating test data and simulations
- Use `json` for data serialization/deserialization
- Use `os` and `sys` for system-level operations
- Always handle import errors gracefully

## Practice Cases

Your functions should handle:

1. Different import styles and their appropriate usage
2. Module functions with various parameter combinations
3. Error handling for invalid inputs
4. Cross-platform compatibility (especially for os module)
5. Performance considerations when importing large modules