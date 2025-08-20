# Practice String 16: Advanced String Validation

**Difficulty:** ⭐⭐⭐☆☆ (Medium)

**Related Topics:** String validation methods, regular expressions, complex logic

## Objective

Create advanced string validation functions using multiple string methods and complex logic.

## Requirements

Build a comprehensive text validator that checks various string properties and formats.

## Example

```python
validator = TextValidator()
result = validator.validate_email("user@example.com")  # {"valid": True, "type": "email"}
result = validator.validate_phone("+1-555-123-4567")  # {"valid": True, "format": "international"}
```

## Hints

- Combine multiple string methods (.isdigit(), .isalpha(), .contains())
- Use string slicing and indexing for pattern checking
- Handle edge cases and invalid inputs gracefully
- Consider different formats and international standards

## Practice Cases

1. Email validation: valid and invalid formats
2. Phone number validation: different formats
3. Password strength: multiple criteria
4. Credit card format validation
5. URL format validation