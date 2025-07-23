# Abstract Base Classes and Interfaces - Test 13

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Learn to create abstract base classes using the `abc` module to define interfaces that child classes must implement.

## Objectives

- Create abstract base classes using `ABC` and `@abstractmethod`
- Understand the concept of interfaces in Python
- Force child classes to implement specific methods
- Use abstract properties and class methods

## Your Tasks

1. **create_abstract_base_class()** - Create abstract Shape class
2. **implement_concrete_classes()** - Create concrete implementations
3. **use_abstract_properties()** - Create abstract properties
4. **demonstrate_polymorphism()** - Show polymorphic behavior

## Example

```python
from abc import ABC, abstractmethod, abstractproperty
import math

# Abstract base class defining an interface
class Shape(ABC):
    """Abstract base class for all shapes."""
    
    def __init__(self, color="white"):
        """Initialize shape with color."""
        self.color = color
    
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by child classes."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by child classes."""
        pass
    
    @property
    @abstractmethod
    def shape_type(self):
        """Get shape type - abstract property."""
        pass
    
    # Concrete method (can be used by all child classes)
    def get_color(self):
        """Get shape color."""
        return self.color
    
    def set_color(self, color):
        """Set shape color."""
        self.color = color
        return f"Color changed to {color}"
    
    def describe(self):
        """Describe the shape (uses abstract methods)."""
        return f"{self.color} {self.shape_type} - Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"
    
    @classmethod
    @abstractmethod
    def from_string(cls, shape_string):
        """Create shape from string - abstract class method."""
        pass

# Abstract base class for drawable objects
class Drawable(ABC):
    """Abstract base class for objects that can be drawn."""
    
    @abstractmethod
    def draw(self):
        """Draw the object - must be implemented."""
        pass
    
    @abstractmethod
    def move(self, x, y):
        """Move the object - must be implemented."""
        pass

# Concrete implementation: Rectangle
class Rectangle(Shape, Drawable):
    """Rectangle implementation of Shape."""
    
    def __init__(self, width, height, color="white"):
        """Initialize rectangle."""
        super().__init__(color)
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
    
    def area(self):
        """Calculate rectangle area."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate rectangle perimeter."""
        return 2 * (self.width + self.height)
    
    @property
    def shape_type(self):
        """Get shape type."""
        return "Rectangle"
    
    def draw(self):
        """Draw the rectangle."""
        return f"Drawing {self.color} rectangle at ({self.x}, {self.y}) - {self.width}x{self.height}"
    
    def move(self, x, y):
        """Move the rectangle."""
        self.x = x
        self.y = y
        return f"Moved rectangle to ({self.x}, {self.y})"
    
    @classmethod
    def from_string(cls, shape_string):
        """Create rectangle from string 'width,height,color'."""
        parts = shape_string.split(',')
        width = float(parts[0])
        height = float(parts[1])
        color = parts[2].strip() if len(parts) > 2 else "white"
        return cls(width, height, color)
    
    def is_square(self):
        """Check if rectangle is a square."""
        return abs(self.width - self.height) < 0.001

# Concrete implementation: Circle
class Circle(Shape, Drawable):
    """Circle implementation of Shape."""
    
    def __init__(self, radius, color="white"):
        """Initialize circle."""
        super().__init__(color)
        self.radius = radius
        self.x = 0
        self.y = 0
    
    def area(self):
        """Calculate circle area."""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate circle circumference."""
        return 2 * math.pi * self.radius
    
    @property
    def shape_type(self):
        """Get shape type."""
        return "Circle"
    
    def draw(self):
        """Draw the circle."""
        return f"Drawing {self.color} circle at ({self.x}, {self.y}) - radius {self.radius}"
    
    def move(self, x, y):
        """Move the circle."""
        self.x = x
        self.y = y
        return f"Moved circle to ({self.x}, {self.y})"
    
    @classmethod
    def from_string(cls, shape_string):
        """Create circle from string 'radius,color'."""
        parts = shape_string.split(',')
        radius = float(parts[0])
        color = parts[1].strip() if len(parts) > 1 else "white"
        return cls(radius, color)
    
    def diameter(self):
        """Calculate circle diameter."""
        return 2 * self.radius

# Concrete implementation: Triangle
class Triangle(Shape, Drawable):
    """Triangle implementation of Shape."""
    
    def __init__(self, side_a, side_b, side_c, color="white"):
        """Initialize triangle."""
        super().__init__(color)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.x = 0
        self.y = 0
        
        # Validate triangle inequality
        if not self._is_valid_triangle():
            raise ValueError("Invalid triangle: sides don't satisfy triangle inequality")
    
    def _is_valid_triangle(self):
        """Check if sides form a valid triangle."""
        return (self.side_a + self.side_b > self.side_c and
                self.side_a + self.side_c > self.side_b and
                self.side_b + self.side_c > self.side_a)
    
    def area(self):
        """Calculate triangle area using Heron's formula."""
        s = self.perimeter() / 2  # semi-perimeter
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def perimeter(self):
        """Calculate triangle perimeter."""
        return self.side_a + self.side_b + self.side_c
    
    @property
    def shape_type(self):
        """Get shape type."""
        if self.is_equilateral():
            return "Equilateral Triangle"
        elif self.is_isosceles():
            return "Isosceles Triangle"
        else:
            return "Scalene Triangle"
    
    def draw(self):
        """Draw the triangle."""
        return f"Drawing {self.color} triangle at ({self.x}, {self.y}) - sides {self.side_a}, {self.side_b}, {self.side_c}"
    
    def move(self, x, y):
        """Move the triangle."""
        self.x = x
        self.y = y
        return f"Moved triangle to ({self.x}, {self.y})"
    
    @classmethod
    def from_string(cls, shape_string):
        """Create triangle from string 'side_a,side_b,side_c,color'."""
        parts = shape_string.split(',')
        side_a = float(parts[0])
        side_b = float(parts[1])
        side_c = float(parts[2])
        color = parts[3].strip() if len(parts) > 3 else "white"
        return cls(side_a, side_b, side_c, color)
    
    def is_equilateral(self):
        """Check if triangle is equilateral."""
        return (abs(self.side_a - self.side_b) < 0.001 and 
                abs(self.side_b - self.side_c) < 0.001)
    
    def is_isosceles(self):
        """Check if triangle is isosceles."""
        return (abs(self.side_a - self.side_b) < 0.001 or
                abs(self.side_b - self.side_c) < 0.001 or
                abs(self.side_a - self.side_c) < 0.001)

# Example usage
def create_abstract_base_class():
    """Demonstrate abstract base classes."""
    print("=== Abstract Base Classes Demo ===")
    
    # Try to create abstract class (this will fail)
    try:
        shape = Shape("red")
    except TypeError as e:
        print(f"Cannot instantiate abstract class: {e}")
    
    # Create concrete implementations
    shapes = [
        Rectangle(5, 3, "red"),
        Circle(4, "blue"),
        Triangle(3, 4, 5, "green")
    ]
    
    print(f"\nCreated {len(shapes)} concrete shapes:")
    for shape in shapes:
        print(f"  {shape.describe()}")
    
    return shapes

def demonstrate_polymorphism(shapes):
    """Demonstrate polymorphic behavior with abstract base class."""
    print(f"\n=== Polymorphism Demo ===")
    
    # All shapes can be treated the same way
    total_area = 0
    total_perimeter = 0
    
    for shape in shapes:
        print(f"\nProcessing {shape.shape_type}:")
        print(f"  {shape.draw()}")
        print(f"  Moving: {shape.move(10, 20)}")
        print(f"  Color: {shape.get_color()}")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}")
        
        total_area += shape.area()
        total_perimeter += shape.perimeter()
    
    print(f"\nTotals:")
    print(f"  Total area: {total_area:.2f}")
    print(f"  Total perimeter: {total_perimeter:.2f}")

def test_alternative_constructors():
    """Test abstract class methods for alternative constructors."""
    print(f"\n=== Alternative Constructors Demo ===")
    
    # Create shapes from strings
    shape_strings = [
        ("Rectangle", "6,4,yellow"),
        ("Circle", "3.5,purple"),
        ("Triangle", "5,5,5,orange")
    ]
    
    shapes = []
    for shape_type, shape_string in shape_strings:
        if shape_type == "Rectangle":
            shape = Rectangle.from_string(shape_string)
        elif shape_type == "Circle":
            shape = Circle.from_string(shape_string)
        elif shape_type == "Triangle":
            shape = Triangle.from_string(shape_string)
        
        shapes.append(shape)
        print(f"Created {shape_type} from string '{shape_string}': {shape.describe()}")
    
    return shapes

def test_type_checking():
    """Test isinstance and issubclass with abstract base classes."""
    print(f"\n=== Type Checking Demo ===")
    
    rect = Rectangle(3, 4, "cyan")
    circle = Circle(2, "magenta")
    
    # Test isinstance
    print(f"Rectangle is Shape: {isinstance(rect, Shape)}")
    print(f"Rectangle is Drawable: {isinstance(rect, Drawable)}")
    print(f"Circle is Shape: {isinstance(circle, Shape)}")
    print(f"Circle is Drawable: {isinstance(circle, Drawable)}")
    
    # Test issubclass
    print(f"Rectangle class is Shape: {issubclass(Rectangle, Shape)}")
    print(f"Circle class is Drawable: {issubclass(Circle, Drawable)}")
    
    # Register a class as implementing an ABC
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def draw(self):
            return f"Drawing point at ({self.x}, {self.y})"
        
        def move(self, x, y):
            self.x = x
            self.y = y
            return f"Moved point to ({self.x}, {self.y})"
    
    # Register Point as implementing Drawable
    Drawable.register(Point)
    
    point = Point(1, 2)
    print(f"Point is Drawable (after registration): {isinstance(point, Drawable)}")

# Test the implementation
if __name__ == "__main__":
    # Test abstract base class creation
    shapes = create_abstract_base_class()
    
    # Test polymorphism
    demonstrate_polymorphism(shapes)
    
    # Test alternative constructors
    string_shapes = test_alternative_constructors()
    
    # Test type checking
    test_type_checking()
    
    # Test specific methods
    print(f"\n=== Specific Shape Methods ===")
    rect = shapes[0]
    circle = shapes[1]
    triangle = shapes[2]
    
    if hasattr(rect, 'is_square'):
        print(f"Rectangle is square: {rect.is_square()}")
    
    if hasattr(circle, 'diameter'):
        print(f"Circle diameter: {circle.diameter():.2f}")
    
    if hasattr(triangle, 'is_equilateral'):
        print(f"Triangle is equilateral: {triangle.is_equilateral()}")
        print(f"Triangle is isosceles: {triangle.is_isosceles()}")
```

## Hints

- Use `from abc import ABC, abstractmethod` to create abstract classes
- Abstract methods must be implemented by all child classes
- Use `@property` with `@abstractmethod` for abstract properties
- Abstract classes cannot be instantiated directly
- Use `isinstance()` and `issubclass()` for type checking

## Test Cases

Your abstract base classes should:

- Prevent instantiation of abstract classes
- Force child classes to implement abstract methods
- Support polymorphic behavior across all implementations
- Work with isinstance() and issubclass() checks
- Allow concrete methods to use abstract methods

## Bonus Challenge

Create an abstract `Vehicle` class with abstract methods for `start()`, `stop()`, and `fuel_efficiency()`, then implement `Car`, `Motorcycle`, and `Bicycle` classes!
