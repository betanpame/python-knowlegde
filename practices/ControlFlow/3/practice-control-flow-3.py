# TODO: Implement basic if-else conditional functions
# Starter code for Control Flow Practice 3

def check_age_category(age):
    """
    Categorize age into Child, Teen, or Adult.
    
    Args:
        age (int): Age to categorize
        
    Returns:
        str: Age category
    """
    # Your implementation here
    # Child: 0-12, Teen: 13-17, Adult: 18+
    pass

def suggest_clothing(temperature):
    """
    Suggest clothing based on temperature.
    
    Args:
        temperature (int): Temperature in Celsius
        
    Returns:
        str: Clothing suggestion
    """
    # Your implementation here
    # Cold: <10, Cool: 10-20, Warm: 21-30, Hot: >30
    pass

def check_password_strength(password):
    """
    Check password strength based on length and characters.
    
    Args:
        password (str): Password to check
        
    Returns:
        str: Strength level (Weak, Medium, Strong)
    """
    # Your implementation here
    # Weak: <6 chars, Medium: 6-10 chars, Strong: >10 chars
    pass

def determine_grade(score):
    """
    Convert numeric score to letter grade.
    
    Args:
        score (int): Numeric score (0-100)
        
    Returns:
        str: Letter grade (A, B, C, D, F)
    """
    # Your implementation here
    # A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60
    pass

def check_number_type(number):
    """
    Determine if number is positive, negative, or zero.
    
    Args:
        number (float): Number to check
        
    Returns:
        str: Number type
    """
    # Your implementation here
    # Check if positive, negative, or zero
    pass

def is_weekend(day):
    """
    Check if given day is a weekend.
    
    Args:
        day (str): Day name (e.g., "Monday", "Saturday")
        
    Returns:
        bool: True if weekend, False otherwise
    """
    # Your implementation here
    # Weekend: Saturday, Sunday
    pass

def calculate_discount(price, is_member):
    """
    Calculate price with member discount.
    
    Args:
        price (float): Original price
        is_member (bool): Whether customer is a member
        
    Returns:
        float: Final price after discount
    """
    # Your implementation here
    # 10% discount for members
    pass

def check_login_status(username, password):
    """
    Validate login credentials.
    
    Args:
        username (str): Username
        password (str): Password
        
    Returns:
        bool: True if valid credentials, False otherwise
    """
    # Your implementation here
    # Simple validation: username="admin", password="password123"
    pass

def run_conditional_tests():
    """Run comprehensive conditional statement tests."""
    
    print("=== Basic If-Else Statement Practices ===")
    
    # Age category tests
    age_tests = [5, 15, 25, 0, 13, 18]
    print("Age Category Practices:")
    for age in age_tests:
        category = check_age_category(age)
        print(f"  Age {age}: {category}")
    print()
    
    # Temperature clothing tests
    temp_tests = [5, 15, 25, 35, -5]
    print("Clothing Suggestion Practices:")
    for temp in temp_tests:
        clothing = suggest_clothing(temp)
        print(f"  {temp}°C: {clothing}")
    print()
    
    # Password strength tests
    password_tests = ["123", "password", "very_secure_password123"]
    print("Password Strength Practices:")
    for pwd in password_tests:
        strength = check_password_strength(pwd)
        print(f"  '{pwd}': {strength}")
    print()
    
    # Grade tests
    score_tests = [95, 85, 75, 65, 45]
    print("Grade Determination Practices:")
    for score in score_tests:
        grade = determine_grade(score)
        print(f"  Score {score}: Grade {grade}")
    print()
    
    # Number type tests
    number_tests = [5, -3, 0, 10.5, -7.2]
    print("Number Type Practices:")
    for num in number_tests:
        num_type = check_number_type(num)
        print(f"  {num}: {num_type}")
    print()
    
    # Weekend tests
    day_tests = ["Monday", "Saturday", "Sunday", "Wednesday", "Friday"]
    print("Weekend Check Practices:")
    for day in day_tests:
        weekend = is_weekend(day)
        print(f"  {day}: {'Weekend' if weekend else 'Weekday'}")
    print()
    
    # Discount tests
    price_tests = [(100, True), (100, False), (50.5, True), (75.0, False)]
    print("Discount Calculation Practices:")
    for price, is_member in price_tests:
        final_price = calculate_discount(price, is_member)
        print(f"  Price ${price}, Member: {is_member} -> ${final_price}")
    print()
    
    # Login tests
    login_tests = [
        ("admin", "password123"),
        ("user", "wrong"),
        ("admin", "wrong"),
        ("wrong", "password123")
    ]
    print("Login Validation Practices:")
    for username, password in login_tests:
        valid = check_login_status(username, password)
        print(f"  {username}/{password}: {'Valid' if valid else 'Invalid'}")

# Practice your implementation
if __name__ == "__main__":
    run_conditional_tests()