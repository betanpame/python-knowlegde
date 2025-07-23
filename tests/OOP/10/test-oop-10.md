# Special Methods (Magic Methods) - Test 10

**Difficulty:** ⭐ (Very Easy)

## Description

Learn to implement special methods (also called magic methods or dunder methods) to make your objects behave like built-in Python types.

## Objectives

- Implement common special methods (`__len__`, `__getitem__`, etc.)
- Make objects work with built-in functions
- Create objects that support operators
- Understand the power of magic methods

## Your Tasks

1. **create_shopping_cart_class()** - Create ShoppingCart with special methods
2. **implement_magic_methods()** - Add len, getitem, setitem, contains
3. **make_iterable()** - Add iterator support
4. **test_magic_methods()** - Test with built-in functions

## Example

```python
class ShoppingCart:
    """Shopping cart class demonstrating magic methods."""
    
    def __init__(self):
        """Initialize empty shopping cart."""
        self._items = {}  # Dictionary to store items and quantities
        self._total_items = 0
    
    def add_item(self, item, quantity=1):
        """Add item to cart."""
        if item in self._items:
            self._items[item] += quantity
        else:
            self._items[item] = quantity
        self._total_items += quantity
        return f"Added {quantity} {item}(s) to cart"
    
    def remove_item(self, item, quantity=1):
        """Remove item from cart."""
        if item not in self._items:
            return f"{item} not in cart"
        
        if self._items[item] <= quantity:
            removed = self._items[item]
            del self._items[item]
            self._total_items -= removed
            return f"Removed all {item}(s) from cart"
        else:
            self._items[item] -= quantity
            self._total_items -= quantity
            return f"Removed {quantity} {item}(s) from cart"
    
    # Magic method for len()
    def __len__(self):
        """Return total number of items in cart."""
        return self._total_items
    
    # Magic method for item access cart[item]
    def __getitem__(self, item):
        """Get quantity of item in cart."""
        return self._items.get(item, 0)
    
    # Magic method for item assignment cart[item] = quantity
    def __setitem__(self, item, quantity):
        """Set quantity of item in cart."""
        if quantity <= 0:
            if item in self._items:
                self._total_items -= self._items[item]
                del self._items[item]
        else:
            old_quantity = self._items.get(item, 0)
            self._items[item] = quantity
            self._total_items = self._total_items - old_quantity + quantity
    
    # Magic method for 'in' operator
    def __contains__(self, item):
        """Check if item is in cart."""
        return item in self._items
    
    # Magic method for iteration
    def __iter__(self):
        """Make cart iterable."""
        return iter(self._items.items())
    
    # Magic method for string representation
    def __str__(self):
        """User-friendly string representation."""
        if not self._items:
            return "Empty shopping cart"
        
        items_str = ", ".join([f"{item}: {qty}" for item, qty in self._items.items()])
        return f"Shopping Cart ({self._total_items} items): {items_str}"
    
    # Magic method for equality comparison
    def __eq__(self, other):
        """Check if two carts are equal."""
        if not isinstance(other, ShoppingCart):
            return False
        return self._items == other._items
    
    # Magic method for addition (combining carts)
    def __add__(self, other):
        """Combine two shopping carts."""
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        
        new_cart = ShoppingCart()
        
        # Add items from first cart
        for item, quantity in self._items.items():
            new_cart[item] = quantity
        
        # Add items from second cart
        for item, quantity in other._items.items():
            if item in new_cart:
                new_cart[item] += quantity
            else:
                new_cart[item] = quantity
        
        return new_cart
    
    # Magic method for bool conversion
    def __bool__(self):
        """Return True if cart has items."""
        return len(self._items) > 0

# Example usage
def create_shopping_cart_class():
    """Create and use ShoppingCart with magic methods."""
    # Create shopping carts
    cart1 = ShoppingCart()
    cart2 = ShoppingCart()
    
    # Add items using regular methods
    print("Adding items to cart1:")
    print(cart1.add_item("apples", 3))
    print(cart1.add_item("bananas", 2))
    print(cart1.add_item("milk", 1))
    
    print("\nAdding items to cart2:")
    print(cart2.add_item("bread", 1))
    print(cart2.add_item("milk", 2))
    print(cart2.add_item("eggs", 6))
    
    # Test __len__ magic method
    print(f"\n=== Testing len() magic method ===")
    print(f"Cart1 length: {len(cart1)}")  # Uses __len__
    print(f"Cart2 length: {len(cart2)}")
    
    # Test __getitem__ magic method
    print(f"\n=== Testing [] access magic method ===")
    print(f"Apples in cart1: {cart1['apples']}")  # Uses __getitem__
    print(f"Milk in cart1: {cart1['milk']}")
    print(f"Oranges in cart1: {cart1['oranges']}")  # Not in cart, should return 0
    
    # Test __setitem__ magic method
    print(f"\n=== Testing [] assignment magic method ===")
    cart1['cookies'] = 5  # Uses __setitem__
    print(f"After adding cookies: {cart1}")
    cart1['apples'] = 10  # Change existing item
    print(f"After changing apples: {cart1}")
    
    # Test __contains__ magic method
    print(f"\n=== Testing 'in' operator magic method ===")
    print(f"'milk' in cart1: {'milk' in cart1}")  # Uses __contains__
    print(f"'oranges' in cart1: {'oranges' in cart1}")
    print(f"'bread' in cart2: {'bread' in cart2}")
    
    # Test __iter__ magic method
    print(f"\n=== Testing iteration magic method ===")
    print("Items in cart1:")
    for item, quantity in cart1:  # Uses __iter__
        print(f"  {item}: {quantity}")
    
    # Test __bool__ magic method
    print(f"\n=== Testing bool conversion magic method ===")
    empty_cart = ShoppingCart()
    print(f"cart1 is truthy: {bool(cart1)}")  # Uses __bool__
    print(f"empty_cart is truthy: {bool(empty_cart)}")
    
    if cart1:  # Uses __bool__ implicitly
        print("Cart1 has items!")
    
    if not empty_cart:  # Uses __bool__ implicitly
        print("Empty cart is indeed empty!")
    
    # Test __eq__ magic method
    print(f"\n=== Testing equality magic method ===")
    cart3 = ShoppingCart()
    cart3.add_item("apples", 10)
    cart3.add_item("bananas", 2)
    cart3.add_item("milk", 1)
    cart3.add_item("cookies", 5)
    
    print(f"cart1 == cart3: {cart1 == cart3}")  # Uses __eq__
    print(f"cart1 == cart2: {cart1 == cart2}")
    
    # Test __add__ magic method
    print(f"\n=== Testing addition magic method ===")
    combined_cart = cart1 + cart2  # Uses __add__
    print(f"Combined cart: {combined_cart}")
    print(f"Combined cart length: {len(combined_cart)}")
    
    return cart1, cart2, combined_cart

# Test the class
if __name__ == "__main__":
    c1, c2, combined = create_shopping_cart_class()
    
    # Final demonstration
    print(f"\n=== Final Demonstration ===")
    print(f"Cart1: {c1}")
    print(f"Cart2: {c2}")
    print(f"Combined: {combined}")
    
    # Show that magic methods make objects work with built-ins
    print(f"\nBuilt-in functions work:")
    print(f"len(combined): {len(combined)}")
    print(f"'milk' in combined: {'milk' in combined}")
    print(f"bool(combined): {bool(combined)}")
```

## Hints

- Magic methods are surrounded by double underscores (`__method__`)
- `__len__` makes `len()` function work
- `__getitem__` enables `obj[key]` access
- `__setitem__` enables `obj[key] = value` assignment
- `__contains__` makes `in` operator work
- `__iter__` makes objects iterable with `for` loops

## Test Cases

Your ShoppingCart should:

- Work with `len()` to get total items
- Support `cart[item]` to get quantities
- Support `cart[item] = quantity` to set quantities
- Work with `item in cart` to check existence
- Be iterable with `for` loops
- Support combining carts with `+` operator

## Bonus Challenge

Add `__delitem__` for `del cart[item]`, `__lt__` for size comparison, and `__repr__` for developer representation!
