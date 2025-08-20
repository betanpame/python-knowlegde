# TODO: Implement advanced string validation
# Starter code for String Practice 18

class TextValidator:
    """Advanced text validation class using string methods."""
    
    def validate_email(self, email):
        """
        Validate email format using string methods only.
        
        Args:
            email (str): Email address to validate
            
        Returns:
            dict: Validation result with details
        """
        # Your implementation here
        # Check for @ symbol, domain, extension, etc.
        pass
    
    def validate_phone(self, phone):
        """
        Validate phone number in various formats.
        
        Args:
            phone (str): Phone number to validate
            
        Returns:
            dict: Validation result with format type
        """
        # Your implementation here
        # Handle formats like: +1-555-123-4567, (555) 123-4567, 555.123.4567
        pass
    
    def validate_password_strength(self, password):
        """
        Validate password strength using multiple criteria.
        
        Args:
            password (str): Password to validate
            
        Returns:
            dict: Validation result with strength score and feedback
        """
        # Your implementation here
        # Check length, uppercase, lowercase, digits, special chars
        pass
    
    def validate_credit_card(self, card_number):
        """
        Validate credit card number format.
        
        Args:
            card_number (str): Credit card number
            
        Returns:
            dict: Validation result with card type if valid
        """
        # Your implementation here
        # Remove spaces/dashes, check length, identify type
        pass
    
    def validate_url(self, url):
        """
        Validate URL format using string methods.
        
        Args:
            url (str): URL to validate
            
        Returns:
            dict: Validation result with URL components
        """
        # Your implementation here
        # Check protocol, domain, path structure
        pass

def run_validation_tests():
    """Run comprehensive validation tests."""
    validator = TextValidator()
    
    # Email test cases
    emails = [
        "user@example.com",
        "invalid.email",
        "@example.com",
        "user@",
        "test.email@domain.co.uk",
        "user+tag@example.org"
    ]
    
    print("=== Email Validation ===")
    for email in emails:
        result = validator.validate_email(email)
        print(f"{email:25} -> {result}")
    
    # Phone test cases
    phones = [
        "+1-555-123-4567",
        "(555) 123-4567",
        "555.123.4567",
        "5551234567",
        "555-123-456",  # Invalid
        "abc-def-ghij"  # Invalid
    ]
    
    print("\n=== Phone Validation ===")
    for phone in phones:
        result = validator.validate_phone(phone)
        print(f"{phone:20} -> {result}")
    
    # Password test cases
    passwords = [
        "Password123!",
        "weakpass",
        "NOLOWERCASE123!",
        "nouppercase123!",
        "NoNumbers!",
        "NoSpecialChars123",
        "Short1!",
        "VeryStrongP@ssw0rd2023!"
    ]
    
    print("\n=== Password Validation ===")
    for password in passwords:
        result = validator.validate_password_strength(password)
        print(f"{password:25} -> {result}")

# Practice your implementation
if __name__ == "__main__":
    run_validation_tests()