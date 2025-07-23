# TODO: Implement built-in functions and memory-efficient operations
# Starter code for Built-in Functions Test 1

import sys
import os
from pathlib import Path

def builtin_functions_demo(data):
    """
    Demonstrate essential built-in functions with practical examples.
    
    Args:
        data (list): Input data for demonstration
    
    Returns:
        dict: Results of various built-in function operations
    """
    # Your implementation here
    # Include: len(), type(), range(), enumerate(), zip(), map(), filter(), sum(), max(), min()
    pass

def memory_efficient_file_reader(filename, chunk_size=8192):
    """
    Read large files in chunks to save memory.
    
    Args:
        filename (str): Path to the file to read
        chunk_size (int): Size of each chunk to read
    
    Yields:
        str: File content in chunks
    """
    # Your implementation here
    # Use generator to yield chunks instead of loading entire file
    pass

def count_uppercase_in_large_file(filepath, chunk_size=8192):
    """
    Count uppercase letters in a large file efficiently
    
    Args:
        filepath (str): Path to the text file
        chunk_size (int): Size of each chunk to process
    
    Returns:
        int: Total count of uppercase letters
    """
    # Your implementation here
    # Process file in chunks to handle large files
    pass

def generator_vs_list_comparison():
    """
    Compare memory usage between generators and lists.
    
    Returns:
        dict: Memory usage comparison results
    """
    # Your implementation here
    # Create equivalent generator and list
    # Compare memory usage using sys.getsizeof()
    pass

def iterator_protocol_demo():
    """
    Demonstrate custom iterator implementation.
    
    Returns:
        dict: Results of custom iterator operations
    """
    
    class NumberSquares:
        """Custom iterator that yields squares of numbers."""
        
        def __init__(self, max_num):
            # Your implementation here
            pass
        
        def __iter__(self):
            # Your implementation here
            pass
        
        def __next__(self):
            # Your implementation here
            # Raise StopIteration when done
            pass
    
    # Test the custom iterator
    # Your implementation here
    pass

def create_sample_file_for_testing():
    """Create a sample file for testing file operations."""
    sample_content = """This Is A Sample Text File For Testing.
It Contains UPPERCASE and lowercase Letters.
The Purpose Is To Test File Reading Capabilities.
We Want To Count UPPERCASE Letters Efficiently.
This File Should Have Multiple Lines With Various Cases.
ANOTHER LINE WITH MORE UPPERCASE LETTERS.
Some lines have Mixed CaSe Letters.
Final line with ENDING UPPERCASE WORDS."""
    
    with open("sample_test_file.txt", "w", encoding="utf-8") as f:
        f.write(sample_content)
    
    return "sample_test_file.txt"

# Test your implementations
if __name__ == "__main__":
    # Test built-in functions
    print("=== Built-in Functions Demo ===")
    try:
        test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        builtin_results = builtin_functions_demo(test_data)
        print(f"Built-in functions: {builtin_results}")
    except Exception as e:
        print(f"Built-in functions error: {e}")
    
    # Create sample file and test file operations
    print("\n=== Memory-Efficient File Operations ===")
    try:
        sample_file = create_sample_file_for_testing()
        
        # Test chunked file reading
        print("Reading file in chunks:")
        chunk_count = 0
        for chunk in memory_efficient_file_reader(sample_file, chunk_size=50):
            chunk_count += 1
            print(f"Chunk {chunk_count}: {len(chunk)} characters")
        
        # Test uppercase counting
        uppercase_count = count_uppercase_in_large_file(sample_file)
        print(f"Total uppercase letters: {uppercase_count}")
        
        # Clean up
        os.remove(sample_file)
    except Exception as e:
        print(f"File operations error: {e}")
    
    # Test generator vs list comparison
    print("\n=== Generator vs List Memory Comparison ===")
    try:
        memory_comparison = generator_vs_list_comparison()
        print(f"Memory comparison: {memory_comparison}")
    except Exception as e:
        print(f"Memory comparison error: {e}")
    
    # Test custom iterator
    print("\n=== Custom Iterator Demo ===")
    try:
        iterator_results = iterator_protocol_demo()
        print(f"Iterator results: {iterator_results}")
    except Exception as e:
        print(f"Iterator demo error: {e}")
    
    # Additional built-in functions examples
    print("\n=== Additional Built-in Function Examples ===")
    try:
        # Example with different data types
        mixed_data = [1, "hello", [1, 2], {"key": "value"}, 42]
        
        print(f"Length of mixed_data: {len(mixed_data)}")
        print(f"Types in mixed_data: {[type(item).__name__ for item in mixed_data]}")
        
        # Example with enumerate and zip
        names = ["Alice", "Bob", "Charlie"]
        scores = [85, 92, 78]
        
        print("Enumerated names:")
        for i, name in enumerate(names):
            print(f"  {i}: {name}")
        
        print("Zipped names and scores:")
        for name, score in zip(names, scores):
            print(f"  {name}: {score}")
        
    except Exception as e:
        print(f"Additional examples error: {e}")
