# TODO: Implement text processing and parsing functions
# Starter code for String Practice 16

def parse_csv_line(line):
    """
    Parse a CSV-like string into a list of values.
    
    Args:
        line (str): CSV line to parse
        
    Returns:
        list: List of parsed values
    """
    # Your implementation here
    # Split by comma and clean up whitespace
    pass

def clean_log_entry(log_line):
    """
    Extract the main message from a log entry.
    
    Args:
        log_line (str): Log entry to clean
        
    Returns:
        str: Clean message text
    """
    # Your implementation here
    # Remove timestamp, log level, and extract main message
    pass

def parse_config_string(config):
    """
    Convert a config string into a dictionary.
    
    Args:
        config (str): Configuration string (key=value;key=value)
        
    Returns:
        dict: Parsed configuration
    """
    # Your implementation here
    # Split by semicolon, then by equals sign
    pass

def extract_numbers(text):
    """
    Find and return all numbers in a text string.
    
    Args:
        text (str): Text to search
        
    Returns:
        list: List of numbers found (as strings)
    """
    # Your implementation here
    # Look for digit patterns, including decimals
    pass

def format_phone_number(phone):
    """
    Format a phone number consistently as (XXX) XXX-XXXX.
    
    Args:
        phone (str): Phone number to format
        
    Returns:
        str: Formatted phone number
    """
    # Your implementation here
    # Extract digits and format properly
    pass

def extract_email_parts(email):
    """
    Split an email into username and domain.
    
    Args:
        email (str): Email address
        
    Returns:
        tuple: (username, domain)
    """
    # Your implementation here
    # Split at @ symbol
    pass

def standardize_name(name):
    """
    Format a name properly using Title Case.
    
    Args:
        name (str): Name to format
        
    Returns:
        str: Properly formatted name
    """
    # Your implementation here
    # Handle proper capitalization
    pass

def parse_date_string(date_str):
    """
    Extract date components from YYYY-MM-DD format.
    
    Args:
        date_str (str): Date string
        
    Returns:
        tuple: (year, month, day)
    """
    # Your implementation here
    # Split date string into components
    pass

def run_parsing_tests():
    """Run comprehensive text parsing tests."""
    
    # Practice cases from the challenge
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
    
    print("=== Text Parsing Practices ===")
    
    # CSV parsing test
    csv_result = parse_csv_line(test_cases[0][0])
    print(f"CSV Parse: {csv_result}")
    print(f"Expected: {test_cases[0][1]}")
    print(f"Match: {csv_result == test_cases[0][1]}")
    print()
    
    # Log cleaning test
    log_result = clean_log_entry(test_cases[1][0])
    print(f"Log Clean: '{log_result}'")
    print(f"Expected: '{test_cases[1][1]}'")
    print(f"Match: {log_result == test_cases[1][1]}")
    print()
    
    # Config parsing test
    config_result = parse_config_string(test_cases[2][0])
    print(f"Config Parse: {config_result}")
    print(f"Expected: {test_cases[2][1]}")
    print(f"Match: {config_result == test_cases[2][1]}")
    print()
    
    # Number extraction test
    numbers_result = extract_numbers(test_cases[3][0])
    print(f"Numbers: {numbers_result}")
    print(f"Expected: {test_cases[3][1]}")
    print(f"Match: {numbers_result == test_cases[3][1]}")
    print()
    
    # Phone formatting test
    phone_result = format_phone_number(test_cases[4][0])
    print(f"Phone Format: '{phone_result}'")
    print(f"Expected: '{test_cases[4][1]}'")
    print(f"Match: {phone_result == test_cases[4][1]}")
    print()
    
    # Email parsing test
    email_result = extract_email_parts(test_cases[5][0])
    print(f"Email Parts: {email_result}")
    print(f"Expected: {test_cases[5][1]}")
    print(f"Match: {email_result == test_cases[5][1]}")
    print()
    
    # Name formatting test
    name_result = standardize_name(test_cases[6][0])
    print(f"Name Format: '{name_result}'")
    print(f"Expected: '{test_cases[6][1]}'")
    print(f"Match: {name_result == test_cases[6][1]}")
    print()
    
    # Date parsing test
    date_result = parse_date_string(test_cases[7][0])
    print(f"Date Parse: {date_result}")
    print(f"Expected: {test_cases[7][1]}")
    print(f"Match: {date_result == test_cases[7][1]}")

# Practice your implementation
if __name__ == "__main__":
    run_parsing_tests()