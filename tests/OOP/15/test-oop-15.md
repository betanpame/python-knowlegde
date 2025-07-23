# Operator Overloading - Test 15

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Learn to overload operators like `+`, `-`, `*`, `==`, `<`, etc., to make your custom objects work with Python's built-in operators.

## Objectives

- Implement arithmetic operators (`+`, `-`, `*`, `/`)
- Implement comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Implement other useful operators (`[]`, `len()`, `in`)
- Understand operator precedence and return types

## Your Tasks

1. **create_vector_class()** - Create Vector class with arithmetic operators
2. **implement_comparison_operators()** - Add comparison functionality
3. **create_fraction_class()** - Create Fraction class with full operator support
4. **test_operator_precedence()** - Test operator combinations

## Example

```python
import math
from functools import total_ordering

class Vector:
    """2D Vector class with operator overloading."""
    
    def __init__(self, x, y):
        """Initialize vector with x and y components."""
        self.x = float(x)
        self.y = float(y)
    
    # Arithmetic operators
    def __add__(self, other):
        """Add two vectors: v1 + v2"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        return NotImplemented
    
    def __radd__(self, other):
        """Right addition: 5 + vector"""
        return self.__add__(other)
    
    def __iadd__(self, other):
        """In-place addition: v1 += v2"""
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, (int, float)):
            self.x += other
            self.y += other
        else:
            return NotImplemented
        return self
    
    def __sub__(self, other):
        """Subtract vectors: v1 - v2"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        return NotImplemented
    
    def __rsub__(self, other):
        """Right subtraction: 5 - vector"""
        if isinstance(other, (int, float)):
            return Vector(other - self.x, other - self.y)
        return NotImplemented
    
    def __mul__(self, other):
        """Multiply vector: v * scalar or v1 * v2 (dot product)"""
        if isinstance(other, Vector):
            # Dot product
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            # Scalar multiplication
            return Vector(self.x * other, self.y * other)
        return NotImplemented
    
    def __rmul__(self, other):
        """Right multiplication: 3 * vector"""
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """Divide vector by scalar: v / 2"""
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide vector by zero")
            return Vector(self.x / other, self.y / other)
        return NotImplemented
    
    def __floordiv__(self, other):
        """Floor divide vector by scalar: v // 2"""
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide vector by zero")
            return Vector(self.x // other, self.y // other)
        return NotImplemented
    
    # Comparison operators
    def __eq__(self, other):
        """Check equality: v1 == v2"""
        if isinstance(other, Vector):
            return abs(self.x - other.x) < 1e-10 and abs(self.y - other.y) < 1e-10
        return False
    
    def __ne__(self, other):
        """Check inequality: v1 != v2"""
        return not self.__eq__(other)
    
    def __lt__(self, other):
        """Compare magnitude: v1 < v2"""
        if isinstance(other, Vector):
            return self.magnitude() < other.magnitude()
        return NotImplemented
    
    def __le__(self, other):
        """Less than or equal: v1 <= v2"""
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        """Greater than: v1 > v2"""
        if isinstance(other, Vector):
            return self.magnitude() > other.magnitude()
        return NotImplemented
    
    def __ge__(self, other):
        """Greater than or equal: v1 >= v2"""
        return self.__gt__(other) or self.__eq__(other)
    
    # Unary operators
    def __neg__(self):
        """Negative vector: -v"""
        return Vector(-self.x, -self.y)
    
    def __pos__(self):
        """Positive vector: +v"""
        return Vector(self.x, self.y)
    
    def __abs__(self):
        """Absolute value (magnitude): abs(v)"""
        return self.magnitude()
    
    # Other magic methods
    def __bool__(self):
        """Boolean conversion: if vector:"""
        return self.x != 0 or self.y != 0
    
    def __round__(self, n=0):
        """Round vector components: round(v, 2)"""
        return Vector(round(self.x, n), round(self.y, n))
    
    def __getitem__(self, index):
        """Index access: v[0] = x, v[1] = y"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")
    
    def __setitem__(self, index, value):
        """Index assignment: v[0] = 5"""
        if index == 0:
            self.x = float(value)
        elif index == 1:
            self.y = float(value)
        else:
            raise IndexError("Vector index out of range")
    
    # Utility methods
    def magnitude(self):
        """Calculate vector magnitude."""
        return math.sqrt(self.x**2 + self.y**2)
    
    def normalize(self):
        """Return normalized vector."""
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0)
        return Vector(self.x / mag, self.y / mag)
    
    def angle(self):
        """Get vector angle in radians."""
        return math.atan2(self.y, self.x)
    
    def __str__(self):
        """String representation."""
        return f"Vector({self.x:.2f}, {self.y:.2f})"
    
    def __repr__(self):
        """Developer representation."""
        return f"Vector({self.x}, {self.y})"

@total_ordering  # Automatically generates comparison methods
class Fraction:
    """Fraction class with full operator overloading."""
    
    def __init__(self, numerator, denominator=1):
        """Initialize fraction."""
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        
        # Handle negative fractions
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        
        # Simplify fraction
        gcd = self._gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd
    
    def _gcd(self, a, b):
        """Calculate greatest common divisor."""
        while b:
            a, b = b, a % b
        return a
    
    # Arithmetic operators
    def __add__(self, other):
        """Add fractions: f1 + f2"""
        if isinstance(other, Fraction):
            num = self.numerator * other.denominator + other.numerator * self.denominator
            den = self.denominator * other.denominator
            return Fraction(num, den)
        elif isinstance(other, (int, float)):
            return self.__add__(Fraction(other))
        return NotImplemented
    
    def __radd__(self, other):
        """Right addition: 5 + fraction"""
        return self.__add__(other)
    
    def __sub__(self, other):
        """Subtract fractions: f1 - f2"""
        if isinstance(other, Fraction):
            num = self.numerator * other.denominator - other.numerator * self.denominator
            den = self.denominator * other.denominator
            return Fraction(num, den)
        elif isinstance(other, (int, float)):
            return self.__sub__(Fraction(other))
        return NotImplemented
    
    def __rsub__(self, other):
        """Right subtraction: 5 - fraction"""
        if isinstance(other, (int, float)):
            return Fraction(other).__sub__(self)
        return NotImplemented
    
    def __mul__(self, other):
        """Multiply fractions: f1 * f2"""
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator,
                          self.denominator * other.denominator)
        elif isinstance(other, (int, float)):
            return self.__mul__(Fraction(other))
        return NotImplemented
    
    def __rmul__(self, other):
        """Right multiplication: 3 * fraction"""
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """Divide fractions: f1 / f2"""
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Fraction(self.numerator * other.denominator,
                          self.denominator * other.numerator)
        elif isinstance(other, (int, float)):
            return self.__truediv__(Fraction(other))
        return NotImplemented
    
    def __rtruediv__(self, other):
        """Right division: 5 / fraction"""
        if isinstance(other, (int, float)):
            return Fraction(other).__truediv__(self)
        return NotImplemented
    
    def __pow__(self, other):
        """Power: fraction ** 2"""
        if isinstance(other, int):
            if other >= 0:
                return Fraction(self.numerator ** other, self.denominator ** other)
            else:
                return Fraction(self.denominator ** abs(other), self.numerator ** abs(other))
        return NotImplemented
    
    # Comparison operators (only need __eq__ and __lt__ with @total_ordering)
    def __eq__(self, other):
        """Check equality: f1 == f2"""
        if isinstance(other, Fraction):
            return (self.numerator == other.numerator and 
                   self.denominator == other.denominator)
        elif isinstance(other, (int, float)):
            return self.__eq__(Fraction(other))
        return False
    
    def __lt__(self, other):
        """Less than: f1 < f2"""
        if isinstance(other, Fraction):
            return (self.numerator * other.denominator < 
                   other.numerator * self.denominator)
        elif isinstance(other, (int, float)):
            return self.__lt__(Fraction(other))
        return NotImplemented
    
    # Unary operators
    def __neg__(self):
        """Negative fraction: -f"""
        return Fraction(-self.numerator, self.denominator)
    
    def __pos__(self):
        """Positive fraction: +f"""
        return Fraction(self.numerator, self.denominator)
    
    def __abs__(self):
        """Absolute value: abs(f)"""
        return Fraction(abs(self.numerator), self.denominator)
    
    # Conversion methods
    def __float__(self):
        """Convert to float: float(fraction)"""
        return self.numerator / self.denominator
    
    def __int__(self):
        """Convert to int: int(fraction)"""
        return self.numerator // self.denominator
    
    def __bool__(self):
        """Boolean conversion: if fraction:"""
        return self.numerator != 0
    
    # String representation
    def __str__(self):
        """String representation."""
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        """Developer representation."""
        return f"Fraction({self.numerator}, {self.denominator})"

# Example usage
def create_vector_class():
    """Demonstrate Vector operator overloading."""
    print("=== Vector Operator Overloading ===")
    
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    
    # Arithmetic operations
    print(f"\nArithmetic operations:")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"3 * v1 = {3 * v1}")
    print(f"v1 * v2 (dot product) = {v1 * v2}")
    print(f"v1 / 2 = {v1 / 2}")
    
    # Comparison operations
    print(f"\nComparison operations:")
    print(f"v1 == v2: {v1 == v2}")
    print(f"v1 > v2: {v1 > v2}")
    print(f"v1 < v2: {v1 < v2}")
    print(f"Magnitude v1: {abs(v1):.2f}")
    print(f"Magnitude v2: {abs(v2):.2f}")
    
    # Unary operations
    print(f"\nUnary operations:")
    print(f"-v1 = {-v1}")
    print(f"+v1 = {+v1}")
    print(f"round(v1, 1) = {round(v1, 1)}")
    
    # Index operations
    print(f"\nIndex operations:")
    print(f"v1[0] = {v1[0]}")
    print(f"v1[1] = {v1[1]}")
    v1[0] = 5
    print(f"After v1[0] = 5: {v1}")
    
    # In-place operations
    print(f"\nIn-place operations:")
    v3 = Vector(1, 1)
    print(f"v3 = {v3}")
    v3 += Vector(2, 3)
    print(f"After v3 += Vector(2, 3): {v3}")
    
    return v1, v2, v3

def create_fraction_class():
    """Demonstrate Fraction operator overloading."""
    print(f"\n=== Fraction Operator Overloading ===")
    
    f1 = Fraction(1, 2)  # 1/2
    f2 = Fraction(1, 3)  # 1/3
    f3 = Fraction(2, 4)  # 2/4 = 1/2 (simplified)
    
    print(f"f1 = {f1}")
    print(f"f2 = {f2}")
    print(f"f3 = {f3} (simplified)")
    
    # Arithmetic operations
    print(f"\nArithmetic operations:")
    print(f"f1 + f2 = {f1 + f2}")
    print(f"f1 - f2 = {f1 - f2}")
    print(f"f1 * f2 = {f1 * f2}")
    print(f"f1 / f2 = {f1 / f2}")
    print(f"f1 ** 2 = {f1 ** 2}")
    print(f"f1 + 1 = {f1 + 1}")
    print(f"2 * f1 = {2 * f1}")
    
    # Comparison operations
    print(f"\nComparison operations:")
    print(f"f1 == f3: {f1 == f3}")
    print(f"f1 > f2: {f1 > f2}")
    print(f"f1 < f2: {f1 < f2}")
    print(f"f1 >= f3: {f1 >= f3}")
    
    # Conversion operations
    print(f"\nConversion operations:")
    print(f"float(f1) = {float(f1)}")
    print(f"int(f1) = {int(f1)}")
    print(f"bool(f1) = {bool(f1)}")
    print(f"bool(Fraction(0)) = {bool(Fraction(0))}")
    
    # Unary operations
    print(f"\nUnary operations:")
    print(f"-f1 = {-f1}")
    print(f"abs(-f1) = {abs(-f1)}")
    
    return f1, f2, f3

def test_operator_precedence():
    """Test operator precedence and combinations."""
    print(f"\n=== Operator Precedence Tests ===")
    
    # Vector operations
    v1 = Vector(2, 3)
    v2 = Vector(1, 1)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 * 2 = {v1 + v2 * 2}")  # Should be v1 + (v2 * 2)
    print(f"(v1 + v2) * 2 = {(v1 + v2) * 2}")
    
    # Fraction operations
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)
    f3 = Fraction(1, 8)
    
    print(f"\nf1 = {f1}, f2 = {f2}, f3 = {f3}")
    print(f"f1 + f2 * f3 = {f1 + f2 * f3}")  # Should be f1 + (f2 * f3)
    print(f"(f1 + f2) * f3 = {(f1 + f2) * f3}")
    print(f"f1 ** 2 + f2 = {f1 ** 2 + f2}")  # Should be (f1 ** 2) + f2

# Test the implementation
if __name__ == "__main__":
    # Test Vector class
    vectors = create_vector_class()
    
    # Test Fraction class
    fractions = create_fraction_class()
    
    # Test operator precedence
    test_operator_precedence()
    
    # Final demonstration
    print(f"\n=== Complex Operations ===")
    
    # Complex vector operations
    v1, v2, v3 = vectors
    result_vector = (v1 + v2) * 0.5 - v3
    print(f"(v1 + v2) * 0.5 - v3 = {result_vector}")
    
    # Complex fraction operations
    f1, f2, f3 = fractions
    result_fraction = f1 ** 2 + f2 * f3 - Fraction(1, 4)
    print(f"f1² + f2*f3 - 1/4 = {result_fraction}")
    
    # Mixed operations
    print(f"Vector magnitude as fraction: {Fraction(int(abs(v1) * 100), 100)}")
```

## Hints

- Return `NotImplemented` when operation isn't supported
- Implement both `__op__` and `__rop__` for commutativity
- Use `@total_ordering` to generate all comparison methods
- Handle type checking carefully in operator methods
- Consider operator precedence when designing your class

## Test Cases

Your operator overloading should:

- Support arithmetic operations between objects and with numbers
- Implement comparison operators for sorting and equality
- Handle both left and right operations (`a + b` and `b + a`)
- Provide meaningful error messages for invalid operations
- Maintain mathematical properties (associativity, commutativity)

## Bonus Challenge

Create a `Matrix` class with full operator overloading for matrix operations, including multiplication, addition, and comparison!
