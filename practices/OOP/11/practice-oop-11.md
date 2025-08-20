# Composition and Aggregation - Practice 11

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Learn the difference between composition and aggregation - two important ways objects can contain or work with other objects.

## Objectives

- Understand composition (strong "has-a" relationship)
- Understand aggregation (weak "has-a" relationship)
- Practice creating complex object relationships
- Learn when to use composition vs aggregation

## Your Tasks

1. **create_composition_example()** - Create Car class that owns Engine (composition)
2. **create_aggregation_example()** - Create School class that uses Teachers (aggregation)
3. **demonstrate_ownership()** - Show lifecycle differences
4. **test_relationships()** - Practice both relationship types

## Example

```python
# Composition Example - Car owns Engine
class Engine:
    """Engine class for composition example."""
    
    def __init__(self, horsepower, fuel_type):
        """Initialize engine."""
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False
    
    def start(self):
        """Start the engine."""
        self.is_running = True
        return f"{self.horsepower}HP {self.fuel_type} engine started"
    
    def stop(self):
        """Stop the engine."""
        self.is_running = False
        return f"Engine stopped"
    
    def get_info(self):
        """Get engine information."""
        status = "running" if self.is_running else "stopped"
        return f"{self.horsepower}HP {self.fuel_type} engine ({status})"

class Car:
    """Car class demonstrating composition (Car owns Engine)."""
    
    def __init__(self, make, model, horsepower, fuel_type):
        """Initialize car with engine (composition)."""
        self.make = make
        self.model = model
        # Composition: Car creates and owns the Engine
        self._engine = Engine(horsepower, fuel_type)
        self.is_locked = True
    
    def start_car(self):
        """Start the car (delegates to engine)."""
        if self.is_locked:
            return "Car is locked! Unlock first."
        return self._engine.start()
    
    def stop_car(self):
        """Stop the car."""
        return self._engine.stop()
    
    def unlock(self):
        """Unlock the car."""
        self.is_locked = False
        return f"{self.make} {self.model} unlocked"
    
    def lock(self):
        """Lock the car."""
        if self._engine.is_running:
            return "Cannot lock while engine is running"
        self.is_locked = True
        return f"{self.make} {self.model} locked"
    
    def get_engine_info(self):
        """Get engine information (delegation)."""
        return self._engine.get_info()
    
    def __str__(self):
        """String representation."""
        lock_status = "locked" if self.is_locked else "unlocked"
        return f"{self.make} {self.model} ({lock_status}) - {self.get_engine_info()}"

# Aggregation Example - School uses Teachers
class Teacher:
    """Teacher class for aggregation example."""
    
    def __init__(self, name, subject, years_experience):
        """Initialize teacher."""
        self.name = name
        self.subject = subject
        self.years_experience = years_experience
        self.schools = []  # Teacher can work at multiple schools
    
    def teach(self):
        """Teach a lesson."""
        return f"{self.name} is teaching {self.subject}"
    
    def add_school(self, school_name):
        """Add school to teacher's list."""
        if school_name not in self.schools:
            self.schools.append(school_name)
    
    def remove_school(self, school_name):
        """Remove school from teacher's list."""
        if school_name in self.schools:
            self.schools.remove(school_name)
    
    def __str__(self):
        """String representation."""
        school_list = ", ".join(self.schools) if self.schools else "No schools"
        return f"{self.name} - {self.subject} teacher ({self.years_experience} years) - Schools: {school_list}"

class School:
    """School class demonstrating aggregation (School uses Teachers)."""
    
    def __init__(self, name, address):
        """Initialize school."""
        self.name = name
        self.address = address
        # Aggregation: School uses existing Teacher objects
        self._teachers = []
        self._subjects = set()
    
    def hire_teacher(self, teacher):
        """Hire a teacher (aggregation - teacher exists independently)."""
        if teacher not in self._teachers:
            self._teachers.append(teacher)
            teacher.add_school(self.name)
            self._subjects.add(teacher.subject)
            return f"Hired {teacher.name} to teach {teacher.subject}"
        return f"{teacher.name} already works here"
    
    def fire_teacher(self, teacher):
        """Fire a teacher (teacher continues to exist)."""
        if teacher in self._teachers:
            self._teachers.remove(teacher)
            teacher.remove_school(self.name)
            # Update subjects list
            self._subjects = {t.subject for t in self._teachers}
            return f"Fired {teacher.name}"
        return f"{teacher.name} doesn't work here"
    
    def get_teachers(self):
        """Get list of teachers."""
        return self._teachers.copy()
    
    def get_subjects(self):
        """Get set of subjects taught."""
        return self._subjects.copy()
    
    def start_classes(self):
        """Start classes for the day."""
        if not self._teachers:
            return "No teachers available for classes"
        
        activities = []
        for teacher in self._teachers:
            activities.append(teacher.teach())
        return f"Classes started at {self.name}:\n" + "\n".join(f"  - {activity}" for activity in activities)
    
    def __str__(self):
        """String representation."""
        teacher_count = len(self._teachers)
        subject_count = len(self._subjects)
        return f"{self.name} - {teacher_count} teachers, {subject_count} subjects"

# Example usage
def create_composition_example():
    """Demonstrate composition with Car and Engine."""
    print("=== Composition Example (Car owns Engine) ===")
    
    # Create cars - each car creates its own engine
    car1 = Car("Toyota", "Camry", 200, "gasoline")
    car2 = Car("Tesla", "Model 3", 350, "electric")
    
    print(f"Created: {car1}")
    print(f"Created: {car2}")
    
    # Try to start locked cars
    print(f"\nTrying to start locked cars:")
    print(f"Car1: {car1.start_car()}")
    print(f"Car2: {car2.start_car()}")
    
    # Unlock and start
    print(f"\nUnlocking and starting cars:")
    print(f"Car1: {car1.unlock()}")
    print(f"Car1: {car1.start_car()}")
    print(f"Car2: {car2.unlock()}")
    print(f"Car2: {car2.start_car()}")
    
    print(f"\nAfter starting:")
    print(f"Car1: {car1}")
    print(f"Car2: {car2}")
    
    # Try to lock running car
    print(f"\nTrying to lock running car:")
    print(f"Car1: {car1.lock()}")
    
    # Stop and lock
    print(f"\nStopping and locking:")
    print(f"Car1: {car1.stop_car()}")
    print(f"Car1: {car1.lock()}")
    
    return car1, car2

def create_aggregation_example():
    """Demonstrate aggregation with School and Teachers."""
    print("\n=== Aggregation Example (School uses Teachers) ===")
    
    # Create teachers first (they exist independently)
    teacher1 = Teacher("Dr. Smith", "Mathematics", 10)
    teacher2 = Teacher("Ms. Johnson", "English", 5)
    teacher3 = Teacher("Mr. Brown", "Science", 8)
    
    print("Created teachers:")
    for teacher in [teacher1, teacher2, teacher3]:
        print(f"  {teacher}")
    
    # Create schools
    school1 = School("Lincoln High", "123 Main St")
    school2 = School("Washington Academy", "456 Oak Ave")
    
    print(f"\nCreated schools:")
    print(f"  {school1}")
    print(f"  {school2}")
    
    # Hire teachers (aggregation)
    print(f"\nHiring teachers:")
    print(f"School1: {school1.hire_teacher(teacher1)}")
    print(f"School1: {school1.hire_teacher(teacher2)}")
    print(f"School2: {school2.hire_teacher(teacher2)}")  # Teacher can work at multiple schools
    print(f"School2: {school2.hire_teacher(teacher3)}")
    
    # Show updated information
    print(f"\nAfter hiring:")
    print(f"  {school1}")
    print(f"  {school2}")
    print(f"\nTeacher status:")
    for teacher in [teacher1, teacher2, teacher3]:
        print(f"  {teacher}")
    
    # Start classes
    print(f"\n{school1.start_classes()}")
    print(f"\n{school2.start_classes()}")
    
    # Fire a teacher from one school (teacher still exists and works at other school)
    print(f"\nFiring teacher from one school:")
    print(f"School1: {school1.fire_teacher(teacher2)}")
    
    print(f"\nAfter firing:")
    print(f"  {school1}")
    print(f"  {teacher2}")  # Teacher still exists and works at school2
    
    return school1, school2, [teacher1, teacher2, teacher3]

# Practice the relationships
if __name__ == "__main__":
    # Practice composition
    cars = create_composition_example()
    
    # Practice aggregation
    schools_and_teachers = create_aggregation_example()
    
    # Demonstrate the key differences
    print("\n=== Key Differences ===")
    print("Composition (Car-Engine):")
    print("  - Engine is created with Car")
    print("  - Engine cannot exist without Car")
    print("  - When Car is destroyed, Engine is destroyed")
    
    print("\nAggregation (School-Teacher):")
    print("  - Teachers exist independently")
    print("  - Teachers can work at multiple schools")
    print("  - When School closes, Teachers continue to exist")
    
    # Memory management demonstration
    print("\n=== Memory Management Demo ===")
    car = cars[0]
    print(f"Car exists: {car}")
    print(f"Engine info: {car.get_engine_info()}")
    # When car goes out of scope, engine is also destroyed (composition)
    
    school, _, teachers = schools_and_teachers
    teacher = teachers[0]
    print(f"Teacher exists: {teacher}")
    # Even if school goes out of scope, teacher continues to exist (aggregation)
```

## Hints

- Composition: "owns-a" relationship, child cannot exist without parent
- Aggregation: "uses-a" relationship, child can exist independently
- In composition, parent creates child objects
- In aggregation, parent uses existing child objects
- Composition = strong relationship, Aggregation = weak relationship

## Practice Cases

Your implementation should show:

- Car creates and owns Engine (composition)
- School uses existing Teachers (aggregation)
- Engine lifecycle tied to Car
- Teachers can work at multiple Schools
- Proper delegation between objects

## Bonus Challenge

Create a `Library` and `Book` system where Library owns Books (composition) and a `University` and `Student` system where University uses Students (aggregation)!