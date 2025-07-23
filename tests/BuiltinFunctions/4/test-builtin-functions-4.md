# String and Sequence Functions - Test 4

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Master Python's built-in functions for working with strings and sequences including `join()`, `split()`, `format()`, `ord()`, `chr()`, `bytes()`, `str.encode()`, and various sequence manipulation functions.

## Objectives

- Process and manipulate strings efficiently
- Convert between different string encodings
- Work with ASCII and Unicode characters
- Handle byte sequences and text encoding
- Format strings in multiple ways

## Your Tasks

1. **string_processors()** - Process strings with built-in functions
2. **character_converters()** - Convert between characters and codes
3. **encoding_handlers()** - Handle text encoding and decoding
4. **string_formatters()** - Format strings using various methods
5. **sequence_manipulators()** - Manipulate sequences efficiently

## Example

```python
import string
import re
from collections import Counter
from typing import List, Dict, Any, Union
import unicodedata

def string_processors():
    """Process strings using built-in string functions."""
    print("=== String Processing Operations ===")
    
    # Basic string operations
    sample_text = "  Hello, World! Python is Amazing!  "
    print(f"Original text: '{sample_text}'")
    
    # String cleaning
    cleaned = sample_text.strip()
    lower_case = cleaned.lower()
    upper_case = cleaned.upper()
    title_case = cleaned.title()
    swapped_case = cleaned.swapcase()
    
    print(f"Stripped: '{cleaned}'")
    print(f"Lower case: '{lower_case}'")
    print(f"Upper case: '{upper_case}'")
    print(f"Title case: '{title_case}'")
    print(f"Swapped case: '{swapped_case}'")
    
    # String testing methods
    text_checks = {
        "isalpha": cleaned.isalpha(),
        "isdigit": cleaned.isdigit(),
        "isalnum": cleaned.isalnum(),
        "isspace": cleaned.isspace(),
        "isupper": cleaned.isupper(),
        "islower": cleaned.islower(),
        "istitle": cleaned.istitle()
    }
    
    print(f"\\nString checks: {text_checks}")
    
    # String splitting and joining
    words = cleaned.split()
    print(f"\\nWords: {words}")
    
    # Different splitting methods
    split_comma = "apple,banana,cherry,date".split(',')
    split_lines = "line1\\nline2\\nline3".splitlines()
    partition_result = cleaned.partition("World")
    
    print(f"Split by comma: {split_comma}")
    print(f"Split lines: {split_lines}")
    print(f"Partition result: {partition_result}")
    
    # String joining
    joined_space = " ".join(words)
    joined_dash = "-".join(words)
    joined_comma = ", ".join(split_comma)
    
    print(f"\\nJoined with space: '{joined_space}'")
    print(f"Joined with dash: '{joined_dash}'")
    print(f"Joined with comma: '{joined_comma}'")
    
    # String replacement
    replaced = cleaned.replace("World", "Universe")
    replaced_multiple = cleaned.replace("o", "0").replace("l", "1")
    
    print(f"\\nReplaced: '{replaced}'")
    print(f"Multiple replacements: '{replaced_multiple}'")
    
    # String searching
    find_result = cleaned.find("Python")
    index_result = cleaned.index("World") if "World" in cleaned else -1
    count_result = cleaned.count("l")
    starts_with = cleaned.startswith("Hello")
    ends_with = cleaned.endswith("Amazing!")
    
    print(f"\\nFind 'Python': {find_result}")
    print(f"Index of 'World': {index_result}")
    print(f"Count of 'l': {count_result}")
    print(f"Starts with 'Hello': {starts_with}")
    print(f"Ends with 'Amazing!': {ends_with}")
    
    # String centering and padding
    centered = "Python".center(20, '*')
    left_justified = "Python".ljust(15, '-')
    right_justified = "Python".rjust(15, '+')
    zero_filled = "42".zfill(8)
    
    print(f"\\nCentered: '{centered}'")
    print(f"Left justified: '{left_justified}'")
    print(f"Right justified: '{right_justified}'")
    print(f"Zero filled: '{zero_filled}'")
    
    return {
        "cleaned": cleaned,
        "words": words,
        "text_checks": text_checks,
        "split_results": {
            "comma": split_comma,
            "lines": split_lines,
            "partition": partition_result
        },
        "joined_results": {
            "space": joined_space,
            "dash": joined_dash,
            "comma": joined_comma
        },
        "search_results": {
            "find": find_result,
            "count": count_result,
            "starts_with": starts_with,
            "ends_with": ends_with
        }
    }

def character_converters():
    """Convert between characters and ASCII/Unicode codes."""
    print("\\n=== Character Conversion Operations ===")
    
    # ASCII character conversions
    print("ASCII Character Conversions:")
    
    # Convert characters to ASCII codes
    chars = ['A', 'Z', 'a', 'z', '0', '9', ' ', '!']
    char_codes = [(char, ord(char)) for char in chars]
    
    print("Character to ASCII code:")
    for char, code in char_codes:
        print(f"  '{char}' -> {code}")
    
    # Convert ASCII codes back to characters
    codes = [65, 90, 97, 122, 48, 57, 32, 33]
    code_chars = [(code, chr(code)) for code in codes]
    
    print("\\nASCII code to character:")
    for code, char in code_chars:
        print(f"  {code} -> '{char}'")
    
    # Generate character ranges
    uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    digits = [chr(i) for i in range(ord('0'), ord('9') + 1)]
    
    print(f"\\nUppercase letters: {uppercase_letters}")
    print(f"Lowercase letters: {lowercase_letters}")
    print(f"Digits: {digits}")
    
    # Unicode character conversions
    print("\\nUnicode Character Conversions:")
    
    unicode_chars = ['€', '©', '®', '™', '∞', '→', '←', '↑', '↓', '♠', '♥', '♦', '♣']
    unicode_codes = [(char, ord(char), hex(ord(char))) for char in unicode_chars]
    
    print("Unicode character to code:")
    for char, decimal, hexadecimal in unicode_codes:
        print(f"  '{char}' -> {decimal} (0x{hexadecimal[2:].upper()})")
    
    # Unicode normalization
    print("\\nUnicode Normalization:")
    
    # Text with accented characters
    accented_text = "café naïve résumé"
    print(f"Original: '{accented_text}'")
    
    # Different normalization forms
    nfc = unicodedata.normalize('NFC', accented_text)
    nfd = unicodedata.normalize('NFD', accented_text)
    nfkc = unicodedata.normalize('NFKC', accented_text)
    nfkd = unicodedata.normalize('NFKD', accented_text)
    
    print(f"NFC:  '{nfc}' (length: {len(nfc)})")
    print(f"NFD:  '{nfd}' (length: {len(nfd)})")
    print(f"NFKC: '{nfkc}' (length: {len(nfkc)})")
    print(f"NFKD: '{nfkd}' (length: {len(nfkd)})")
    
    # Character categories
    print("\\nCharacter Categories:")
    sample_chars = ['A', 'a', '5', ' ', '!', '€', '\\n', '\\t']
    
    for char in sample_chars:
        category = unicodedata.category(char)
        name = unicodedata.name(char, 'NO NAME')
        print(f"  '{repr(char)}' -> Category: {category}, Name: {name}")
    
    # Create lookup tables
    ascii_to_char = {i: chr(i) for i in range(128)}
    char_to_ascii = {chr(i): i for i in range(128)}
    
    print(f"\\nCreated ASCII lookup tables with {len(ascii_to_char)} entries")
    
    return {
        "char_codes": char_codes,
        "code_chars": code_chars,
        "character_ranges": {
            "uppercase": uppercase_letters,
            "lowercase": lowercase_letters,
            "digits": digits
        },
        "unicode_codes": unicode_codes,
        "normalized_text": {
            "nfc": nfc,
            "nfd": nfd,
            "nfkc": nfkc,
            "nfkd": nfkd
        },
        "lookup_tables": {
            "ascii_to_char": ascii_to_char,
            "char_to_ascii": char_to_ascii
        }
    }

def encoding_handlers():
    """Handle text encoding and decoding operations."""
    print("\\n=== Encoding and Decoding Operations ===")
    
    # String to bytes conversion
    sample_text = "Hello, 世界! 🌍 Café résumé"
    print(f"Original text: '{sample_text}'")
    
    # Different encoding formats
    encodings = ['utf-8', 'utf-16', 'utf-32', 'ascii', 'latin-1']
    encoded_results = {}
    
    print("\\nEncoding to bytes:")
    for encoding in encodings:
        try:
            encoded = sample_text.encode(encoding)
            encoded_results[encoding] = encoded
            print(f"  {encoding}: {len(encoded)} bytes -> {encoded[:30]}{'...' if len(encoded) > 30 else ''}")
        except UnicodeEncodeError as e:
            print(f"  {encoding}: ERROR - {e}")
            encoded_results[encoding] = None
    
    # Decoding back to strings
    print("\\nDecoding back to strings:")
    for encoding, encoded_bytes in encoded_results.items():
        if encoded_bytes is not None:
            try:
                decoded = encoded_bytes.decode(encoding)
                match = decoded == sample_text
                print(f"  {encoding}: Match = {match}")
            except UnicodeDecodeError as e:
                print(f"  {encoding}: ERROR - {e}")
    
    # Bytes object creation and manipulation
    print("\\nBytes Object Operations:")
    
    # Create bytes objects
    bytes_from_list = bytes([72, 101, 108, 108, 111])  # "Hello"
    bytes_from_string = b"Hello, World!"
    bytes_from_range = bytes(range(10))
    
    print(f"Bytes from list: {bytes_from_list} -> '{bytes_from_list.decode()}'")
    print(f"Bytes literal: {bytes_from_string} -> '{bytes_from_string.decode()}'")
    print(f"Bytes from range: {bytes_from_range}")
    
    # Bytes operations
    bytes_upper = bytes_from_string.upper()
    bytes_replace = bytes_from_string.replace(b"World", b"Python")
    bytes_split = bytes_from_string.split(b", ")
    bytes_join = b" | ".join([b"apple", b"banana", b"cherry"])
    
    print(f"\\nBytes operations:")
    print(f"  Upper: {bytes_upper}")
    print(f"  Replace: {bytes_replace}")
    print(f"  Split: {bytes_split}")
    print(f"  Join: {bytes_join}")
    
    # Hex representation
    print("\\nHex Representation:")
    sample_bytes = "Hello! 🚀".encode('utf-8')
    hex_string = sample_bytes.hex()
    hex_with_sep = sample_bytes.hex(' ')
    hex_upper = sample_bytes.hex().upper()
    
    print(f"Original bytes: {sample_bytes}")
    print(f"Hex string: {hex_string}")
    print(f"Hex with separator: {hex_with_sep}")
    print(f"Hex uppercase: {hex_upper}")
    
    # Convert hex back to bytes
    bytes_from_hex = bytes.fromhex(hex_string)
    decoded_from_hex = bytes_from_hex.decode('utf-8')
    
    print(f"Bytes from hex: {bytes_from_hex}")
    print(f"Decoded: '{decoded_from_hex}'")
    
    # Error handling strategies
    print("\\nError Handling Strategies:")
    
    # Text with problematic characters
    problematic_text = "Hello 🌍 World"
    
    # Different error handling modes
    error_modes = ['strict', 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace']
    
    for mode in error_modes:
        try:
            encoded = problematic_text.encode('ascii', errors=mode)
            print(f"  {mode}: {encoded}")
        except UnicodeEncodeError as e:
            print(f"  {mode}: ERROR - {e}")
    
    return {
        "encoded_results": {k: v for k, v in encoded_results.items() if v is not None},
        "bytes_operations": {
            "from_list": bytes_from_list,
            "from_string": bytes_from_string,
            "upper": bytes_upper,
            "replace": bytes_replace,
            "split": bytes_split,
            "join": bytes_join
        },
        "hex_operations": {
            "hex_string": hex_string,
            "hex_with_sep": hex_with_sep,
            "bytes_from_hex": bytes_from_hex,
            "decoded_from_hex": decoded_from_hex
        }
    }

def string_formatters():
    """Format strings using various methods."""
    print("\\n=== String Formatting Operations ===")
    
    # Sample data for formatting
    name = "Alice"
    age = 30
    salary = 75000.50
    pi = 3.14159265359
    
    # Old-style % formatting
    print("Old-style % Formatting:")
    
    old_format_1 = "Hello, %s! You are %d years old." % (name, age)
    old_format_2 = "Salary: $%.2f" % salary
    old_format_3 = "Pi: %.4f" % pi
    
    print(f"  Basic: {old_format_1}")
    print(f"  Float precision: {old_format_2}")
    print(f"  Scientific: {old_format_3}")
    
    # .format() method
    print("\\n.format() Method:")
    
    format_1 = "Hello, {}! You are {} years old.".format(name, age)
    format_2 = "Hello, {0}! You are {1} years old.".format(name, age)
    format_3 = "Hello, {name}! You are {age} years old.".format(name=name, age=age)
    format_4 = "Salary: ${:.2f}".format(salary)
    format_5 = "Pi: {:.6f}".format(pi)
    
    print(f"  Positional: {format_1}")
    print(f"  Indexed: {format_2}")
    print(f"  Named: {format_3}")
    print(f"  Float precision: {format_4}")
    print(f"  More precision: {format_5}")
    
    # f-string formatting (Python 3.6+)
    print("\\nf-string Formatting:")
    
    f_format_1 = f"Hello, {name}! You are {age} years old."
    f_format_2 = f"Salary: ${salary:.2f}"
    f_format_3 = f"Pi: {pi:.6f}"
    f_format_4 = f"Age in hex: {age:#x}"
    f_format_5 = f"Percentage: {0.85:.1%}"
    
    print(f"  Basic: {f_format_1}")
    print(f"  Float precision: {f_format_2}")
    print(f"  Scientific: {f_format_3}")
    print(f"  Hexadecimal: {f_format_4}")
    print(f"  Percentage: {f_format_5}")
    
    # Advanced formatting options
    print("\\nAdvanced Formatting:")
    
    # Number formatting
    large_number = 1234567.89
    
    formatted_numbers = {
        "comma_separator": f"{large_number:,}",
        "underscore_separator": f"{large_number:_}",
        "scientific": f"{large_number:.2e}",
        "fixed_width": f"{large_number:15.2f}",
        "zero_padded": f"{age:05d}",
        "signed": f"{age:+d}"
    }
    
    print("Number formatting:")
    for style, result in formatted_numbers.items():
        print(f"  {style}: '{result}'")
    
    # String alignment
    text = "Python"
    width = 20
    
    alignment_examples = {
        "left": f"'{text:<{width}}'",
        "right": f"'{text:>{width}}'",
        "center": f"'{text:^{width}}'",
        "left_fill": f"'{text:-<{width}}'",
        "right_fill": f"'{text:*>{width}}'",
        "center_fill": f"'{text:={width}}'",
    }
    
    print("\\nString alignment:")
    for style, result in alignment_examples.items():
        print(f"  {style}: {result}")
    
    # Date formatting
    from datetime import datetime
    now = datetime.now()
    
    date_formats = {
        "iso": f"{now:%Y-%m-%d}",
        "us_format": f"{now:%m/%d/%Y}",
        "long_format": f"{now:%B %d, %Y}",
        "time_24h": f"{now:%H:%M:%S}",
        "time_12h": f"{now:%I:%M:%S %p}",
        "full": f"{now:%A, %B %d, %Y at %I:%M %p}"
    }
    
    print("\\nDate formatting:")
    for style, result in date_formats.items():
        print(f"  {style}: {result}")
    
    # Template strings
    from string import Template
    
    template = Template("Hello, $name! Your balance is $$$amount.")
    template_result = template.substitute(name="Bob", amount="1,234.56")
    
    print(f"\\nTemplate string: {template_result}")
    
    # Safe template substitution
    template_safe = Template("Hello, $name! Your $item costs $$$price.")
    try:
        safe_result = template_safe.safe_substitute(name="Charlie", price="99.99")
        print(f"Safe template (missing item): {safe_result}")
    except KeyError as e:
        print(f"Template error: {e}")
    
    return {
        "old_style": [old_format_1, old_format_2, old_format_3],
        "format_method": [format_1, format_2, format_3, format_4, format_5],
        "f_strings": [f_format_1, f_format_2, f_format_3, f_format_4, f_format_5],
        "number_formatting": formatted_numbers,
        "alignment": alignment_examples,
        "date_formats": date_formats,
        "template_result": template_result
    }

def sequence_manipulators():
    """Manipulate sequences using built-in functions."""
    print("\\n=== Sequence Manipulation Operations ===")
    
    # Working with various sequence types
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30, 40, 50)
    sample_string = "Hello"
    sample_range = range(5, 15)
    
    print(f"Sample list: {sample_list}")
    print(f"Sample tuple: {sample_tuple}")
    print(f"Sample string: '{sample_string}'")
    print(f"Sample range: {list(sample_range)}")
    
    # Sequence functions
    print("\\nSequence Functions:")
    
    # Length
    lengths = {
        "list": len(sample_list),
        "tuple": len(sample_tuple),
        "string": len(sample_string),
        "range": len(sample_range)
    }
    
    print(f"Lengths: {lengths}")
    
    # Min and Max
    min_max = {
        "list_min": min(sample_list),
        "list_max": max(sample_list),
        "tuple_min": min(sample_tuple),
        "tuple_max": max(sample_tuple),
        "string_min": min(sample_string),
        "string_max": max(sample_string)
    }
    
    print(f"Min/Max values: {min_max}")
    
    # Sum (for numeric sequences)
    sums = {
        "list_sum": sum(sample_list),
        "tuple_sum": sum(sample_tuple),
        "range_sum": sum(sample_range)
    }
    
    print(f"Sums: {sums}")
    
    # Any and All
    bool_tests = [True, True, True]
    mixed_tests = [True, False, True]
    empty_tests = []
    
    any_all_results = {
        "any_all_true": (any(bool_tests), all(bool_tests)),
        "any_all_mixed": (any(mixed_tests), all(mixed_tests)),
        "any_all_empty": (any(empty_tests), all(empty_tests))
    }
    
    print(f"\\nAny/All results: {any_all_results}")
    
    # Enumerate
    print("\\nEnumerate Examples:")
    
    fruits = ["apple", "banana", "cherry"]
    
    # Basic enumerate
    enum_basic = list(enumerate(fruits))
    print(f"Basic enumerate: {enum_basic}")
    
    # Enumerate with start
    enum_start = list(enumerate(fruits, start=1))
    print(f"Enumerate with start=1: {enum_start}")
    
    # Enumerate in loop simulation
    enum_loop = [(i, fruit.upper()) for i, fruit in enumerate(fruits)]
    print(f"Enumerate with transformation: {enum_loop}")
    
    # Zip
    print("\\nZip Examples:")
    
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    cities = ["NYC", "LA", "Chicago"]
    
    # Basic zip
    zip_basic = list(zip(names, ages))
    print(f"Zip names and ages: {zip_basic}")
    
    # Zip multiple sequences
    zip_multiple = list(zip(names, ages, cities))
    print(f"Zip three sequences: {zip_multiple}")
    
    # Zip with different lengths
    short_list = [1, 2]
    long_list = [10, 20, 30, 40, 50]
    zip_different = list(zip(short_list, long_list))
    print(f"Zip different lengths: {zip_different}")
    
    # Unzip (transpose)
    paired_data = [(1, 'a'), (2, 'b'), (3, 'c')]
    unzipped = list(zip(*paired_data))
    print(f"Unzip: {unzipped}")
    
    # Advanced sequence operations
    print("\\nAdvanced Sequence Operations:")
    
    # Create sequences
    created_sequences = {
        "list_from_string": list(sample_string),
        "tuple_from_list": tuple(sample_list),
        "set_from_list": set([1, 2, 2, 3, 3, 4]),
        "dict_from_pairs": dict(zip(names[:3], ages[:3]))
    }
    
    print(f"Created sequences: {created_sequences}")
    
    # Sequence slicing and indexing
    text = "Programming"
    
    slicing_examples = {
        "first_three": text[:3],
        "last_three": text[-3:],
        "every_second": text[::2],
        "reversed": text[::-1],
        "middle": text[2:8],
        "step_reverse": text[::-2]
    }
    
    print(f"\\nSlicing examples for '{text}': {slicing_examples}")
    
    # Sequence membership testing
    test_values = [2, 10, 'l', 'z']
    membership_results = {}
    
    for value in test_values:
        membership_results[value] = {
            "in_list": value in sample_list,
            "in_tuple": value in sample_tuple,
            "in_string": value in sample_string
        }
    
    print(f"\\nMembership testing: {membership_results}")
    
    return {
        "lengths": lengths,
        "min_max": min_max,
        "sums": sums,
        "any_all_results": any_all_results,
        "enumerate_results": {
            "basic": enum_basic,
            "start": enum_start,
            "loop": enum_loop
        },
        "zip_results": {
            "basic": zip_basic,
            "multiple": zip_multiple,
            "different": zip_different,
            "unzipped": unzipped
        },
        "created_sequences": created_sequences,
        "slicing_examples": slicing_examples,
        "membership_results": membership_results
    }

# Main execution
if __name__ == "__main__":
    print("=== Built-in String and Sequence Functions ===")
    
    print("\\n1. String Processing:")
    string_results = string_processors()
    
    print("\\n2. Character Conversion:")
    char_results = character_converters()
    
    print("\\n3. Encoding/Decoding:")
    encoding_results = encoding_handlers()
    
    print("\\n4. String Formatting:")
    format_results = string_formatters()
    
    print("\\n5. Sequence Manipulation:")
    sequence_results = sequence_manipulators()
    
    print("\\n" + "="*60)
    print("=== STRING AND SEQUENCE OPERATIONS COMPLETE ===")
    print("✓ String processing and manipulation")
    print("✓ Character and Unicode conversions")
    print("✓ Text encoding and decoding")
    print("✓ String formatting methods")
    print("✓ Sequence operations and manipulation")
    print("✓ Advanced string and sequence techniques")
```

## Hints

- Use `.strip()`, `.split()`, and `.join()` for basic string processing
- `ord()` and `chr()` convert between characters and ASCII codes
- Use `.encode()` and `.decode()` for text encoding operations
- f-strings (f"") are the preferred formatting method in modern Python
- `enumerate()` and `zip()` are essential for working with sequences

## Test Cases

Your functions should handle:

1. Various string cleaning and transformation operations
2. ASCII and Unicode character conversions correctly
3. Multiple text encodings (UTF-8, UTF-16, ASCII, etc.)
4. Different string formatting methods with proper syntax
5. Complex sequence manipulations and transformations

## Bonus Challenge

Create a text processing pipeline that handles multilingual text, performs encoding detection, and generates formatted reports with statistics!
