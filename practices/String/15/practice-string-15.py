# TODO: Implement string formatting functions
# Starter code for String Practice 15

def format_with_f_string(name, age):
    """
    Format string using f-string syntax.
    
    Args:
        name (str): Person's name
        age (int): Person's age
        
    Returns:
        str: Formatted string
    """
    # Your implementation here using f-strings
    pass

def format_with_format_method(template, *args, **kwargs):
    """
    Format string using .format() method.
    
    Args:
        template (str): Template string with placeholders
        *args: Positional arguments
        **kwargs: Keyword arguments
        
    Returns:
        str: Formatted string
    """
    # Your implementation here using .format()
    pass

def format_number_with_precision(number, precision):
    """
    Format a number with specific decimal places.
    
    Args:
        number (float): Number to format
        precision (int): Number of decimal places
        
    Returns:
        str: Formatted number string
    """
    # Your implementation here
    pass

def create_table_row(columns, width=10):
    """
    Create a formatted table row with fixed column widths.
    
    Args:
        columns (list): List of column values
        width (int): Width of each column
        
    Returns:
        str: Formatted table row
    """
    # Your implementation here
    pass

def format_currency(amount, currency="USD"):
    """
    Format amount as currency.
    
    Args:
        amount (float): Amount to format
        currency (str): Currency code
        
    Returns:
        str: Formatted currency string
    """
    # Your implementation here
    pass

# Practice your implementation
if __name__ == "__main__":
    print("=== F-String Formatting ===")
    names_ages = [
        ("Alice", 25),
        ("Bob", 30),
        ("Charlie", 35)
    ]
    
    for name, age in names_ages:
        result = format_with_f_string(name, age)
        print(f"F-string result: {result}")
    
    print("\n=== Format Method ===")
    template_cases = [
        ("Hello {}, you are {} years old", ("Alice", 25), {}),
        ("Hello {name}, you are {age} years old", (), {"name": "Bob", "age": 30}),
        ("{0} + {1} = {2}", (5, 3, 8), {})
    ]
    
    for template, args, kwargs in template_cases:
        result = format_with_format_method(template, *args, **kwargs)
        print(f"Format method result: {result}")
    
    print("\n=== Number Precision ===")
    number_cases = [
        (3.14159, 2),
        (123.456789, 3),
        (10, 2),
        (1/3, 4)
    ]
    
    for number, precision in number_cases:
        result = format_number_with_precision(number, precision)
        print(f"{number} with {precision} decimals: {result}")
    
    print("\n=== Table Rows ===")
    table_data = [
        ["Name", "Age", "City"],
        ["Alice", "25", "New York"],
        ["Bob", "30", "London"],
        ["Charlie", "35", "Tokyo"]
    ]
    
    for row in table_data:
        result = create_table_row(row, 12)
        print(result)
    
    print("\n=== Currency Formatting ===")
    amounts = [1234.56, 99.99, 0.50, 1000000]
    
    for amount in amounts:
        usd = format_currency(amount, "USD")
        eur = format_currency(amount, "EUR")
        print(f"{amount} -> USD: {usd}, EUR: {eur}")