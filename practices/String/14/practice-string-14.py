# TODO: Implement string split and join functions
# Starter code for String Practice 14

def split_by_delimiter(text, delimiter):
    """
    Split string by a specific delimiter.
    
    Args:
        text (str): String to split
        delimiter (str): Character(s) to split on
        
    Returns:
        list: List of string parts
    """
    # Your implementation here
    pass

def split_by_whitespace(text):
    """
    Split string by any whitespace (spaces, tabs, newlines).
    
    Args:
        text (str): String to split
        
    Returns:
        list: List of words
    """
    # Your implementation here
    pass

def join_with_delimiter(string_list, delimiter):
    """
    Join list of strings with a delimiter.
    
    Args:
        string_list (list): List of strings to join
        delimiter (str): Character(s) to join with
        
    Returns:
        str: Joined string
    """
    # Your implementation here
    pass

def split_and_clean(text, delimiter):
    """
    Split string and remove empty parts and whitespace.
    
    Args:
        text (str): String to split
        delimiter (str): Character(s) to split on
        
    Returns:
        list: List of cleaned string parts
    """
    # Your implementation here
    pass

def create_csv_line(data_list):
    """
    Create a CSV line from a list of data.
    
    Args:
        data_list (list): List of data items
        
    Returns:
        str: CSV formatted string
    """
    # Your implementation here
    pass

# Practice your implementation
if __name__ == "__main__":
    print("=== Split by Delimiter ===")
    split_cases = [
        ("apple,banana,cherry", ","),
        ("one;two;three", ";"),
        ("a|b|c|d", "|"),
        ("single", ","),
        ("", ",")
    ]
    
    for text, delim in split_cases:
        result = split_by_delimiter(text, delim)
        print(f"'{text}' split by '{delim}' -> {result}")
    
    print("\n=== Split by Whitespace ===")
    whitespace_cases = [
        "Hello World Python",
        "  multiple   spaces  ",
        "tab\tseparated\tvalues",
        "line1\nline2\nline3",
        "single"
    ]
    
    for text in whitespace_cases:
        result = split_by_whitespace(text)
        print(f"'{text}' -> {result}")
    
    print("\n=== Join with Delimiter ===")
    join_cases = [
        (["apple", "banana", "cherry"], ", "),
        (["one", "two", "three"], " | "),
        (["a", "b", "c"], "-"),
        (["single"], ","),
        ([], ",")
    ]
    
    for string_list, delim in join_cases:
        result = join_with_delimiter(string_list, delim)
        print(f"{string_list} joined with '{delim}' -> '{result}'")
    
    print("\n=== Split and Clean ===")
    dirty_cases = [
        ("  apple , banana , cherry  ", ","),
        ("one;  ;two; ;three", ";"),
        ("a||b|c||", "|")
    ]
    
    for text, delim in dirty_cases:
        result = split_and_clean(text, delim)
        print(f"'{text}' split and cleaned -> {result}")
    
    print("\n=== Create CSV Line ===")
    csv_cases = [
        ["John", "Doe", "30", "Engineer"],
        ["Alice", "Smith", "25", "Designer"],
        ["Data with, comma", "Quote \"test\"", "Special chars!"]
    ]
    
    for data in csv_cases:
        result = create_csv_line(data)
        print(f"{data} -> CSV: '{result}'")