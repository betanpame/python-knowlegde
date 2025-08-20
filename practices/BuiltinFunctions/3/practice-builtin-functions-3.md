# Type Conversion and Validation Functions - Practice 3

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Master Python's built-in type conversion functions (`int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()`, `dict()`) and validation functions (`isinstance()`, `issubclass()`, `hasattr()`, `callable()`). Learn safe type conversion with error handling.

## Objectives

- Convert between different data types safely
- Validate data types and object properties
- Handle conversion errors gracefully
- Understand type hierarchy and relationships
- Use type checking for robust code

## Your Tasks

1. **type_converter()** - Convert between different types
2. **safe_converter()** - Type conversion with error handling
3. **type_validator()** - Validate types and properties
4. **data_cleaner()** - Clean and convert messy data
5. **type_analyzer()** - Analyze and categorize data types

## Example

```python
import ast
import json
from decimal import Decimal
from datetime import datetime
from typing import Any, Union, List, Dict, Tuple, Optional

def type_converter():
    """Demonstrate basic type conversion functions."""
    print("=== Type Conversion Operations ===")
    
    # String to numeric conversions
    string_numbers = ["42", "3.14", "100", "0", "-25"]
    
    # Convert to integers
    integers = []
    for s in string_numbers:
        try:
            integers.append(int(float(s)))  # Handle both int and float strings
        except ValueError:
            integers.append(None)
    
    print(f"String numbers: {string_numbers}")
    print(f"Converted to int: {integers}")
    
    # Convert to floats
    floats = [float(s) for s in string_numbers]
    print(f"Converted to float: {floats}")
    
    # Numeric to string conversions
    numbers = [42, 3.14159, 0, -25, 1e6]
    string_versions = [str(num) for num in numbers]
    print(f"\\nNumbers: {numbers}")
    print(f"As strings: {string_versions}")
    
    # Boolean conversions
    various_values = [0, 1, "", "hello", [], [1, 2], {}, {"key": "value"}, None]
    boolean_values = [bool(val) for val in various_values]
    
    print(f"\\nVarious values: {various_values}")
    print(f"As booleans: {boolean_values}")
    
    # Sequence conversions
    original_string = "hello"
    original_list = [1, 2, 3, 4, 5]
    original_tuple = (10, 20, 30)
    original_set = {100, 200, 300}
    
    # String to other types
    string_to_list = list(original_string)
    string_to_tuple = tuple(original_string)
    string_to_set = set(original_string)
    
    print(f"\\nString '{original_string}' conversions:")
    print(f"  To list: {string_to_list}")
    print(f"  To tuple: {string_to_tuple}")
    print(f"  To set: {string_to_set}")
    
    # List conversions
    list_to_tuple = tuple(original_list)
    list_to_set = set(original_list)
    list_to_string = str(original_list)
    
    print(f"\\nList {original_list} conversions:")
    print(f"  To tuple: {list_to_tuple}")
    print(f"  To set: {list_to_set}")
    print(f"  To string: '{list_to_string}'")
    
    # Dictionary conversions
    sample_dict = {"a": 1, "b": 2, "c": 3}
    
    dict_keys = list(sample_dict.keys())
    dict_values = list(sample_dict.values())
    dict_items = list(sample_dict.items())
    
    print(f"\\nDictionary {sample_dict} conversions:")
    print(f"  Keys as list: {dict_keys}")
    print(f"  Values as list: {dict_values}")
    print(f"  Items as list: {dict_items}")
    
    # Create dictionary from sequences
    keys = ["name", "age", "city"]
    values = ["Alice", 25, "New York"]
    created_dict = dict(zip(keys, values))
    print(f"\\nCreated dictionary: {created_dict}")
    
    # Binary conversions
    number = 42
    binary_string = bin(number)
    octal_string = oct(number)
    hex_string = hex(number)
    
    print(f"\\nNumber {number} in different bases:")
    print(f"  Binary: {binary_string}")
    print(f"  Octal: {octal_string}")
    print(f"  Hexadecimal: {hex_string}")
    
    # Convert back from string representations
    from_binary = int(binary_string, 2)
    from_octal = int(octal_string, 8)
    from_hex = int(hex_string, 16)
    
    print(f"\\nConverted back to decimal:")
    print(f"  From binary: {from_binary}")
    print(f"  From octal: {from_octal}")
    print(f"  From hex: {from_hex}")
    
    return {
        "integers": integers,
        "floats": floats,
        "boolean_values": boolean_values,
        "string_conversions": {
            "list": string_to_list,
            "tuple": string_to_tuple,
            "set": string_to_set
        },
        "created_dict": created_dict,
        "number_bases": {
            "binary": binary_string,
            "octal": octal_string,
            "hex": hex_string
        }
    }

def safe_converter():
    """Demonstrate safe type conversion with error handling."""
    print("\\n=== Safe Type Conversion ===")
    
    # Safe string to number conversion
    def safe_int(value, default=0):
        \"\"\"Safely convert to integer with default value.\"\"\""
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
    
    def safe_float(value, default=0.0):
        \"\"\"Safely convert to float with default value.\"\"\""
        try:
            return float(value)
        except (ValueError, TypeError):
            return default
    
    # Practice data with various problematic values
    test_data = ["42", "3.14", "hello", None, "", "0", "invalid", [1, 2, 3]]
    
    print("Safe integer conversions:")
    for item in test_data:
        result = safe_int(item, default=-1)
        print(f"  {repr(item)} -> {result}")
    
    print("\\nSafe float conversions:")
    for item in test_data:
        result = safe_float(item, default=-1.0)
        print(f"  {repr(item)} -> {result}")
    
    # Advanced safe conversion with multiple attempts
    def smart_numeric_convert(value):
        \"\"\"Try multiple conversion strategies.\"\"\""
        if value is None:
            return None
        
        # Try direct int conversion
        try:
            return int(value)
        except (ValueError, TypeError):
            pass
        
        # Try float conversion, then int
        try:
            float_val = float(value)
            if float_val.is_integer():
                return int(float_val)
            return float_val
        except (ValueError, TypeError):
            pass
        
        # Try to extract numbers from string
        if isinstance(value, str):
            import re
            numbers = re.findall(r'-?\\d+\\.?\\d*', value)
            if numbers:
                try:
                    num_str = numbers[0]
                    if '.' in num_str:
                        return float(num_str)
                    return int(num_str)
                except ValueError:
                    pass
        
        # Return original value if no conversion possible
        return value
    
    complex_test_data = [
        "42",
        "3.14",
        "price: $25.50",
        "age: 30 years",
        "invalid text",
        "123abc456",
        "",
        None,
        [1, 2, 3]
    ]
    
    print("\\nSmart numeric conversion:")
    for item in complex_test_data:
        result = smart_numeric_convert(item)
        print(f"  {repr(item)} -> {repr(result)} ({type(result).__name__})")
    
    # Safe dictionary creation
    def safe_dict_from_pairs(pairs, default_dict=None):
        \"\"\"Safely create dictionary from key-value pairs.\"\"\""
        if default_dict is None:
            default_dict = {}
        
        try:
            return dict(pairs)
        except (ValueError, TypeError):
            return default_dict.copy()
    
    # Practice safe dictionary creation
    dict_test_data = [
        [("a", 1), ("b", 2)],  # Valid pairs
        ["ab", "cd"],  # Invalid - strings not pairs
        [(1, 2, 3)],  # Invalid - triple instead of pair
        [],  # Empty
        None  # None
    ]
    
    print("\\nSafe dictionary creation:")
    for pairs in dict_test_data:
        result = safe_dict_from_pairs(pairs, {"error": "invalid"})
        print(f"  {repr(pairs)} -> {result}")
    
    # Safe list conversion with filtering
    def safe_list_convert(value, item_converter=None, filter_none=True):
        \"\"\"Safely convert to list with optional item conversion.\"\"\""
        try:
            if value is None:
                return []
            
            # Convert to list
            if isinstance(value, (list, tuple, set)):
                items = list(value)
            elif isinstance(value, str):
                items = list(value)
            elif isinstance(value, dict):
                items = list(value.items())
            else:
                items = [value]
            
            # Apply item converter if provided
            if item_converter:
                converted_items = []
                for item in items:
                    try:
                        converted_items.append(item_converter(item))
                    except Exception:
                        if not filter_none:
                            converted_items.append(None)
                items = converted_items
            
            # Filter None values if requested
            if filter_none:
                items = [item for item in items if item is not None]
            
            return items
            
        except Exception:
            return []
    
    list_test_data = [
        "hello",
        [1, 2, 3],
        (4, 5, 6),
        {"a": 1, "b": 2},
        {7, 8, 9},
        42,
        None
    ]
    
    print("\\nSafe list conversion:")
    for item in list_test_data:
        result = safe_list_convert(item)
        print(f"  {repr(item)} -> {result}")
    
    print("\\nSafe list conversion with int converter:")
    for item in list_test_data:
        result = safe_list_convert(item, item_converter=safe_int)
        print(f"  {repr(item)} -> {result}")
    
    return {
        "safe_int_results": [safe_int(item, -1) for item in test_data],
        "smart_conversions": [smart_numeric_convert(item) for item in complex_test_data],
        "safe_dicts": [safe_dict_from_pairs(pairs, {"error": "invalid"}) for pairs in dict_test_data],
        "safe_lists": [safe_list_convert(item) for item in list_test_data]
    }

def type_validator():
    """Demonstrate type validation functions."""
    print("\\n=== Type Validation Functions ===")
    
    # Practice data with various types
    test_objects = [
        42,
        3.14,
        "hello",
        [1, 2, 3],
        (4, 5, 6),
        {"key": "value"},
        {7, 8, 9},
        True,
        None,
        lambda x: x * 2,
        type,
        print
    ]
    
    # Basic type checking with isinstance
    print("isinstance() validation:")
    type_checks = [
        (int, "integer"),
        (float, "float"),
        (str, "string"),
        (list, "list"),
        (tuple, "tuple"),
        (dict, "dictionary"),
        (set, "set"),
        (bool, "boolean"),
        (type(None), "None type")
    ]
    
    for obj in test_objects:
        obj_type = type(obj).__name__
        checks = []
        for check_type, type_name in type_checks:
            if isinstance(obj, check_type):
                checks.append(type_name)
        
        print(f"  {repr(obj)} ({obj_type}): {', '.join(checks) if checks else 'no matches'}")
    
    # Multiple type checking
    def is_numeric(value):
        \"\"\"Check if value is numeric (int or float).\"\"\""
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    
    def is_sequence(value):
        \"\"\"Check if value is a sequence (but not string).\"\"\""
        return isinstance(value, (list, tuple)) and not isinstance(value, str)
    
    def is_iterable(value):
        \"\"\"Check if value is iterable.\"\"\""
        try:
            iter(value)
            return True
        except TypeError:
            return False
    
    print("\\nCustom type validation:")
    for obj in test_objects:
        validations = []
        if is_numeric(obj):
            validations.append("numeric")
        if is_sequence(obj):
            validations.append("sequence")
        if is_iterable(obj):
            validations.append("iterable")
        
        print(f"  {repr(obj)}: {', '.join(validations) if validations else 'none'}")
    
    # Attribute checking with hasattr
    class SampleClass:
        def __init__(self):
            self.instance_attr = "instance"
            self._private_attr = "private"
        
        def instance_method(self):
            return "method"
        
        @classmethod
        def class_method(cls):
            return "class method"
        
        @staticmethod
        def static_method():
            return "static method"
    
    sample_obj = SampleClass()
    
    attributes_to_check = [
        "instance_attr",
        "_private_attr",
        "instance_method",
        "class_method",
        "static_method",
        "nonexistent_attr",
        "__init__",
        "__class__",
        "__dict__"
    ]
    
    print("\\nhasattr() validation:")
    for attr in attributes_to_check:
        has_attr = hasattr(sample_obj, attr)
        print(f"  {attr}: {has_attr}")
    
    # Callable checking
    callable_test = [
        print,
        len,
        lambda x: x,
        SampleClass,
        sample_obj.instance_method,
        "not callable",
        42,
        []
    ]
    
    print("\\nCallable validation:")
    for obj in callable_test:
        is_call = callable(obj)
        print(f"  {repr(obj)}: {is_call}")
    
    # Class hierarchy checking with issubclass
    class Animal:
        pass
    
    class Mammal(Animal):
        pass
    
    class Dog(Mammal):
        pass
    
    class Cat(Mammal):
        pass
    
    class Fish(Animal):
        pass
    
    classes = [Animal, Mammal, Dog, Cat, Fish]
    
    print("\\nClass hierarchy (issubclass):")
    print("Classes:", [cls.__name__ for cls in classes])
    
    for cls in classes:
        relationships = []
        if issubclass(cls, Animal):
            relationships.append("Animal")
        if issubclass(cls, Mammal):
            relationships.append("Mammal")
        
        print(f"  {cls.__name__} is subclass of: {', '.join(relationships) if relationships else 'none'}")
    
    # Advanced type validation
    def detailed_type_info(obj):
        \"\"\"Get detailed type information about an object.\"\"\""
        info = {
            "value": repr(obj),
            "type": type(obj).__name__,
            "module": type(obj).__module__,
            "mro": [cls.__name__ for cls in type(obj).__mro__],
            "is_callable": callable(obj),
            "is_iterable": is_iterable(obj),
            "has_len": hasattr(obj, "__len__"),
            "has_getitem": hasattr(obj, "__getitem__"),
            "dir_count": len(dir(obj))
        }
        
        # Type-specific information
        if isinstance(obj, (list, tuple, str, dict, set)):
            info["length"] = len(obj)
        
        if isinstance(obj, (int, float)):
            info["is_positive"] = obj > 0
            info["is_zero"] = obj == 0
        
        if isinstance(obj, str):
            info["is_empty"] = len(obj) == 0
            info["is_alpha"] = obj.isalpha()
            info["is_digit"] = obj.isdigit()
        
        return info
    
    print("\\nDetailed type analysis:")
    sample_objects = [42, "hello", [1, 2, 3], {"key": "value"}, lambda x: x]
    
    for obj in sample_objects:
        info = detailed_type_info(obj)
        print(f"\\n  {info['value']} ({info['type']}):")
        for key, value in info.items():
            if key != "value":
                print(f"    {key}: {value}")
    
    return {
        "type_checks": {repr(obj): [name for check_type, name in type_checks if isinstance(obj, check_type)] for obj in test_objects},
        "custom_validations": {repr(obj): {"numeric": is_numeric(obj), "sequence": is_sequence(obj), "iterable": is_iterable(obj)} for obj in test_objects},
        "hasattr_results": {attr: hasattr(sample_obj, attr) for attr in attributes_to_check},
        "callable_results": {repr(obj): callable(obj) for obj in callable_test}
    }

def data_cleaner():
    """Clean and convert messy data using type conversions."""
    print("\\n=== Data Cleaning and Conversion ===")
    
    # Messy dataset simulation
    messy_data = [
        {"name": "Alice", "age": "25", "salary": "$50,000", "active": "true"},
        {"name": "Bob", "age": 30, "salary": 60000, "active": True},
        {"name": "Charlie", "age": "invalid", "salary": "N/A", "active": "false"},
        {"name": "", "age": None, "salary": "$45,500.50", "active": 0},
        {"name": "Diana", "age": "28", "salary": "55000.0", "active": 1},
        {"name": None, "age": "35", "salary": "", "active": "yes"}
    ]
    
    print("Original messy data:")
    for i, record in enumerate(messy_data):
        print(f"  {i}: {record}")
    
    def clean_name(name):
        \"\"\"Clean name field.\"\"\""
        if name is None or name == "":
            return "Unknown"
        return str(name).strip().title()
    
    def clean_age(age):
        \"\"\"Clean age field.\"\"\""
        try:
            age_val = int(float(str(age)))
            return age_val if 0 <= age_val <= 150 else None
        except (ValueError, TypeError):
            return None
    
    def clean_salary(salary):
        \"\"\"Clean salary field.\"\"\""
        if salary is None or salary == "" or str(salary).upper() == "N/A":
            return None
        
        # Remove currency symbols and commas
        salary_str = str(salary).replace("$", "").replace(",", "")
        
        try:
            return float(salary_str)
        except (ValueError, TypeError):
            return None
    
    def clean_active(active):
        \"\"\"Clean active field.\"\"\""
        if active is None:
            return False
        
        if isinstance(active, bool):
            return active
        
        if isinstance(active, (int, float)):
            return bool(active)
        
        if isinstance(active, str):
            active_lower = active.lower().strip()
            true_values = {"true", "yes", "1", "active", "on"}
            false_values = {"false", "no", "0", "inactive", "off"}
            
            if active_lower in true_values:
                return True
            elif active_lower in false_values:
                return False
        
        return False
    
    # Clean the data
    cleaned_data = []
    for record in messy_data:
        cleaned_record = {
            "name": clean_name(record.get("name")),
            "age": clean_age(record.get("age")),
            "salary": clean_salary(record.get("salary")),
            "active": clean_active(record.get("active"))
        }
        cleaned_data.append(cleaned_record)
    
    print("\\nCleaned data:")
    for i, record in enumerate(cleaned_data):
        print(f"  {i}: {record}")
    
    # Data validation and statistics
    valid_records = [r for r in cleaned_data if r["name"] != "Unknown" and r["age"] is not None]
    
    print(f"\\nData quality statistics:")
    print(f"  Total records: {len(cleaned_data)}")
    print(f"  Valid records: {len(valid_records)}")
    print(f"  Records with missing names: {sum(1 for r in cleaned_data if r['name'] == 'Unknown')}")
    print(f"  Records with missing ages: {sum(1 for r in cleaned_data if r['age'] is None)}")
    print(f"  Records with missing salaries: {sum(1 for r in cleaned_data if r['salary'] is None)}")
    print(f"  Active employees: {sum(1 for r in cleaned_data if r['active'])}")
    
    # Convert to different formats
    def to_csv_format(data):
        \"\"\"Convert to CSV-like format.\"\"\""
        headers = ["name", "age", "salary", "active"]
        rows = [headers]
        
        for record in data:
            row = [
                record["name"] or "",
                str(record["age"]) if record["age"] is not None else "",
                f"{record['salary']:.2f}" if record["salary"] is not None else "",
                "Yes" if record["active"] else "No"
            ]
            rows.append(row)
        
        return rows
    
    def to_json_format(data):
        \"\"\"Convert to JSON-serializable format.\"\"\""
        json_data = []
        for record in data:
            json_record = {}
            for key, value in record.items():
                if value is not None:
                    json_record[key] = value
            json_data.append(json_record)
        return json_data
    
    csv_format = to_csv_format(cleaned_data)
    json_format = to_json_format(cleaned_data)
    
    print("\\nCSV format (first 3 rows):")
    for row in csv_format[:3]:
        print(f"  {','.join(row)}")
    
    print("\\nJSON format (first 2 records):")
    for record in json_format[:2]:
        print(f"  {record}")
    
    return {
        "original_count": len(messy_data),
        "cleaned_count": len(cleaned_data),
        "valid_count": len(valid_records),
        "cleaned_data": cleaned_data,
        "csv_format": csv_format,
        "json_format": json_format
    }

def type_analyzer():
    """Analyze and categorize data types in complex structures."""
    print("\\n=== Type Analysis and Categorization ===")
    
    # Complex nested data structure
    complex_data = {
        "users": [
            {"id": 1, "name": "Alice", "scores": [85, 92, 78], "active": True},
            {"id": 2, "name": "Bob", "scores": [88, 90, 95], "active": False},
            {"id": 3, "name": "Charlie", "scores": [], "active": None}
        ],
        "metadata": {
            "version": 1.2,
            "created": "2024-01-15",
            "tags": ["production", "user-data"],
            "config": {
                "max_users": 1000,
                "timeout": 30.5,
                "features": {"notifications": True, "analytics": False}
            }
        },
        "statistics": (100, 85.5, 92),
        "errors": None,
        "lambda_func": lambda x: x * 2
    }
    
    def analyze_type(obj, path="root"):
        \"\"\"Recursively analyze types in nested structure.\"\"\""
        analysis = {
            "path": path,
            "type": type(obj).__name__,
            "value": repr(obj) if len(repr(obj)) < 50 else f"{repr(obj)[:47]}...",
            "size": None,
            "children": []
        }
        
        # Add size information for sized objects
        if hasattr(obj, "__len__"):
            try:
                analysis["size"] = len(obj)
            except:
                pass
        
        # Recursively analyze nested structures
        if isinstance(obj, dict):
            for key, value in obj.items():
                child_analysis = analyze_type(value, f"{path}.{key}")
                analysis["children"].append(child_analysis)
        
        elif isinstance(obj, (list, tuple)):
            for i, item in enumerate(obj):
                child_analysis = analyze_type(item, f"{path}[{i}]")
                analysis["children"].append(child_analysis)
        
        return analysis
    
    # Perform type analysis
    type_analysis = analyze_type(complex_data)
    
    def print_analysis(analysis, indent=0):
        \"\"\"Print type analysis in tree format.\"\"\""
        indent_str = "  " * indent
        size_info = f" (size: {analysis['size']})" if analysis["size"] is not None else ""
        print(f"{indent_str}{analysis['path']}: {analysis['type']}{size_info}")
        
        for child in analysis["children"]:
            print_analysis(child, indent + 1)
    
    print("Type analysis tree:")
    print_analysis(type_analysis)
    
    # Collect type statistics
    def collect_type_stats(analysis, stats=None):
        \"\"\"Collect statistics about types in the structure.\"\"\""
        if stats is None:
            stats = {}
        
        type_name = analysis["type"]
        stats[type_name] = stats.get(type_name, 0) + 1
        
        for child in analysis["children"]:
            collect_type_stats(child, stats)
        
        return stats
    
    type_stats = collect_type_stats(type_analysis)
    
    print("\\nType statistics:")
    for type_name, count in sorted(type_stats.items()):
        print(f"  {type_name}: {count}")
    
    # Find all paths of specific types
    def find_paths_by_type(analysis, target_type, paths=None):
        \"\"\"Find all paths containing objects of a specific type.\"\"\""
        if paths is None:
            paths = []
        
        if analysis["type"] == target_type:
            paths.append(analysis["path"])
        
        for child in analysis["children"]:
            find_paths_by_type(child, target_type, paths)
        
        return paths
    
    # Find paths for different types
    string_paths = find_paths_by_type(type_analysis, "str")
    list_paths = find_paths_by_type(type_analysis, "list")
    dict_paths = find_paths_by_type(type_analysis, "dict")
    
    print(f"\\nString paths: {string_paths}")
    print(f"List paths: {list_paths}")
    print(f"Dict paths: {dict_paths}")
    
    # Type conversion suggestions
    def suggest_conversions(analysis, suggestions=None):
        \"\"\"Suggest possible type conversions.\"\"\""
        if suggestions is None:
            suggestions = []
        
        type_name = analysis["type"]
        path = analysis["path"]
        
        # Suggest conversions based on type and context
        if type_name == "str":
            suggestions.append(f"{path}: Consider int() or float() if numeric")
        elif type_name == "list" and analysis["size"] == 0:
            suggestions.append(f"{path}: Empty list - consider None or default value")
        elif type_name == "NoneType":
            suggestions.append(f"{path}: None value - consider default or validation")
        
        for child in analysis["children"]:
            suggest_conversions(child, suggestions)
        
        return suggestions
    
    conversion_suggestions = suggest_conversions(type_analysis)
    
    print("\\nConversion suggestions:")
    for suggestion in conversion_suggestions[:5]:  # Show first 5
        print(f"  {suggestion}")
    
    # Memory usage estimation (simplified)
    def estimate_memory_usage(obj):
        \"\"\"Estimate memory usage of object.\"\"\""
        import sys
        
        try:
            return sys.getsizeof(obj)
        except:
            return 0
    
    def total_memory_estimate(analysis):
        \"\"\"Estimate total memory usage.\"\"\""
        # This is a simplified estimation
        base_sizes = {
            "int": 28,
            "float": 24,
            "str": 50,  # Base + content
            "list": 56,  # Base + items
            "dict": 240,  # Base + items
            "tuple": 48,
            "bool": 28,
            "NoneType": 16
        }
        
        total = base_sizes.get(analysis["type"], 32)
        
        # Add estimated size for containers
        if analysis["size"] is not None:
            if analysis["type"] in ["str"]:
                total += analysis["size"]
            elif analysis["type"] in ["list", "tuple"]:
                total += analysis["size"] * 8  # Pointer size
            elif analysis["type"] == "dict":
                total += analysis["size"] * 24  # Key-value pairs
        
        # Add children
        for child in analysis["children"]:
            total += total_memory_estimate(child)
        
        return total
    
    memory_estimate = total_memory_estimate(type_analysis)
    
    print(f"\\nEstimated memory usage: {memory_estimate} bytes ({memory_estimate/1024:.2f} KB)")
    
    return {
        "type_stats": type_stats,
        "string_paths": string_paths,
        "conversion_suggestions": conversion_suggestions,
        "memory_estimate": memory_estimate,
        "total_objects": sum(type_stats.values())
    }

# Main execution
if __name__ == "__main__":
    print("=== Built-in Type Conversion and Validation Functions ===")
    
    print("\\n1. Type Conversion:")
    conversion_results = type_converter()
    
    print("\\n2. Safe Conversion:")
    safe_results = safe_converter()
    
    print("\\n3. Type Validation:")
    validation_results = type_validator()
    
    print("\\n4. Data Cleaning:")
    cleaning_results = data_cleaner()
    
    print("\\n5. Type Analysis:")
    analysis_results = type_analyzer()
    
    print("\\n" + "="*60)
    print("=== TYPE OPERATIONS COMPLETE ===")
    print("✓ Basic type conversions")
    print("✓ Safe conversion with error handling")
    print("✓ Type validation and checking")
    print("✓ Data cleaning and normalization")
    print("✓ Complex type analysis")
    print("✓ Memory usage estimation")
```

## Hints

- Use `try-except` blocks for safe type conversion
- `isinstance()` is preferred over `type()` for type checking
- Check for `None` values before conversion attempts
- Use `hasattr()` to check for method/attribute existence
- `callable()` tests if object can be called like a function

## Practice Cases

Your functions should handle:

1. Invalid conversion attempts gracefully
2. Multiple type checking scenarios
3. Nested data structure validation
4. Edge cases like `None`, empty strings, zero values
5. Complex object hierarchies and inheritance

## Bonus Challenge

Create a robust data validation framework, implement automatic type inference for datasets, and build a type-safe configuration system!