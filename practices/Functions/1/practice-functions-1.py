# TODO: Implement functions with proper documentation and scope handling
# Starter code for Functions Practice 1

# Global variable for scope demonstration
global_counter = 0

def calculate_area(shape, **dimensions):
    """
    Calculate the area of different geometric shapes.
    
    Args:
        shape (str): The type of shape ('rectangle', 'circle', 'triangle')
        **dimensions: Keyword arguments for shape dimensions
            - rectangle: length, width
            - circle: radius
            - triangle: base, height
    
    Returns:
        float: The calculated area
        
    Raises:
        ValueError: If shape is not supported or dimensions are missing
    """
    # Your implementation here
    pass

def temperature_converter(temp, from_unit, to_unit):
    """
    Convert temperature between different units.
    
    Args:
        temp (float): Temperature value to convert
        from_unit (str): Source unit ('celsius', 'fahrenheit', 'kelvin')
        to_unit (str): Target unit ('celsius', 'fahrenheit', 'kelvin')
    
    Returns:
        float: Converted temperature value
        
    Raises:
        ValueError: If units are not supported
    """
    # Your implementation here
    pass

def scope_demonstration():
    """
    Demonstrate local vs global scope.
    
    Returns:
        dict: Results showing scope behavior
    """
    global global_counter
    local_counter = 0
    
    # Your implementation here
    # Modify both global and local variables
    # Return dictionary showing the differences
    pass

def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n (int): Position in Fibonacci sequence (1-indexed)
    
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is less than 1
    """
    # Your implementation here
    # Remember to include base cases
    pass

def input_validator(value, data_type, constraints=None):
    """
    Validate input value against type and optional constraints.
    
    Args:
        value: The value to validate
        data_type (type): Expected data type (int, str, float, etc.)
        constraints (dict, optional): Additional constraints
            - min_value: Minimum value for numbers
            - max_value: Maximum value for numbers
            - min_length: Minimum length for strings
            - max_length: Maximum length for strings
    
    Returns:
        bool: True if valid, False otherwise
    """
    if constraints is None:
        constraints = {}
    
    # Your implementation here
    pass

# Practice your implementations
if __name__ == "__main__":
    # Practice area calculation
    try:
        rect_area = calculate_area("rectangle", length=5, width=3)
        print(f"Rectangle area: {rect_area}")
        
        circle_area = calculate_area("circle", radius=3)
        print(f"Circle area: {circle_area}")
    except Exception as e:
        print(f"Area calculation error: {e}")
    
    # Practice temperature conversion
    try:
        celsius = temperature_converter(32, "fahrenheit", "celsius")
        print(f"32°F = {celsius}°C")
        
        kelvin = temperature_converter(0, "celsius", "kelvin")
        print(f"0°C = {kelvin}K")
    except Exception as e:
        print(f"Temperature conversion error: {e}")
    
    # Practice scope demonstration
    print(f"Global counter before: {global_counter}")
    scope_result = scope_demonstration()
    print(f"Scope demonstration: {scope_result}")
    print(f"Global counter after: {global_counter}")
    
    # Practice Fibonacci
    try:
        for i in range(1, 8):
            fib = fibonacci_recursive(i)
            print(f"Fibonacci({i}) = {fib}")
    except Exception as e:
        print(f"Fibonacci error: {e}")
    
    # Practice input validator
    print(f"Validate 5 as int: {input_validator(5, int)}")
    print(f"Validate 'hello' as str with length 3-10: {input_validator('hello', str, {'min_length': 3, 'max_length': 10})}")
    print(f"Validate 15 as int with max 10: {input_validator(15, int, {'max_value': 10})}")