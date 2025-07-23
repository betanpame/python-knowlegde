# Test Lists 1: List Manipulation and Methods

**Difficulty:** ⭐⭐☆☆☆ (Easy-Medium)

**Related Topics:** List methods, list operations, indexing, Classes

## Objective

Create a shopping cart system using list methods to manage items.

## Requirements

Implement a `ShoppingCart` class with the following methods:

1. `add_item(item)` - Add an item to the cart
2. `remove_item(item)` - Remove the first occurrence of an item
3. `get_last_item()` - Return the last item added (using negative indexing)
4. `count_item(item)` - Count how many times an item appears
5. `clear_cart()` - Remove all items
6. `get_unique_items()` - Return a list of unique items (no duplicates)

## Example

```python
cart = ShoppingCart()
cart.add_item("apple")
cart.add_item("banana")
cart.add_item("apple")
print(cart.get_last_item())  # "apple"
print(cart.count_item("apple"))  # 2
print(cart.get_unique_items())  # ["apple", "banana"]
```

## Hints

- Use `.append()` to add items
- Use `.remove()` to remove items
- Use `[-1]` for last item access
- Use `.count()` method for counting
- Use `.clear()` to empty the list
- Consider using `set()` for unique items

## Test Cases

Your implementation should handle:

1. Adding multiple items including duplicates
2. Removing items that exist and don't exist
3. Getting the last item from empty and non-empty lists
4. Counting items correctly
5. Clearing the cart completely
