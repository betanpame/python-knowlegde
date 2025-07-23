# Static Methods and Class Methods - Test 9

**Difficulty:** ⭐ (Very Easy)

## Description

Learn the difference between static methods (`@staticmethod`) and class methods (`@classmethod`), and when to use each.

## Objectives

- Create static methods using `@staticmethod`
- Create class methods using `@classmethod`
- Understand when to use each type of method
- Practice accessing class and static methods

## Your Tasks

1. **create_math_utility_class()** - Create MathUtils class with static methods
2. **create_person_class_methods()** - Create Person class with class methods
3. **demonstrate_static_methods()** - Show static method usage
4. **demonstrate_class_methods()** - Show class method usage

## Example

```python
class MathUtils:
    """Utility class with static methods for mathematical operations."""
    
    # Class attribute
    pi = 3.14159
    
    @staticmethod
    def add(a, b):
        """Add two numbers (static method - no self or cls needed)."""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b
    
    @staticmethod
    def is_even(number):
        """Check if a number is even."""
        return number % 2 == 0
    
    @staticmethod
    def factorial(n):
        """Calculate factorial of a number."""
        if n < 0:
            return None
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)
    
    @classmethod
    def circle_area(cls, radius):
        """Calculate circle area using class attribute pi."""
        return cls.pi * radius ** 2
    
    @classmethod
    def get_pi(cls):
        """Get the value of pi (class method to access class attribute)."""
        return cls.pi

class Person:
    """Person class demonstrating class methods for object creation."""
    
    total_people = 0  # Class attribute to track total people
    
    def __init__(self, name, age):
        """Initialize a Person."""
        self.name = name
        self.age = age
        Person.total_people += 1
    
    @classmethod
    def from_string(cls, person_string):
        """Create Person from string 'name,age' (alternative constructor)."""
        name, age = person_string.split(',')
        return cls(name.strip(), int(age.strip()))
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Create Person from birth year (alternative constructor)."""
        current_year = 2024
        age = current_year - birth_year
        return cls(name, age)
    
    @classmethod
    def get_total_people(cls):
        """Get total number of people created."""
        return cls.total_people
    
    @staticmethod
    def is_adult(age):
        """Check if age represents an adult (static method - doesn't need class)."""
        return age >= 18
    
    @staticmethod
    def calculate_age_from_year(birth_year):
        """Calculate age from birth year."""
        return 2024 - birth_year
    
    def __str__(self):
        """String representation of Person."""
        adult_status = "adult" if Person.is_adult(self.age) else "minor"
        return f"{self.name} ({self.age} years old) - {adult_status}"

# Example usage
def create_math_utility_class():
    """Demonstrate static methods usage."""
    print("=== Static Methods Demo ===")
    
    # Call static methods without creating an instance
    print(f"5 + 3 = {MathUtils.add(5, 3)}")
    print(f"5 * 3 = {MathUtils.multiply(5, 3)}")
    print(f"Is 8 even? {MathUtils.is_even(8)}")
    print(f"Is 7 even? {MathUtils.is_even(7)}")
    print(f"5! = {MathUtils.factorial(5)}")
    
    # Call class methods (notice they use class attribute)
    print(f"Circle area (radius=3): {MathUtils.circle_area(3):.2f}")
    print(f"Pi value: {MathUtils.get_pi()}")
    
    # Static methods can also be called on instances
    math_instance = MathUtils()
    print(f"10 + 20 = {math_instance.add(10, 20)}")  # Still works, but not recommended
    
    return math_instance

def create_person_class_methods():
    """Demonstrate class methods for alternative constructors."""
    print("\n=== Class Methods Demo ===")
    
    # Regular constructor
    person1 = Person("Alice", 25)
    print(f"Person1: {person1}")
    
    # Alternative constructor from string
    person2 = Person.from_string("Bob, 30")
    print(f"Person2: {person2}")
    
    # Alternative constructor from birth year
    person3 = Person.from_birth_year("Charlie", 1995)
    print(f"Person3: {person3}")
    
    # Class method to get statistics
    print(f"Total people created: {Person.get_total_people()}")
    
    # Static methods for utility functions
    print(f"Is age 16 adult? {Person.is_adult(16)}")
    print(f"Is age 21 adult? {Person.is_adult(21)}")
    print(f"Age if born in 2000: {Person.calculate_age_from_year(2000)}")
    
    return [person1, person2, person3]

# Test the classes
if __name__ == "__main__":
    # Test MathUtils
    math_utils = create_math_utility_class()
    
    # Test Person
    people = create_person_class_methods()
    
    # Additional demonstrations
    print("\n=== Additional Demonstrations ===")
    
    # Show that static methods don't have access to self or cls
    print(f"Static method result: {MathUtils.is_even(42)}")
    
    # Show that class methods have access to class attributes
    print(f"Class method uses class attribute: {MathUtils.circle_area(2):.2f}")
    
    # Create more people to show total count
    Person.from_string("Diana, 28")
    Person.from_birth_year("Eve", 1990)
    print(f"Final total people: {Person.get_total_people()}")
    
    # Show all people
    print("\nAll people:")
    for i, person in enumerate(people, 1):
        print(f"{i}. {person}")
```

## Hints

- `@staticmethod` - doesn't receive `self` or `cls`, works like regular function
- `@classmethod` - receives `cls` parameter, can access class attributes
- Static methods are for utility functions that don't need class data
- Class methods are often used for alternative constructors
- Both can be called on class or instance

## Test Cases

Your static and class methods should:

- Static methods work without creating instances
- Class methods have access to class attributes via `cls`
- Alternative constructors create valid objects
- Utility methods provide helpful functionality
- Methods can be called on both class and instances

## Bonus Challenge

Create a `DateUtils` class with static methods for date operations and class methods for creating dates from different formats!
