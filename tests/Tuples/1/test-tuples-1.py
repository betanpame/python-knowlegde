# TODO: Implement tuple operations and comparisons
# Starter code for Tuples Test 1

def analyze_coordinates(coordinates):
    """
    Analyze a tuple of coordinates and return statistics.
    
    Args:
        coordinates (tuple): Tuple of x-coordinates
        
    Returns:
        dict: Analysis results
    """
    if not coordinates:
        return {'total_points': 0, 'unique_x_coords': [], 'most_common_x': None, 'average_x': 0}
    
    # Your implementation here
    # Use tuple methods like .count() and .index()
    pass

def count_occurrences(data_tuple, element):
    """Count occurrences of element in tuple."""
    # Your implementation here using tuple.count()
    pass

def find_element_position(data_tuple, element):
    """Find first position of element in tuple."""
    # Your implementation here using tuple.index()
    # Handle case where element doesn't exist
    pass

def demonstrate_immutability():
    """Demonstrate that tuples cannot be modified."""
    sample_tuple = (1, 2, 3, 4, 5)
    
    print("Original tuple:", sample_tuple)
    
    # Try to demonstrate immutability
    try:
        # Attempt to modify tuple (this should fail)
        # Your code here to show tuple immutability
        pass
    except TypeError as e:
        print(f"Cannot modify tuple: {e}")
    
    # Show how to create a new tuple instead
    # Your implementation here
    pass

def tuple_vs_list_comparison():
    """Compare tuple and list operations and performance."""
    import time
    
    # Create large dataset
    large_data = tuple(range(1000000))
    large_list = list(range(1000000))
    
    # Your implementation here
    # Compare access times, memory usage, etc.
    pass

# Test your implementations
if __name__ == "__main__":
    # Test coordinate analysis
    coords = (3, 4, 3, 7, 4, 3, 8, 3)
    print(f"Coordinate analysis: {analyze_coordinates(coords)}")
    
    # Test counting
    test_tuple = (1, 2, 3, 2, 4, 2, 5)
    print(f"Count of 2: {count_occurrences(test_tuple, 2)}")
    
    # Test position finding
    print(f"Position of 4: {find_element_position(test_tuple, 4)}")
    
    # Demonstrate immutability
    print("\nDemonstrating immutability:")
    demonstrate_immutability()
    
    # Compare tuple vs list
    print("\nTuple vs List comparison:")
    tuple_vs_list_comparison()
