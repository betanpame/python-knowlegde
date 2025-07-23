# TODO: Implement loop control functions
# Starter code for Control Flow Test 2

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_first_prime(start, end):
    """Find the first prime number in the given range using break."""
    # Your implementation here
    # Use break to exit loop when first prime is found
    pass

def skip_negative_sum(numbers):
    """Sum only positive numbers using continue to skip negatives."""
    total = 0
    # Your implementation here
    # Use continue to skip negative numbers
    pass

def process_with_placeholder(data):
    """
    Process data with placeholder logic using pass.
    This simulates a function under development.
    """
    result = []
    
    for item in data:
        if isinstance(item, int):
            # TODO: Implement integer processing logic
            pass  # Placeholder for future implementation
        elif isinstance(item, str):
            # TODO: Implement string processing logic
            pass  # Placeholder for future implementation
        else:
            # TODO: Handle other data types
            pass  # Placeholder for future implementation
    
    # Your implementation here
    # Use pass appropriately for unimplemented sections
    pass

def controlled_input_loop():
    """
    Interactive loop with proper break conditions.
    Simulate getting user input and breaking on specific conditions.
    """
    # Simulate user inputs for testing
    simulated_inputs = ["hello", "world", "quit", "more", "exit"]
    input_index = 0
    
    collected_data = []
    
    while True:
        # Simulate user input
        if input_index >= len(simulated_inputs):
            break
        
        user_input = simulated_inputs[input_index]
        input_index += 1
        
        # Your implementation here
        # Use break for exit conditions
        # Use continue for invalid input
        pass
    
    return collected_data

def nested_loop_control(matrix, target):
    """
    Search for target value in 2D matrix with proper loop control.
    Return the position (row, col) of the target.
    """
    # Your implementation here
    # Use break/continue effectively in nested loops
    # Return position as tuple (row, col) or None if not found
    pass

# Test your implementations
if __name__ == "__main__":
    # Test prime finding
    print(f"First prime between 10-30: {find_first_prime(10, 30)}")
    print(f"First prime between 2-10: {find_first_prime(2, 10)}")
    
    # Test positive sum
    numbers = [-1, 2, -3, 4, -5, 6, 0, -7, 8]
    print(f"Sum of positive numbers: {skip_negative_sum(numbers)}")
    
    # Test placeholder processing
    test_data = [1, "hello", 2.5, "world", 3, None]
    result = process_with_placeholder(test_data)
    print(f"Processed data: {result}")
    
    # Test controlled input
    collected = controlled_input_loop()
    print(f"Collected data: {collected}")
    
    # Test nested loop control
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    position = nested_loop_control(matrix, 5)
    print(f"Position of 5: {position}")
    
    position = nested_loop_control(matrix, 10)
    print(f"Position of 10: {position}")
