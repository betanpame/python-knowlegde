# TODO: Implement string repetition functions
# Starter code for String Test 9

def repeat_string(text, times):
    """
    Repeat a string a specified number of times.
    
    Args:
        text (str): String to repeat
        times (int): Number of times to repeat
        
    Returns:
        str: Repeated string
    """
    # Your implementation here
    pass

def repeat_with_separator(text, times, separator):
    """
    Repeat a string with separator between repetitions.
    
    Args:
        text (str): String to repeat
        times (int): Number of times to repeat
        separator (str): Separator between repetitions
        
    Returns:
        str: Repeated string with separators
    """
    # Your implementation here
    pass

# Test your implementation
if __name__ == "__main__":
    test_cases = [
        ("Hi", 3),
        ("Python", 2),
        ("Test", 0),
        ("A", 5),
        ("Hello", 1),
        ("", 3)
    ]
    
    print("=== Basic String Repetition ===")
    for text, times in test_cases:
        result = repeat_string(text, times)
        print(f"'{text}' * {times} = '{result}'")
    
    print("\n=== Repetition with Separator ===")
    separator_cases = [
        ("Hi", 3, "-"),
        ("Python", 2, " "),
        ("Test", 4, ", ")
    ]
    
    for text, times, sep in separator_cases:
        result = repeat_with_separator(text, times, sep)
        print(f"'{text}' repeated {times} times with '{sep}' = '{result}'")
