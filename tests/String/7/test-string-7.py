# TODO: Implement string contains functions
# Starter code for String Test 7

def check_contains(text, substring):
    """
    Check if text contains substring (case-sensitive).
    
    Args:
        text (str): Text to search in
        substring (str): Substring to search for
        
    Returns:
        bool: True if substring is found, False otherwise
    """
    # Your implementation here
    pass

def check_contains_case_insensitive(text, substring):
    """
    Check if text contains substring (case-insensitive).
    
    Args:
        text (str): Text to search in
        substring (str): Substring to search for
        
    Returns:
        bool: True if substring is found, False otherwise
    """
    # Your implementation here
    pass

def check_contains_character(text, char):
    """
    Check if text contains a specific character.
    
    Args:
        text (str): Text to search in
        char (str): Character to search for
        
    Returns:
        bool: True if character is found, False otherwise
    """
    # Your implementation here
    pass

# Test your implementation
if __name__ == "__main__":
    test_cases = [
        ("Python Programming", "Python"),
        ("Python Programming", "Java"),
        ("Hello World", "o"),
        ("Hello World", "xyz"),
        ("Programming", "gram"),
        ("", "test"),
        ("test", "")
    ]
    
    print("=== Case-Sensitive Search ===")
    for text, substring in test_cases:
        result = check_contains(text, substring)
        print(f"'{text}' contains '{substring}': {result}")
    
    print("\n=== Case-Insensitive Search ===")
    case_test_cases = [
        ("HELLO", "hello"),
        ("Python", "PYTHON"),
        ("MiXeD", "mixed")
    ]
    
    for text, substring in case_test_cases:
        result = check_contains_case_insensitive(text, substring)
        print(f"'{text}' contains '{substring}' (case-insensitive): {result}")
    
    print("\n=== Character Search ===")
    char_test_cases = [
        ("Hello", "H"),
        ("Hello", "x"),
        ("Python", "n")
    ]
    
    for text, char in char_test_cases:
        result = check_contains_character(text, char)
        print(f"'{text}' contains '{char}': {result}")
