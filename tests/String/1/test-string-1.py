# VALIDATED:
# Starter code for String Test 1

def reverse_string(text: str) -> str:
    """
    Reverse the characters in a string.

    Args:
        text (str): The string to reverse

    Returns:
        str: The reversed string
    """
    # Use slicing with step -1 to go through the string backwards.
    # Example: "abc"[::-1] -> "cba"
    # This is simple and runs in O(n) time where n is the string length.
    # Note: For some combined characters (like certain emojis or letters with combining accents),
    # reversing by code points may not give the visually expected result.
    return text[::-1]

# Test your implementation
if __name__ == "__main__":
    test_cases = [
        "Pamela",
        "Python",
        "",
        "a",
        "12345",
        "Hello World!",
        "é"  # example with 'e' + combining accent (results may vary with normalization)
    ]

    # Show the original and reversed string for each test case.
    for test in test_cases:
        result = reverse_string(test)
        print(f"Original: '{test}' -> Reversed: '{result}'")