# Data Transformation Functions - Practice 2

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Master Python's built-in data transformation functions including `map()`, `filter()`, `reduce()`, `sorted()`, and `reversed()`. Learn to transform and manipulate data efficiently using functional programming concepts.

## Objectives

- Use `map()` for applying functions to iterables
- Filter data with `filter()` function
- Implement reduction operations with `functools.reduce()`
- Sort data with `sorted()` and custom key functions
- Reverse sequences with `reversed()`
- Understand functional programming principles

## Your Tasks

1. **data_mapper()** - Transform data using map() function
2. **data_filter()** - Filter data based on conditions
3. **data_reducer()** - Aggregate data using reduce()
4. **advanced_sorting()** - Sort complex data structures
5. **sequence_reverser()** - Reverse different sequence types

## Example

```python
from functools import reduce
import operator
from typing import List, Dict, Any, Callable, Union
import re
from datetime import datetime

def data_mapper():
    """Demonstrate map() function with various transformations."""
    print("=== Data Mapping Operations ===")
    
    # Basic mapping - square numbers
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print(f"Original: {numbers}")
    print(f"Squared: {squared}")
    
    # Map with built-in functions
    strings = ["hello", "world", "python", "programming"]
    
    # Convert to uppercase
    uppercase = list(map(str.upper, strings))
    print(f"\\nUppercase: {uppercase}")
    
    # Get string lengths
    lengths = list(map(len, strings))
    print(f"Lengths: {lengths}")
    
    # Multiple iterables with map
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    cities = ["New York", "London", "Tokyo"]
    
    # Combine multiple lists
    combined = list(map(lambda n, a, c: f"{n} ({a}) from {c}", names, ages, cities))
    print(f"\\nCombined data: {combined}")
    
    # Map with custom functions
    def format_currency(amount):
        """Format number as currency."""
        return f"${amount:,.2f}"
    
    amounts = [1234.56, 9876.54, 555.55, 12345.67]
    formatted = list(map(format_currency, amounts))
    print(f"\\nFormatted currency: {formatted}")
    
    # Map with type conversion
    string_numbers = ["10", "20", "30", "40"]
    integers = list(map(int, string_numbers))
    print(f"\\nString to int: {string_numbers} -> {integers}")
    
    # Map with complex transformations
    users = [
        {"name": "John", "email": "john@email.com"},
        {"name": "Jane", "email": "jane@email.com"},
        {"name": "Bob", "email": "bob@email.com"}
    ]
    
    # Extract emails
    emails = list(map(lambda user: user["email"], users))
    print(f"\\nExtracted emails: {emails}")
    
    # Transform dictionaries
    user_summaries = list(map(
        lambda user: f"{user['name']} <{user['email']}>", 
        users
    ))
    print(f"User summaries: {user_summaries}")
    
    # Mathematical operations on multiple lists
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50]
    
    # Add corresponding elements
    sums = list(map(operator.add, list1, list2))
    print(f"\\nElement-wise addition: {list1} + {list2} = {sums}")
    
    # Multiply corresponding elements
    products = list(map(operator.mul, list1, list2))
    print(f"Element-wise multiplication: {list1} * {list2} = {products}")
    
    return {
        "squared": squared,
        "uppercase": uppercase,
        "lengths": lengths,
        "combined": combined,
        "formatted": formatted,
        "integers": integers,
        "emails": emails,
        "sums": sums,
        "products": products
    }

def data_filter():
    """Demonstrate filter() function with various conditions."""
    print("\\n=== Data Filtering Operations ===")
    
    # Basic filtering - even numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Original: {numbers}")
    print(f"Even numbers: {even_numbers}")
    
    # Filter strings by length
    words = ["cat", "elephant", "dog", "hippopotamus", "ant", "whale"]
    long_words = list(filter(lambda word: len(word) > 5, words))
    print(f"\\nWords longer than 5 chars: {long_words}")
    
    # Filter with built-in functions
    mixed_data = [0, 1, "", "hello", [], [1, 2], None, False, True, 42]
    truthy_values = list(filter(bool, mixed_data))
    print(f"\\nTruthy values: {truthy_values}")
    
    # Filter numbers by range
    scores = [45, 78, 92, 65, 88, 34, 99, 56, 73, 81]
    passing_scores = list(filter(lambda x: x >= 70, scores))
    high_scores = list(filter(lambda x: x >= 90, scores))
    print(f"\\nPassing scores (>=70): {passing_scores}")
    print(f"High scores (>=90): {high_scores}")
    
    # Filter dictionaries
    students = [
        {"name": "Alice", "grade": 85, "subject": "Math"},
        {"name": "Bob", "grade": 92, "subject": "Science"},
        {"name": "Charlie", "grade": 78, "subject": "Math"},
        {"name": "Diana", "grade": 95, "subject": "Science"},
        {"name": "Eve", "grade": 67, "subject": "Math"}
    ]
    
    # Filter by grade
    honor_students = list(filter(lambda s: s["grade"] >= 90, students))
    print(f"\\nHonor students: {[s['name'] for s in honor_students]}")
    
    # Filter by subject
    math_students = list(filter(lambda s: s["subject"] == "Math", students))
    print(f"Math students: {[s['name'] for s in math_students]}")
    
    # Complex filtering with multiple conditions
    def is_excellent_math_student(student):
        return student["subject"] == "Math" and student["grade"] >= 80
    
    excellent_math = list(filter(is_excellent_math_student, students))
    print(f"Excellent Math students: {[s['name'] for s in excellent_math]}")
    
    # Filter strings with regex
    emails = [
        "user@gmail.com", 
        "test@yahoo.com", 
        "invalid-email", 
        "admin@company.org",
        "user@domain",
        "contact@site.net"
    ]
    
    # Simple email validation
    def is_valid_email(email):
        return "@" in email and "." in email.split("@")[-1]
    
    valid_emails = list(filter(is_valid_email, emails))
    print(f"\\nValid emails: {valid_emails}")
    
    # Filter with regex
    gmail_emails = list(filter(lambda email: email.endswith("@gmail.com"), emails))
    print(f"Gmail emails: {gmail_emails}")
    
    # Filter None values
    data_with_none = [1, None, 2, None, 3, 4, None, 5]
    clean_data = list(filter(lambda x: x is not None, data_with_none))
    print(f"\\nCleaned data: {clean_data}")
    
    # Custom filter function
    def filter_by_criteria(items, criteria_func):
        """Generic filter function."""
        return list(filter(criteria_func, items))
    
    # Use custom filter
    positive_numbers = filter_by_criteria([-5, -2, 0, 3, 7, -1, 8], lambda x: x > 0)
    print(f"Positive numbers: {positive_numbers}")
    
    return {
        "even_numbers": even_numbers,
        "long_words": long_words,
        "truthy_values": truthy_values,
        "passing_scores": passing_scores,
        "honor_students": honor_students,
        "valid_emails": valid_emails,
        "clean_data": clean_data
    }

def data_reducer():
    """Demonstrate reduce() function for data aggregation."""
    print("\\n=== Data Reduction Operations ===")
    
    # Basic reduction - sum
    numbers = [1, 2, 3, 4, 5]
    total = reduce(operator.add, numbers)
    print(f"Sum using reduce: {total}")
    
    # Product of all numbers
    product = reduce(operator.mul, numbers)
    print(f"Product using reduce: {product}")
    
    # Find maximum using reduce
    numbers_list = [45, 78, 23, 67, 89, 12, 56]
    maximum = reduce(lambda a, b: a if a > b else b, numbers_list)
    print(f"\\nMaximum using reduce: {maximum}")
    
    # Find minimum using reduce
    minimum = reduce(lambda a, b: a if a < b else b, numbers_list)
    print(f"Minimum using reduce: {minimum}")
    
    # String concatenation
    words = ["Python", "is", "awesome", "for", "programming"]
    sentence = reduce(lambda a, b: a + " " + b, words)
    print(f"\\nJoined sentence: {sentence}")
    
    # Flatten nested lists
    nested_lists = [[1, 2], [3, 4], [5, 6], [7, 8]]
    flattened = reduce(operator.add, nested_lists)
    print(f"\\nFlattened list: {flattened}")
    
    # Count occurrences
    def count_occurrences(counter, item):
        counter[item] = counter.get(item, 0) + 1
        return counter
    
    items = ["apple", "banana", "apple", "orange", "banana", "apple"]
    counts = reduce(count_occurrences, items, {})
    print(f"\\nItem counts: {counts}")
    
    # Group by category
    def group_by_category(groups, item):
        category = item["category"]
        if category not in groups:
            groups[category] = []
        groups[category].append(item)
        return groups
    
    products = [
        {"name": "Apple", "category": "Fruit"},
        {"name": "Carrot", "category": "Vegetable"},
        {"name": "Banana", "category": "Fruit"},
        {"name": "Broccoli", "category": "Vegetable"},
        {"name": "Orange", "category": "Fruit"}
    ]
    
    grouped = reduce(group_by_category, products, {})
    print(f"\\nGrouped products: {grouped}")
    
    # Calculate factorial
    def factorial(n):
        if n <= 1:
            return 1
        return reduce(operator.mul, range(1, n + 1))
    
    fact_5 = factorial(5)
    print(f"\\nFactorial of 5: {fact_5}")
    
    # Sum of squares
    squares_sum = reduce(lambda acc, x: acc + x**2, numbers, 0)
    print(f"Sum of squares: {squares_sum}")
    
    # Merge dictionaries
    dict_list = [
        {"a": 1, "b": 2},
        {"c": 3, "d": 4},
        {"e": 5, "f": 6}
    ]
    
    merged_dict = reduce(lambda d1, d2: {**d1, **d2}, dict_list, {})
    print(f"\\nMerged dictionary: {merged_dict}")
    
    # Calculate cumulative statistics
    def update_stats(stats, value):
        stats["count"] += 1
        stats["sum"] += value
        stats["min"] = min(stats["min"], value) if stats["min"] is not None else value
        stats["max"] = max(stats["max"], value) if stats["max"] is not None else value
        stats["avg"] = stats["sum"] / stats["count"]
        return stats
    
    data_points = [10, 15, 8, 22, 18, 5, 12]
    initial_stats = {"count": 0, "sum": 0, "min": None, "max": None, "avg": 0}
    final_stats = reduce(update_stats, data_points, initial_stats)
    print(f"\\nFinal statistics: {final_stats}")
    
    return {
        "total": total,
        "product": product,
        "maximum": maximum,
        "minimum": minimum,
        "sentence": sentence,
        "flattened": flattened,
        "counts": counts,
        "grouped": grouped,
        "factorial": fact_5,
        "merged_dict": merged_dict,
        "final_stats": final_stats
    }

def advanced_sorting():
    """Demonstrate sorted() function with custom key functions."""
    print("\\n=== Advanced Sorting Operations ===")
    
    # Basic sorting
    numbers = [64, 34, 25, 12, 22, 11, 90]
    sorted_asc = sorted(numbers)
    sorted_desc = sorted(numbers, reverse=True)
    print(f"Original: {numbers}")
    print(f"Ascending: {sorted_asc}")
    print(f"Descending: {sorted_desc}")
    
    # Sort strings
    words = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_words = sorted(words)
    sorted_by_length = sorted(words, key=len)
    sorted_by_length_desc = sorted(words, key=len, reverse=True)
    
    print(f"\\nWords: {words}")
    print(f"Alphabetical: {sorted_words}")
    print(f"By length: {sorted_by_length}")
    print(f"By length (desc): {sorted_by_length_desc}")
    
    # Sort by last character
    sorted_by_last_char = sorted(words, key=lambda word: word[-1])
    print(f"By last character: {sorted_by_last_char}")
    
    # Sort dictionaries
    students = [
        {"name": "Alice", "grade": 85, "age": 20},
        {"name": "Bob", "grade": 92, "age": 19},
        {"name": "Charlie", "grade": 78, "age": 21},
        {"name": "Diana", "grade": 96, "age": 20}
    ]
    
    # Sort by grade
    sorted_by_grade = sorted(students, key=lambda s: s["grade"])
    print(f"\\nSorted by grade: {[s['name'] for s in sorted_by_grade]}")
    
    # Sort by multiple criteria (age, then grade)
    sorted_multi = sorted(students, key=lambda s: (s["age"], s["grade"]))
    print(f"Sorted by age, then grade: {[(s['name'], s['age'], s['grade']) for s in sorted_multi]}")
    
    # Sort by name length, then alphabetically
    sorted_complex = sorted(students, key=lambda s: (len(s["name"]), s["name"]))
    print(f"By name length, then alphabetically: {[s['name'] for s in sorted_complex]}")
    
    # Sort tuples
    coordinates = [(3, 4), (1, 2), (5, 1), (2, 3), (4, 5)]
    
    # Sort by x-coordinate
    sorted_by_x = sorted(coordinates, key=lambda point: point[0])
    print(f"\\nCoordinates by x: {sorted_by_x}")
    
    # Sort by distance from origin
    sorted_by_distance = sorted(coordinates, key=lambda point: (point[0]**2 + point[1]**2)**0.5)
    print(f"By distance from origin: {sorted_by_distance}")
    
    # Sort strings with custom logic
    mixed_case = ["Apple", "banana", "Cherry", "date", "Elderberry"]
    
    # Case-insensitive sort
    case_insensitive = sorted(mixed_case, key=str.lower)
    print(f"\\nCase-insensitive: {case_insensitive}")
    
    # Sort by vowel count
    def count_vowels(word):
        return sum(1 for char in word.lower() if char in 'aeiou')
    
    sorted_by_vowels = sorted(mixed_case, key=count_vowels)
    print(f"By vowel count: {sorted_by_vowels}")
    
    # Sort dates
    date_strings = ["2024-03-15", "2024-01-20", "2024-12-05", "2024-07-10"]
    sorted_dates = sorted(date_strings, key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
    print(f"\\nSorted dates: {sorted_dates}")
    
    # Sort with custom comparison function
    def custom_sort_key(item):
        \"\"\"Complex sorting logic.\"\"\""
        if isinstance(item, str):
            return (0, len(item), item.lower())  # Strings first, by length, then alphabetically
        elif isinstance(item, int):
            return (1, item)  # Numbers second, by value
        else:
            return (2, str(item))  # Others last, as string
    
    mixed_data = ["hello", 42, "world", 15, "python", 7, "data"]
    sorted_mixed = sorted(mixed_data, key=custom_sort_key)
    print(f"\\nCustom sorted mixed data: {sorted_mixed}")
    
    # Sort with stability demonstration
    stable_data = [("Alice", 1), ("Bob", 2), ("Alice", 3), ("Bob", 1)]
    sorted_stable = sorted(stable_data, key=lambda x: x[0])  # Sort by name, maintain order for same names
    print(f"\\nStable sort by name: {sorted_stable}")
    
    return {
        "sorted_asc": sorted_asc,
        "sorted_desc": sorted_desc,
        "sorted_by_length": sorted_by_length,
        "sorted_by_grade": sorted_by_grade,
        "sorted_multi": sorted_multi,
        "sorted_by_distance": sorted_by_distance,
        "case_insensitive": case_insensitive,
        "sorted_dates": sorted_dates,
        "sorted_mixed": sorted_mixed
    }

def sequence_reverser():
    """Demonstrate reversed() function and sequence reversal."""
    print("\\n=== Sequence Reversal Operations ===")
    
    # Reverse lists
    numbers = [1, 2, 3, 4, 5]
    reversed_list = list(reversed(numbers))
    print(f"Original list: {numbers}")
    print(f"Reversed list: {reversed_list}")
    
    # Reverse strings
    text = "Hello, World!"
    reversed_text = "".join(reversed(text))
    print(f"\\nOriginal text: '{text}'")
    print(f"Reversed text: '{reversed_text}'")
    
    # Reverse tuples
    colors = ("red", "green", "blue", "yellow")
    reversed_colors = tuple(reversed(colors))
    print(f"\\nOriginal tuple: {colors}")
    print(f"Reversed tuple: {reversed_colors}")
    
    # Reverse using slicing (alternative method)
    slice_reversed = numbers[::-1]
    slice_text = text[::-1]
    print(f"\\nSlice reversed list: {slice_reversed}")
    print(f"Slice reversed text: '{slice_text}'")
    
    # Reverse words in a sentence
    sentence = "Python programming is fun and powerful"
    words = sentence.split()
    reversed_words = list(reversed(words))
    reversed_sentence = " ".join(reversed_words)
    
    print(f"\\nOriginal sentence: '{sentence}'")
    print(f"Reversed words: {reversed_words}")
    print(f"Reversed sentence: '{reversed_sentence}'")
    
    # Reverse each word in sentence
    reversed_each_word = " ".join(word[::-1] for word in words)
    print(f"Each word reversed: '{reversed_each_word}'")
    
    # Reverse dictionary items (by keys)
    student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96}
    reversed_dict_items = list(reversed(list(student_grades.items())))
    print(f"\\nOriginal dict items: {list(student_grades.items())}")
    print(f"Reversed dict items: {reversed_dict_items}")
    
    # Reverse nested structures
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Reverse rows
    reversed_rows = list(reversed(matrix))
    print(f"\\nOriginal matrix: {matrix}")
    print(f"Reversed rows: {reversed_rows}")
    
    # Reverse elements in each row
    reversed_elements = [list(reversed(row)) for row in matrix]
    print(f"Reversed elements: {reversed_elements}")
    
    # Reverse both rows and elements
    fully_reversed = [list(reversed(row)) for row in reversed(matrix)]
    print(f"Fully reversed: {fully_reversed}")
    
    # Reverse with enumerate
    items = ["apple", "banana", "cherry"]
    reversed_with_index = list(enumerate(reversed(items)))
    print(f"\\nReversed with new indices: {reversed_with_index}")
    
    # Original indices with reversed items
    original_indices_reversed = [(i, item) for i, item in reversed(list(enumerate(items)))]
    print(f"Original indices reversed: {original_indices_reversed}")
    
    # Reverse file lines (simulation)
    file_lines = [
        "Line 1: Introduction",
        "Line 2: Main content", 
        "Line 3: More details",
        "Line 4: Conclusion"
    ]
    
    reversed_file = list(reversed(file_lines))
    print(f"\\nOriginal file lines:")
    for line in file_lines:
        print(f"  {line}")
    
    print("\\nReversed file lines:")
    for line in reversed_file:
        print(f"  {line}")
    
    # Palindrome checker using reverse
    def is_palindrome(text):
        \"\"\"Check if text is palindrome using reverse.\"\"\""
        cleaned = "".join(char.lower() for char in text if char.isalnum())
        return cleaned == cleaned[::-1]
    
    test_words = ["racecar", "hello", "A man a plan a canal Panama", "python"]
    palindromes = [(word, is_palindrome(word)) for word in test_words]
    print(f"\\nPalindrome check:")
    for word, is_pal in palindromes:
        print(f"  '{word}': {is_pal}")
    
    return {
        "reversed_list": reversed_list,
        "reversed_text": reversed_text,
        "reversed_colors": reversed_colors,
        "reversed_sentence": reversed_sentence,
        "reversed_each_word": reversed_each_word,
        "reversed_rows": reversed_rows,
        "reversed_elements": reversed_elements,
        "palindromes": palindromes
    }

# Main execution
if __name__ == "__main__":
    print("=== Built-in Data Transformation Functions ===")
    
    print("\\n1. Data Mapping:")
    map_results = data_mapper()
    
    print("\\n2. Data Filtering:")
    filter_results = data_filter()
    
    print("\\n3. Data Reduction:")
    reduce_results = data_reducer()
    
    print("\\n4. Advanced Sorting:")
    sort_results = advanced_sorting()
    
    print("\\n5. Sequence Reversal:")
    reverse_results = sequence_reverser()
    
    print("\\n" + "="*60)
    print("=== DATA TRANSFORMATION COMPLETE ===")
    print("✓ Map operations for data transformation")
    print("✓ Filter operations for data selection")
    print("✓ Reduce operations for data aggregation")
    print("✓ Advanced sorting with custom keys")
    print("✓ Sequence reversal techniques")
    print("✓ Functional programming concepts")
```

## Hints

- `map()` returns an iterator - convert to list to see results
- `filter()` removes falsy values when no condition is specified
- `reduce()` requires importing from `functools` module
- `sorted()` creates new sequence, `list.sort()` modifies in-place
- Use `operator` module for common operations in reduce

## Practice Cases

Your functions should handle:

1. Empty sequences and edge cases
2. Multiple iterables with different lengths
3. Custom key functions for complex sorting
4. Type conversion and validation
5. Memory-efficient operations for large datasets

## Bonus Challenge

Implement a pipeline that combines map, filter, and reduce operations to process a dataset, create custom sorting algorithms, and build a functional programming utility library!