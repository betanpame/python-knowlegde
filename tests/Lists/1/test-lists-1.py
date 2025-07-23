# TODO: Implement ShoppingCart class
# Starter code for Lists Test 1

class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []
    
    def add_item(self, item):
        """Add an item to the cart."""
        # Your implementation here
        pass
    
    def remove_item(self, item):
        """Remove the first occurrence of an item."""
        # Your implementation here
        # Handle case where item doesn't exist
        pass
    
    def get_last_item(self):
        """Return the last item added (using negative indexing)."""
        # Your implementation here
        # Handle empty cart case
        pass
    
    def count_item(self, item):
        """Count how many times an item appears."""
        # Your implementation here
        pass
    
    def clear_cart(self):
        """Remove all items."""
        # Your implementation here
        pass
    
    def get_unique_items(self):
        """Return a list of unique items (no duplicates)."""
        # Your implementation here
        pass
    
    def __str__(self):
        """String representation of the cart."""
        return f"Cart: {self.items}"

# Test your implementation
if __name__ == "__main__":
    cart = ShoppingCart()
    
    # Test adding items
    cart.add_item("apple")
    cart.add_item("banana")
    cart.add_item("apple")
    print(f"After adding items: {cart}")
    
    # Test other methods
    print(f"Last item: {cart.get_last_item()}")
    print(f"Apple count: {cart.count_item('apple')}")
    print(f"Unique items: {cart.get_unique_items()}")
    
    # Test removing items
    cart.remove_item("apple")
    print(f"After removing one apple: {cart}")
    
    # Test clearing
    cart.clear_cart()
    print(f"After clearing: {cart}")
