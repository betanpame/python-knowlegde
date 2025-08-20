# Practice File Operations 21: File Handling and Context Managers

**Difficulty:** ⭐⭐⭐☆☆ (Medium)

**Related Topics:** File operations, context managers (with open), file modes, os module

## Objective

Master file operations, different file modes, and the operating system module for file management.

## Requirements

Create functions that demonstrate comprehensive file handling:

1. `file_mode_demonstration()` - Show different file opening modes
2. `safe_file_operations(filename, content)` - Use context managers properly
3. `file_system_operations()` - Use os module for file/directory operations
4. `text_file_processor(input_file, output_file)` - Process text files line by line
5. `binary_file_handler()` - Work with binary files

## File Modes to Demonstrate

- `'r'` - Read mode (default)
- `'w'` - Write mode (overwrites existing file)
- `'a'` - Append mode
- `'x'` - Exclusive creation mode
- `'b'` - Binary mode
- `'t'` - Text mode (default)

## Examples

```python
# Safe file writing with context manager
safe_file_operations("test.txt", "Hello, World!")

# File system operations
file_system_operations()  # Creates, lists, renames, deletes files
```

## Hints

- Always use `with open()` for automatic file closing
- Handle `FileNotFoundError` and `PermissionError`
- Use `os.path.exists()` to check file existence
- Use `pathlib` module as modern alternative to os.path
- Be careful with binary vs text modes
- Use appropriate encoding (utf-8) for text files

## Practice Cases

Your functions should handle:

1. Creating, reading, writing, and deleting files
2. Working with both text and binary files
3. Handling file permissions and access errors
4. Cross-platform path handling
5. Large file processing with memory efficiency