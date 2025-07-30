# TODO: Implement functions using list comprehensions
# Starter code for Lists Test 2

def filter_even_squares(numbers):
    """Return squares of even numbers only using list comprehension."""
    # Your implementation here
    return [x**2 for x in numbers if x%2 == 0]

 
    # Example: [x**2 for x in numbers if condition]
    pass

def extract_initials(names):
    """Extract first letter of each word in each name."""
    # Your implementation here
    return [[word[0] for word in name.split()] for name in names]
  
 

    # Hint: Use nested list comprehension and .split()
    pass

def flatten_matrix(matrix):
    """Flatten a 2D list into 1D using list comprehension."""
    # Your implementation here
    return [item for new_list in matrix for item in new_list]
    # Hint: [item for sublist in matrix for item in sublist]
    pass

def filter_long_words(sentences, min_length):
    """Get words longer than min_length from all sentences."""
    # Your implementation here
    return [word for sentence in sentences for word in sentence.split() if len(word) > min_length]
    # Hint: Combine list comprehension with string operations
    pass

def create_multiplication_table(n):
    """Create an n×n multiplication table using list comprehension."""
    # Your implementation here
    return [[(i + 1) * (j + 1) for j in range(n)] for i in range(n)]
    # Hint: Use nested list comprehension with range()
    pass

# Test your implementations
if __name__ == "__main__":
    # Test filter_even_squares
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"Even squares: {filter_even_squares(numbers)}")
    
    # Test extract_initials
    names = ["John Doe", "Jane Smith", "Bob Wilson"]
    print(f"Initials: {extract_initials(names)}")
    
    # Test flatten_matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Flattened: {flatten_matrix(matrix)}")
    
    # Test filter_long_words
    sentences = ["Hello world", "Python programming", "Short text"]
    print(f"Long words (>5 chars): {filter_long_words(sentences, 5)}")
    
    # Test multiplication table
    table = create_multiplication_table(3)
    print(f"3x3 multiplication table: {table}")
