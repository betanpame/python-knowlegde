# List String Operations - Practice 11

**Difficulty:** ⭐ (Very Easy)

**Related Topics:** String-List Conversion, Join, Split

## Objectives

- Learn to convert between strings and lists
- Practice joining list elements into strings
- Understand splitting strings into lists

## Description

Master the conversion between strings and lists, which is essential for text processing and data manipulation.

## Examples

```python
words = ["Hello", "World", "Python"]
print(join_with_spaces(words))           # "Hello World Python"
print(join_with_commas(words))           # "Hello,World,Python"

sentence = "Python is awesome"
print(split_into_words(sentence))        # ["Python", "is", "awesome"]
```

## Your Tasks

1. **join_with_spaces(word_list)** - Join words with spaces
2. **join_with_commas(word_list)** - Join words with commas
3. **join_with_custom_separator(word_list, separator)** - Join with custom separator
4. **split_into_words(sentence)** - Split sentence into word list
5. **split_by_character(text, char)** - Split text by specific character
6. **convert_to_string_list(number_list)** - Convert numbers to strings
7. **convert_to_number_list(string_list)** - Convert string numbers to integers
8. **create_csv_line(data_list)** - Create comma-separated values string

Remember: `join()` combines list elements, `split()` breaks strings apart!