# Python Knowledge Curriculum

## 1. Python Data Types and Methods

### 1.1 Strings and String Methods

- String manipulation: `.split()`, `.join()`, `.strip()`, `.replace()`, `.find()`
- String formatting: f-strings, `.format()`, % formatting
- String validation: `.isdigit()`, `.isalpha()`, `.isupper()`, `.islower()`

### 1.2 Lists and List Methods

- Mutable sequences: creation, indexing, slicing
- List methods: `.append()`, `.remove()`, `.pop()`, `.insert()`, `.extend()`
- List comprehensions and operations
- Accessing last index with negative indexing (`list[-1]`)

### 1.3 Tuples and Tuple Methods

- Immutable sequences: creation, indexing, slicing
- Tuple methods: `.count()`, `.index()`
- Differences between lists and tuples (mutability)

### 1.4 Arrays (Alternative Libraries)

- **Built-in**: `list` (dynamic arrays)
- **NumPy**: `numpy.array` (numerical computing)
- **Array module**: `array.array` (efficient numerical arrays)

## 2. Control Flow and Operators

### 2.1 Conditional Operators

- Identity operators: `is`, `is not`
- Membership operators: `in`, `not in`
- Logical operators: `and`, `or`, `not`

### 2.2 Loop Control Statements

- `break`: exit loop completely
- `continue`: skip current iteration
- `pass`: placeholder statement (does nothing)

## 3. Functions and Parameters

### 3.1 Function Definition and Usage

- Function syntax with `def`
- Return statements and function scope
- Function documentation with docstrings

### 3.2 Advanced Function Parameters

- `*args`: variable-length positional arguments
- `**kwargs`: variable-length keyword arguments
- Default parameters and parameter ordering

## 4. Modules and Packages

### 4.1 Built-in Modules

- **Math operations**: `math`, `statistics`, `random`
- **Date/Time**: `datetime`, `time`, `calendar`
- **System operations**: `os`, `sys`, `pathlib`
- **Data serialization**: `json`, `pickle`, `csv`

### 4.2 Package Management

- Understanding packages vs modules
- Import statements: `import`, `from...import`, `as`
- Package structure and `__init__.py`

## 5. File Operations and System Interaction

### 5.1 File Handling

- File opening modes: `r`, `w`, `a`, `x`, `b`, `t`
- Context managers: `with open()` statement
- File paths: absolute vs relative, cross-platform compatibility

### 5.2 Operating System Module

- **File operations**: `os.remove()`, `os.rename()`, `os.path`
- **Directory operations**: `os.mkdir()`, `os.listdir()`, `os.getcwd()`
- **Modern alternative**: `pathlib` module

## 6. Object-Oriented Programming (OOP)

### 6.1 Classes and Objects

- Class definition with `class`
- Instance attributes and methods
- Constructor method `__init__()`

### 6.2 OOP Principles

- **Inheritance**: parent-child class relationships
- **Encapsulation**: data hiding and access control
- **Polymorphism**: method overriding
- Private attributes (name mangling with `_` and `__`)

## 7. Data Science and Numerical Computing

### 7.1 NumPy

- Array operations and mathematical functions
- Percentage calculations: `(part/total) * 100`
- Statistical operations and array manipulations

### 7.2 Pandas

- DataFrames and Series
- Data manipulation and analysis
- Reading/writing various file formats

### 7.3 Data Processing

- Chunking large datasets for memory efficiency
- Processing data in manageable blocks

## 8. Web Technologies and APIs

### 8.1 Web Scraping Libraries

- **Requests**: HTTP library for API calls and web requests
- **BeautifulSoup**: HTML/XML parsing and extraction
- **Selenium**: Browser automation for dynamic content
- **Scrapy**: Framework for large-scale web scraping

### 8.2 Image and File Download

- **urllib.request**: Built-in module for downloading files
- **requests**: More user-friendly HTTP library
- **pathlib**: Modern path handling

### 8.3 Data Extraction Examples

- IMDb top movies scraping
- Image downloading from URLs
- API data consumption

## 9. Built-in Functions and Utilities

### 9.1 Essential Built-in Functions

- `len()`: get length of sequences
- `type()`: get object type
- `range()`: generate number sequences
- `enumerate()`: get index-value pairs
- `zip()`: combine multiple iterables

### 9.2 Memory-Efficient Programming

- Reading large files in chunks
- Generator functions and expressions
- Iterator protocol and lazy evaluation
