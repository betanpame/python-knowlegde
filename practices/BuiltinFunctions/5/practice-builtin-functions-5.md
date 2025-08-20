# Mathematical and Logical Functions - Practice 5

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Master Python's built-in mathematical and logical functions including `abs()`, `round()`, `pow()`, `divmod()`, `min()`, `max()`, `any()`, `all()`, and advanced mathematical operations.

## Objectives

- Use mathematical functions for numeric operations
- Apply logical functions for conditional testing
- Understand rounding and precision control
- Work with absolute values and powers
- Perform complex mathematical calculations

## Your Tasks

1. **mathematical_operations()** - Perform basic math operations
2. **rounding_precision()** - Control number rounding and precision
3. **logical_evaluations()** - Use logical functions on collections
4. **power_operations()** - Work with exponents and powers
5. **mathematical_utilities()** - Apply utility math functions

## Example

```python
import math
import decimal
import fractions
from typing import List, Any, Union, Tuple
import statistics

def mathematical_operations():
    """Demonstrate basic mathematical built-in functions."""
    print("=== Mathematical Operations ===")
    
    # Absolute values
    print("Absolute Values:")
    
    numbers = [-10, -3.5, 0, 5.2, 15, -100.7]
    abs_values = [abs(num) for num in numbers]
    
    print(f"Original numbers: {numbers}")
    print(f"Absolute values: {abs_values}")
    
    # Complex numbers
    complex_nums = [3+4j, -2-5j, 1+0j, 0-3j]
    complex_abs = [abs(c) for c in complex_nums]
    
    print(f"\\nComplex numbers: {complex_nums}")
    print(f"Complex absolute values: {complex_abs}")
    
    # Min and Max operations
    print("\\nMin and Max Operations:")
    
    data_sets = [
        [5, 2, 8, 1, 9],
        [-3, -1, -5, -2],
        [10.5, 3.2, 7.8, 2.1],
        ['apple', 'banana', 'cherry']
    ]
    
    for i, data in enumerate(data_sets):
        min_val = min(data)
        max_val = max(data)
        print(f"  Dataset {i+1}: {data}")
        print(f"    Min: {min_val}, Max: {max_val}")
    
    # Min/Max with multiple arguments
    multi_min = min(5, 2, 8, 1, 9)
    multi_max = max(5, 2, 8, 1, 9)
    print(f"\\nMultiple args - Min: {multi_min}, Max: {multi_max}")
    
    # Min/Max with key function
    words = ['python', 'java', 'c', 'javascript', 'go']
    shortest = min(words, key=len)
    longest = max(words, key=len)
    
    print(f"\\nWords: {words}")
    print(f"Shortest word: '{shortest}' (length: {len(shortest)})")
    print(f"Longest word: '{longest}' (length: {len(longest)})")
    
    # Min/Max with custom objects
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __repr__(self):
            return f"Person('{self.name}', {self.age})"
    
    people = [
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 35),
        Person("Diana", 28)
    ]
    
    youngest = min(people, key=lambda p: p.age)
    oldest = max(people, key=lambda p: p.age)
    
    print(f"\\nPeople: {people}")
    print(f"Youngest: {youngest}")
    print(f"Oldest: {oldest}")
    
    # Sum function
    print("\\nSum Operations:")
    
    numbers_to_sum = [1, 2, 3, 4, 5]
    total = sum(numbers_to_sum)
    total_with_start = sum(numbers_to_sum, 100)  # Start value
    
    print(f"Numbers: {numbers_to_sum}")
    print(f"Sum: {total}")
    print(f"Sum with start value 100: {total_with_start}")
    
    # Sum with different types
    floats = [1.1, 2.2, 3.3, 4.4]
    float_sum = sum(floats)
    
    fractions_list = [fractions.Fraction(1, 2), fractions.Fraction(1, 3), fractions.Fraction(1, 4)]
    fraction_sum = sum(fractions_list)
    
    print(f"\\nFloat sum: {floats} = {float_sum}")
    print(f"Fraction sum: {fractions_list} = {fraction_sum}")
    
    # Advanced sum operations
    nested_numbers = [[1, 2], [3, 4], [5, 6]]
    flattened_sum = sum([sum(sublist) for sublist in nested_numbers])
    
    print(f"\\nNested numbers: {nested_numbers}")
    print(f"Sum of sums: {flattened_sum}")
    
    return {
        "abs_values": abs_values,
        "complex_abs": complex_abs,
        "min_max_results": [(min(data), max(data)) for data in data_sets[:-1]],  # Exclude string data
        "word_lengths": {"shortest": (shortest, len(shortest)), "longest": (longest, len(longest))},
        "age_extremes": {"youngest": youngest.age, "oldest": oldest.age},
        "sum_results": {"basic": total, "with_start": total_with_start, "float": float_sum},
        "fraction_sum": fraction_sum,
        "nested_sum": flattened_sum
    }

def rounding_precision():
    """Demonstrate rounding and precision control functions."""
    print("\\n=== Rounding and Precision Operations ===")
    
    # Basic rounding
    print("Basic Rounding:")
    
    numbers = [3.14159, 2.71828, 1.41421, 0.57721, 9.80665]
    
    for num in numbers:
        rounded_0 = round(num)
        rounded_2 = round(num, 2)
        rounded_4 = round(num, 4)
        
        print(f"  {num}: round() = {rounded_0}, round(2) = {rounded_2}, round(4) = {rounded_4}")
    
    # Rounding edge cases
    print("\\nRounding Edge Cases:")
    
    edge_cases = [2.5, 3.5, -2.5, -3.5, 2.675, 2.685]
    
    for num in edge_cases:
        rounded = round(num)
        rounded_1 = round(num, 1)
        print(f"  {num}: round() = {rounded}, round(1) = {rounded_1}")
    
    # Rounding to negative decimal places
    print("\\nRounding to Negative Decimal Places:")
    
    large_numbers = [12345.67, 98765.43, 555555.55]
    
    for num in large_numbers:
        round_tens = round(num, -1)      # Round to nearest 10
        round_hundreds = round(num, -2)  # Round to nearest 100
        round_thousands = round(num, -3) # Round to nearest 1000
        
        print(f"  {num}:")
        print(f"    Tens: {round_tens}")
        print(f"    Hundreds: {round_hundreds}")
        print(f"    Thousands: {round_thousands}")
    
    # Precision with Decimal
    print("\\nPrecision with Decimal:")
    
    # Set decimal precision
    decimal.getcontext().prec = 10
    
    decimal_nums = [
        decimal.Decimal('3.141592653589793'),
        decimal.Decimal('2.718281828459045'),
        decimal.Decimal('1.4142135623730951')
    ]
    
    for d_num in decimal_nums:
        print(f"  Decimal: {d_num}")
        print(f"    Quantized to 3 places: {d_num.quantize(decimal.Decimal('0.001'))}")
        print(f"    Quantized to 6 places: {d_num.quantize(decimal.Decimal('0.000001'))}")
    
    # Financial calculations with precise rounding
    print("\\nFinancial Calculations:")
    
    prices = [19.99, 25.50, 7.33, 12.95]
    tax_rate = decimal.Decimal('0.08')  # 8% tax
    
    total_before_tax = sum(decimal.Decimal(str(price)) for price in prices)
    tax_amount = total_before_tax * tax_rate
    total_after_tax = total_before_tax + tax_amount
    
    print(f"  Prices: {prices}")
    print(f"  Subtotal: ${total_before_tax}")
    print(f"  Tax (8%): ${tax_amount.quantize(decimal.Decimal('0.01'))}")
    print(f"  Total: ${total_after_tax.quantize(decimal.Decimal('0.01'))}")
    
    # Different rounding modes
    print("\\nDifferent Rounding Modes:")
    
    test_value = decimal.Decimal('2.675')
    rounding_modes = [
        (decimal.ROUND_HALF_UP, "ROUND_HALF_UP"),
        (decimal.ROUND_HALF_DOWN, "ROUND_HALF_DOWN"),
        (decimal.ROUND_HALF_EVEN, "ROUND_HALF_EVEN"),
        (decimal.ROUND_UP, "ROUND_UP"),
        (decimal.ROUND_DOWN, "ROUND_DOWN"),
        (decimal.ROUND_CEILING, "ROUND_CEILING"),
        (decimal.ROUND_FLOOR, "ROUND_FLOOR")
    ]
    
    print(f"  Value: {test_value}")
    for mode, name in rounding_modes:
        rounded = test_value.quantize(decimal.Decimal('0.01'), rounding=mode)
        print(f"    {name}: {rounded}")
    
    return {
        "basic_rounding": [round(num, 2) for num in numbers],
        "edge_cases": [(num, round(num), round(num, 1)) for num in edge_cases],
        "large_number_rounding": [(num, round(num, -1), round(num, -2)) for num in large_numbers],
        "decimal_precision": [d_num.quantize(decimal.Decimal('0.001')) for d_num in decimal_nums],
        "financial_total": float(total_after_tax.quantize(decimal.Decimal('0.01'))),
        "rounding_modes": {name: float(test_value.quantize(decimal.Decimal('0.01'), rounding=mode)) 
                          for mode, name in rounding_modes}
    }

def logical_evaluations():
    """Demonstrate logical evaluation functions."""
    print("\\n=== Logical Evaluation Operations ===")
    
    # Any function
    print("Any Function:")
    
    test_cases_any = [
        [True, False, False],
        [False, False, False],
        [True, True, True],
        [],
        [0, 1, 2],
        [0, 0, 0],
        ["", "hello", ""],
        ["", "", ""]
    ]
    
    for i, case in enumerate(test_cases_any):
        result = any(case)
        print(f"  Case {i+1}: {case} -> any() = {result}")
    
    # All function
    print("\\nAll Function:")
    
    test_cases_all = [
        [True, True, True],
        [True, False, True],
        [False, False, False],
        [],
        [1, 2, 3],
        [1, 0, 3],
        ["hello", "world", "python"],
        ["hello", "", "python"]
    ]
    
    for i, case in enumerate(test_cases_all):
        result = all(case)
        print(f"  Case {i+1}: {case} -> all() = {result}")
    
    # Practical examples with any/all
    print("\\nPractical Examples:")
    
    # Check if any number is negative
    number_sets = [
        [1, 2, 3, 4],
        [-1, 2, 3, 4],
        [1, -2, -3, 4],
        [-1, -2, -3, -4]
    ]
    
    print("Checking for negative numbers:")
    for nums in number_sets:
        has_negative = any(n < 0 for n in nums)
        all_negative = all(n < 0 for n in nums)
        print(f"  {nums}: any negative = {has_negative}, all negative = {all_negative}")
    
    # Validate data
    print("\\nData Validation:")
    
    user_data = [
        {"name": "Alice", "age": 25, "email": "alice@example.com"},
        {"name": "Bob", "age": 30, "email": "bob@example.com"},
        {"name": "", "age": 28, "email": "charlie@example.com"},
        {"name": "Diana", "age": -5, "email": "diana@example.com"},
        {"name": "Eve", "age": 35, "email": ""}
    ]
    
    for i, user in enumerate(user_data):
        # Check if all required fields are present and valid
        name_valid = bool(user["name"])
        age_valid = user["age"] > 0
        email_valid = bool(user["email"]) and "@" in user["email"]
        
        all_valid = all([name_valid, age_valid, email_valid])
        any_invalid = any([not name_valid, not age_valid, not email_valid])
        
        print(f"  User {i+1}: {user}")
        print(f"    All valid: {all_valid}, Any invalid: {any_invalid}")
    
    # Permission checking
    print("\\nPermission Checking:")
    
    users_permissions = [
        {"name": "Admin", "permissions": ["read", "write", "delete", "admin"]},
        {"name": "Editor", "permissions": ["read", "write"]},
        {"name": "Viewer", "permissions": ["read"]},
        {"name": "Guest", "permissions": []}
    ]
    
    required_permissions = ["read", "write"]
    admin_permissions = ["admin", "delete"]
    
    for user in users_permissions:
        permissions = user["permissions"]
        
        # Check if user has all required permissions
        has_required = all(perm in permissions for perm in required_permissions)
        
        # Check if user has any admin permissions
        has_admin = any(perm in permissions for perm in admin_permissions)
        
        print(f"  {user['name']}: permissions = {permissions}")
        print(f"    Has required permissions: {has_required}")
        print(f"    Has admin permissions: {has_admin}")
    
    # Boolean logic with generators
    print("\\nBoolean Logic with Generators:")
    
    # Check large datasets efficiently
    large_range = range(1000000)
    
    # Check if any number in range is divisible by 777777
    has_divisible = any(n % 777777 == 0 for n in large_range)
    print(f"Any number 0-999999 divisible by 777777: {has_divisible}")
    
    # Check if all numbers in small range are less than 10
    small_range = range(5)
    all_small = all(n < 10 for n in small_range)
    print(f"All numbers in range(5) < 10: {all_small}")
    
    return {
        "any_results": [any(case) for case in test_cases_any],
        "all_results": [all(case) for case in test_cases_all],
        "negative_checks": [(any(n < 0 for n in nums), all(n < 0 for n in nums)) for nums in number_sets],
        "data_validation": [all([bool(user["name"]), user["age"] > 0, bool(user["email"]) and "@" in user["email"]]) 
                           for user in user_data],
        "permission_results": [(all(perm in user["permissions"] for perm in required_permissions),
                               any(perm in user["permissions"] for perm in admin_permissions))
                              for user in users_permissions],
        "large_dataset_check": has_divisible,
        "small_range_check": all_small
    }

def power_operations():
    """Demonstrate power and exponent operations."""
    print("\\n=== Power and Exponent Operations ===")
    
    # Basic pow function
    print("Basic Power Operations:")
    
    base_exp_pairs = [
        (2, 3),      # 2^3 = 8
        (5, 2),      # 5^2 = 25
        (3, 4),      # 3^4 = 81
        (10, 0),     # 10^0 = 1
        (7, 1),      # 7^1 = 7
        (2, -2),     # 2^-2 = 0.25
        (4, 0.5),    # 4^0.5 = 2 (square root)
        (27, 1/3)    # 27^(1/3) = 3 (cube root)
    ]
    
    for base, exp in base_exp_pairs:
        result = pow(base, exp)
        result_alt = base ** exp  # Alternative syntax
        print(f"  {base}^{exp} = {result} (** operator: {result_alt})")
    
    # Modular exponentiation
    print("\\nModular Exponentiation:")
    
    # pow(base, exp, mod) is more efficient than (base ** exp) % mod for large numbers
    mod_cases = [
        (2, 10, 1000),    # 2^10 mod 1000
        (3, 20, 100),     # 3^20 mod 100
        (5, 13, 7),       # 5^13 mod 7
        (123, 456, 789)   # Large numbers
    ]
    
    for base, exp, mod in mod_cases:
        result_pow = pow(base, exp, mod)
        result_alt = (base ** exp) % mod  # Less efficient for large numbers
        print(f"  {base}^{exp} mod {mod} = {result_pow}")
        print(f"    Verification: {result_alt} (matches: {result_pow == result_alt})")
    
    # Complex number powers
    print("\\nComplex Number Powers:")
    
    complex_bases = [1+1j, 2+3j, -1+0j, 0+1j]
    exponents = [2, 3, 0.5, -1]
    
    for base in complex_bases:
        print(f"  Base: {base}")
        for exp in exponents:
            result = pow(base, exp)
            print(f"    {base}^{exp} = {result}")
    
    # Mathematical constants and powers
    print("\\nMathematical Constants and Powers:")
    
    # Common mathematical calculations
    calculations = [
        ("e^2", math.e, 2),
        ("π^2", math.pi, 2),
        ("Golden ratio^2", (1 + math.sqrt(5)) / 2, 2),
        ("√2^4", math.sqrt(2), 4),
        ("10^log10(100)", 10, math.log10(100))
    ]
    
    for name, base, exp in calculations:
        result = pow(base, exp)
        print(f"  {name}: {base:.6f}^{exp:.6f} = {result:.6f}")
    
    # Large number exponentiation
    print("\\nLarge Number Exponentiation:")
    
    # Demonstrate efficiency difference
    import time
    
    base, exp = 123456, 100
    
    # Using pow() - efficient
    start_time = time.time()
    result_pow = pow(base, exp)
    pow_time = time.time() - start_time
    
    # Using ** operator - less efficient for very large numbers
    start_time = time.time()
    result_exp = base ** exp
    exp_time = time.time() - start_time
    
    print(f"  {base}^{exp}:")
    print(f"    Result length: {len(str(result_pow))} digits")
    print(f"    pow() time: {pow_time:.6f} seconds")
    print(f"    ** time: {exp_time:.6f} seconds")
    print(f"    Results match: {result_pow == result_exp}")
    
    # Fractional exponents (roots)
    print("\\nFractional Exponents (Roots):")
    
    root_cases = [
        (16, 1/2),      # Square root of 16
        (27, 1/3),      # Cube root of 27
        (81, 1/4),      # Fourth root of 81
        (32, 1/5),      # Fifth root of 32
        (64, 2/3),      # (64^2)^(1/3) = 4^2 = 16
    ]
    
    for base, exp in root_cases:
        result = pow(base, exp)
        # Verification using math functions where applicable
        if exp == 1/2:
            verification = math.sqrt(base)
        elif exp == 1/3:
            verification = base ** (1/3)
        else:
            verification = base ** exp
        
        print(f"  {base}^{exp} = {result:.6f} (verification: {verification:.6f})")
    
    return {
        "basic_powers": [(base, exp, pow(base, exp)) for base, exp in base_exp_pairs],
        "modular_results": [(base, exp, mod, pow(base, exp, mod)) for base, exp, mod in mod_cases],
        "complex_powers": {str(base): [pow(base, exp) for exp in exponents] for base in complex_bases},
        "math_constants": [(name, pow(base, exp)) for name, base, exp in calculations],
        "large_number_digits": len(str(result_pow)),
        "performance_comparison": {"pow_time": pow_time, "exp_time": exp_time},
        "root_calculations": [(base, exp, pow(base, exp)) for base, exp in root_cases]
    }

def mathematical_utilities():
    """Demonstrate utility mathematical functions."""
    print("\\n=== Mathematical Utility Functions ===")
    
    # Divmod function
    print("Divmod Function:")
    
    divmod_cases = [
        (17, 5),     # 17 ÷ 5 = 3 remainder 2
        (100, 7),    # 100 ÷ 7 = 14 remainder 2
        (25, 5),     # 25 ÷ 5 = 5 remainder 0
        (7, 10),     # 7 ÷ 10 = 0 remainder 7
        (-17, 5),    # Negative dividend
        (17, -5),    # Negative divisor
        (3.5, 1.2)   # Float division
    ]
    
    for dividend, divisor in divmod_cases:
        quotient, remainder = divmod(dividend, divisor)
        verification = quotient * divisor + remainder
        
        print(f"  divmod({dividend}, {divisor}) = ({quotient}, {remainder})")
        print(f"    Verification: {quotient} * {divisor} + {remainder} = {verification}")
    
    # Practical divmod applications
    print("\\nPractical Divmod Applications:")
    
    # Time conversion
    total_seconds = 7265
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(f"  Convert {total_seconds} seconds:")
    print(f"    {hours} hours, {minutes} minutes, {seconds} seconds")
    
    # Money change calculation
    amount_cents = 287
    dollars, cents = divmod(amount_cents, 100)
    
    print(f"  Convert {amount_cents} cents:")
    print(f"    ${dollars}.{cents:02d}")
    
    # Pagination
    total_items = 157
    items_per_page = 10
    pages, items_on_last_page = divmod(total_items, items_per_page)
    
    if items_on_last_page == 0:
        total_pages = pages
        items_on_last = items_per_page
    else:
        total_pages = pages + 1
        items_on_last = items_on_last_page
    
    print(f"  Pagination for {total_items} items ({items_per_page} per page):")
    print(f"    Total pages: {total_pages}")
    print(f"    Items on last page: {items_on_last}")
    
    # Binary representation
    print("\\nBinary Representation:")
    
    numbers = [42, 255, 1024, 7]
    
    for num in numbers:
        binary = bin(num)
        octal = oct(num)
        hexadecimal = hex(num)
        
        print(f"  {num}:")
        print(f"    Binary: {binary} ({binary[2:]})")
        print(f"    Octal: {octal}")
        print(f"    Hexadecimal: {hexadecimal}")
    
    # Hash function
    print("\\nHash Function:")
    
    hashable_objects = [
        42,
        "hello",
        (1, 2, 3),
        frozenset([1, 2, 3]),
        True,
        None
    ]
    
    print("Hash values:")
    for obj in hashable_objects:
        hash_value = hash(obj)
        print(f"  hash({repr(obj)}) = {hash_value}")
    
    # Demonstrate hash consistency
    print("\\nHash Consistency:")
    string1 = "python"
    string2 = "python"
    print(f"  hash('{string1}') = {hash(string1)}")
    print(f"  hash('{string2}') = {hash(string2)}")
    print(f"  Hashes equal: {hash(string1) == hash(string2)}")
    
    # ID function
    print("\\nObject Identity:")
    
    # Immutable objects
    a = 1000
    b = 1000
    c = a
    
    print(f"  a = {a}, id(a) = {id(a)}")
    print(f"  b = {b}, id(b) = {id(b)}")
    print(f"  c = a, id(c) = {id(c)}")
    print(f"  a is b: {a is b}")
    print(f"  a is c: {a is c}")
    
    # Small integers are cached
    small_a = 5
    small_b = 5
    print(f"\\n  small_a = {small_a}, id(small_a) = {id(small_a)}")
    print(f"  small_b = {small_b}, id(small_b) = {id(small_b)}")
    print(f"  small_a is small_b: {small_a is small_b}")
    
    # Statistical functions
    print("\\nBasic Statistical Functions:")
    
    data_sets = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40, 50],
        [1.5, 2.7, 3.9, 4.1, 5.8],
        [-5, -2, 0, 3, 7]
    ]
    
    for i, data in enumerate(data_sets):
        mean_val = statistics.mean(data)
        median_val = statistics.median(data)
        
        try:
            mode_val = statistics.mode(data)
        except statistics.StatisticsError:
            mode_val = "No unique mode"
        
        print(f"  Dataset {i+1}: {data}")
        print(f"    Mean: {mean_val:.2f}")
        print(f"    Median: {median_val}")
        print(f"    Mode: {mode_val}")
    
    return {
        "divmod_results": [(dividend, divisor, divmod(dividend, divisor)) for dividend, divisor in divmod_cases],
        "time_conversion": {"hours": hours, "minutes": minutes, "seconds": seconds},
        "money_conversion": {"dollars": dollars, "cents": cents},
        "pagination": {"total_pages": total_pages, "items_on_last": items_on_last},
        "number_representations": {num: {"binary": bin(num), "octal": oct(num), "hex": hex(num)} 
                                 for num in numbers},
        "hash_values": {repr(obj): hash(obj) for obj in hashable_objects},
        "identity_comparison": {"large_nums_same_id": a is b, "small_nums_same_id": small_a is small_b},
        "statistics": {f"dataset_{i+1}": {"mean": statistics.mean(data), "median": statistics.median(data)} 
                      for i, data in enumerate(data_sets)}
    }

# Main execution
if __name__ == "__main__":
    print("=== Built-in Mathematical and Logical Functions ===")
    
    print("\\n1. Mathematical Operations:")
    math_results = mathematical_operations()
    
    print("\\n2. Rounding and Precision:")
    rounding_results = rounding_precision()
    
    print("\\n3. Logical Evaluations:")
    logical_results = logical_evaluations()
    
    print("\\n4. Power Operations:")
    power_results = power_operations()
    
    print("\\n5. Mathematical Utilities:")
    utility_results = mathematical_utilities()
    
    print("\\n" + "="*60)
    print("=== MATHEMATICAL AND LOGICAL FUNCTIONS COMPLETE ===")
    print("✓ Basic mathematical operations")
    print("✓ Precision control and rounding")
    print("✓ Logical evaluation functions")
    print("✓ Power and exponent calculations")
    print("✓ Utility mathematical functions")
    print("✓ Statistical operations")
```

## Hints

- Use `abs()` for absolute values including complex numbers
- `round()` can take negative precision for rounding to tens, hundreds, etc.
- `any()` returns `True` if at least one element is truthy
- `all()` returns `True` if all elements are truthy (empty iterable returns `True`)
- `pow(x, y, z)` is more efficient than `(x**y) % z` for large numbers

## Practice Cases

Your functions should handle:

1. Mathematical operations on various numeric types including complex numbers
2. Rounding with different precision levels and edge cases
3. Logical evaluation on empty and mixed-type collections
4. Power operations with fractional exponents and modular arithmetic
5. Utility functions for practical applications like time conversion

## Bonus Challenge

Create a mathematical expression evaluator, implement custom rounding algorithms, and build a statistical analysis toolkit using only built-in functions!