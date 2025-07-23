# Tuple Data Structures - Test 12

**Difficulty:** ⭐⭐⭐ (Easy-Medium)

**Related Topics:** Structured Data, Records, Data Organization

## Objectives

- Use tuples for structured data representation
- Work with records and data collections
- Process tuple-based data efficiently

## Description

Learn to use tuples for representing structured data like records, coordinates, and complex data structures. Focus on real-world data organization scenarios.

## Examples

```python
# Student records as tuples
students = [
    ("Alice", 20, "Computer Science", 3.8),
    ("Bob", 19, "Mathematics", 3.6),
    ("Charlie", 21, "Physics", 3.9)
]

# Process student data
high_gpa = filter_students_by_gpa(students, 3.7)
by_major = group_students_by_major(students)
```

## Your Tasks

1. **create_student_record(name, age, major, gpa)** - Create student tuple
2. **extract_student_names(student_records)** - Get all student names
3. **filter_students_by_gpa(students, min_gpa)** - Filter by GPA threshold
4. **group_students_by_major(students)** - Group by academic major
5. **calculate_average_gpa(students)** - Calculate overall GPA average
6. **find_oldest_student(students)** - Find student with highest age
7. **sort_students_by_gpa(students)** - Sort by GPA (descending)
8. **create_student_summary(students)** - Generate summary statistics

## Hints

- Use tuple indexing to access specific fields
- List comprehensions work well with tuples
- Group data using dictionaries with tuples as values
- Consider creating constants for field indices
- Handle edge cases like empty data

## Test Cases

```python
sample_students = [
    ("Alice", 20, "CS", 3.8),
    ("Bob", 19, "Math", 3.6),
    ("Charlie", 21, "Physics", 3.9),
    ("Diana", 20, "CS", 3.7)
]

# Expected results:
# filter_students_by_gpa(sample_students, 3.7) -> Alice, Charlie, Diana
# group_students_by_major -> {"CS": 2, "Math": 1, "Physics": 1}
```

Remember: Tuples are perfect for representing fixed-structure records!
