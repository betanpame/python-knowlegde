# Basic If-Else Statements - Practice 3

**Difficulty:** ⭐ (Very Easy)

**Related Topics:** Conditional Statements, Boolean Logic, Decision Making

## Objectives

- Learn fundamental if-else statement structure
- Practice basic conditional logic
- Understand boolean expressions and comparisons

## Description

Master the most basic control flow mechanism in Python: if-else statements. These allow your programs to make decisions based on conditions.

## Examples

```python
age = 18
result = check_age_category(age)
print(result)  # "Adult"

temperature = 25
clothing = suggest_clothing(temperature)
print(clothing)  # "Light clothing"
```

## Your Tasks

1. **check_age_category(age)** - Return "Child", "Teen", or "Adult" based on age
2. **suggest_clothing(temperature)** - Suggest clothing based on temperature
3. **check_password_strength(password)** - Return "Weak", "Medium", or "Strong"
4. **determine_grade(score)** - Return letter grade (A, B, C, D, F) for score
5. **check_number_type(number)** - Return "Positive", "Negative", or "Zero"
6. **is_weekend(day)** - Return True if day is weekend, False otherwise
7. **calculate_discount(price, is_member)** - Apply discount if member
8. **check_login_status(username, password)** - Validate login credentials

## Hints

- Use `if`, `elif`, and `else` for multiple conditions
- Comparison operators: `<`, `>`, `<=`, `>=`, `==`, `!=`
- Logical operators: `and`, `or`, `not`
- Consider edge cases and invalid inputs
- Use clear and readable condition expressions

## Practice Cases

```python
# Age categories
test_cases = [
    (5, "Child"),     # Under 13
    (15, "Teen"),     # 13-17
    (25, "Adult"),    # 18+
    (0, "Child"),     # Edge case
    (13, "Teen")      # Boundary
]
```

## Bonus Challenges

- Add validation for negative ages
- Handle non-integer inputs gracefully
- Create more nuanced age categories
- Add special cases for very young or very old

Remember: If-else statements are the foundation of program logic!