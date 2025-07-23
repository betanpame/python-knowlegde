# TODO: Implement string comparison functions
# Starter code for String Test 10

def strings_equal(str1, str2):
    """
    Check if two strings are equal (case-sensitive).
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        bool: True if strings are equal, False otherwise
    """
    # Your implementation here
    pass

def strings_equal_ignore_case(str1, str2):
    """
    Check if two strings are equal (case-insensitive).
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        bool: True if strings are equal ignoring case, False otherwise
    """
    # Your implementation here
    pass

def strings_not_equal(str1, str2):
    """
    Check if two strings are not equal.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        bool: True if strings are not equal, False otherwise
    """
    # Your implementation here
    pass

# Test your implementation
if __name__ == "__main__":
    test_cases = [
        ("Hello", "Hello"),
        ("Hello", "hello"),
        ("Python", "Java"),
        ("", ""),
        ("Test", "Test"),
        ("ABC", "abc")
    ]
    
    print("=== Case-Sensitive Comparison ===")
    for str1, str2 in test_cases:
        equal = strings_equal(str1, str2)
        not_equal = strings_not_equal(str1, str2)
        print(f"'{str1}' == '{str2}': {equal}")
        print(f"'{str1}' != '{str2}': {not_equal}")
        print()
    
    print("=== Case-Insensitive Comparison ===")
    for str1, str2 in test_cases:
        equal_ignore_case = strings_equal_ignore_case(str1, str2)
        print(f"'{str1}' == '{str2}' (ignore case): {equal_ignore_case}")
