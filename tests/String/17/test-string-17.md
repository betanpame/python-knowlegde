# String Template and Formatting - Test 17

**Difficulty:** ⭐⭐⭐ (Easy-Medium)

**Related Topics:** String Formatting, Templates, Text Generation

## Objectives

- Master advanced string formatting techniques
- Work with template strings and placeholders
- Generate formatted output for different use cases
- Handle complex formatting requirements

## Description

Create a comprehensive string formatting system that can handle various template types, from simple placeholders to complex report generation. You'll work with different formatting styles and dynamic content generation.

## Examples

```python
# Simple template formatting
template = "Hello {name}, you have {count} messages"
result = format_template(template, name="Alice", count=5)
print(result)  # "Hello Alice, you have 5 messages"

# Report generation
data = {"sales": 15000, "target": 20000, "month": "December"}
report = generate_sales_report(data)
print(report)
# Sales Report for December
# Target: $20,000
# Actual: $15,000
# Achievement: 75.0%

# Table formatting
headers = ["Name", "Age", "City"]
rows = [["Alice", "25", "Boston"], ["Bob", "30", "Seattle"]]
table = format_table(headers, rows)
print(table)
# | Name  | Age | City    |
# |-------|-----|---------|
# | Alice | 25  | Boston  |
# | Bob   | 30  | Seattle |
```

## Your Tasks

1. **format_template(template, **kwargs)** - Replace placeholders with values
2. **generate_sales_report(data)** - Create a formatted sales report
3. **format_table(headers, rows)** - Generate ASCII table
4. **create_progress_bar(current, total, width=20)** - Text progress bar
5. **format_currency(amount, currency="USD")** - Format money values
6. **generate_invoice(items, customer)** - Create invoice text
7. **format_multiline_text(text, width=80)** - Wrap text to specified width
8. **create_ascii_banner(text)** - Generate decorative text banner

## Hints

- Use f-strings and `.format()` method for placeholders
- String multiplication creates repeated patterns
- `ljust()`, `rjust()`, `center()` help with alignment
- Calculate percentages for progress indicators
- Use string concatenation for building complex output
- Consider padding and spacing for table formatting
- Break long text into chunks for wrapping

## Test Cases

```python
# Test data for validation
test_cases = [
    ("Hello {user}!", {"user": "World"}, "Hello World!"),
    ({"sales": 8000, "target": 10000, "month": "Jan"}, None, "Achievement: 80.0%"),
    (["ID", "Name"], [["1", "Alice"], ["2", "Bob"]], "| ID | Name  |"),
    ((50, 100, 10), None, "[█████     ] 50%"),
    (1234.56, "EUR", "€1,234.56"),
    (80, 60, "very long text that needs to be wrapped properly"),
    ("HELLO", None, "ASCII banner format")
]
```

## Bonus Challenges

- Support nested placeholders in templates
- Add color codes to progress bars
- Implement different table border styles
- Support right-to-left text formatting
- Add thousand separators for large numbers
- Create responsive table formatting
- Generate QR code using ASCII characters

Remember: Focus on clean, readable formatting and handle edge cases like empty data or very long text!
