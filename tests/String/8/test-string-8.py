# TODO: Implement string indexing functions
# Starter code for String Test 8

def get_first_character(text):
    """
    Get the first character of a string.
    
    Args:
        text (str): Input string
        
    Returns:
        str: First character, or empty string if text is empty
    """
    # Your implementation here
    pass

def get_last_character(text):
    """
    Get the last character of a string.
    
    Args:
        text (str): Input string
        
    Returns:
        str: Last character, or empty string if text is empty
    """
    # Your implementation here
    pass

def get_character_at_index(text, index):
    """
    Get character at specific index.
    
    Args:
        text (str): Input string
        index (int): Index of character to retrieve
        
    Returns:
        str: Character at index, or empty string if index is invalid
    """
    # Your implementation here
    pass

def get_middle_character(text):
    """
    Get the middle character(s) of a string.
    
    Args:
        text (str): Input string
        
    Returns:
        str: Middle character(s)
    """
    # Your implementation here
    pass

# Test your implementation
if __name__ == "__main__":
    test_strings = ["Python", "Hello", "a", "", "Programming"]
    
    print("=== First and Last Characters ===")
    for text in test_strings:
        first = get_first_character(text)
        last = get_last_character(text)
        print(f"'{text}' -> First: '{first}', Last: '{last}'")
    
    print("\n=== Character at Index ===")
    index_tests = [
        ("Python", 0),
        ("Python", 2),
        ("Python", 5),
        ("Hello", 1),
        ("Programming", 4)
    ]
    
    for text, index in index_tests:
        char = get_character_at_index(text, index)
        print(f"'{text}'[{index}] = '{char}'")
    
    print("\n=== Middle Characters ===")
    for text in test_strings:
        middle = get_middle_character(text)
        print(f"'{text}' -> Middle: '{middle}'")
