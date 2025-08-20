# Simple Class with Constructor - Practice 2

**Difficulty:** ⭐ (Very Easy)

## Description

Learn to create a class with a constructor (`__init__` method) to initialize object attributes.

## Objectives

- Understand the `__init__` method
- Initialize object attributes
- Create and use simple objects
- Practice basic object creation

## Your Tasks

1. **create_book_class()** - Create a Book class with title and author
2. **initialize_attributes()** - Use constructor to set attributes
3. **create_multiple_books()** - Create several book objects
4. **display_book_info()** - Show book information

## Example

```python
class Book:
    """A simple Book class."""
    
    def __init__(self, title, author, pages=0):
        """Initialize a Book with title, author, and optional pages."""
        self.title = title
        self.author = author
        self.pages = pages
        self.is_open = False
    
    def open_book(self):
        """Open the book."""
        self.is_open = True
        return f"Opening '{self.title}' by {self.author}"
    
    def close_book(self):
        """Close the book."""
        self.is_open = False
        return f"Closing '{self.title}'"
    
    def get_info(self):
        """Get book information."""
        status = "open" if self.is_open else "closed"
        return f"'{self.title}' by {self.author} ({self.pages} pages) - {status}"

# Example usage
def create_book_class():
    """Create and use Book objects."""
    # Create books
    book1 = Book("Python Programming", "John Doe", 300)
    book2 = Book("Data Science", "Jane Smith", 450)
    book3 = Book("Web Development", "Bob Johnson")  # No pages specified
    
    # Use the books
    print(book1.open_book())
    print(book1.get_info())
    
    print(book2.get_info())
    print(book2.open_book())
    print(book2.get_info())
    
    print(book3.get_info())
    book3.pages = 250  # Set pages later
    print(book3.get_info())
    
    return [book1, book2, book3]

# Practice the class
if __name__ == "__main__":
    books = create_book_class()
    
    # Display all books
    print("\nAll books:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book.get_info()}")
```

## Hints

- `__init__` is called automatically when creating an object
- Use default parameters for optional attributes
- `self` refers to the current object instance
- Initialize all attributes in the constructor

## Practice Cases

Your Book class should:
- Initialize with title, author, and optional pages
- Track whether the book is open or closed
- Provide methods to open and close the book
- Display comprehensive book information

## Bonus Challenge

Add a `read_pages(num_pages)` method that tracks current page position and prevents reading beyond the total pages!