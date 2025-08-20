# List Data Processing - Practice 13

**Difficulty:** ⭐⭐⭐ (Easy-Medium)

**Related Topics:** Data Processing, Filtering, Transformation

## Objectives

- Process structured data using lists
- Apply multiple filtering and transformation operations
- Handle real-world data scenarios

## Description

Work with lists containing structured data like records, scores, or measurements. Learn to extract insights and transform data for analysis.

## Examples

```python
# Student records: [name, age, grade]
students = [
    ["Alice", 20, 85],
    ["Bob", 19, 92],
    ["Charlie", 21, 78],
    ["Diana", 20, 96]
]

high_performers = filter_by_grade(students, 90)
# [["Bob", 19, 92], ["Diana", 20, 96]]

ages = extract_column(students, 1)
# [20, 19, 21, 20]
```

## Your Tasks

1. **filter_by_grade(student_list, min_grade)** - Filter students with grade >= min_grade
2. **extract_column(data_list, column_index)** - Extract specific column from 2D list
3. **sort_by_column(data_list, column_index)** - Sort records by specific column
4. **group_by_age(student_list)** - Group students by age
5. **calculate_grade_statistics(student_list)** - Calculate min, max, average grades
6. **find_top_performers(student_list, n)** - Find top n students by grade
7. **add_grade_categories(student_list)** - Add "A"/"B"/"C" based on grade
8. **merge_student_data(list1, list2)** - Combine two student datasets

## Hints

- Use list comprehensions for filtering and transformation
- Access nested list elements with double indexing
- Sort with `key=lambda x: x[column_index]`
- Use dictionaries for grouping data
- Calculate statistics using min(), max(), sum(), len()
- Consider edge cases like empty lists

## Practice Cases

```python
sample_data = [
    ["John", 18, 88],
    ["Jane", 19, 94],
    ["Mike", 18, 76],
    ["Sara", 20, 91]
]

# Expected results:
# filter_by_grade(sample_data, 90) -> [["Jane", 19, 94], ["Sara", 20, 91]]
# extract_column(sample_data, 2) -> [88, 94, 76, 91]
# sort_by_column(sample_data, 2) -> sorted by grades
```

Remember: Handle different data structures and edge cases gracefully!