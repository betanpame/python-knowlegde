# TODO: Implement clean_text function
# Starter code for String Test 2

def clean_text(text):
    """
    Clean and format user input text.
    
    Args:
        text (str): The messy input text
        
    Returns:
        str: Cleaned and formatted text
    """
    # Your implementation here
    pass

# Test your function
if __name__ == "__main__":
    test_cases = [
        "  hello   world  this is bad  text bad  ",
        "  python   programming  ",
        "bad code is bad",
        "",
        "   single   "
    ]
    
    for test in test_cases:
        result = clean_text(test)
        print(f"Input: '{test}' -> Output: '{result}'")
