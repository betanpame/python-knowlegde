# Descriptors and Advanced Properties - Practice 17

**Difficulty:** ⭐⭐⭐ (Medium)

## Description

Learn to create descriptors - a powerful Python feature that allows you to customize attribute access and create reusable property-like behavior across multiple classes.

## Objectives

- Create descriptor classes with `__get__`, `__set__`, and `__delete__`
- Understand data vs non-data descriptors
- Build reusable validation descriptors
- Use descriptors for attribute access control

## Your Tasks

1. **create_basic_descriptor()** - Create simple descriptor class
2. **implement_validation_descriptors()** - Build descriptors with validation
3. **create_typed_descriptors()** - Add type checking descriptors
4. **demonstrate_descriptor_protocols()** - Show descriptor behavior

## Example

```python
import re
import weakref
from typing import Any, Type, Union, Callable
from datetime import datetime, date
import logging

# Basic descriptor example
class LoggedAttribute:
    """Descriptor that logs all access to an attribute."""
    
    def __init__(self, initial_value=None, name=None):
        """Initialize the logged attribute."""
        self.name = name
        self.initial_value = initial_value
    
    def __set_name__(self, owner, name):
        """Called when descriptor is assigned to a class attribute."""
        if self.name is None:
            self.name = name
        self.private_name = f'_{name}'
    
    def __get__(self, instance, owner):
        """Get attribute value."""
        if instance is None:
            return self  # Return descriptor when accessed from class
        
        value = getattr(instance, self.private_name, self.initial_value)
        logging.info(f"Getting {self.name} from {owner.__name__}: {value}")
        return value
    
    def __set__(self, instance, value):
        """Set attribute value."""
        old_value = getattr(instance, self.private_name, self.initial_value)
        setattr(instance, self.private_name, value)
        logging.info(f"Setting {self.name} on {type(instance).__name__}: {old_value} -> {value}")
    
    def __delete__(self, instance):
        """Delete attribute."""
        old_value = getattr(instance, self.private_name, self.initial_value)
        delattr(instance, self.private_name)
        logging.info(f"Deleting {self.name} from {type(instance).__name__}: {old_value}")

class ValidatedAttribute:
    """Base class for validated attributes."""
    
    def __init__(self, default=None, doc=None):
        """Initialize validated attribute."""
        self.default = default
        self.doc = doc
        
    def __set_name__(self, owner, name):
        """Set the name when assigned to class."""
        self.name = name
        self.private_name = f'_{name}'
    
    def __get__(self, instance, owner):
        """Get attribute value."""
        if instance is None:
            return self
        
        return getattr(instance, self.private_name, self.default)
    
    def __set__(self, instance, value):
        """Set attribute value with validation."""
        validated_value = self.validate(value)
        setattr(instance, self.private_name, validated_value)
    
    def validate(self, value):
        """Override this method in subclasses for specific validation."""
        return value

class PositiveNumber(ValidatedAttribute):
    """Descriptor for positive numbers only."""
    
    def validate(self, value):
        """Validate that value is a positive number."""
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} must be a number, got {type(value).__name__}")
        
        if value <= 0:
            raise ValueError(f"{self.name} must be positive, got {value}")
        
        return float(value)

class StringLength(ValidatedAttribute):
    """Descriptor for strings with length constraints."""
    
    def __init__(self, min_length=0, max_length=None, **kwargs):
        """Initialize string length validator."""
        super().__init__(**kwargs)
        self.min_length = min_length
        self.max_length = max_length
    
    def validate(self, value):
        """Validate string length."""
        if not isinstance(value, str):
            raise TypeError(f"{self.name} must be a string, got {type(value).__name__}")
        
        if len(value) < self.min_length:
            raise ValueError(f"{self.name} must be at least {self.min_length} characters, got {len(value)}")
        
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f"{self.name} must be at most {self.max_length} characters, got {len(value)}")
        
        return value

class EmailAddress(ValidatedAttribute):
    """Descriptor for email address validation."""
    
    EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    def validate(self, value):
        """Validate email address format."""
        if not isinstance(value, str):
            raise TypeError(f"{self.name} must be a string, got {type(value).__name__}")
        
        if not self.EMAIL_PATTERN.match(value):
            raise ValueError(f"{self.name} must be a valid email address, got '{value}'")
        
        return value.lower()  # Normalize to lowercase

class TypedAttribute:
    """Descriptor that enforces type checking."""
    
    def __init__(self, expected_type: Union[Type, tuple], default=None, allow_none=False):
        """Initialize typed attribute."""
        self.expected_type = expected_type
        self.default = default
        self.allow_none = allow_none
    
    def __set_name__(self, owner, name):
        """Set the name when assigned to class."""
        self.name = name
        self.private_name = f'_{name}'
    
    def __get__(self, instance, owner):
        """Get attribute value."""
        if instance is None:
            return self
        
        return getattr(instance, self.private_name, self.default)
    
    def __set__(self, instance, value):
        """Set attribute value with type checking."""
        if value is None and not self.allow_none:
            raise ValueError(f"{self.name} cannot be None")
        
        if value is not None and not isinstance(value, self.expected_type):
            expected_names = (self.expected_type.__name__ 
                            if hasattr(self.expected_type, '__name__') 
                            else str(self.expected_type))
            raise TypeError(f"{self.name} must be {expected_names}, got {type(value).__name__}")
        
        setattr(instance, self.private_name, value)

class CachedProperty:
    """Descriptor that caches the result of expensive computations."""
    
    def __init__(self, func):
        """Initialize cached property."""
        self.func = func
        self.name = func.__name__
        self.doc = func.__doc__
    
    def __get__(self, instance, owner):
        """Get cached value or compute and cache it."""
        if instance is None:
            return self
        
        # Check if value is already cached
        cache_name = f'_cached_{self.name}'
        
        if hasattr(instance, cache_name):
            logging.info(f"Returning cached value for {self.name}")
            return getattr(instance, cache_name)
        
        # Compute and cache the value
        logging.info(f"Computing value for {self.name}")
        value = self.func(instance)
        setattr(instance, cache_name, value)
        return value
    
    def __set__(self, instance, value):
        """Set cached value directly."""
        cache_name = f'_cached_{self.name}'
        setattr(instance, cache_name, value)
    
    def __delete__(self, instance):
        """Clear cached value."""
        cache_name = f'_cached_{self.name}'
        if hasattr(instance, cache_name):
            delattr(instance, cache_name)
            logging.info(f"Cleared cache for {self.name}")

class LazyProperty:
    """Descriptor for lazy evaluation of properties."""
    
    def __init__(self, func):
        """Initialize lazy property."""
        self.func = func
        self.name = func.__name__
        self.doc = func.__doc__
    
    def __get__(self, instance, owner):
        """Get value, computing it only once."""
        if instance is None:
            return self
        
        # Use instance's __dict__ to avoid infinite recursion
        try:
            return instance.__dict__[self.name]
        except KeyError:
            value = self.func(instance)
            instance.__dict__[self.name] = value
            return value
    
    def __set__(self, instance, value):
        """Set value directly in instance dict."""
        instance.__dict__[self.name] = value
    
    def __delete__(self, instance):
        """Delete value from instance dict."""
        try:
            del instance.__dict__[self.name]
        except KeyError:
            raise AttributeError(f"No attribute '{self.name}'")

class ObservableAttribute:
    """Descriptor that notifies observers when value changes."""
    
    def __init__(self, default=None):
        """Initialize observable attribute."""
        self.default = default
        self.observers = weakref.WeakSet()
    
    def __set_name__(self, owner, name):
        """Set the name when assigned to class."""
        self.name = name
        self.private_name = f'_{name}'
    
    def __get__(self, instance, owner):
        """Get attribute value."""
        if instance is None:
            return self
        
        return getattr(instance, self.private_name, self.default)
    
    def __set__(self, instance, value):
        """Set attribute value and notify observers."""
        old_value = getattr(instance, self.private_name, self.default)
        setattr(instance, self.private_name, value)
        
        if old_value != value:
            self._notify_observers(instance, old_value, value)
    
    def add_observer(self, observer):
        """Add an observer that will be called on value changes."""
        self.observers.add(observer)
    
    def remove_observer(self, observer):
        """Remove an observer."""
        self.observers.discard(observer)
    
    def _notify_observers(self, instance, old_value, new_value):
        """Notify all observers of value change."""
        for observer in self.observers:
            try:
                observer(instance, self.name, old_value, new_value)
            except Exception as e:
                logging.error(f"Error notifying observer: {e}")

# Example classes using descriptors
class Product:
    """Product class demonstrating various descriptors."""
    
    # Various descriptor types
    name = StringLength(min_length=1, max_length=100, doc="Product name")
    price = PositiveNumber(doc="Product price in dollars")
    category = TypedAttribute(str, default="General")
    created_at = TypedAttribute(datetime, allow_none=True)
    stock_count = ObservableAttribute(default=0)
    
    def __init__(self, name, price, category="General"):
        """Initialize product."""
        self.name = name
        self.price = price
        self.category = category
        self.created_at = datetime.now()
    
    @CachedProperty
    def formatted_price(self):
        """Get formatted price string (cached)."""
        import time
        time.sleep(0.1)  # Simulate expensive operation
        return f"${self.price:.2f}"
    
    @LazyProperty
    def description(self):
        """Get product description (lazy evaluation)."""
        return f"{self.name} in {self.category} category - {self.formatted_price}"
    
    def __str__(self):
        """String representation."""
        return f"{self.name} ({self.category}) - ${self.price:.2f}"

class Person:
    """Person class demonstrating logged attributes."""
    
    # Logged attributes
    first_name = LoggedAttribute()
    last_name = LoggedAttribute()
    email = EmailAddress()
    age = PositiveNumber()
    
    def __init__(self, first_name, last_name, email, age):
        """Initialize person."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
    
    @property
    def full_name(self):
        """Get full name."""
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        """String representation."""
        return f"{self.full_name} ({self.email}) - {self.age} years old"

# Example usage and tests
def create_basic_descriptor():
    """Demonstrate basic descriptor usage."""
    print("=== Basic Descriptor Usage ===")
    
    # Setup logging to see descriptor activity
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    # Create person with logged attributes
    print("1. Creating person with logged attributes:")
    person = Person("Alice", "Smith", "alice@example.com", 30)
    
    print("\n2. Accessing attributes (logged):")
    print(f"First name: {person.first_name}")
    print(f"Full name: {person.full_name}")
    
    print("\n3. Modifying attributes (logged):")
    person.age = 31
    person.last_name = "Johnson"
    
    print(f"Updated person: {person}")
    
    return person

def test_validation_descriptors():
    """Practice validation descriptors."""
    print("\n=== Validation Descriptors ===")
    
    # Create product with validation
    print("1. Valid product creation:")
    product = Product("Laptop", 999.99, "Electronics")
    print(f"Created: {product}")
    
    # Practice validation errors
    print("\n2. Testing validation errors:")
    
    # Invalid price
    try:
        product.price = -100
    except ValueError as e:
        print(f"Price validation error: {e}")
    
    # Invalid name length
    try:
        product.name = ""
    except ValueError as e:
        print(f"Name validation error: {e}")
    
    # Invalid email
    try:
        person = Person("Bob", "Wilson", "invalid-email", 25)
    except ValueError as e:
        print(f"Email validation error: {e}")
    
    # Invalid type
    try:
        product.category = 123
    except TypeError as e:
        print(f"Type validation error: {e}")
    
    return product

def test_cached_and_lazy_properties():
    """Practice cached and lazy properties."""
    print("\n=== Cached and Lazy Properties ===")
    
    product = Product("Smartphone", 699.99, "Electronics")
    
    print("1. Testing cached property:")
    print(f"First access: {product.formatted_price}")  # Will compute and cache
    print(f"Second access: {product.formatted_price}")  # Will use cache
    print(f"Third access: {product.formatted_price}")   # Will use cache
    
    print("\n2. Testing lazy property:")
    print(f"First description access: {product.description}")  # Will compute
    print(f"Second description access: {product.description}")  # Will use stored value
    
    # Clear cache
    del product.formatted_price
    print(f"After cache clear: {product.formatted_price}")  # Will recompute
    
    return product

def test_observable_attributes():
    """Practice observable attributes."""
    print("\n=== Observable Attributes ===")
    
    # Create observer function
    def stock_observer(instance, attr_name, old_value, new_value):
        print(f"Stock change notification: {instance.name} {attr_name} changed from {old_value} to {new_value}")
        if new_value < 5:
            print(f"WARNING: Low stock for {instance.name}!")
    
    # Create product and add observer
    product = Product("Tablet", 299.99, "Electronics")
    Product.stock_count.add_observer(stock_observer)
    
    print("1. Setting stock levels (with observer):")
    product.stock_count = 10
    product.stock_count = 3  # Should trigger warning
    product.stock_count = 15
    product.stock_count = 2  # Should trigger warning again
    
    return product

def demonstrate_descriptor_protocols():
    """Demonstrate different descriptor protocols."""
    print("\n=== Descriptor Protocols ===")
    
    # Show descriptor access from class vs instance
    print("1. Descriptor access patterns:")
    
    # Access from class returns descriptor
    print(f"Product.name from class: {Product.name}")
    print(f"Product.price from class: {Product.price}")
    
    # Access from instance returns value
    product = Product("Monitor", 199.99)
    print(f"product.name from instance: {product.name}")
    print(f"product.price from instance: {product.price}")
    
    # Show data vs non-data descriptors
    print("\n2. Data vs Non-data descriptors:")
    print("Data descriptors (with __set__): name, price, category")
    print("Non-data descriptors: methods, functions")
    
    # Practice attribute deletion
    print("\n3. Attribute deletion:")
    person = Person("Charlie", "Brown", "charlie@example.com", 28)
    print(f"Before deletion: {person.first_name}")
    
    try:
        del person.first_name
        print("After deletion: attribute removed")
    except AttributeError as e:
        print(f"Deletion error: {e}")
    
    return product, person

# Practice the implementation
if __name__ == "__main__":
    # Practice basic descriptors
    person = create_basic_descriptor()
    
    # Practice validation descriptors
    product = test_validation_descriptors()
    
    # Practice cached and lazy properties
    cached_product = test_cached_and_lazy_properties()
    
    # Practice observable attributes
    observable_product = test_observable_attributes()
    
    # Demonstrate descriptor protocols
    demo_results = demonstrate_descriptor_protocols()
    
    print("\n=== Final Demonstration ===")
    
    # Create a comprehensive example
    final_product = Product("Gaming Laptop", 1299.99, "Electronics")
    
    # Add stock observer
    def inventory_observer(instance, attr_name, old_value, new_value):
        if new_value == 0:
            print(f"ALERT: {instance.name} is out of stock!")
        elif new_value > old_value:
            print(f"Inventory restocked: {instance.name} (+{new_value - old_value})")
    
    Product.stock_count.add_observer(inventory_observer)
    
    # Simulate inventory changes
    final_product.stock_count = 50
    final_product.stock_count = 25
    final_product.stock_count = 0
    final_product.stock_count = 100
    
    print(f"Final product: {final_product}")
    print(f"Description: {final_product.description}")
    print(f"Formatted price: {final_product.formatted_price}")
```

## Hints

- Use `__set_name__` to automatically get the attribute name
- Data descriptors (with `__set__`) take precedence over instance dict
- Non-data descriptors (without `__set__`) can be overridden by instance attributes
- Use weakref for observers to avoid memory leaks
- Cache expensive computations in descriptors

## Practice Cases

Your descriptors should:

- Properly implement `__get__`, `__set__`, and optionally `__delete__`
- Validate data according to specific rules
- Handle both class and instance attribute access
- Support type checking and constraint enforcement
- Work with inheritance and multiple instances

## Bonus Challenge

Create a `DatabaseField` descriptor that automatically handles database serialization/deserialization and tracks dirty fields for ORM-like behavior!