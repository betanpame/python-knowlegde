# TODO: Implement basic list modification methods
# Starter code for Lists Practice 4

def add_to_end(my_list, item):
    """
    Add item to end of list.
    
    Args:
        my_list (list): List to modify
        item (any): Item to add
    """
    # Your implementation here
    my_list.append(item) 

    # Use append() method
    pass

def add_to_beginning(my_list, item):
    """
    Add item to beginning of list.
    
    Args:
        my_list (list): List to modify
        item (any): Item to add
    """
    # Your implementation here
    my_list.insert(0, item)


    # Use insert() method at position 0
    pass

def remove_first_occurrence(my_list, item):
    """
    Remove first occurrence of item from list.
    
    Args:
        my_list (list): List to modify
        item (any): Item to remove
        
    Returns:
        bool: True if item was removed, False if not found
    """
    # Your implementation here
    try:
        my_list.remove(item)
        return True
    except ValueError:
        return False

    # Use remove() method with try/except for error handling
    pass

def remove_last_element(my_list):
    """
    Remove and return last element from list.
    
    Args:
        my_list (list): List to modify
        
    Returns:
        any: Last element, or None if list is empty
    """
    # Your implementation here
    if my_list:
        return my_list.pop()
    else:
        return None 
    
    # Use pop() method with error handling
    pass

def clear_list(my_list):
    """
    Remove all elements from list.
    
    Args:
        my_list (list): List to clear
    """
    # Your implementation here
    my_list.clear() 

    # Use clear() method
    pass

def add_multiple_items(my_list, items):
    """
    Add multiple items to end of list.
    
    Args:
        my_list (list): List to modify
        items (list): Items to add
    """
    # Your implementation here
    my_list.extend(items)

    # Use extend() method
    pass

def insert_at_position(my_list, index, item):
    """
    Insert item at specific position.
    
    Args:
        my_list (list): List to modify
        index (int): Position to insert at
        item (any): Item to insert
        
    Returns:
        bool: True if successful, False if index invalid
    """
    # Your implementation here
    if 0 <= index <= len(my_list):
        my_list.insert(index, item)
        return True
    else:
        return False
    # Use insert() method with bounds checking
    pass

def remove_at_position(my_list, index):
    """
    Remove item at specific position.
    
    Args:
        my_list (list): List to modify
        index (int): Position to remove from
        
    Returns:
        any: Removed item, or None if index invalid
    """
    # Your implementation here
    if 0 <= index < len(my_list):
        return my_list.pop(index)
    else:
        return None
    # Use pop() method with index and error handling
    pass

def run_modification_tests():
    """Run comprehensive list modification tests."""
    
    print("=== List Modification Practices ===")
    
    # Practice adding to end
    test_list = [1, 2, 3]
    print(f"Original list: {test_list}")
    add_to_end(test_list, 4)
    print(f"After adding 4 to end: {test_list}")
    
    # Practice adding to beginning
    add_to_beginning(test_list, 0)
    print(f"After adding 0 to beginning: {test_list}")
    
    # Practice removing first occurrence
    test_list.append(2)  # Add duplicate
    print(f"List with duplicate 2: {test_list}")
    removed = remove_first_occurrence(test_list, 2)
    print(f"After removing first 2: {test_list}, Success: {removed}")
    
    # Practice removing non-existent item
    removed = remove_first_occurrence(test_list, 99)
    print(f"Trying to remove 99: {test_list}, Success: {removed}")
    print()
    
    # Practice removing last element
    last_item = remove_last_element(test_list)
    print(f"Removed last element: {last_item}")
    print(f"List after removing last: {test_list}")
    
    # Practice with empty list
    empty_list = []
    last_item = remove_last_element(empty_list)
    print(f"Remove from empty list: {last_item}")
    print()
    
    # Practice adding multiple items
    test_list2 = [1, 2]
    print(f"Original list: {test_list2}")
    add_multiple_items(test_list2, [3, 4, 5])
    print(f"After adding [3, 4, 5]: {test_list2}")
    print()
    
    # Practice insertion at position
    test_list3 = [1, 3, 4]
    print(f"Original list: {test_list3}")
    success = insert_at_position(test_list3, 1, 2)
    print(f"After inserting 2 at position 1: {test_list3}, Success: {success}")
    
    # Practice invalid insertion
    success = insert_at_position(test_list3, 99, 5)
    print(f"Trying to insert at position 99: {test_list3}, Success: {success}")
    print()
    
    # Practice removal at position
    removed_item = remove_at_position(test_list3, 2)
    print(f"Removed item at position 2: {removed_item}")
    print(f"List after removal: {test_list3}")
    
    # Practice invalid removal
    removed_item = remove_at_position(test_list3, 99)
    print(f"Trying to remove at position 99: {removed_item}")
    print()
    
    # Practice clearing list
    test_list4 = [1, 2, 3, 4, 5]
    print(f"List before clearing: {test_list4}")
    clear_list(test_list4)
    print(f"List after clearing: {test_list4}")

# Practice your implementation
if __name__ == "__main__":
    run_modification_tests()