# Input/Output and Format Functions - Practice 7

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Master Python's built-in input/output functions including `input()`, `print()`, `format()`, `repr()`, `ascii()`, and advanced formatting techniques for user interaction and data presentation.

## Objectives

- Handle user input with `input()` and type conversion
- Master `print()` function with various options and formatting
- Use `format()` and f-strings for string formatting
- Understand `repr()`, `str()`, and `ascii()` for object representation
- Apply advanced formatting techniques for data presentation

## Your Tasks

1. **input_operations()** - Handle various types of user input
2. **print_formatting()** - Master print function options and formatting
3. **string_formatting()** - Use format() and f-strings effectively
4. **representation_functions()** - Work with repr(), str(), and ascii()
5. **advanced_formatting()** - Apply complex formatting patterns

## Example

```python
import sys
import io
from datetime import datetime, date
from decimal import Decimal
import json
import csv
from contextlib import redirect_stdout

def input_operations():
    """Demonstrate input function and user interaction patterns."""
    print("=== Input Operations ===")
    
    # Simulate user input for demonstration
    # In real scenarios, these would come from actual user input
    
    simulated_inputs = [
        "John Doe",
        "25",
        "3.14159",
        "True",
        "[1, 2, 3, 4, 5]",
        "{'name': 'Alice', 'age': 30}",
        "2024-01-15",
        "not a number",
        ""
    ]
    
    input_index = 0
    
    def mock_input(prompt=""):
        """Mock input function for demonstration."""
        nonlocal input_index
        if input_index < len(simulated_inputs):
            value = simulated_inputs[input_index]
            input_index += 1
            print(f"{prompt}{value}")
            return value
        return ""
    
    print("Basic Input Operations:")
    
    # Basic string input
    name = mock_input("Enter your name: ")
    print(f"Hello, {name}!")
    
    # Numeric input with validation
    print("\\nNumeric Input with Validation:")
    
    def get_integer(prompt, min_val=None, max_val=None):
        while True:
            try:
                value = int(mock_input(prompt))
                if min_val is not None and value < min_val:
                    print(f"Value must be at least {min_val}")
                    continue
                if max_val is not None and value > max_val:
                    print(f"Value must be at most {max_val}")
                    continue
                return value
            except ValueError:
                print("Please enter a valid integer")
                # In real scenario, would continue loop
                return 0  # For demo purposes
    
    age = get_integer("Enter your age (0-120): ", 0, 120)
    print(f"You are {age} years old")
    
    # Float input
    print("\\nFloat Input:")
    
    def get_float(prompt):
        try:
            return float(mock_input(prompt))
        except ValueError:
            print("Invalid float, using default")
            return 0.0
    
    pi_value = get_float("Enter a decimal number: ")
    print(f"You entered: {pi_value}")
    
    # Boolean input
    print("\\nBoolean Input:")
    
    def get_boolean(prompt):
        response = mock_input(prompt).lower()
        return response in ['true', 'yes', 'y', '1', 'on']
    
    is_student = get_boolean("Are you a student? (yes/no): ")
    print(f"Student status: {is_student}")
    
    # List input
    print("\\nList Input:")
    
    def get_list(prompt):
        try:
            input_str = mock_input(prompt)
            # Try to evaluate as Python literal
            import ast
            return ast.literal_eval(input_str)
        except (ValueError, SyntaxError):
            print("Invalid list format, using empty list")
            return []
    
    numbers = get_list("Enter a list of numbers [1,2,3]: ")
    print(f"Your list: {numbers}")
    print(f"Sum: {sum(numbers) if numbers else 0}")
    
    # Dictionary input
    print("\\nDictionary Input:")
    
    def get_dict(prompt):
        try:
            input_str = mock_input(prompt)
            import ast
            result = ast.literal_eval(input_str)
            if isinstance(result, dict):
                return result
            else:
                print("Input is not a dictionary")
                return {}
        except (ValueError, SyntaxError):
            print("Invalid dictionary format")
            return {}
    
    user_data = get_dict("Enter user data as dict: ")
    print(f"User data: {user_data}")
    
    # Date input
    print("\\nDate Input:")
    
    def get_date(prompt):
        try:
            date_str = mock_input(prompt)
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format, using today")
            return date.today()
    
    birth_date = get_date("Enter birth date (YYYY-MM-DD): ")
    print(f"Birth date: {birth_date}")
    
    # Multi-line input simulation
    print("\\nMulti-line Input:")
    
    def get_multiline_input():
        lines = []
        print("Enter multiple lines (empty line to finish):")
        
        # Simulate multi-line input
        sample_lines = ["Line 1", "Line 2", "Line 3", ""]
        for line in sample_lines:
            if line:
                print(f"> {line}")
                lines.append(line)
            else:
                print("> (empty line - finished)")
                break
        
        return "\\n".join(lines)
    
    multi_text = get_multiline_input()
    print(f"Multi-line text:\\n{multi_text}")
    
    # Input with default values
    print("\\nInput with Defaults:")
    
    def get_input_with_default(prompt, default):
        response = mock_input(f"{prompt} (default: {default}): ")
        return response if response.strip() else default
    
    username = get_input_with_default("Enter username", "guest")
    print(f"Username: {username}")
    
    # Secure input simulation (password)
    print("\\nSecure Input (Password):")
    
    def get_password():
        # In real applications, use getpass module
        import getpass
        try:
            # Simulate password input
            password = "hidden_password"
            print("Password: " + "*" * len(password))
            return password
        except KeyboardInterrupt:
            print("\\nPassword input cancelled")
            return ""
    
    password = get_password()
    print(f"Password length: {len(password)}")
    
    return {
        "name": name,
        "age": age,
        "pi_value": pi_value,
        "is_student": is_student,
        "numbers": numbers,
        "user_data": user_data,
        "birth_date": str(birth_date),
        "multi_text_lines": len(multi_text.split("\\n")),
        "username": username,
        "password_length": len(password)
    }

def print_formatting():
    """Demonstrate print function options and formatting."""
    print("\\n=== Print Formatting ===")
    
    # Capture print output for demonstration
    output_buffer = io.StringIO()
    
    print("Basic Print Operations:")
    
    # Basic printing
    print("Hello, World!")
    print("Multiple", "arguments", "separated", "by", "spaces")
    print(1, 2, 3, 4, 5)
    
    # Custom separator
    print("\\nCustom Separators:")
    print("A", "B", "C", "D", sep="-")
    print("apple", "banana", "cherry", sep=" | ")
    print(1, 2, 3, 4, sep="")
    print("HTML", "tags", sep="</li><li>")
    
    # Custom end character
    print("\\nCustom End Characters:")
    print("Loading", end="")
    for i in range(5):
        print(".", end="")
    print(" Done!")
    
    print("Line 1", end=" -> ")
    print("Line 2")
    
    # Print to different streams
    print("\\nPrint to Different Streams:")
    
    # Capture stdout
    with redirect_stdout(output_buffer):
        print("This goes to buffer")
        print("Multiple lines")
        print("In the buffer")
    
    captured_output = output_buffer.getvalue()
    print(f"Captured output:\\n{captured_output}")
    
    # Print to stderr (for errors)
    print("Error message", file=sys.stderr)
    print("Normal output to stdout")
    
    # Flush output
    print("\\nFlush Output:")
    print("Immediate output", flush=True)
    
    # Print formatting with variables
    print("\\nVariable Formatting:")
    
    name = "Alice"
    age = 30
    salary = 75000.50
    
    # Old-style formatting
    print("Old style: %s is %d years old and earns $%.2f" % (name, age, salary))
    
    # .format() method
    print("Format method: {} is {} years old and earns ${:.2f}".format(name, age, salary))
    
    # f-strings (Python 3.6+)
    print(f"F-string: {name} is {age} years old and earns ${salary:.2f}")
    
    # Print with alignment
    print("\\nAlignment and Padding:")
    
    items = [
        ("Product", "Price", "Quantity"),
        ("Apple", 1.50, 10),
        ("Banana", 0.75, 25),
        ("Orange", 2.00, 8),
        ("Grape", 3.25, 12)
    ]
    
    # Print table with formatting
    for item, price, qty in items:
        if isinstance(price, str):  # Header row
            print(f"{item:<12} {price:>8} {qty:>8}")
        else:
            print(f"{item:<12} ${price:>7.2f} {qty:>8}")
    
    # Print with colors (ANSI escape codes)
    print("\\nColor Printing (ANSI):")
    
    # Color codes
    RED = "\\033[31m"
    GREEN = "\\033[32m"
    YELLOW = "\\033[33m"
    BLUE = "\\033[34m"
    RESET = "\\033[0m"
    
    print(f"{RED}This is red text{RESET}")
    print(f"{GREEN}This is green text{RESET}")
    print(f"{YELLOW}This is yellow text{RESET}")
    print(f"{BLUE}This is blue text{RESET}")
    
    # Print progress bar
    print("\\nProgress Bar:")
    
    def print_progress_bar(percentage, width=20):
        filled = int(width * percentage / 100)
        bar = "█" * filled + "░" * (width - filled)
        print(f"\\r[{bar}] {percentage:3.0f}%", end="", flush=True)
    
    for i in range(0, 101, 20):
        print_progress_bar(i)
    print()  # New line after progress bar
    
    # Print with Unicode
    print("\\nUnicode Printing:")
    
    unicode_chars = ["★", "♠", "♥", "♦", "♣", "→", "←", "↑", "↓", "⚡", "🐍", "🔥"]
    print("Unicode characters:", " ".join(unicode_chars))
    
    # Print boxed text
    print("\\nBoxed Text:")
    
    def print_boxed(text, width=None):
        if width is None:
            width = len(text) + 4
        
        horizontal = "─" * (width - 2)
        print(f"┌{horizontal}┐")
        
        lines = text.split("\\n")
        for line in lines:
            padding = width - len(line) - 3
            print(f"│ {line}{' ' * padding}│")
        
        print(f"└{horizontal}┘")
    
    print_boxed("Hello\\nWorld!")
    
    # Print JSON formatted
    print("\\nJSON Formatting:")
    
    data = {
        "name": "John Doe",
        "age": 30,
        "skills": ["Python", "JavaScript", "SQL"],
        "active": True,
        "salary": None
    }
    
    print("Compact JSON:")
    print(json.dumps(data, separators=(',', ':')))
    
    print("\\nFormatted JSON:")
    print(json.dumps(data, indent=2))
    
    # Print debugging info
    print("\\nDebugging Print:")
    
    variables = {"x": 10, "y": 20, "result": 30}
    
    for name, value in variables.items():
        print(f"DEBUG: {name} = {value} ({type(value).__name__})")
    
    return {
        "captured_output": captured_output.strip(),
        "table_items": len(items),
        "unicode_chars": unicode_chars,
        "json_data": data,
        "debug_variables": variables
    }

def string_formatting():
    """Demonstrate format() function and advanced string formatting."""
    print("\\n=== String Formatting ===")
    
    # Basic format() usage
    print("Basic format() Usage:")
    
    template = "Hello, {}! You are {} years old."
    formatted = template.format("Alice", 25)
    print(formatted)
    
    # Positional arguments
    print("\\nPositional Arguments:")
    
    template = "{0} + {1} = {2}"
    result = template.format(5, 3, 8)
    print(result)
    
    # Reusing arguments
    template = "{0} {1} {0}"
    result = template.format("Hello", "World")
    print(result)
    
    # Named arguments
    print("\\nNamed Arguments:")
    
    template = "{name} is {age} years old and lives in {city}"
    result = template.format(name="Bob", age=30, city="New York")
    print(result)
    
    # Mixing positional and named
    template = "{0} {name} is {1} years old"
    result = template.format("Mr.", "Charlie", name="Smith")
    print(result)
    
    # Format specifications
    print("\\nFormat Specifications:")
    
    # Number formatting
    number = 1234.5678
    
    print(f"Original: {number}")
    print(f"2 decimal places: {number:.2f}")
    print(f"No decimal places: {number:.0f}")
    print(f"Scientific notation: {number:.2e}")
    print(f"Percentage: {0.1234:.2%}")
    
    # Integer formatting
    integer = 42
    
    print(f"\\nInteger: {integer}")
    print(f"Binary: {integer:b}")
    print(f"Octal: {integer:o}")
    print(f"Hexadecimal: {integer:x}")
    print(f"Hexadecimal (upper): {integer:X}")
    
    # Padding and alignment
    print("\\nPadding and Alignment:")
    
    text = "Python"
    number = 123
    
    print(f"'{text}' left-aligned in 20 chars: '{text:<20}'")
    print(f"'{text}' right-aligned in 20 chars: '{text:>20}'")
    print(f"'{text}' center-aligned in 20 chars: '{text:^20}'")
    print(f"'{number}' zero-padded to 8 digits: '{number:08d}'")
    
    # Custom fill characters
    print(f"'{text}' centered with dots: '{text:.<20}'")
    print(f"'{text}' centered with stars: '{text:*^20}'")
    
    # Advanced number formatting
    print("\\nAdvanced Number Formatting:")
    
    large_number = 1234567890
    print(f"Large number with commas: {large_number:,}")
    print(f"Large number with underscores: {large_number:_}")
    
    # Currency formatting
    price = 1234.56
    print(f"Currency (simple): ${price:.2f}")
    print(f"Currency (formatted): {price:,.2f}")
    
    # Sign handling
    positive = 42
    negative = -42
    zero = 0
    
    print(f"\\nSign Handling:")
    print(f"Positive: {positive:+d}")
    print(f"Negative: {negative:+d}")
    print(f"Zero: {zero:+d}")
    print(f"Space for positive: {positive: d}")
    
    # Date and time formatting
    print("\\nDate and Time Formatting:")
    
    now = datetime.now()
    
    print(f"Current time: {now}")
    print(f"Formatted date: {now:%Y-%m-%d}")
    print(f"Formatted time: {now:%H:%M:%S}")
    print(f"Full format: {now:%A, %B %d, %Y at %I:%M %p}")
    
    # Dictionary formatting
    print("\\nDictionary Formatting:")
    
    person = {
        "name": "Diana",
        "age": 28,
        "occupation": "Engineer",
        "salary": 75000
    }
    
    # Access dictionary values in format string
    template = "{name} is a {age}-year-old {occupation} earning ${salary:,}"
    result = template.format(**person)
    print(result)
    
    # Object attribute formatting
    print("\\nObject Attribute Formatting:")
    
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    person_obj = Person("Eve", 32)
    template = "{p.name} is {p.age} years old"
    result = template.format(p=person_obj)
    print(result)
    
    # Format method chaining
    print("\\nFormat Method Chaining:")
    
    template = "Processing {item}... {status}"
    
    items = ["file1.txt", "file2.txt", "file3.txt"]
    statuses = ["✓ Done", "✗ Error", "⚠ Warning"]
    
    for item, status in zip(items, statuses):
        print(template.format(item=item, status=status))
    
    # Custom format function
    print("\\nCustom Format Functions:")
    
    def format_bytes(bytes_value):
        """Format bytes in human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_value < 1024.0:
                return f"{bytes_value:.1f} {unit}"
            bytes_value /= 1024.0
        return f"{bytes_value:.1f} PB"
    
    file_sizes = [512, 2048, 1048576, 1073741824, 1099511627776]
    
    for size in file_sizes:
        print(f"{size} bytes = {format_bytes(size)}")
    
    # Template strings (alternative to format)
    print("\\nTemplate Strings:")
    
    from string import Template
    
    template = Template("$name lives in $city and works as a $job")
    result = template.substitute(name="Frank", city="Boston", job="Developer")
    print(result)
    
    # Safe substitution (handles missing keys)
    template = Template("$name likes $food and $drink")
    result = template.safe_substitute(name="Grace", food="pizza")
    print(f"Safe substitution: {result}")
    
    return {
        "basic_format": formatted,
        "positional_format": result,
        "named_format": template.format(name="Bob", age=30, city="New York"),
        "number_formats": {
            "decimal": f"{number:.2f}",
            "scientific": f"{number:.2e}",
            "percentage": f"{0.1234:.2%}"
        },
        "alignment_examples": {
            "left": f"{text:<20}",
            "right": f"{text:>20}",
            "center": f"{text:^20}"
        },
        "large_number_comma": f"{large_number:,}",
        "person_format": result,
        "byte_formats": [format_bytes(size) for size in file_sizes],
        "template_result": result
    }

def representation_functions():
    """Demonstrate repr(), str(), and ascii() functions."""
    print("\\n=== Representation Functions ===")
    
    # str() vs repr()
    print("str() vs repr():")
    
    test_objects = [
        "Hello\\nWorld",
        42,
        3.14159,
        [1, 2, 3],
        {"key": "value"},
        datetime.now(),
        None,
        True
    ]
    
    for obj in test_objects:
        str_repr = str(obj)
        repr_repr = repr(obj)
        print(f"Object: {type(obj).__name__}")
        print(f"  str():  {str_repr}")
        print(f"  repr(): {repr_repr}")
        print(f"  Same: {str_repr == repr_repr}")
        print()
    
    # ASCII representation
    print("ASCII Representation:")
    
    unicode_strings = [
        "Hello",
        "Café",
        "Python🐍",
        "Émile",
        "北京",
        "مرحبا",
        "Здравствуй"
    ]
    
    for text in unicode_strings:
        ascii_repr = ascii(text)
        print(f"'{text}' -> {ascii_repr}")
    
    # Custom __str__ and __repr__
    print("\\nCustom __str__ and __repr__:")
    
    class Book:
        def __init__(self, title, author, year):
            self.title = title
            self.author = author
            self.year = year
        
        def __str__(self):
            return f"'{self.title}' by {self.author}"
        
        def __repr__(self):
            return f"Book('{self.title}', '{self.author}', {self.year})"
    
    book = Book("1984", "George Orwell", 1949)
    
    print(f"Book object:")
    print(f"  str(book):  {str(book)}")
    print(f"  repr(book): {repr(book)}")
    print(f"  book:       {book}")  # Uses __str__
    
    # Collections with custom objects
    print("\\nCollections with Custom Objects:")
    
    books = [
        Book("1984", "George Orwell", 1949),
        Book("To Kill a Mockingbird", "Harper Lee", 1960),
        Book("Pride and Prejudice", "Jane Austen", 1813)
    ]
    
    print(f"List of books (str): {str(books)}")
    print(f"List of books (repr): {repr(books)}")
    
    # Nested structures
    print("\\nNested Structures:")
    
    nested_data = {
        "users": [
            {"name": "Alice", "data": [1, 2, 3]},
            {"name": "Bob", "data": [4, 5, 6]}
        ],
        "meta": {
            "version": "1.0",
            "created": datetime(2024, 1, 1, 12, 0, 0)
        }
    }
    
    print("Nested data structure:")
    print(f"str():\\n{str(nested_data)}")
    print(f"\\nrepr():\\n{repr(nested_data)}")
    
    # Debugging with repr
    print("\\nDebugging with repr:")
    
    def debug_vars(**kwargs):
        for name, value in kwargs.items():
            print(f"{name} = {repr(value)}")
    
    name = "John\\tDoe"
    numbers = [1, 2, 3, None, "4"]
    config = {"debug": True, "timeout": 30.5}
    
    debug_vars(name=name, numbers=numbers, config=config)
    
    # Eval and repr relationship
    print("\\nEval and repr relationship:")
    
    # For simple objects, eval(repr(obj)) should recreate the object
    simple_objects = [
        42,
        "hello",
        [1, 2, 3],
        {"a": 1, "b": 2},
        (1, 2, 3)
    ]
    
    for obj in simple_objects:
        repr_str = repr(obj)
        try:
            recreated = eval(repr_str)
            is_equal = obj == recreated
            print(f"{repr_str} -> eval() -> {recreated} (Equal: {is_equal})")
        except:
            print(f"{repr_str} -> eval() failed")
    
    # String escaping comparison
    print("\\nString Escaping Comparison:")
    
    special_strings = [
        "Line 1\\nLine 2",
        "Tab\\there",
        "Quote: \\"Hello\\"",
        "Backslash: \\\\",
        "Unicode: \\u2603"  # Snowman
    ]
    
    for s in special_strings:
        print(f"Original: {s}")
        print(f"repr():   {repr(s)}")
        print(f"ascii():  {ascii(s)}")
        print()
    
    # Pretty printing for complex objects
    print("Pretty Printing:")
    
    import pprint
    
    complex_data = {
        "level1": {
            "level2a": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "level2b": {
                "level3": {
                    "items": ["a", "b", "c", "d", "e"],
                    "values": list(range(20))
                }
            }
        }
    }
    
    print("Regular repr:")
    print(repr(complex_data))
    
    print("\\nPretty printed:")
    pprint.pprint(complex_data, width=50)
    
    return {
        "str_vs_repr": [(str(obj), repr(obj), str(obj) == repr(obj)) for obj in test_objects[:3]],
        "ascii_representations": [(text, ascii(text)) for text in unicode_strings[:3]],
        "book_representations": {
            "str": str(book),
            "repr": repr(book)
        },
        "eval_success": [obj == eval(repr(obj)) for obj in simple_objects],
        "special_string_escapes": [(s, repr(s), ascii(s)) for s in special_strings[:2]]
    }

def advanced_formatting():
    """Demonstrate advanced formatting patterns and techniques."""
    print("\\n=== Advanced Formatting ===")
    
    # Conditional formatting
    print("Conditional Formatting:")
    
    students = [
        {"name": "Alice", "grade": 95},
        {"name": "Bob", "grade": 87},
        {"name": "Charlie", "grade": 92},
        {"name": "Diana", "grade": 78},
        {"name": "Eve", "grade": 65}
    ]
    
    def format_grade(grade):
        if grade >= 90:
            return f"🟢 {grade}% (Excellent)"
        elif grade >= 80:
            return f"🟡 {grade}% (Good)"
        elif grade >= 70:
            return f"🟠 {grade}% (Average)"
        else:
            return f"🔴 {grade}% (Needs Improvement)"
    
    print("Student Grades:")
    for student in students:
        formatted_grade = format_grade(student["grade"])
        print(f"  {student['name']:<10} {formatted_grade}")
    
    # Dynamic formatting based on data
    print("\\nDynamic Formatting:")
    
    data_sets = [
        {"values": [1, 2, 3], "precision": 0},
        {"values": [1.234, 2.567, 3.891], "precision": 2},
        {"values": [1234567, 2345678, 3456789], "precision": None},
        {"values": [0.001, 0.002, 0.003], "precision": 4}
    ]
    
    for i, dataset in enumerate(data_sets):
        values = dataset["values"]
        precision = dataset["precision"]
        
        print(f"Dataset {i+1}:")
        for value in values:
            if precision is None:
                # Format large numbers with commas
                print(f"  {value:,}")
            else:
                # Format with specified precision
                print(f"  {value:.{precision}f}")
    
    # Table formatting with dynamic columns
    print("\\nDynamic Table Formatting:")
    
    sales_data = [
        {"product": "Laptop", "price": 999.99, "sold": 15, "revenue": 14999.85},
        {"product": "Mouse", "price": 25.50, "sold": 150, "revenue": 3825.00},
        {"product": "Keyboard", "price": 75.00, "sold": 45, "revenue": 3375.00},
        {"product": "Monitor", "price": 299.99, "sold": 25, "revenue": 7499.75}
    ]
    
    # Calculate column widths
    headers = ["Product", "Price", "Sold", "Revenue"]
    col_widths = [len(header) for header in headers]
    
    # Update widths based on data
    for item in sales_data:
        col_widths[0] = max(col_widths[0], len(item["product"]))
        col_widths[1] = max(col_widths[1], len(f"${item['price']:.2f}"))
        col_widths[2] = max(col_widths[2], len(str(item["sold"])))
        col_widths[3] = max(col_widths[3], len(f"${item['revenue']:,.2f}"))
    
    # Print header
    header_row = " | ".join([
        headers[0].ljust(col_widths[0]),
        headers[1].rjust(col_widths[1]),
        headers[2].rjust(col_widths[2]),
        headers[3].rjust(col_widths[3])
    ])
    print(header_row)
    print("-" * len(header_row))
    
    # Print data rows
    for item in sales_data:
        row = " | ".join([
            item["product"].ljust(col_widths[0]),
            f"${item['price']:.2f}".rjust(col_widths[1]),
            str(item["sold"]).rjust(col_widths[2]),
            f"${item['revenue']:,.2f}".rjust(col_widths[3])
        ])
        print(row)
    
    # Format with locale (if available)
    print("\\nLocale-aware Formatting:")
    
    try:
        import locale
        # Try to set locale (may not work on all systems)
        try:
            locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        except locale.Error:
            print("Locale not available, using default formatting")
        
        amounts = [1234.56, 9876543.21, 0.99]
        
        for amount in amounts:
            try:
                formatted = locale.currency(amount, grouping=True)
                print(f"  {amount} -> {formatted}")
            except:
                print(f"  {amount} -> ${amount:,.2f} (fallback)")
    
    except ImportError:
        print("Locale module not available")
    
    # Percentage formatting with context
    print("\\nPercentage Formatting with Context:")
    
    metrics = [
        {"name": "CPU Usage", "value": 0.75, "threshold": 0.8},
        {"name": "Memory Usage", "value": 0.92, "threshold": 0.9},
        {"name": "Disk Usage", "value": 0.45, "threshold": 0.8},
        {"name": "Network Usage", "value": 0.15, "threshold": 0.7}
    ]
    
    for metric in metrics:
        percentage = metric["value"]
        threshold = metric["threshold"]
        
        # Color coding based on threshold
        if percentage >= threshold:
            status = "⚠️  HIGH"
            color = "🔴"
        elif percentage >= threshold * 0.7:
            status = "⚡ MEDIUM"
            color = "🟡"
        else:
            status = "✅ LOW"
            color = "🟢"
        
        print(f"{color} {metric['name']:<15} {percentage:>6.1%} ({status})")
    
    # Multi-line formatting with alignment
    print("\\nMulti-line Aligned Formatting:")
    
    code_stats = [
        {"file": "main.py", "lines": 156, "functions": 8, "classes": 2},
        {"file": "utils.py", "lines": 89, "functions": 12, "classes": 1},
        {"file": "tests.py", "lines": 234, "functions": 15, "classes": 3},
        {"file": "config.py", "lines": 45, "functions": 3, "classes": 0}
    ]
    
    print("Code Statistics:")
    print("┌" + "─" * 12 + "┬" + "─" * 8 + "┬" + "─" * 12 + "┬" + "─" * 10 + "┐")
    print("│ File       │ Lines  │ Functions  │ Classes  │")
    print("├" + "─" * 12 + "┼" + "─" * 8 + "┼" + "─" * 12 + "┼" + "─" * 10 + "┤")
    
    for stat in code_stats:
        print(f"│ {stat['file']:<10} │ {stat['lines']:>6} │ {stat['functions']:>10} │ {stat['classes']:>8} │")
    
    print("└" + "─" * 12 + "┴" + "─" * 8 + "┴" + "─" * 12 + "┴" + "─" * 10 + "┘")
    
    # Summary row
    totals = {
        "lines": sum(stat["lines"] for stat in code_stats),
        "functions": sum(stat["functions"] for stat in code_stats),
        "classes": sum(stat["classes"] for stat in code_stats)
    }
    
    print(f"Total: {totals['lines']} lines, {totals['functions']} functions, {totals['classes']} classes")
    
    # Custom formatting class
    print("\\nCustom Formatting Class:")
    
    class DataFormatter:
        def __init__(self):
            self.formatters = {
                'currency': lambda x: f"${x:,.2f}",
                'percentage': lambda x: f"{x:.1%}",
                'large_number': lambda x: f"{x:,}",
                'scientific': lambda x: f"{x:.2e}",
                'bytes': self._format_bytes
            }
        
        def _format_bytes(self, bytes_value):
            for unit in ['B', 'KB', 'MB', 'GB']:
                if bytes_value < 1024:
                    return f"{bytes_value:.1f} {unit}"
                bytes_value /= 1024
            return f"{bytes_value:.1f} TB"
        
        def format(self, value, format_type):
            formatter = self.formatters.get(format_type, str)
            return formatter(value)
    
    formatter = DataFormatter()
    
    test_values = [
        (1234.56, 'currency'),
        (0.1234, 'percentage'),
        (1234567, 'large_number'),
        (0.000001234, 'scientific'),
        (1073741824, 'bytes')
    ]
    
    print("Custom formatted values:")
    for value, format_type in test_values:
        formatted = formatter.format(value, format_type)
        print(f"  {value} ({format_type}): {formatted}")
    
    return {
        "student_grades": [(s["name"], format_grade(s["grade"])) for s in students],
        "sales_table_width": len(header_row),
        "metric_statuses": [(m["name"], m["value"], m["value"] >= m["threshold"]) for m in metrics],
        "code_totals": totals,
        "custom_formats": [(value, fmt_type, formatter.format(value, fmt_type)) for value, fmt_type in test_values]
    }

# Main execution
if __name__ == "__main__":
    print("=== Built-in Input/Output and Format Functions ===")
    
    print("\\n1. Input Operations:")
    input_results = input_operations()
    
    print("\\n2. Print Formatting:")
    print_results = print_formatting()
    
    print("\\n3. String Formatting:")
    format_results = string_formatting()
    
    print("\\n4. Representation Functions:")
    repr_results = representation_functions()
    
    print("\\n5. Advanced Formatting:")
    advanced_results = advanced_formatting()
    
    print("\\n" + "="*60)
    print("=== INPUT/OUTPUT AND FORMAT FUNCTIONS COMPLETE ===")
    print("✓ User input handling and validation")
    print("✓ Print function options and formatting")
    print("✓ String formatting with format() and f-strings")
    print("✓ Object representation with repr(), str(), ascii()")
    print("✓ Advanced formatting patterns and techniques")
    print("✓ Dynamic and conditional formatting")
    print("✓ Custom formatting implementations")
```

## Hints

- `input()` always returns a string - convert to other types as needed
- Use `print()` with `sep`, `end`, and `file` parameters for custom output
- f-strings are generally preferred for string formatting in modern Python
- `repr()` should return a string that could recreate the object
- Use format specifications like `{:.2f}` for number formatting

## Practice Cases

Your functions should handle:

1. Input validation and type conversion with error handling
2. Print formatting with custom separators, alignment, and colors
3. String formatting with various numeric and date formats
4. Representation functions for debugging and object display
5. Advanced formatting patterns for tables and dynamic content

## Bonus Challenge

Create an interactive data entry system, implement a custom formatting mini-language, and build a pretty-printing system for complex data structures!