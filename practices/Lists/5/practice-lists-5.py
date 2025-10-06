# TODO:
# filepath: c:\Users\shady\OneDrive\Documentos\GITHUB\python-knowlegde\practices\Lists\5\practice-lists-5.py

"""
Practice Lists 5: List Searching and Counting

Implement functions for searching, counting, and analyzing lists.
"""

def is_item_in_list(my_list, item):
    """Check if item exists in list.
    Args:
        my_list (list): The list to search.
        item: The item to check.
    Returns:
        bool: True if item is in the list, False otherwise.
    """
    pass

def count_occurrences(my_list, item):
    """Count how many times item appears in the list.
    Args:
        my_list (list): The list to search.
        item: The item to count.
    Returns:
        int: Number of occurrences.
    """
    pass

def find_first_index(my_list, item):
    """Find index of first occurrence of item in the list.
    Args:
        my_list (list): The list to search.
        item: The item to find.
    Returns:
        int: Index of first occurrence, or -1 if not found.
    """
    pass

def find_all_indices(my_list, item):
    """Find all indices where item appears in the list.
    Args:
        my_list (list): The list to search.
        item: The item to find.
    Returns:
        list: List of indices.
    """
    pass

def get_unique_items(my_list):
    """Return a list of unique items from the list.
    Args:
        my_list (list): The list to process.
    Returns:
        list: Unique items.
    """
    pass

def has_duplicates(my_list):
    """Check if the list contains any duplicates.
    Args:
        my_list (list): The list to check.
    Returns:
        bool: True if duplicates exist, False otherwise.
    """
    pass

def find_max_value(my_list):
    """Find largest value in the list.
    Args:
        my_list (list): The list to search.
    Returns:
        value: The largest value in the list.
    """
    pass

def find_min_value(my_list):
    """Find smallest value in the list.
    Args:
        my_list (list): The list to search.
    Returns:
        value: The smallest value in the list.
    """
    pass

def solve():
    """
    Run all practice cases for List Searching and Counting.
    Args:
        None
    Returns:
        None
    """
    numbers = [1, 2, 3, 2, 4, 2]
    print(is_item_in_list(numbers, 5))    # False
    print(count_occurrences(numbers, 2))  # 3
    print(find_first_index(numbers, 3))   # 2

    test_data = [1, 2, 3, 2, 4, 2, 5]
    print(find_all_indices(test_data, 2))  # [1, 3, 5]
    print(get_unique_items(test_data))      # [1, 2, 3, 4, 5] (order may vary)
    print(has_duplicates(test_data))        # True
    print(find_max_value(test_data))        # 5
    print(find_min_value(test_data))        # 1

if __name__ == "__main__":
    solve()