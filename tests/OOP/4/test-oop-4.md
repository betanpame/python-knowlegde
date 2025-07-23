# String Representation Methods - Test 4

**Difficulty:** ⭐ (Very Easy)

## Description

Learn to implement `__str__` and `__repr__` methods to control how objects are displayed.

## Objectives

- Implement the `__str__` method for user-friendly output
- Implement the `__repr__` method for developer representation
- Understand when each method is called
- Practice string formatting in methods

## Your Tasks

1. **create_student_class()** - Create a Student class with string methods
2. **implement_str_method()** - Add user-friendly string representation
3. **implement_repr_method()** - Add developer string representation
4. **test_representations()** - Test both string methods

## Example

```python
class Student:
    """A student class with string representation methods."""
    
    def __init__(self, name, age, grade, student_id):
        """Initialize a Student."""
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id
        self.courses = []
    
    def add_course(self, course):
        """Add a course to the student's schedule."""
        if course not in self.courses:
            self.courses.append(course)
            return f"Added {course} to {self.name}'s schedule"
        return f"{course} already in schedule"
    
    def remove_course(self, course):
        """Remove a course from the student's schedule."""
        if course in self.courses:
            self.courses.remove(course)
            return f"Removed {course} from {self.name}'s schedule"
        return f"{course} not found in schedule"
    
    def __str__(self):
        """User-friendly string representation."""
        course_list = ", ".join(self.courses) if self.courses else "No courses"
        return f"{self.name} (Age: {self.age}, Grade: {self.grade}) - Courses: {course_list}"
    
    def __repr__(self):
        """Developer string representation."""
        return f"Student(name='{self.name}', age={self.age}, grade='{self.grade}', student_id='{self.student_id}')"

# Example usage
def create_student_class():
    """Create and use Student objects."""
    # Create students
    student1 = Student("Alice Johnson", 16, "10th", "STU001")
    student2 = Student("Bob Smith", 17, "11th", "STU002")
    
    # Add courses
    print(student1.add_course("Mathematics"))
    print(student1.add_course("Physics"))
    print(student1.add_course("Chemistry"))
    
    print(student2.add_course("Biology"))
    print(student2.add_course("English"))
    
    # Test string representations
    print("\n--- Using str() (user-friendly) ---")
    print(str(student1))
    print(str(student2))
    
    print("\n--- Using repr() (developer representation) ---")
    print(repr(student1))
    print(repr(student2))
    
    # When you just print the object, it uses __str__
    print("\n--- Direct printing (uses __str__) ---")
    print(student1)
    print(student2)
    
    # In a list, objects use __repr__
    print("\n--- In a list (uses __repr__) ---")
    students = [student1, student2]
    print(students)
    
    return students

# Test the class
if __name__ == "__main__":
    students = create_student_class()
    
    # Demonstrate the difference
    print("\n--- Demonstrating the difference ---")
    for student in students:
        print(f"str():  {str(student)}")
        print(f"repr(): {repr(student)}")
        print()
```

## Hints

- `__str__` should return a human-readable string
- `__repr__` should return a string that could recreate the object
- `print()` automatically calls `__str__`
- Lists and containers use `__repr__` for their elements

## Test Cases

Your Student class should:

- Display user-friendly information with `__str__`
- Show technical details with `__repr__`
- Handle students with and without courses
- Work correctly when printed directly or in collections

## Bonus Challenge

Add a `__len__` method that returns the number of courses, and a `__contains__` method to check if a course is in the student's schedule!
