# TODO: Implement string reversal
# Starter code for String Test 1

def reverse_string(text):
    """
    Reverse the characters in a string.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
    """
    # Your implementation here
    pass

# Test your implementation
if __name__ == "__main__":
    test_cases = [
        "Pamela",
        "Python",
        "",
        "a",
        "12345",
        "Hello World!"
    ]
    
    for test in test_cases:
        result = reverse_string(test)
        print(f"Original: '{test}' -> Reversed: '{result}'")