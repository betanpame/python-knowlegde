# TODO: Implement string length function
# Starter code for String Test 4

def get_string_length(text):
    """
    Get the length of a string.
    
    Args:
        text (str): The input string
        
    Returns:
        int: The length of the string
    """
    # Your implementation here
    return len(text)
    


# Test your implementation
if __name__ == "__main__":
    test_cases = [
        "Hello",
        "",
        "Python Programming",
        "123",
        "Hello World!",
        "   spaces   "
    ]
    
    for test in test_cases:
        length = get_string_length(test)
        print(f"String: '{test}' -> Length: {length}")
