# Advanced String Algorithms - Test 19

**Difficulty:** ⭐⭐⭐⭐ (Medium-Hard)

**Related Topics:** String Algorithms, Pattern Matching, Text Processing

## Objectives

- Implement sophisticated string algorithms
- Master pattern matching and text analysis
- Work with complex string transformations
- Optimize string operations for performance

## Description

Develop advanced string processing algorithms that can handle complex text analysis tasks. This includes implementing string matching algorithms, text compression, and advanced pattern recognition systems.

## Examples

```python
# Advanced pattern matching
text = "abcabcabcabc"
pattern = "abcabc"
positions = find_all_overlapping_matches(text, pattern)
print(positions)  # [0, 3, 6]

# String compression using run-length encoding
original = "aaabbccccdddd"
compressed = compress_string(original)
print(compressed)  # "a3b2c4d4"
decompressed = decompress_string(compressed)
print(decompressed)  # "aaabbccccdddd"

# Advanced string transformation
text = "The Quick Brown Fox"
result = advanced_caesar_cipher(text, shift=3, preserve_case=True)
print(result)  # "Wkh Txlfn Eurzq Ira"
```

## Your Tasks

1. **find_all_overlapping_matches(text, pattern)** - Find all pattern occurrences (including overlapping)
2. **compress_string(text)** - Implement run-length encoding compression
3. **decompress_string(compressed)** - Decompress run-length encoded string
4. **advanced_caesar_cipher(text, shift, preserve_case=True)** - Enhanced Caesar cipher
5. **longest_palindromic_substring(text)** - Find longest palindrome in string
6. **string_distance(str1, str2)** - Calculate edit distance between strings
7. **find_repeated_substrings(text, min_length=2)** - Find all repeated substrings
8. **advanced_string_search(text, patterns)** - Multi-pattern string matching
9. **text_similarity_score(text1, text2)** - Calculate text similarity percentage
10. **optimize_string_operations(operations)** - Efficiently apply multiple string operations

## Hints

- Use sliding window technique for pattern matching
- Implement efficient algorithms like KMP for string searching
- Dynamic programming helps with edit distance calculations
- Consider using hash tables for pattern storage
- String slicing and indexing are crucial for substring operations
- Think about time complexity when dealing with large texts
- Caching results can improve performance for repeated operations

## Test Cases

```python
# Comprehensive test data
test_cases = {
    'pattern_matching': [
        ("abababa", "aba", [0, 2, 4]),
        ("aaaaaa", "aa", [0, 1, 2, 3, 4]),
        ("hello world", "ll", [2])
    ],
    'compression': [
        ("aabbcc", "a2b2c2"),
        ("abcdef", "a1b1c1d1e1f1"),
        ("aaaa", "a4")
    ],
    'cipher': [
        ("ABC", 1, "BCD"),
        ("xyz", 3, "abc"),
        ("Hello World!", 13, "Uryyb Jbeyq!")
    ],
    'palindromes': [
        ("racecar", "racecar"),
        ("hello", "ll"),
        ("abcdef", "a")
    ],
    'edit_distance': [
        ("kitten", "sitting", 3),
        ("saturday", "sunday", 3),
        ("abc", "abc", 0)
    ]
}
```

## Advanced Challenges

- Implement Boyer-Moore string search algorithm
- Add support for regex-like pattern matching
- Create a spell checker using edit distance
- Implement suffix array for advanced string operations
- Add text fingerprinting for plagiarism detection
- Create a string tokenizer with custom rules
- Implement Huffman coding for text compression

## Performance Requirements

- Pattern matching should handle texts up to 10,000 characters efficiently
- Compression should achieve reasonable ratios for repetitive text
- Edit distance calculation should work for strings up to 1,000 characters
- Multi-pattern search should handle up to 100 patterns simultaneously

Remember: Focus on algorithm efficiency and handle edge cases like empty strings, special characters, and Unicode text!
