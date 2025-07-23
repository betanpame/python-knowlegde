# TODO: Implement basic list operations
# Starter code for Lists Test 3

def get_first_element(my_list):
    """
    Return the first element of a list.
    
    Args:
        my_list (list): Input list
        
    Returns:
        any: First element, or None if list is empty
    """
    # Your implementation here
    # Check if list is not empty, then return first element
    pass

def get_last_element(my_list):
    """
    Return the last element of a list.
    
    Args:
        my_list (list): Input list
        
    Returns:
        any: Last element, or None if list is empty
    """
    # Your implementation here
    # Use negative indexing or length-based indexing
    pass

def get_list_length(my_list):
    """
    Return the number of elements in a list.
    
    Args:
        my_list (list): Input list
        
    Returns:
        int: Number of elements
    """
    # Your implementation here
    # Use built-in len() function
    pass

def get_middle_element(my_list):
    """
    Return the middle element for odd-length lists.
    
    Args:
        my_list (list): Input list (odd length)
        
    Returns:
        any: Middle element, or None if even length or empty
    """
    # Your implementation here
    # Calculate middle index and return element
    pass

def is_list_empty(my_list):
    """
    Check if a list is empty.
    
    Args:
        my_list (list): Input list
        
    Returns:
        bool: True if empty, False otherwise
    """
    # Your implementation here
    # Check length or use truthiness
    pass

def get_element_at_position(my_list, index):
    """
    Get element at specific index safely.
    
    Args:
        my_list (list): Input list
        index (int): Index to access
        
    Returns:
        any: Element at index, or None if index invalid
    """
    # Your implementation here
    # Check bounds before accessing
    pass

def create_number_list(start, end):
    """
    Create list of numbers from start to end (inclusive).
    
    Args:
        start (int): Starting number
        end (int): Ending number
        
    Returns:
        list: List of numbers
    """
    # Your implementation here
    # Use range() to create sequence
    pass

def combine_two_lists(list1, list2):
    """
    Combine two lists into one.
    
    Args:
        list1 (list): First list
        list2 (list): Second list
        
    Returns:
        list: Combined list
    """
    # Your implementation here
    # Use + operator or extend method
    pass

def run_basic_list_tests():
    """Run comprehensive basic list operation tests."""
    
    print("=== Basic List Operations Tests ===")
    
    # Test with different types of lists
    test_lists = [
        [1, 2, 3, 4, 5],           # numbers
        ["apple", "banana", "cherry"],  # strings
        [True, False, True],        # booleans
        [1, "hello", True, 3.14],  # mixed types
        [42],                      # single element
        []                         # empty list
    ]
    
    for i, test_list in enumerate(test_lists):
        print(f"Test List {i+1}: {test_list}")
        
        # First element
        first = get_first_element(test_list)
        print(f"  First element: {first}")
        
        # Last element
        last = get_last_element(test_list)
        print(f"  Last element: {last}")
        
        # Length
        length = get_list_length(test_list)
        print(f"  Length: {length}")
        
        # Middle element (for odd-length lists)
        if length % 2 == 1 and length > 0:
            middle = get_middle_element(test_list)
            print(f"  Middle element: {middle}")
        
        # Is empty
        empty = is_list_empty(test_list)
        print(f"  Is empty: {empty}")
        
        print()
    
    # Test element access
    numbers = [10, 20, 30, 40, 50]
    print("Element Access Tests:")
    for index in [0, 2, 4, -1, 10, -10]:
        element = get_element_at_position(numbers, index)
        print(f"  Index {index}: {element}")
    print()
    
    # Test list creation
    print("Number List Creation:")
    ranges = [(1, 5), (0, 3), (5, 5), (10, 15)]
    for start, end in ranges:
        number_list = create_number_list(start, end)
        print(f"  Range {start}-{end}: {number_list}")
    print()
    
    # Test list combination
    print("List Combination:")
    combinations = [
        ([1, 2], [3, 4]),
        (["a", "b"], ["c", "d"]),
        ([1], [2, 3, 4]),
        ([], [1, 2, 3]),
        ([1, 2, 3], [])
    ]
    
    for list1, list2 in combinations:
        combined = combine_two_lists(list1, list2)
        print(f"  {list1} + {list2} = {combined}")

# Test your implementation
if __name__ == "__main__":
    run_basic_list_tests()
