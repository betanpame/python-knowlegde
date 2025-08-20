# Basic Inheritance - Practice 6

**Difficulty:** ⭐ (Very Easy)

## Description

Learn the basics of inheritance - creating child classes that inherit from parent classes.

## Objectives

- Create a parent (base) class
- Create child classes that inherit from the parent
- Understand inherited methods and attributes
- Practice the `super()` function

## Your Tasks

1. **create_shape_class()** - Create a base Shape class
2. **create_child_classes()** - Create Rectangle and Circle classes
3. **demonstrate_inheritance()** - Show inherited behavior
4. **use_super()** - Practice calling parent methods

## Example

```python
class Shape:
    """Base class for all shapes."""
    
    def __init__(self, color="white"):
        """Initialize a shape with color."""
        self.color = color
        self.created_at = "2024"
    
    def get_color(self):
        """Get the shape's color."""
        return self.color
    
    def set_color(self, color):
        """Set the shape's color."""
        self.color = color
        return f"Color changed to {color}"
    
    def describe(self):
        """Basic description of the shape."""
        return f"This is a {self.color} shape"

class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""
    
    def __init__(self, width, height, color="white"):
        """Initialize a rectangle."""
        super().__init__(color)  # Call parent constructor
        self.width = width
        self.height = height
    
    def get_area(self):
        """Calculate rectangle area."""
        return self.width * self.height
    
    def get_perimeter(self):
        """Calculate rectangle perimeter."""
        return 2 * (self.width + self.height)
    
    def describe(self):
        """Describe the rectangle (overrides parent method)."""
        area = self.get_area()
        return f"This is a {self.color} rectangle with area {area}"

class Circle(Shape):
    """Circle class that inherits from Shape."""
    
    def __init__(self, radius, color="white"):
        """Initialize a circle."""
        super().__init__(color)  # Call parent constructor
        self.radius = radius
    
    def get_area(self):
        """Calculate circle area."""
        import math
        return math.pi * self.radius ** 2
    
    def get_circumference(self):
        """Calculate circle circumference."""
        import math
        return 2 * math.pi * self.radius
    
    def describe(self):
        """Describe the circle (overrides parent method)."""
        area = self.get_area()
        return f"This is a {self.color} circle with area {area:.2f}"

# Example usage
def create_shape_class():
    """Create and use Shape inheritance."""
    # Create shapes
    rectangle = Rectangle(5, 3, "red")
    circle = Circle(4, "blue")
    basic_shape = Shape("green")
    
    # Practice inherited methods
    print("Testing inherited methods:")
    print(f"Rectangle color: {rectangle.get_color()}")
    print(f"Circle color: {circle.get_color()}")
    print(f"Basic shape color: {basic_shape.get_color()}")
    
    # Practice inherited attributes
    print(f"\nTesting inherited attributes:")
    print(f"Rectangle created at: {rectangle.created_at}")
    print(f"Circle created at: {circle.created_at}")
    
    # Practice overridden methods
    print(f"\nTesting describe method (overridden):")
    print(rectangle.describe())
    print(circle.describe())
    print(basic_shape.describe())
    
    # Practice child-specific methods
    print(f"\nTesting child-specific methods:")
    print(f"Rectangle area: {rectangle.get_area()}")
    print(f"Rectangle perimeter: {rectangle.get_perimeter()}")
    print(f"Circle area: {circle.get_area():.2f}")
    print(f"Circle circumference: {circle.get_circumference():.2f}")
    
    # Practice inherited method to change color
    print(f"\nChanging colors:")
    print(rectangle.set_color("yellow"))
    print(circle.set_color("purple"))
    
    print(f"\nAfter color change:")
    print(rectangle.describe())
    print(circle.describe())
    
    return rectangle, circle, basic_shape

# Practice the classes
if __name__ == "__main__":
    rect, circ, shape = create_shape_class()
    
    # Show that they are instances of both child and parent classes
    print(f"\nInstance checking:")
    print(f"Rectangle is Shape: {isinstance(rect, Shape)}")
    print(f"Rectangle is Rectangle: {isinstance(rect, Rectangle)}")
    print(f"Circle is Shape: {isinstance(circ, Shape)}")
    print(f"Circle is Circle: {isinstance(circ, Circle)}")
```

## Hints

- Use `class Child(Parent):` syntax for inheritance
- Call `super().__init__()` to initialize the parent class
- Child classes inherit all parent methods and attributes
- Child classes can override parent methods
- Use `isinstance()` to check object types

## Practice Cases

Your inheritance hierarchy should:

- Allow Rectangle and Circle to inherit from Shape
- Correctly initialize parent attributes using `super()`
- Override the `describe()` method in child classes
- Provide child-specific methods for area calculations
- Maintain access to inherited methods like color management

## Bonus Challenge

Create a Square class that inherits from Rectangle, and a Sphere class that inherits from Circle!