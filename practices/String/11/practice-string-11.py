# TODO: Implement string prefix/suffix checking functions
# Starter code for String Practice 11

def starts_with(text, prefix):
    """
    Check if string starts with given prefix.
    
    Args:
        text (str): String to check
        prefix (str): Prefix to look for
        
    Returns:
        bool: True if string starts with prefix, False otherwise
    """
    # Your implementation here
    pass

def ends_with(text, suffix):
    """
    Check if string ends with given suffix.
    
    Args:
        text (str): String to check
        suffix (str): Suffix to look for
        
    Returns:
        bool: True if string ends with suffix, False otherwise
    """
    # Your implementation here
    pass

def starts_with_any(text, prefixes):
    """
    Check if string starts with any of the given prefixes.
    
    Args:
        text (str): String to check
        prefixes (list): List of prefixes to check
        
    Returns:
        bool: True if string starts with any prefix, False otherwise
    """
    # Your implementation here
    pass

def ends_with_any(text, suffixes):
    """
    Check if string ends with any of the given suffixes.
    
    Args:
        text (str): String to check
        suffixes (list): List of suffixes to check
        
    Returns:
        bool: True if string ends with any suffix, False otherwise
    """
    # Your implementation here
    pass

# Practice your implementation
if __name__ == "__main__":
    test_cases = [
        ("Python Programming", "Python"),
        ("Python Programming", "Java"),
        ("Hello World", "Hello"),
        ("Hello World", "hello"),
        ("test.txt", ".txt"),
        ("image.jpg", ".png")
    ]
    
    print("=== Starts With Practices ===")
    for text, prefix in test_cases:
        result = starts_with(text, prefix)
        print(f"'{text}' starts with '{prefix}': {result}")
    
    print("\n=== Ends With Practices ===")
    suffix_cases = [
        ("Python Programming", "ing"),
        ("Hello World", "World"),
        ("Hello World", "world"),
        ("test.txt", ".txt"),
        ("image.jpg", ".jpg")
    ]
    
    for text, suffix in suffix_cases:
        result = ends_with(text, suffix)
        print(f"'{text}' ends with '{suffix}': {result}")
    
    print("\n=== Multiple Options Practices ===")
    multi_tests = [
        ("test.txt", [".txt", ".doc", ".pdf"]),
        ("hello.py", [".txt", ".py", ".java"]),
        ("README.md", [".txt", ".doc"])
    ]
    
    for text, options in multi_tests:
        starts_result = starts_with_any(text, ["test", "hello", "README"])
        ends_result = ends_with_any(text, options)
        print(f"'{text}' -> starts with any: {starts_result}, ends with any: {ends_result}")