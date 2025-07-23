import string

# TODO: Implement password validation function
# Starter code for String Test 3

def validate_password(password):
    """
    Validate password strength and requirements.
    
    Args:
        password (str): The password to validate
        
    Returns:
        dict: Validation results with 'valid', 'errors', and 'strength' keys
    """
    result = {
        "valid": False,
        "errors": [],
        "strength": "Weak"
    }
    
    # Your implementation here
    # Check length, uppercase, lowercase, digits, special characters
    
    return result

# Test your function
if __name__ == "__main__":
    test_passwords = [
        "password",
        "Password123",
        "Pass123!",
        "MySecurePass123!",
        "abc123",
        "ABC123!",
        "MyPassword123!"
    ]
    
    for pwd in test_passwords:
        result = validate_password(pwd)
        print(f"Password: '{pwd}'")
        print(f"Result: {result}")
        print("-" * 40)
