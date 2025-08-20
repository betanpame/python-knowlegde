# TODO: Implement string concatenation functions
# Starter code for String Practice 6

def concatenate_strings(str1, str2):
    """
    Concatenate two strings together.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        str: Concatenated string
    """
    # Your implementation here
    pass

def concatenate_with_separator(str1, str2, separator):
    """
    Concatenate two strings with a separator.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        separator (str): Separator to use between strings
        
    Returns:
        str: Concatenated string with separator
    """
    # Your implementation here
    pass

def concatenate_multiple(strings):
    """
    Concatenate multiple strings from a list.
    
    Args:
        strings (list): List of strings to concatenate
        
    Returns:
        str: Concatenated string
    """
    # Your implementation here
    pass

# Practice your implementation
if __name__ == "__main__":
    # Practice basic concatenation
    print("=== Basic Concatenation ===")
    test_pairs = [
        ("Hello", "World"),
        ("Python", "Programming"),
        ("", "Practice"),
        ("Practice", "")
    ]
    
    for str1, str2 in test_pairs:
        result = concatenate_strings(str1, str2)
        print(f"'{str1}' + '{str2}' = '{result}'")
    
    # Practice with separator
    print("\n=== Concatenation with Separator ===")
    for str1, str2 in test_pairs:
        result = concatenate_with_separator(str1, str2, " ")
        print(f"'{str1}' + ' ' + '{str2}' = '{result}'")
    
    # Practice multiple strings
    print("\n=== Multiple String Concatenation ===")
    test_lists = [
        ["Hello", "World", "Python"],
        ["One", "Two", "Three"],
        [""],
        ["Single"]
    ]
    
    for strings in test_lists:
        result = concatenate_multiple(strings)
        print(f"{strings} -> '{result}'")