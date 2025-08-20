# Iterator and Generator Functions - Practice 6

**Difficulty:** ⭐⭐⭐ (Medium)

## Description

Master Python's built-in functions for working with iterators and generators including `iter()`, `next()`, `enumerate()`, `zip()`, `reversed()`, `range()`, and advanced iteration patterns.

## Objectives

- Create and work with iterators using `iter()` and `next()`
- Use `enumerate()` for indexed iteration
- Combine multiple iterables with `zip()`
- Reverse sequences with `reversed()`
- Generate numeric sequences with `range()`
- Understand lazy evaluation and memory efficiency

## Your Tasks

1. **iterator_basics()** - Work with basic iterator creation and consumption
2. **enumeration_patterns()** - Use enumerate for indexed iteration
3. **zip_operations()** - Combine and align multiple iterables
4. **reverse_operations()** - Reverse sequences and iterables
5. **advanced_iteration()** - Complex iteration patterns and optimizations

## Example

```python
import itertools
from typing import Iterator, List, Tuple, Any, Union
import sys
import time

def iterator_basics():
    """Demonstrate basic iterator creation and usage."""
    print("=== Iterator Basics ===")
    
    # Creating iterators from iterables
    print("Creating Iterators:")
    
    # List iterator
    numbers = [1, 2, 3, 4, 5]
    number_iter = iter(numbers)
    
    print(f"Original list: {numbers}")
    print(f"Iterator object: {number_iter}")
    print(f"Iterator type: {type(number_iter)}")
    
    # Consuming iterator with next()
    print("\\nConsuming with next():")
    try:
        print(f"First: {next(number_iter)}")
        print(f"Second: {next(number_iter)}")
        print(f"Third: {next(number_iter)}")
    except StopIteration:
        print("Iterator exhausted!")
    
    # Iterator with default value
    print("\\nIterator with default values:")
    
    small_list = [10, 20]
    small_iter = iter(small_list)
    
    print(f"Value 1: {next(small_iter, 'No more values')}")
    print(f"Value 2: {next(small_iter, 'No more values')}")
    print(f"Value 3: {next(small_iter, 'No more values')}")  # Default returned
    print(f"Value 4: {next(small_iter, 'No more values')}")  # Default returned
    
    # String iterator
    print("\\nString Iterator:")
    
    text = "Python"
    text_iter = iter(text)
    
    print(f"Original string: '{text}'")
    characters = [next(text_iter, '') for _ in range(len(text) + 2)]
    print(f"Characters: {characters}")
    
    # Dictionary iterators
    print("\\nDictionary Iterators:")
    
    data = {"name": "Alice", "age": 30, "city": "New York"}
    
    # Iterator over keys
    key_iter = iter(data)
    print(f"Keys: {list(key_iter)}")
    
    # Iterator over values
    value_iter = iter(data.values())
    print(f"Values: {list(value_iter)}")
    
    # Iterator over items
    item_iter = iter(data.items())
    print(f"Items: {list(item_iter)}")
    
    # Custom iterator function
    print("\\nCustom Iterator Function:")
    
    def countdown(n):
        """Create a countdown iterator."""
        return iter(range(n, 0, -1))
    
    countdown_iter = countdown(5)
    countdown_list = list(countdown_iter)
    print(f"Countdown from 5: {countdown_list}")
    
    # Callable iterator
    print("\\nCallable Iterator:")
    
    import random
    random.seed(42)  # For reproducible results
    
    # Iterator that calls a function until sentinel value is reached
    random_iter = iter(lambda: random.randint(1, 6), 6)  # Roll dice until 6
    
    rolls = []
    for roll in random_iter:
        rolls.append(roll)
        if len(rolls) > 10:  # Safety break
            break
    
    print(f"Dice rolls until 6: {rolls}")
    
    # File iterator (simulated)
    print("\\nFile-like Iterator:")
    
    # Simulate file lines
    file_content = ["Line 1\\n", "Line 2\\n", "Line 3\\n", "Line 4\\n"]
    file_iter = iter(file_content)
    
    print("Reading file lines:")
    for line_num, line in enumerate(file_iter, 1):
        print(f"  {line_num}: {line.strip()}")
    
    # Iterator protocol implementation
    print("\\nCustom Iterator Class:")
    
    class SquareIterator:
        def __init__(self, max_value):
            self.max_value = max_value
            self.current = 0
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.current >= self.max_value:
                raise StopIteration
            result = self.current ** 2
            self.current += 1
            return result
    
    square_iter = SquareIterator(5)
    squares = list(square_iter)
    print(f"Squares 0-4: {squares}")
    
    return {
        "basic_iteration": list(iter([1, 2, 3, 4, 5])),
        "string_chars": list(iter("Python")),
        "dict_keys": list(iter(data.keys())),
        "countdown": countdown_list,
        "dice_rolls": rolls,
        "file_lines": [line.strip() for line in file_content],
        "squares": squares
    }

def enumeration_patterns():
    """Demonstrate enumerate function for indexed iteration."""
    print("\\n=== Enumeration Patterns ===")
    
    # Basic enumerate
    print("Basic Enumerate:")
    
    fruits = ["apple", "banana", "orange", "grape", "kiwi"]
    
    print("Default enumeration (start=0):")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")
    
    print("\\nEnumeration with custom start:")
    for index, fruit in enumerate(fruits, start=1):
        print(f"  {index}. {fruit}")
    
    # Enumerate with different data types
    print("\\nEnumerate with Different Types:")
    
    # String enumeration
    text = "Hello"
    print(f"String '{text}':")
    for i, char in enumerate(text):
        print(f"  Position {i}: '{char}'")
    
    # Tuple enumeration
    coordinates = [(0, 0), (1, 2), (3, 4), (5, 6)]
    print(f"\\nCoordinates: {coordinates}")
    for i, (x, y) in enumerate(coordinates):
        print(f"  Point {i}: ({x}, {y})")
    
    # Dictionary enumeration
    student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 88}
    print(f"\\nStudent grades:")
    for rank, (name, grade) in enumerate(student_grades.items(), 1):
        print(f"  #{rank}: {name} - {grade}%")
    
    # Practical enumerate applications
    print("\\nPractical Applications:")
    
    # Finding indices of specific elements
    numbers = [10, 25, 10, 30, 10, 45]
    target = 10
    
    indices = [i for i, num in enumerate(numbers) if num == target]
    print(f"Numbers: {numbers}")
    print(f"Indices of {target}: {indices}")
    
    # Creating lookup tables
    words = ["python", "java", "javascript", "c++", "go"]
    word_to_index = {word: i for i, word in enumerate(words)}
    index_to_word = {i: word for i, word in enumerate(words)}
    
    print(f"\\nWords: {words}")
    print(f"Word to index: {word_to_index}")
    print(f"Index to word: {index_to_word}")
    
    # Processing with position awareness
    print("\\nPosition-Aware Processing:")
    
    data = [100, 200, 150, 300, 250]
    
    # Add position-based bonus
    processed_data = []
    for i, value in enumerate(data):
        bonus = i * 10  # Position-based bonus
        new_value = value + bonus
        processed_data.append(new_value)
        print(f"  Position {i}: {value} + {bonus} = {new_value}")
    
    # Enumerate with slicing
    print("\\nEnumerate with Slicing:")
    
    large_list = list(range(20))
    print(f"Original list: {large_list}")
    
    # Enumerate every other element
    print("Every other element (start from index 0):")
    for i, value in enumerate(large_list[::2]):
        actual_index = i * 2
        print(f"  Enum index {i}, Actual index {actual_index}: {value}")
    
    # Enumerate reversed list
    print("\\nReversed enumeration:")
    reversed_fruits = list(reversed(fruits))
    for i, fruit in enumerate(reversed_fruits):
        original_index = len(fruits) - 1 - i
        print(f"  Enum index {i}, Original index {original_index}: {fruit}")
    
    # Multiple enumerations
    print("\\nMultiple Lists Enumeration:")
    
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    cities = ["New York", "London", "Tokyo"]
    
    for i, (name, age, city) in enumerate(zip(names, ages, cities)):
        print(f"  Person {i+1}: {name}, {age} years old, lives in {city}")
    
    # Grouped enumeration
    print("\\nGrouped Enumeration:")
    
    items = ["a", "b", "c", "d", "e", "f", "g", "h"]
    group_size = 3
    
    for group_num, start_idx in enumerate(range(0, len(items), group_size)):
        group = items[start_idx:start_idx + group_size]
        print(f"  Group {group_num + 1}: {group}")
    
    return {
        "basic_enumeration": list(enumerate(fruits)),
        "custom_start": list(enumerate(fruits, start=1)),
        "string_enumeration": list(enumerate("Hello")),
        "coordinate_enumeration": list(enumerate(coordinates)),
        "target_indices": indices,
        "lookup_tables": {"word_to_index": word_to_index, "index_to_word": index_to_word},
        "processed_data": processed_data,
        "reversed_enumeration": list(enumerate(reversed_fruits)),
        "grouped_items": [items[i:i+group_size] for i in range(0, len(items), group_size)]
    }

def zip_operations():
    """Demonstrate zip function for combining iterables."""
    print("\\n=== Zip Operations ===")
    
    # Basic zip
    print("Basic Zip:")
    
    numbers = [1, 2, 3, 4, 5]
    letters = ['a', 'b', 'c', 'd', 'e']
    
    zipped = list(zip(numbers, letters))
    print(f"Numbers: {numbers}")
    print(f"Letters: {letters}")
    print(f"Zipped: {zipped}")
    
    # Unzipping
    print("\\nUnzipping:")
    unzipped_numbers, unzipped_letters = zip(*zipped)
    print(f"Unzipped numbers: {list(unzipped_numbers)}")
    print(f"Unzipped letters: {list(unzipped_letters)}")
    
    # Zip with different lengths
    print("\\nZip with Different Lengths:")
    
    short_list = [1, 2, 3]
    long_list = ['a', 'b', 'c', 'd', 'e', 'f']
    
    zipped_different = list(zip(short_list, long_list))
    print(f"Short: {short_list}")
    print(f"Long: {long_list}")
    print(f"Zipped (stops at shortest): {zipped_different}")
    
    # Zip with more than two iterables
    print("\\nMultiple Iterables:")
    
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    cities = ["NYC", "LA", "Chicago"]
    salaries = [50000, 60000, 70000]
    
    employee_data = list(zip(names, ages, cities, salaries))
    print("Employee data:")
    for name, age, city, salary in employee_data:
        print(f"  {name}: {age} years, {city}, ${salary:,}")
    
    # Zip with ranges
    print("\\nZip with Ranges:")
    
    indices = range(5)
    values = [10, 20, 30, 40, 50]
    
    indexed_values = list(zip(indices, values))
    print(f"Indices: {list(indices)}")
    print(f"Values: {values}")
    print(f"Indexed values: {indexed_values}")
    
    # Dictionary creation with zip
    print("\\nDictionary Creation:")
    
    keys = ["name", "age", "city", "occupation"]
    values = ["Diana", 28, "Boston", "Engineer"]
    
    person_dict = dict(zip(keys, values))
    print(f"Keys: {keys}")
    print(f"Values: {values}")
    print(f"Dictionary: {person_dict}")
    
    # Zip for parallel processing
    print("\\nParallel Processing:")
    
    prices = [19.99, 25.50, 12.75, 8.99]
    quantities = [2, 1, 3, 4]
    
    totals = [price * qty for price, qty in zip(prices, quantities)]
    print("Item calculations:")
    for i, (price, qty, total) in enumerate(zip(prices, quantities, totals), 1):
        print(f"  Item {i}: ${price:.2f} × {qty} = ${total:.2f}")
    
    grand_total = sum(totals)
    print(f"Grand total: ${grand_total:.2f}")
    
    # Zip with string operations
    print("\\nString Operations:")
    
    first_names = ["John", "Jane", "Bob"]
    last_names = ["Doe", "Smith", "Johnson"]
    
    full_names = [f"{first} {last}" for first, last in zip(first_names, last_names)]
    initials = [f"{first[0]}.{last[0]}." for first, last in zip(first_names, last_names)]
    
    print("Name processing:")
    for full, initial in zip(full_names, initials):
        print(f"  {full} -> {initial}")
    
    # Transpose with zip
    print("\\nMatrix Transpose:")
    
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Original matrix:")
    for row in matrix:
        print(f"  {row}")
    
    transposed = list(zip(*matrix))
    print("\\nTransposed matrix:")
    for row in transposed:
        print(f"  {list(row)}")
    
    # Zip with itertools combinations
    print("\\nAdvanced Zip Patterns:")
    
    # Pairwise iteration (adjacent pairs)
    sequence = [1, 2, 3, 4, 5]
    pairs = list(zip(sequence, sequence[1:]))
    print(f"Sequence: {sequence}")
    print(f"Adjacent pairs: {pairs}")
    
    # Differences between adjacent elements
    differences = [b - a for a, b in pairs]
    print(f"Differences: {differences}")
    
    # Zip with enumerate for indexed pairs
    indexed_pairs = list(enumerate(zip(first_names, last_names)))
    print(f"\\nIndexed pairs:")
    for i, (first, last) in indexed_pairs:
        print(f"  {i}: ({first}, {last})")
    
    # Filtering with zip
    print("\\nFiltering with Zip:")
    
    scores = [85, 92, 78, 96, 88, 71]
    passed = [score >= 80 for score in scores]
    
    print("Score analysis:")
    for i, (score, is_passed) in enumerate(zip(scores, passed), 1):
        status = "PASS" if is_passed else "FAIL"
        print(f"  Student {i}: {score}% - {status}")
    
    passed_count = sum(passed)
    print(f"\\nPassed: {passed_count}/{len(scores)} students")
    
    return {
        "basic_zip": zipped,
        "unzipped": (list(unzipped_numbers), list(unzipped_letters)),
        "different_lengths": zipped_different,
        "employee_data": employee_data,
        "person_dict": person_dict,
        "price_totals": totals,
        "full_names": full_names,
        "initials": initials,
        "transposed_matrix": [list(row) for row in transposed],
        "adjacent_pairs": pairs,
        "differences": differences,
        "pass_count": passed_count
    }

def reverse_operations():
    """Demonstrate reversed function and reverse operations."""
    print("\\n=== Reverse Operations ===")
    
    # Basic reversed
    print("Basic Reversed:")
    
    numbers = [1, 2, 3, 4, 5]
    reversed_numbers = list(reversed(numbers))
    
    print(f"Original: {numbers}")
    print(f"Reversed: {reversed_numbers}")
    print(f"Original unchanged: {numbers}")
    
    # String reversal
    print("\\nString Reversal:")
    
    text = "Python Programming"
    reversed_text = ''.join(reversed(text))
    
    print(f"Original: '{text}'")
    print(f"Reversed: '{reversed_text}'")
    
    # Reverse different types
    print("\\nReverse Different Types:")
    
    # Tuple reversal
    colors = ("red", "green", "blue", "yellow")
    reversed_colors = tuple(reversed(colors))
    print(f"Tuple: {colors} -> {reversed_colors}")
    
    # Range reversal
    number_range = range(1, 6)
    reversed_range = list(reversed(number_range))
    print(f"Range: {list(number_range)} -> {reversed_range}")
    
    # Dictionary items reversal (Python 3.7+ maintains insertion order)
    data = {"first": 1, "second": 2, "third": 3}
    reversed_items = list(reversed(data.items()))
    print(f"Dict items: {list(data.items())} -> {reversed_items}")
    
    # Practical reverse applications
    print("\\nPractical Applications:")
    
    # Palindrome checking
    def is_palindrome(text):
        cleaned = ''.join(text.lower().split())
        return cleaned == ''.join(reversed(cleaned))
    
    test_phrases = [
        "racecar",
        "A man a plan a canal Panama",
        "race a car",
        "hello world",
        "Was it a rat I saw"
    ]
    
    print("Palindrome checking:")
    for phrase in test_phrases:
        result = is_palindrome(phrase)
        print(f"  '{phrase}': {result}")
    
    # Reverse iteration patterns
    print("\\nReverse Iteration Patterns:")
    
    # Last N elements
    items = list(range(1, 11))  # [1, 2, 3, ..., 10]
    last_3 = list(reversed(items))[:3]
    
    print(f"Items: {items}")
    print(f"Last 3 (reversed): {last_3}")
    
    # Countdown processing
    countdown_nums = list(range(5, 0, -1))
    print(f"\\nCountdown: {countdown_nums}")
    
    for i, num in enumerate(countdown_nums):
        if num == 1:
            print(f"  {num} - LAUNCH!")
        else:
            print(f"  {num} - Preparing...")
    
    # Reverse with conditions
    print("\\nConditional Reverse Processing:")
    
    grades = [85, 92, 78, 96, 88, 71, 94]
    
    # Process from highest to lowest (assuming sorted)
    sorted_grades = sorted(grades, reverse=True)
    print(f"Grades (high to low): {sorted_grades}")
    
    # Award rankings
    rankings = ["1st", "2nd", "3rd"] + [f"{i}th" for i in range(4, len(sorted_grades) + 1)]
    
    for rank, grade in zip(rankings, sorted_grades):
        print(f"  {rank} place: {grade}%")
    
    # Reverse slicing vs reversed()
    print("\\nReverse Slicing vs reversed():")
    
    original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Method 1: Slice with step -1
    slice_reversed = original[::-1]
    
    # Method 2: reversed() function
    func_reversed = list(reversed(original))
    
    print(f"Original: {original}")
    print(f"Slice [::-1]: {slice_reversed}")
    print(f"reversed(): {func_reversed}")
    print(f"Results equal: {slice_reversed == func_reversed}")
    
    # Memory efficiency demonstration
    print("\\nMemory Efficiency:")
    
    large_list = list(range(1000))
    
    # reversed() returns an iterator (memory efficient)
    rev_iterator = reversed(large_list)
    print(f"reversed() object: {rev_iterator}")
    print(f"Type: {type(rev_iterator)}")
    
    # Get first 3 elements without creating full list
    first_3_reversed = [next(rev_iterator) for _ in range(3)]
    print(f"First 3 from reversed iterator: {first_3_reversed}")
    
    # Chained reversals
    print("\\nChained Reversals:")
    
    text_list = ["hello", "world", "python", "programming"]
    
    # Reverse the list, then reverse each string
    double_reversed = [''.join(reversed(word)) for word in reversed(text_list)]
    
    print(f"Original: {text_list}")
    print(f"Double reversed: {double_reversed}")
    
    # Custom reverse function
    print("\\nCustom Reverse Applications:")
    
    def reverse_words_in_sentence(sentence):
        words = sentence.split()
        reversed_words = [word for word in reversed(words)]
        return ' '.join(reversed_words)
    
    def reverse_each_word(sentence):
        words = sentence.split()
        reversed_each = [''.join(reversed(word)) for word in words]
        return ' '.join(reversed_each)
    
    sentence = "Python is awesome"
    
    print(f"Original: '{sentence}'")
    print(f"Reversed words: '{reverse_words_in_sentence(sentence)}'")
    print(f"Each word reversed: '{reverse_each_word(sentence)}'")
    
    return {
        "basic_reverse": reversed_numbers,
        "string_reverse": reversed_text,
        "tuple_reverse": reversed_colors,
        "range_reverse": reversed_range,
        "palindrome_results": [(phrase, is_palindrome(phrase)) for phrase in test_phrases],
        "last_elements": last_3,
        "grade_rankings": list(zip(rankings, sorted_grades)),
        "slice_vs_func": slice_reversed == func_reversed,
        "first_3_reversed": first_3_reversed,
        "double_reversed": double_reversed,
        "sentence_reversals": {
            "word_order": reverse_words_in_sentence(sentence),
            "each_word": reverse_each_word(sentence)
        }
    }

def advanced_iteration():
    """Demonstrate advanced iteration patterns and optimizations."""
    print("\\n=== Advanced Iteration Patterns ===")
    
    # Iterator chaining
    print("Iterator Chaining:")
    
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [7, 8, 9]
    
    # Manual chaining
    chained_manual = []
    for lst in [list1, list2, list3]:
        chained_manual.extend(lst)
    
    # Using itertools.chain
    chained_itertools = list(itertools.chain(list1, list2, list3))
    
    print(f"Lists: {list1}, {list2}, {list3}")
    print(f"Manual chaining: {chained_manual}")
    print(f"itertools.chain: {chained_itertools}")
    
    # Flatten nested structure
    nested = [[1, 2], [3, 4, 5], [6], [7, 8, 9]]
    flattened = list(itertools.chain.from_iterable(nested))
    print(f"Nested: {nested}")
    print(f"Flattened: {flattened}")
    
    # Cycle iteration
    print("\\nCycle Iteration:")
    
    colors = ['red', 'green', 'blue']
    color_cycle = itertools.cycle(colors)
    
    # Get first 10 colors from infinite cycle
    cycled_colors = [next(color_cycle) for _ in range(10)]
    print(f"Colors: {colors}")
    print(f"Cycled (10 items): {cycled_colors}")
    
    # Repeat iteration
    print("\\nRepeat Iteration:")
    
    # Repeat a value
    repeated = list(itertools.repeat('X', 5))
    print(f"Repeat 'X' 5 times: {repeated}")
    
    # Infinite repeat (be careful!)
    infinite_repeat = itertools.repeat(42)
    first_5_repeats = [next(infinite_repeat) for _ in range(5)]
    print(f"Infinite 42s (first 5): {first_5_repeats}")
    
    # Count iteration
    print("\\nCount Iteration:")
    
    # Start counting from 10, step by 2
    counter = itertools.count(10, 2)
    first_10_counts = [next(counter) for _ in range(10)]
    print(f"Count from 10, step 2: {first_10_counts}")
    
    # Takewhile and dropwhile
    print("\\nTakewhile and Dropwhile:")
    
    numbers = [1, 3, 5, 7, 8, 10, 12, 14, 15, 17]
    
    # Take while condition is true
    take_odd = list(itertools.takewhile(lambda x: x % 2 == 1, numbers))
    
    # Drop while condition is true
    drop_odd = list(itertools.dropwhile(lambda x: x % 2 == 1, numbers))
    
    print(f"Numbers: {numbers}")
    print(f"Take while odd: {take_odd}")
    print(f"Drop while odd: {drop_odd}")
    
    # Groupby iteration
    print("\\nGroupby Iteration:")
    
    # Group consecutive identical elements
    data = [1, 1, 2, 2, 2, 3, 1, 1, 1]
    grouped = [(key, list(group)) for key, group in itertools.groupby(data)]
    
    print(f"Data: {data}")
    print(f"Grouped: {grouped}")
    
    # Group by key function
    words = ["apple", "ant", "bear", "cat", "car", "dog"]
    by_first_letter = [(letter, list(group)) for letter, group in 
                      itertools.groupby(sorted(words), key=lambda x: x[0])]
    
    print(f"Words: {words}")
    print(f"Grouped by first letter: {by_first_letter}")
    
    # Islice for lazy slicing
    print("\\nLazy Slicing with islice:")
    
    # Create a large range but only take middle portion
    large_range = range(1000000)
    middle_slice = list(itertools.islice(large_range, 499995, 500005))
    
    print(f"Middle 10 elements of range(1000000): {middle_slice}")
    
    # Skip and take patterns
    every_third = list(itertools.islice(range(20), 2, None, 3))  # Start at 2, step by 3
    print(f"Every third element from 2: {every_third}")
    
    # Combinations and permutations
    print("\\nCombinations and Permutations:")
    
    items = ['A', 'B', 'C', 'D']
    
    # Combinations (order doesn't matter)
    combinations_2 = list(itertools.combinations(items, 2))
    combinations_3 = list(itertools.combinations(items, 3))
    
    print(f"Items: {items}")
    print(f"Combinations of 2: {combinations_2}")
    print(f"Combinations of 3: {combinations_3}")
    
    # Permutations (order matters)
    permutations_2 = list(itertools.permutations(items, 2))
    print(f"Permutations of 2: {permutations_2[:8]}...")  # Show first 8
    
    # Product (cartesian product)
    print("\\nCartesian Product:")
    
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', 'K']
    
    # Create deck of cards (limited)
    cards = list(itertools.product(ranks, suits))
    print(f"Sample cards: {cards}")
    
    # Memory efficiency comparison
    print("\\nMemory Efficiency Comparison:")
    
    # Memory-inefficient approach
    def inefficient_processing(n):
        # Creates all lists in memory
        numbers = list(range(n))
        squared = [x**2 for x in numbers]
        filtered = [x for x in squared if x % 2 == 0]
        return filtered[:10]
    
    # Memory-efficient approach
    def efficient_processing(n):
        # Uses iterators, processes lazily
        numbers = range(n)
        squared = (x**2 for x in numbers)
        filtered = (x for x in squared if x % 2 == 0)
        return list(itertools.islice(filtered, 10))
    
    # Practice with large number
    n = 100000
    
    import time
    
    # Time inefficient approach
    start = time.time()
    result_inefficient = inefficient_processing(n)
    time_inefficient = time.time() - start
    
    # Time efficient approach
    start = time.time()
    result_efficient = efficient_processing(n)
    time_efficient = time.time() - start
    
    print(f"Processing first 10 even squares from range({n}):")
    print(f"  Inefficient result: {result_inefficient}")
    print(f"  Efficient result: {result_efficient}")
    print(f"  Results match: {result_inefficient == result_efficient}")
    print(f"  Inefficient time: {time_inefficient:.4f}s")
    print(f"  Efficient time: {time_efficient:.4f}s")
    print(f"  Speedup: {time_inefficient/time_efficient:.2f}x")
    
    # Custom iterator for Fibonacci sequence
    print("\\nCustom Fibonacci Iterator:")
    
    class FibonacciIterator:
        def __init__(self, max_count=None):
            self.max_count = max_count
            self.count = 0
            self.current = 0
            self.next_val = 1
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.max_count and self.count >= self.max_count:
                raise StopIteration
            
            result = self.current
            self.current, self.next_val = self.next_val, self.current + self.next_val
            self.count += 1
            return result
    
    fib_iter = FibonacciIterator(15)
    fibonacci_sequence = list(fib_iter)
    print(f"Fibonacci sequence (15 terms): {fibonacci_sequence}")
    
    return {
        "chained_lists": chained_itertools,
        "flattened_nested": flattened,
        "cycled_colors": cycled_colors,
        "repeated_values": repeated,
        "count_sequence": first_10_counts,
        "takewhile_result": take_odd,
        "dropwhile_result": drop_odd,
        "grouped_data": grouped,
        "grouped_words": by_first_letter,
        "middle_slice": middle_slice,
        "combinations": combinations_2,
        "permutations": permutations_2[:8],
        "cards": cards[:8],
        "efficiency_comparison": {
            "inefficient_time": time_inefficient,
            "efficient_time": time_efficient,
            "speedup": time_inefficient/time_efficient
        },
        "fibonacci": fibonacci_sequence
    }

# Main execution
if __name__ == "__main__":
    print("=== Built-in Iterator and Generator Functions ===")
    
    print("\\n1. Iterator Basics:")
    iterator_results = iterator_basics()
    
    print("\\n2. Enumeration Patterns:")
    enumeration_results = enumeration_patterns()
    
    print("\\n3. Zip Operations:")
    zip_results = zip_operations()
    
    print("\\n4. Reverse Operations:")
    reverse_results = reverse_operations()
    
    print("\\n5. Advanced Iteration:")
    advanced_results = advanced_iteration()
    
    print("\\n" + "="*60)
    print("=== ITERATOR AND GENERATOR FUNCTIONS COMPLETE ===")
    print("✓ Iterator creation and consumption")
    print("✓ Enumeration for indexed iteration")
    print("✓ Zip operations for parallel processing")
    print("✓ Reverse operations and patterns")
    print("✓ Advanced iteration with itertools")
    print("✓ Memory-efficient processing")
    print("✓ Custom iterator implementations")
```

## Hints

- `iter()` creates iterators from iterables, supports callable with sentinel
- `next()` can take a default value to avoid StopIteration exceptions
- `enumerate()` provides both index and value, supports custom start values
- `zip()` stops at the shortest iterable, use `itertools.zip_longest()` for different behavior
- `reversed()` returns an iterator, not a list - use `list()` to materialize

## Practice Cases

Your functions should handle:

1. Iterator creation from various iterable types
2. Enumeration with different start values and data types
3. Zip operations with multiple iterables of different lengths
4. Reverse operations on sequences and strings
5. Advanced patterns using itertools for memory efficiency

## Bonus Challenge

Implement a custom iterator class, create memory-efficient data processing pipelines, and build advanced iteration patterns using itertools combinations!