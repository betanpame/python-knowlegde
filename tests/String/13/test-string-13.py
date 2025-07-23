# TODO: Implement string cleaning functions
# Starter code for String Test 13

def strip_whitespace(text):
    """
    Remove leading and trailing whitespace from string.
    
    Args:
        text (str): String to clean
        
    Returns:
        str: String with whitespace removed
    """
    # Your implementation here
    pass

def strip_left_whitespace(text):
    """
    Remove only leading whitespace from string.
    
    Args:
        text (str): String to clean
        
    Returns:
        str: String with leading whitespace removed
    """
    # Your implementation here
    pass

def strip_right_whitespace(text):
    """
    Remove only trailing whitespace from string.
    
    Args:
        text (str): String to clean
        
    Returns:
        str: String with trailing whitespace removed
    """
    # Your implementation here
    pass

def strip_characters(text, chars_to_remove):
    """
    Remove specific characters from beginning and end of string.
    
    Args:
        text (str): String to clean
        chars_to_remove (str): Characters to remove
        
    Returns:
        str: String with specified characters removed
    """
    # Your implementation here
    pass

# Test your implementation
if __name__ == "__main__":
    test_cases = [
        "  Hello World  ",
        "   Python   ",
        "Test",
        "   ",
        "\t\nHello\t\n",
        "     Programming     "
    ]
    
    print("=== Strip All Whitespace ===")
    for text in test_cases:
        result = strip_whitespace(text)
        print(f"'{text}' -> '{result}'")
    
    print("\n=== Strip Left Whitespace Only ===")
    for text in test_cases:
        result = strip_left_whitespace(text)
        print(f"'{text}' -> '{result}'")
    
    print("\n=== Strip Right Whitespace Only ===")
    for text in test_cases:
        result = strip_right_whitespace(text)
        print(f"'{text}' -> '{result}'")
    
    print("\n=== Strip Specific Characters ===")
    char_cases = [
        ("...Hello...", "."),
        ("***Python***", "*"),
        ("---Test---", "-"),
        ("()()Hello()()", "()"),
        ("123Number321", "123")
    ]
    
    for text, chars in char_cases:
        result = strip_characters(text, chars)
        print(f"'{text}' strip '{chars}' -> '{result}'")
