# Method Overriding - Test 7

**Difficulty:** ⭐ (Very Easy)

## Description

Learn how child classes can override parent methods to provide specialized behavior while still accessing parent functionality.

## Objectives

- Override parent methods in child classes
- Use `super()` to call parent methods from overridden methods
- Understand when and why to override methods
- Practice extending parent functionality

## Your Tasks

1. **create_employee_class()** - Create base Employee class
2. **create_manager_class()** - Create Manager class with overridden methods
3. **create_developer_class()** - Create Developer class with overridden methods
4. **demonstrate_overriding()** - Show how overriding works

## Example

```python
class Employee:
    """Base Employee class."""
    
    def __init__(self, name, employee_id, salary):
        """Initialize an Employee."""
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.department = "General"
    
    def work(self):
        """Basic work method."""
        return f"{self.name} is working"
    
    def get_salary(self):
        """Get employee salary."""
        return self.salary
    
    def get_info(self):
        """Get employee information."""
        return f"{self.name} (ID: {self.employee_id}) - Salary: ${self.salary}"
    
    def take_break(self):
        """Take a break."""
        return f"{self.name} is taking a break"

class Manager(Employee):
    """Manager class that inherits from Employee."""
    
    def __init__(self, name, employee_id, salary, team_size):
        """Initialize a Manager."""
        super().__init__(name, employee_id, salary)  # Call parent constructor
        self.team_size = team_size
        self.department = "Management"
    
    def work(self):
        """Override work method for managers."""
        # Call parent method and extend it
        base_work = super().work()
        return f"{base_work} and managing {self.team_size} team members"
    
    def get_info(self):
        """Override get_info to include team size."""
        base_info = super().get_info()
        return f"{base_info} - Team Size: {self.team_size}"
    
    def hold_meeting(self):
        """Manager-specific method."""
        return f"{self.name} is holding a team meeting"
    
    def get_salary(self):
        """Override salary calculation for managers (bonus for team size)."""
        base_salary = super().get_salary()
        bonus = self.team_size * 1000  # $1000 bonus per team member
        return base_salary + bonus

class Developer(Employee):
    """Developer class that inherits from Employee."""
    
    def __init__(self, name, employee_id, salary, programming_languages):
        """Initialize a Developer."""
        super().__init__(name, employee_id, salary)
        self.programming_languages = programming_languages
        self.department = "Engineering"
    
    def work(self):
        """Override work method for developers."""
        base_work = super().work()
        languages = ", ".join(self.programming_languages[:2])  # Show first 2 languages
        return f"{base_work} with {languages}"
    
    def get_info(self):
        """Override get_info to include programming languages."""
        base_info = super().get_info()
        lang_count = len(self.programming_languages)
        return f"{base_info} - Languages: {lang_count}"
    
    def code_review(self):
        """Developer-specific method."""
        return f"{self.name} is reviewing code"
    
    def take_break(self):
        """Override break method for developers."""
        base_break = super().take_break()
        return f"{base_break} (debugging in background)"

# Example usage
def create_employee_class():
    """Create and use Employee inheritance with method overriding."""
    # Create employees
    regular_employee = Employee("John Doe", "E001", 50000)
    manager = Manager("Alice Smith", "M001", 80000, 5)
    developer = Developer("Bob Johnson", "D001", 70000, ["Python", "JavaScript", "Go"])
    
    employees = [regular_employee, manager, developer]
    
    # Test work method (overridden in child classes)
    print("Work methods:")
    for emp in employees:
        print(f"- {emp.work()}")
    
    # Test get_info method (overridden in child classes)
    print(f"\nEmployee information:")
    for emp in employees:
        print(f"- {emp.get_info()}")
    
    # Test salary method (overridden in Manager)
    print(f"\nSalary calculations:")
    for emp in employees:
        print(f"- {emp.name}: ${emp.get_salary()}")
    
    # Test take_break method (overridden in Developer)
    print(f"\nBreak time:")
    for emp in employees:
        print(f"- {emp.take_break()}")
    
    # Test specific methods for each class
    print(f"\nSpecific methods:")
    print(f"- {manager.hold_meeting()}")
    print(f"- {developer.code_review()}")
    
    return employees

# Test the classes
if __name__ == "__main__":
    employees = create_employee_class()
    
    # Show department assignments
    print(f"\nDepartment assignments:")
    for emp in employees:
        print(f"- {emp.name}: {emp.department}")
    
    # Demonstrate that overridden methods still have access to parent
    print(f"\nDemonstrating super() usage:")
    dev = employees[2]  # Developer
    print(f"Developer languages: {', '.join(dev.programming_languages)}")
```

## Hints

- Use the same method name in child class to override
- Call `super().method_name()` to access parent method
- You can extend parent functionality or completely replace it
- Overriding allows specialization while maintaining the interface

## Test Cases

Your method overriding should:

- Override `work()` method to show specialized behavior
- Override `get_info()` to include class-specific information
- Use `super()` to extend rather than replace parent functionality
- Maintain consistent method signatures across classes

## Bonus Challenge

Add a `Intern` class that overrides methods to show learning behavior, and create a method that works with any Employee type!
