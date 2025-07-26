# TODO: Implement case conversion functions
# Starter code for String Test 5

def to_uppercase(text):
    """
    Convert string to uppercase.
    
    Args:
        text (str): The input string
        
    Returns:
        str: The uppercase version of the string
    """
    return text.upper()
    

def to_lowercase(text):
    """
    Convert string to lowercase.
    
    Args:
        text (str): The input string
        
    Returns:
        str: The lowercase version of the string
    """
    return text.lower()
    

# Test your implementation
if __name__ == "__main__":
    test_cases = [
        "Hello World",
        "PYTHON",
        "MiXeD cAsE",
        "123",
        "",
        "Programming!"
    ]
    
    for test in test_cases:
        upper_result = to_uppercase(test)
        lower_result = to_lowercase(test)
        print(f"Original: '{test}'")
        print(f"  Upper: '{upper_result}'")
        print(f"  Lower: '{lower_result}'")
        print()
