# TODO: Implement string replacement functions
# Starter code for String Practice 12

def replace_text(text, old_text, new_text):
    """
    Replace all occurrences of old_text with new_text.
    
    Args:
        text (str): Original string
        old_text (str): Text to replace
        new_text (str): Replacement text
        
    Returns:
        str: String with replacements made
    """
    # Your implementation here
    pass

def replace_first_occurrence(text, old_text, new_text):
    """
    Replace only the first occurrence of old_text with new_text.
    
    Args:
        text (str): Original string
        old_text (str): Text to replace
        new_text (str): Replacement text
        
    Returns:
        str: String with first occurrence replaced
    """
    # Your implementation here
    pass

def replace_multiple(text, replacements):
    """
    Replace multiple different texts in a string.
    
    Args:
        text (str): Original string
        replacements (dict): Dictionary of {old_text: new_text} pairs
        
    Returns:
        str: String with all replacements made
    """
    # Your implementation here
    pass

# Practice your implementation
if __name__ == "__main__":
    test_cases = [
        ("Hello World", "World", "Python"),
        ("test test test", "test", "demo"),
        ("Python", "Java", "C++"),
        ("aaa", "a", "b"),
        ("Hello", "l", "L"),
        ("Programming", "gram", "code")
    ]
    
    print("=== Replace All Occurrences ===")
    for text, old, new in test_cases:
        result = replace_text(text, old, new)
        print(f"'{text}' -> replace '{old}' with '{new}' -> '{result}'")
    
    print("\n=== Replace First Occurrence Only ===")
    first_cases = [
        ("test test test", "test", "demo"),
        ("Hello Hello World", "Hello", "Hi"),
        ("aaa", "a", "b")
    ]
    
    for text, old, new in first_cases:
        result = replace_first_occurrence(text, old, new)
        print(f"'{text}' -> replace first '{old}' with '{new}' -> '{result}'")
    
    print("\n=== Multiple Replacements ===")
    multi_cases = [
        ("Hello World", {"Hello": "Hi", "World": "Python"}),
        ("I like cats and dogs", {"cats": "dogs", "dogs": "cats"}),
        ("abc def ghi", {"a": "1", "e": "2", "i": "3"})
    ]
    
    for text, replacements in multi_cases:
        result = replace_multiple(text, replacements)
        print(f"'{text}' with {replacements} -> '{result}'")