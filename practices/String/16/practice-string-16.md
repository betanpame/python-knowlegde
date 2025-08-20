# String Manipulation Challenge - Practice 16

**Difficulty:** ⭐⭐⭐ (Easy-Medium)

**Related Topics:** String Operations, Text Processing, Parsing

## Objectives
- Work with complex string parsing and manipulation
- Handle multiple string operations in sequence
- Extract information from formatted text
- Apply string methods for data cleaning

## Description
Create a text processor that can extract and manipulate data from formatted text strings. You'll work with CSV-like data, log entries, and structured text.

## Examples
```python
# Processing CSV-like data
data = "John,25,Engineer,New York"
parsed = parse_csv_line(data)
print(parsed)  # ['John', '25', 'Engineer', 'New York']

# Cleaning log entries
log = "[2023-12-25 10:30:15] ERROR: Database connection failed (error_code: 500)"
cleaned = clean_log_entry(log)
print(cleaned)  # "Database connection failed"

# Extracting key-value pairs
config = "host=localhost;port=5432;user=admin;password=secret123"
parsed_config = parse_config_string(config)
print(parsed_config)  # {'host': 'localhost', 'port': '5432', 'user': 'admin', 'password': 'secret123'}
```

## Your Tasks
1. **parse_csv_line(line)** - Parse a CSV-like string into a list of values
2. **clean_log_entry(log_line)** - Extract the main message from a log entry
3. **parse_config_string(config)** - Convert a config string into a dictionary
4. **extract_numbers(text)** - Find and return all numbers in a text string
5. **format_phone_number(phone)** - Format a phone number consistently
6. **extract_email_parts(email)** - Split an email into username and domain
7. **standardize_name(name)** - Format a name properly (Title Case)
8. **parse_date_string(date_str)** - Extract date components from various formats

## Hints
- Use `split()` method with different separators
- `strip()` helps remove unwanted whitespace
- Regular string methods can handle most parsing tasks
- Consider edge cases like empty strings or malformed data
- String slicing and indexing are useful for extraction
- `replace()` can help clean up unwanted characters

## Practice Cases
```python
# Practice data for validation
test_cases = [
    ("Alice,30,Doctor,Boston", ['Alice', '30', 'Doctor', 'Boston']),
    ("[INFO] User logged in successfully", "User logged in successfully"),
    ("name=John;age=25", {'name': 'John', 'age': '25'}),
    ("Price: $25.99, Discount: 10%", ['25.99', '10']),
    ("555-123-4567", "(555) 123-4567"),
    ("john.doe@example.com", ("john.doe", "example.com")),
    ("JOHN DOE", "John Doe"),
    ("2023-12-25", ('2023', '12', '25'))
]
```

## Bonus Challenges
- Handle quoted values in CSV parsing
- Support different log entry formats
- Add validation for parsed data
- Handle international phone number formats
- Support multiple date formats (DD/MM/YYYY, MM-DD-YYYY, etc.)

Remember: Focus on string manipulation techniques and handle edge cases gracefully!