# Test String 3: String Validation and Analysis

**Difficulty:** ⭐⭐⭐☆☆ (Medium)

**Related Topics:** String validation methods, conditional logic

## Objective

Create a password validator function that checks if a password meets security requirements using string validation methods.

## Requirements

Create a function `validate_password(password)` that returns a dictionary with validation results. The password must:

1. Be at least 8 characters long
2. Contain at least one uppercase letter
3. Contain at least one lowercase letter
4. Contain at least one digit
5. Contain at least one special character (not alphanumeric)

## Return Format

```python
{
    "valid": True/False,
    "errors": ["list", "of", "error", "messages"],
    "strength": "Weak"|"Medium"|"Strong"
}
```

The strenght should be determined by how many validations pass: 

- 1-2: Weak
- 3-4: Medium
- 5: Strong

## Example

```python
password = "MyPass123!"
result = validate_password(password)
# Expected output:
# {
#     "valid": True,
#     "errors": [],
#     "strength": "Strong"
# }
```

## Hints

- Use `.isdigit()`, `.isalpha()`, `.isupper()`, `.islower()` methods
- Use `any()` function with generator expressions
- Use `len()` to check length
- Consider using `string` module for character sets

## Test Cases

Your function should handle these cases:

1. `"password"` → Invalid (no uppercase, no digits, no special chars)
2. `"Password123"` → Invalid (no special characters)
3. `"Pass123!"` → Invalid (too short)
4. `"MySecurePass123!"` → Valid, Strong
