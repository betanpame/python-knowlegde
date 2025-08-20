# Basic Module Imports - Practice 2

**Difficulty:** ⭐ (Very Easy)

**Related Topics:** Import Statement, Module Access, Standard Library

## Objectives

- Learn basic import statement syntax
- Practice accessing module functions and attributes
- Understand standard library modules

## Description

Master the fundamental concepts of importing and using modules in Python. Modules allow you to organize code and access powerful libraries.

## Examples

```python
# Basic imports
import math
result = use_math_module()
print(result)  # Uses math.pi, math.sqrt, etc.

# From imports
from datetime import datetime
current_time = get_current_time()
print(current_time)
```

## Your Tasks

1. **use_math_module()** - Use math.pi, math.sqrt, math.ceil functions
2. **use_random_module()** - Use random.randint, random.choice functions
3. **use_datetime_module()** - Get current date and time
4. **use_os_module()** - Get current working directory and environment
5. **import_with_alias()** - Import modules with aliases (as keyword)
6. **from_import_specific()** - Import specific functions from modules
7. **check_module_attributes()** - Explore module attributes and help
8. **use_string_module()** - Use string constants and methods

## Hints

- Use `import module_name` for full module import
- Use `from module_name import function_name` for specific imports
- Use `import module_name as alias` for shorter names
- Access module functions with dot notation: `module.function()`
- Use `dir(module)` to see available functions
- Use `help(module)` for module documentation

## Practice Cases

```python
# Practice importing and using modules
import math
assert math.pi > 3.14
assert math.sqrt(16) == 4.0

from random import randint
number = randint(1, 10)
assert 1 <= number <= 10
```

Remember: Modules make Python powerful by providing pre-built functionality!