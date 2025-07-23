# Class Methods and Instance Variables - Test 3

**Difficulty:** ⭐ (Very Easy)

## Description

Learn to create methods that work with instance variables and understand the difference between methods and functions.

## Objectives

- Create methods that use instance variables
- Understand method vs function differences
- Practice method calls and return values
- Work with object state

## Your Tasks

1. **create_counter_class()** - Create a Counter class with increment/decrement
2. **track_state()** - Use instance variables to track counter state
3. **create_methods()** - Add methods to manipulate the counter
4. **test_counter()** - Test counter functionality

## Example

```python
class Counter:
    """A simple counter class."""
    
    def __init__(self, start_value=0):
        """Initialize counter with starting value."""
        self.value = start_value
        self.operations_count = 0
    
    def increment(self, amount=1):
        """Increase counter by amount (default 1)."""
        self.value += amount
        self.operations_count += 1
        return self.value
    
    def decrement(self, amount=1):
        """Decrease counter by amount (default 1)."""
        self.value -= amount
        self.operations_count += 1
        return self.value
    
    def reset(self):
        """Reset counter to 0."""
        self.value = 0
        self.operations_count += 1
        return "Counter reset to 0"
    
    def get_value(self):
        """Get current counter value."""
        return self.value
    
    def get_stats(self):
        """Get counter statistics."""
        return {
            'current_value': self.value,
            'operations_performed': self.operations_count
        }

# Example usage
def create_counter_class():
    """Create and use Counter objects."""
    # Create counters
    counter1 = Counter()  # Starts at 0
    counter2 = Counter(10)  # Starts at 10
    
    # Test counter1
    print(f"Counter1 initial value: {counter1.get_value()}")
    print(f"After increment: {counter1.increment()}")
    print(f"After increment by 5: {counter1.increment(5)}")
    print(f"After decrement: {counter1.decrement()}")
    print(f"Stats: {counter1.get_stats()}")
    
    # Test counter2
    print(f"\nCounter2 initial value: {counter2.get_value()}")
    print(f"After decrement by 3: {counter2.decrement(3)}")
    print(f"After increment by 2: {counter2.increment(2)}")
    print(counter2.reset())
    print(f"Stats: {counter2.get_stats()}")
    
    return counter1, counter2

# Test the class
if __name__ == "__main__":
    c1, c2 = create_counter_class()
    
    # Compare final states
    print(f"\nFinal values:")
    print(f"Counter1: {c1.get_value()} (operations: {c1.operations_count})")
    print(f"Counter2: {c2.get_value()} (operations: {c2.operations_count})")
```

## Hints

- Methods have access to `self` and instance variables
- Use default parameters for flexible method calls
- Track additional state like operation counts
- Return values from methods for chaining or feedback

## Test Cases

Your Counter class should:
- Initialize with default or custom starting values
- Increment and decrement by specified amounts
- Track the number of operations performed
- Provide statistics about the counter state
- Reset to zero when requested

## Bonus Challenge

Add methods like `double()`, `halve()`, and `is_even()` to extend the counter's functionality!
