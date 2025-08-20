# TODO: Implement password validation function
import string

# Starter code for String Test 3

def validate_password(password):
    """
    Validate password strength and requirements.
    
    Args:
        password (str): The password to validate
        
    Returns:
        dict: Validation results with 'valid', 'errors', and 'strength' keys
    """
    # Your implementation here

    errors = []

    if not len(password) >= 8:
        errors.append("La contraseña debe tener al menos 8 caracteres.")
    
    if not any(letra.isupper() for letra in password):
        errors.append("La contraseña debe tener al menos una mayúscula.") 
    
    if not any(letra.islower()for letra in password): 
        errors.append("La contraseña debe tener al menos una minúscula.") 
    
    if not any(letra.isdigit() for letra in password):
        errors.append("La contraseña debe tener al menos un número.")
        
    if not any(letra in string.punctuation for letra in password):
        errors.append("La contraseña debe tener al menos un caracter especial.")
    
    valid=False
    strength="weak"
    
    if len(errors) == 0:
        valid=True
        strength="strong"
    elif len(errors) <=2:
        strength="medium"
    
    
    output = {
        "valid": valid,
        "errors": errors,
        "strength": strength
    }


    # Check length, uppercase, lowercase, digits, special characters
    
    return output

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
