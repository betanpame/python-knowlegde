# TODO: Implement functions using *args and **kwargs
# Starter code for Functions Practice 2

def flexible_calculator(operation, *args, **kwargs):
    """
    Flexible calculator that works with variable number of arguments.
    
    Args:
        operation (str): Operation to perform ('add', 'multiply', 'average', etc.)
        *args: Variable number of numeric arguments
        **kwargs: Additional options like 'precision', 'round_result'
    
    Returns:
        float: Result of the calculation
    """
    # Your implementation here
    # Handle different operations and options
    pass

def log_function_call(func, *args, **kwargs):
    """
    Log a function call and execute it with given arguments.
    
    Args:
        func: Function to call
        *args: Positional arguments for the function
        **kwargs: Keyword arguments for the function
    
    Returns:
        tuple: (result, log_info)
    """
    # Your implementation here
    # Log the function call details and execute the function
    pass

def merge_configurations(*config_dicts, **override_options):
    """
    Merge multiple configuration dictionaries with override options.
    
    Args:
        *config_dicts: Multiple configuration dictionaries
        **override_options: Override options that take precedence
    
    Returns:
        dict: Merged configuration
    """
    # Your implementation here
    # Merge configs in order, with later ones overriding earlier ones
    # override_options should have highest precedence
    pass

def create_formatted_string(template, *values, **formatting_options):
    """
    Create formatted string with variable values and formatting options.
    
    Args:
        template (str): String template with placeholders
        *values: Values to insert into template
        **formatting_options: Formatting options like 'uppercase', 'padding', etc.
    
    Returns:
        str: Formatted string
    """
    # Your implementation here
    # Apply formatting options and insert values
    pass

def statistical_analysis(*datasets, **analysis_options):
    """
    Perform statistical analysis on multiple datasets.
    
    Args:
        *datasets: Multiple datasets (lists of numbers)
        **analysis_options: Analysis options like 'include_median', 'precision', etc.
    
    Returns:
        dict: Statistical analysis results for all datasets
    """
    # Your implementation here
    # Calculate statistics for each dataset based on options
    pass

# Helper function for testing log_function_call
def sample_function(a, b, c=3, d=4):
    """Sample function for testing log_function_call."""
    return a + b + c + d

# Practice your implementations
if __name__ == "__main__":
    # Practice flexible calculator
    print("=== Flexible Calculator ===")
    try:
        result1 = flexible_calculator("add", 1, 2, 3, 4, 5)
        print(f"Add 1,2,3,4,5: {result1}")
        
        result2 = flexible_calculator("multiply", 2, 3, 4, precision=2)
        print(f"Multiply 2,3,4: {result2}")
        
        result3 = flexible_calculator("average", 10, 20, 30, round_result=True)
        print(f"Average 10,20,30: {result3}")
    except Exception as e:
        print(f"Calculator error: {e}")
    
    # Practice function call logger
    print("\n=== Function Call Logger ===")
    try:
        result, log_info = log_function_call(sample_function, 1, 2, c=5, d=6)
        print(f"Function result: {result}")
        print(f"Log info: {log_info}")
    except Exception as e:
        print(f"Logger error: {e}")
    
    # Practice configuration merger
    print("\n=== Configuration Merger ===")
    try:
        config1 = {"host": "localhost", "port": 5432, "database": "test"}
        config2 = {"port": 3306, "username": "user"}
        config3 = {"password": "pass", "ssl": True}
        
        merged = merge_configurations(config1, config2, config3, 
                                    timeout=30, debug=True)
        print(f"Merged config: {merged}")
    except Exception as e:
        print(f"Config merger error: {e}")
    
    # Practice formatted string creator
    print("\n=== Formatted String Creator ===")
    try:
        template = "Hello {}, you have {} messages"
        result = create_formatted_string(template, "Alice", 5, 
                                       uppercase=True, padding=2)
        print(f"Formatted string: '{result}'")
    except Exception as e:
        print(f"String formatter error: {e}")
    
    # Practice statistical analysis
    print("\n=== Statistical Analysis ===")
    try:
        dataset1 = [1, 2, 3, 4, 5]
        dataset2 = [10, 20, 30, 40, 50]
        dataset3 = [100, 200, 300]
        
        stats = statistical_analysis(dataset1, dataset2, dataset3,
                                   include_median=True, 
                                   include_std=True,
                                   precision=2)
        print(f"Statistical analysis: {stats}")
    except Exception as e:
        print(f"Statistical analysis error: {e}")