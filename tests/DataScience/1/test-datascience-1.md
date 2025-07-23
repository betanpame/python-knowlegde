# Basic Data Types and NumPy Arrays - Test 1

**Difficulty:** ⭐ (Very Easy)

## Description

Learn the fundamentals of data science in Python by working with basic data types and NumPy arrays. Understand how to create, manipulate, and perform basic operations on arrays.

## Objectives

- Create and manipulate NumPy arrays
- Understand array indexing and slicing
- Perform basic mathematical operations on arrays
- Convert between Python lists and NumPy arrays
- Explore array attributes and properties

## Your Tasks

1. **create_basic_arrays()** - Create arrays from lists and ranges
2. **array_indexing_slicing()** - Practice indexing and slicing operations
3. **basic_math_operations()** - Perform arithmetic operations on arrays
4. **array_properties()** - Explore shape, size, and data types
5. **array_reshaping()** - Reshape and resize arrays

## Example

```python
import numpy as np

def create_basic_arrays():
    """Create different types of NumPy arrays."""
    
    # Create array from list
    list_array = np.array([1, 2, 3, 4, 5])
    print(f"Array from list: {list_array}")
    
    # Create array with zeros
    zeros_array = np.zeros(5)
    print(f"Zeros array: {zeros_array}")
    
    # Create array with ones
    ones_array = np.ones(3)
    print(f"Ones array: {ones_array}")
    
    # Create array with range
    range_array = np.arange(0, 10, 2)
    print(f"Range array: {range_array}")
    
    # Create array with evenly spaced values
    linspace_array = np.linspace(0, 1, 5)
    print(f"Linspace array: {linspace_array}")
    
    return list_array, zeros_array, ones_array, range_array, linspace_array

def array_indexing_slicing():
    """Practice array indexing and slicing."""
    
    # Create sample array
    arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print(f"Original array: {arr}")
    
    # Single element indexing
    first_element = arr[0]
    last_element = arr[-1]
    print(f"First element: {first_element}")
    print(f"Last element: {last_element}")
    
    # Slicing
    first_three = arr[:3]
    last_three = arr[-3:]
    middle_elements = arr[2:5]
    every_second = arr[::2]
    
    print(f"First three: {first_three}")
    print(f"Last three: {last_three}")
    print(f"Middle elements: {middle_elements}")
    print(f"Every second: {every_second}")
    
    return first_element, last_element, first_three, last_three

def basic_math_operations():
    """Perform basic mathematical operations on arrays."""
    
    # Create sample arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([10, 20, 30, 40, 50])
    
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    
    # Element-wise operations
    addition = arr1 + arr2
    subtraction = arr2 - arr1
    multiplication = arr1 * arr2
    division = arr2 / arr1
    
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")
    
    # Operations with scalars
    scalar_add = arr1 + 10
    scalar_multiply = arr1 * 3
    
    print(f"Scalar addition: {scalar_add}")
    print(f"Scalar multiplication: {scalar_multiply}")
    
    # Mathematical functions
    sqrt_arr = np.sqrt(arr1)
    square_arr = np.square(arr1)
    
    print(f"Square root: {sqrt_arr}")
    print(f"Square: {square_arr}")
    
    return addition, subtraction, multiplication, division

def array_properties():
    """Explore array attributes and properties."""
    
    # Create 2D array
    arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"2D Array:\n{arr_2d}")
    
    # Array properties
    shape = arr_2d.shape
    size = arr_2d.size
    ndim = arr_2d.ndim
    dtype = arr_2d.dtype
    
    print(f"Shape: {shape}")
    print(f"Size: {size}")
    print(f"Dimensions: {ndim}")
    print(f"Data type: {dtype}")
    
    # Different data types
    int_array = np.array([1, 2, 3], dtype=int)
    float_array = np.array([1.0, 2.0, 3.0], dtype=float)
    bool_array = np.array([True, False, True], dtype=bool)
    
    print(f"Integer array: {int_array} (dtype: {int_array.dtype})")
    print(f"Float array: {float_array} (dtype: {float_array.dtype})")
    print(f"Boolean array: {bool_array} (dtype: {bool_array.dtype})")
    
    # Array statistics
    arr_1d = np.array([1, 5, 3, 9, 2, 8, 4])
    
    minimum = np.min(arr_1d)
    maximum = np.max(arr_1d)
    mean = np.mean(arr_1d)
    sum_total = np.sum(arr_1d)
    
    print(f"Array: {arr_1d}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Mean: {mean}")
    print(f"Sum: {sum_total}")
    
    return shape, size, ndim, dtype

def array_reshaping():
    """Practice reshaping and resizing arrays."""
    
    # Create 1D array
    arr_1d = np.arange(12)
    print(f"Original 1D array: {arr_1d}")
    
    # Reshape to 2D
    arr_2d = arr_1d.reshape(3, 4)
    print(f"Reshaped to 3x4:\n{arr_2d}")
    
    # Reshape to 3D
    arr_3d = arr_1d.reshape(2, 2, 3)
    print(f"Reshaped to 2x2x3:\n{arr_3d}")
    
    # Flatten back to 1D
    flattened = arr_2d.flatten()
    print(f"Flattened: {flattened}")
    
    # Transpose
    transposed = arr_2d.T
    print(f"Transposed:\n{transposed}")
    
    # Create array with specific shape
    shaped_array = np.full((2, 3), 7)
    print(f"2x3 array filled with 7s:\n{shaped_array}")
    
    return arr_2d, arr_3d, flattened, transposed

# Test all functions
if __name__ == "__main__":
    print("=== Basic Data Types and NumPy Arrays ===")
    
    print("\n1. Creating Basic Arrays:")
    arrays = create_basic_arrays()
    
    print("\n2. Array Indexing and Slicing:")
    indexed_elements = array_indexing_slicing()
    
    print("\n3. Basic Math Operations:")
    math_results = basic_math_operations()
    
    print("\n4. Array Properties:")
    properties = array_properties()
    
    print("\n5. Array Reshaping:")
    reshaped_arrays = array_reshaping()
    
    print("\n=== NumPy Basics Complete! ===")
```

## Hints

- Use `np.array()` to create arrays from Python lists
- Array operations are element-wise by default
- Use `.shape` to get array dimensions
- Use `reshape()` to change array dimensions while preserving data
- NumPy arrays are more efficient than Python lists for numerical operations

## Test Cases

Your functions should:

- Create arrays of different types (zeros, ones, ranges)
- Access array elements using positive and negative indices
- Perform arithmetic operations element-wise
- Return correct array properties (shape, size, dtype)
- Successfully reshape arrays without losing data

## Bonus Challenge

Create a function that generates a random 3D array and calculates statistics along different axes!
