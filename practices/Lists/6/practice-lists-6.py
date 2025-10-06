# TODO:
"""
Practice Lists 6: List Slicing Basics

Starter implementations for basic list slicing operations. Follow the practice markdown in
`practices/Lists/6/practice-lists-6.md` for task descriptions and practice cases.
"""

def get_first_n_items(my_list, n):
    """Get first n elements from the list.

    Args:
        my_list (list): The list to slice.
        n (int): Number of elements to return from the start.

    Returns:
        list: New list with the first n items (or entire list if n >= len).
    """
    return my_list[:n]


def get_last_n_items(my_list, n):
    """Get last n elements from the list.

    Args:
        my_list (list): The list to slice.
        n (int): Number of elements to return from the end.

    Returns:
        list: New list with the last n items (empty list if n == 0).
    """
    if n <= 0:
        return []
    return my_list[-n:]


def get_middle_items(my_list, start, end):
    """Get elements from start index up to (but not including) end index.

    Args:
        my_list (list): The list to slice.
        start (int): Start index (inclusive).
        end (int): End index (exclusive).

    Returns:
        list: New list with the requested slice.
    """
    return my_list[start:end]


def get_every_second_item(my_list):
    """Get every second element from the list (starting with index 0).

    Args:
        my_list (list): The list to slice.

    Returns:
        list: New list containing every second item.
    """
    return my_list[::2]


def reverse_list(my_list):
    """Return a reversed copy of the list.

    Args:
        my_list (list): The list to reverse.

    Returns:
        list: New list with elements in reverse order.
    """
    return my_list[::-1]


def get_odd_positioned_items(my_list):
    """Get elements at odd indices (1, 3, 5, ...).

    Args:
        my_list (list): The list to slice.

    Returns:
        list: New list with items from odd positions.
    """
    return my_list[1::2]


def get_even_positioned_items(my_list):
    """Get elements at even indices (0, 2, 4, ...).

    Args:
        my_list (list): The list to slice.

    Returns:
        list: New list with items from even positions.
    """
    return my_list[0::2]


def skip_first_and_last(my_list):
    """Return all elements except the first and last.

    Args:
        my_list (list): The list to slice.

    Returns:
        list: New list without the first and last elements.
    """
    return my_list[1:-1]


def solve():
    """Run simple practice cases for list slicing functions.

    Args:
        None
    Returns:
        None
    """
    test_list = [1,2,3,4,5,6,7,8,9,10]
    print("Original:", test_list)
    print("get_first_n_items(..., 3) ->", get_first_n_items(test_list, 3))     # [1, 2, 3]
    print("get_last_n_items(..., 3) ->", get_last_n_items(test_list, 3))       # [8, 9, 10]
    print("get_middle_items(..., 2, 5) ->", get_middle_items(test_list, 2, 5)) # [3, 4, 5]
    print("get_every_second_item(...) ->", get_every_second_item(test_list))   # [1, 3, 5, 7, 9]
    print("reverse_list(...) ->", reverse_list(test_list))                     # [10,9,8,7,6,5,4,3,2,1]
    print("get_odd_positioned_items(...) ->", get_odd_positioned_items(test_list))   # [2,4,6,8,10]
    print("get_even_positioned_items(...) ->", get_even_positioned_items(test_list)) # [1,3,5,7,9]
    print("skip_first_and_last(...) ->", skip_first_and_last(test_list))       # [2,3,4,5,6,7,8,9]


if __name__ == "__main__":
    solve()
