# TODO: Implement data processing functions for lists
# Starter code for Lists Practice 13

def filter_by_grade(student_list, min_grade):
    """
    Filter students with grade >= min_grade.
    
    Args:
        student_list (list): List of [name, age, grade] records
        min_grade (int): Minimum grade threshold
        
    Returns:
        list: Filtered list of students
    """
    # Your implementation here
    # Use list comprehension or loop to filter
    pass

def extract_column(data_list, column_index):
    """
    Extract specific column from 2D list.
    
    Args:
        data_list (list): 2D list of records
        column_index (int): Index of column to extract
        
    Returns:
        list: Values from specified column
    """
    # Your implementation here
    # Access each row's column_index element
    pass

def sort_by_column(data_list, column_index):
    """
    Sort records by specific column.
    
    Args:
        data_list (list): 2D list of records
        column_index (int): Index of column to sort by
        
    Returns:
        list: Sorted list of records
    """
    # Your implementation here
    # Use sorted() with key parameter
    pass

def group_by_age(student_list):
    """
    Group students by age.
    
    Args:
        student_list (list): List of [name, age, grade] records
        
    Returns:
        dict: Dictionary with age as key, list of students as value
    """
    # Your implementation here
    # Create dictionary and group by age
    pass

def calculate_grade_statistics(student_list):
    """
    Calculate min, max, average grades.
    
    Args:
        student_list (list): List of [name, age, grade] records
        
    Returns:
        dict: Statistics including min, max, average
    """
    # Your implementation here
    # Extract grades and calculate statistics
    pass

def find_top_performers(student_list, n):
    """
    Find top n students by grade.
    
    Args:
        student_list (list): List of [name, age, grade] records
        n (int): Number of top performers to return
        
    Returns:
        list: Top n students sorted by grade (descending)
    """
    # Your implementation here
    # Sort by grade descending and take first n
    pass

def add_grade_categories(student_list):
    """
    Add grade categories: A (90+), B (80-89), C (70-79), F (<70).
    
    Args:
        student_list (list): List of [name, age, grade] records
        
    Returns:
        list: Records with added category [name, age, grade, category]
    """
    # Your implementation here
    # Add category based on grade ranges
    pass

def merge_student_data(list1, list2):
    """
    Combine two student datasets, removing duplicates by name.
    
    Args:
        list1 (list): First student dataset
        list2 (list): Second student dataset
        
    Returns:
        list: Combined dataset without duplicate names
    """
    # Your implementation here
    # Combine lists and handle duplicates
    pass

def run_data_processing_tests():
    """Run comprehensive data processing tests."""
    
    # Sample student data
    students = [
        ["Alice", 20, 85],
        ["Bob", 19, 92],
        ["Charlie", 21, 78],
        ["Diana", 20, 96],
        ["Eve", 19, 73],
        ["Frank", 22, 88]
    ]
    
    print("=== List Data Processing Practices ===")
    print(f"Original data: {len(students)} students")
    for student in students:
        print(f"  {student}")
    print()
    
    # Practice filtering by grade
    high_performers = filter_by_grade(students, 90)
    print(f"Students with grade >= 90: {high_performers}")
    print()
    
    # Practice column extraction
    names = extract_column(students, 0)
    ages = extract_column(students, 1)
    grades = extract_column(students, 2)
    print(f"Names: {names}")
    print(f"Ages: {ages}")
    print(f"Grades: {grades}")
    print()
    
    # Practice sorting by different columns
    sorted_by_name = sort_by_column(students, 0)
    sorted_by_grade = sort_by_column(students, 2)
    print("Sorted by name:")
    for student in sorted_by_name[:3]:  # Show first 3
        print(f"  {student}")
    
    print("Sorted by grade:")
    for student in sorted_by_grade[:3]:  # Show first 3
        print(f"  {student}")
    print()
    
    # Practice grouping by age
    age_groups = group_by_age(students)
    print("Students grouped by age:")
    for age, group in age_groups.items():
        print(f"  Age {age}: {[s[0] for s in group]}")
    print()
    
    # Practice grade statistics
    stats = calculate_grade_statistics(students)
    print(f"Grade statistics: {stats}")
    print()
    
    # Practice top performers
    top_3 = find_top_performers(students, 3)
    print("Top 3 performers:")
    for student in top_3:
        print(f"  {student}")
    print()
    
    # Practice grade categories
    categorized = add_grade_categories(students)
    print("Students with grade categories:")
    for student in categorized:
        print(f"  {student}")
    print()
    
    # Practice merging datasets
    new_students = [
        ["Grace", 20, 89],
        ["Alice", 20, 87],  # Duplicate name
        ["Henry", 21, 94]
    ]
    
    merged = merge_student_data(students, new_students)
    print(f"Merged dataset: {len(merged)} students")
    print("Sample merged data:")
    for student in merged[-3:]:  # Show last 3
        print(f"  {student}")

# Practice your implementation
if __name__ == "__main__":
    run_data_processing_tests()