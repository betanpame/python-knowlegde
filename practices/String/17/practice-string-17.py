# TODO: Implement string formatting and template functions
# Starter code for String Practice 17

def format_template(template, **kwargs):
    """
    Replace placeholders in template with provided values.
    
    Args:
        template (str): Template string with {placeholder} format
        **kwargs: Values to substitute
        
    Returns:
        str: Formatted string
    """
    # Your implementation here
    # Use .format() or f-string techniques
    pass

def generate_sales_report(data):
    """
    Create a formatted sales report from data.
    
    Args:
        data (dict): Sales data with 'sales', 'target', 'month'
        
    Returns:
        str: Formatted report
    """
    # Your implementation here
    # Calculate achievement percentage and format nicely
    pass

def format_table(headers, rows):
    """
    Generate ASCII table from headers and rows.
    
    Args:
        headers (list): Column headers
        rows (list): List of row data
        
    Returns:
        str: Formatted table
    """
    # Your implementation here
    # Calculate column widths and create aligned table
    pass

def create_progress_bar(current, total, width=20):
    """
    Create a text-based progress bar.
    
    Args:
        current (int): Current progress value
        total (int): Total/maximum value
        width (int): Width of progress bar
        
    Returns:
        str: Progress bar string
    """
    # Your implementation here
    # Calculate fill ratio and create bar with █ and spaces
    pass

def format_currency(amount, currency="USD"):
    """
    Format amount as currency with proper symbol and separators.
    
    Args:
        amount (float): Amount to format
        currency (str): Currency code (USD, EUR, etc.)
        
    Returns:
        str: Formatted currency string
    """
    # Your implementation here
    # Add currency symbol and thousand separators
    pass

def generate_invoice(items, customer):
    """
    Create formatted invoice text from items and customer data.
    
    Args:
        items (list): List of (name, quantity, price) tuples
        customer (dict): Customer information
        
    Returns:
        str: Formatted invoice
    """
    # Your implementation here
    # Create professional invoice layout
    pass

def format_multiline_text(text, width=80):
    """
    Wrap text to specified width while preserving words.
    
    Args:
        text (str): Text to wrap
        width (int): Maximum line width
        
    Returns:
        str: Wrapped text
    """
    # Your implementation here
    # Break text into lines without splitting words
    pass

def create_ascii_banner(text):
    """
    Generate decorative ASCII banner for text.
    
    Args:
        text (str): Text to make into banner
        
    Returns:
        str: ASCII banner
    """
    # Your implementation here
    # Create decorative border around text
    pass

def run_formatting_tests():
    """Run comprehensive string formatting tests."""
    
    print("=== String Formatting Practices ===")
    
    # Template formatting test
    template = "Hello {name}, you have {count} messages"
    result = format_template(template, name="Alice", count=5)
    print(f"Template: '{result}'")
    print(f"Expected: 'Hello Alice, you have 5 messages'")
    print()
    
    # Sales report test
    sales_data = {"sales": 15000, "target": 20000, "month": "December"}
    report = generate_sales_report(sales_data)
    print("Sales Report:")
    print(report)
    print()
    
    # Table formatting test
    headers = ["Name", "Age", "City"]
    rows = [["Alice", "25", "Boston"], ["Bob", "30", "Seattle"]]
    table = format_table(headers, rows)
    print("Table Format:")
    print(table)
    print()
    
    # Progress bar test
    progress_tests = [(25, 100), (50, 100), (75, 100), (100, 100)]
    print("Progress Bars:")
    for current, total in progress_tests:
        bar = create_progress_bar(current, total, 20)
        print(f"{current:3d}%: {bar}")
    print()
    
    # Currency formatting test
    currency_tests = [
        (1234.56, "USD"),
        (1000.00, "EUR"), 
        (999.99, "GBP"),
        (50.5, "JPY")
    ]
    print("Currency Formatting:")
    for amount, currency in currency_tests:
        formatted = format_currency(amount, currency)
        print(f"{amount} {currency} -> {formatted}")
    print()
    
    # Invoice test
    invoice_items = [
        ("Widget A", 2, 25.99),
        ("Widget B", 1, 45.50),
        ("Service Fee", 1, 10.00)
    ]
    customer_info = {
        "name": "John Doe",
        "address": "123 Main St",
        "city": "Anytown, ST 12345"
    }
    invoice = generate_invoice(invoice_items, customer_info)
    print("Invoice:")
    print(invoice)
    print()
    
    # Text wrapping test
    long_text = "This is a very long line of text that should be wrapped to multiple lines when it exceeds the specified width limit."
    wrapped = format_multiline_text(long_text, 40)
    print("Wrapped Text (width=40):")
    print(wrapped)
    print()
    
    # ASCII banner test
    banner = create_ascii_banner("PYTHON")
    print("ASCII Banner:")
    print(banner)

# Practice your implementation
if __name__ == "__main__":
    run_formatting_tests()