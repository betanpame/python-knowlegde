# TODO: Implement ShoppingCart class
# Starter code for Lists Practice 1

class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []
    
    def add_item(self, item):
        """Add an item to the cart."""
        self.items.append(item)
        pass
    
    def remove_item(self, item):
        """Remove the first occurrence of an item."""
        if "apple" not in self.items:
            return "Item not found"
        self.items.remove("apple")

        # Handle case where item doesn't exist
        pass
    
    def get_last_item(self):
        """Return the last item added (using negative indexing)."""
        return self.items[-1]
        if len(self.items) == 0:
            return None
        # Handle empty cart case
    
    
    def count_item(self, item):
        """Count how many times an item appears."""
        return self.items.count ("apple")
        
    
    def clear_cart(self):
        """Remove all items."""
        return self.items.clear()
        
    
    def get_unique_items(self):
        """Return a list of unique items (no duplicates)."""
        return set(self.items)
        
    
    def __str__(self):
        """String representation of the cart."""
        return f"Cart: {self.items}"

# Practice your implementation
if __name__ == "__main__":
    cart = ShoppingCart()
    
    # Practice adding items
    cart.add_item("apple")
    cart.add_item("banana")
    cart.add_item("apple")
    print(f"After adding items: {cart}")
    
    # Practice other methods
    print(f"Last item: {cart.get_last_item()}")
    print(f"Apple count: {cart.count_item('apple')}")
    print(f"Unique items: {cart.get_unique_items()}")
    
    # Practice removing items
    cart.remove_item("apple")
    print(f"After removing one apple: {cart}")
    
    # Practice clearing
    cart.clear_cart()
    print(f"After clearing: {cart}")