# Multiple Inheritance and Method Resolution Order - Test 12

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Learn how Python handles multiple inheritance and the Method Resolution Order (MRO) to understand which method gets called when multiple parent classes have the same method.

## Objectives

- Create classes with multiple inheritance
- Understand Method Resolution Order (MRO)
- Practice using `super()` with multiple inheritance
- Handle diamond inheritance problem

## Your Tasks

1. **create_multiple_inheritance()** - Create classes with multiple parents
2. **demonstrate_mro()** - Show Method Resolution Order
3. **handle_diamond_problem()** - Deal with diamond inheritance
4. **use_super_properly()** - Use super() correctly with multiple inheritance

## Example

```python
# Base classes for multiple inheritance
class Flyable:
    """Mixin class for flying ability."""
    
    def __init__(self):
        """Initialize flyable object."""
        self.altitude = 0
        super().__init__()  # Important: call super() in mixins
    
    def take_off(self):
        """Take off and start flying."""
        self.altitude = 100
        return f"Taking off! Now at {self.altitude} feet"
    
    def land(self):
        """Land and stop flying."""
        self.altitude = 0
        return "Landing! Back on the ground"
    
    def fly_higher(self, feet):
        """Increase altitude."""
        self.altitude += feet
        return f"Flying higher! Now at {self.altitude} feet"
    
    def get_flight_status(self):
        """Get current flight status."""
        if self.altitude > 0:
            return f"Flying at {self.altitude} feet"
        return "On the ground"

class Swimmable:
    """Mixin class for swimming ability."""
    
    def __init__(self):
        """Initialize swimmable object."""
        self.depth = 0
        super().__init__()  # Important: call super() in mixins
    
    def dive(self):
        """Dive underwater."""
        self.depth = 10
        return f"Diving! Now at {self.depth} feet underwater"
    
    def surface(self):
        """Return to surface."""
        self.depth = 0
        return "Surfacing! Back at water level"
    
    def swim_deeper(self, feet):
        """Increase depth."""
        self.depth += feet
        return f"Swimming deeper! Now at {self.depth} feet underwater"
    
    def get_swim_status(self):
        """Get current swimming status."""
        if self.depth > 0:
            return f"Swimming at {self.depth} feet underwater"
        return "At water surface"

class Animal:
    """Base animal class."""
    
    def __init__(self, name, species):
        """Initialize animal."""
        self.name = name
        self.species = species
        self.energy = 100
        super().__init__()
    
    def eat(self):
        """Eat food to gain energy."""
        self.energy = min(100, self.energy + 20)
        return f"{self.name} is eating. Energy: {self.energy}"
    
    def rest(self):
        """Rest to gain energy."""
        self.energy = min(100, self.energy + 10)
        return f"{self.name} is resting. Energy: {self.energy}"
    
    def get_info(self):
        """Get animal information."""
        return f"{self.name} the {self.species} (Energy: {self.energy})"
    
    def move(self):
        """Basic movement."""
        self.energy = max(0, self.energy - 5)
        return f"{self.name} is moving. Energy: {self.energy}"

# Multiple inheritance examples
class Duck(Animal, Flyable, Swimmable):
    """Duck class with multiple inheritance (can fly and swim)."""
    
    def __init__(self, name):
        """Initialize duck."""
        super().__init__(name, "Duck")
        self.is_migrating = False
    
    def quack(self):
        """Duck-specific sound."""
        return f"{self.name} says: Quack!"
    
    def migrate(self):
        """Start migration (uses flying ability)."""
        if self.altitude == 0:
            result = self.take_off()
            self.is_migrating = True
            return f"{result} - Starting migration!"
        return "Already in flight for migration"
    
    def move(self):
        """Override move method."""
        # Duck can move by walking, flying, or swimming
        base_result = super().move()
        
        if self.altitude > 0:
            return f"{base_result} (flying)"
        elif self.depth > 0:
            return f"{base_result} (swimming)"
        else:
            return f"{base_result} (walking)"
    
    def get_status(self):
        """Get comprehensive duck status."""
        info = [self.get_info()]
        info.append(self.get_flight_status())
        info.append(self.get_swim_status())
        
        if self.is_migrating:
            info.append("Status: Migrating")
        
        return " | ".join(info)

class Penguin(Animal, Swimmable):
    """Penguin class (can swim but not fly)."""
    
    def __init__(self, name):
        """Initialize penguin."""
        super().__init__(name, "Penguin")
        self.colony_size = 1
    
    def waddle(self):
        """Penguin-specific movement on land."""
        self.energy = max(0, self.energy - 3)
        return f"{self.name} is waddling. Energy: {self.energy}"
    
    def join_colony(self, size):
        """Join a penguin colony."""
        self.colony_size = size
        return f"{self.name} joined a colony of {size} penguins"
    
    def move(self):
        """Override move method."""
        if self.depth > 0:
            return super().move() + " (swimming)"
        else:
            return self.waddle()
    
    def get_status(self):
        """Get comprehensive penguin status."""
        info = [self.get_info()]
        info.append(self.get_swim_status())
        info.append(f"Colony size: {self.colony_size}")
        return " | ".join(info)

class Eagle(Animal, Flyable):
    """Eagle class (can fly but not swim well)."""
    
    def __init__(self, name):
        """Initialize eagle."""
        super().__init__(name, "Eagle")
        self.territory_size = 10  # square miles
    
    def hunt(self):
        """Eagle-specific hunting behavior."""
        if self.altitude > 50:
            self.energy = max(0, self.energy - 15)
            return f"{self.name} is hunting from above. Energy: {self.energy}"
        return f"{self.name} needs to fly higher to hunt effectively"
    
    def establish_territory(self, size):
        """Establish hunting territory."""
        self.territory_size = size
        return f"{self.name} established {size} square mile territory"
    
    def move(self):
        """Override move method."""
        if self.altitude > 0:
            return super().move() + " (soaring)"
        else:
            return super().move() + " (walking)"
    
    def get_status(self):
        """Get comprehensive eagle status."""
        info = [self.get_info()]
        info.append(self.get_flight_status())
        info.append(f"Territory: {self.territory_size} sq miles")
        return " | ".join(info)

# Example usage
def create_multiple_inheritance():
    """Demonstrate multiple inheritance."""
    print("=== Multiple Inheritance Demo ===")
    
    # Create animals with different abilities
    duck = Duck("Donald")
    penguin = Penguin("Pingu")
    eagle = Eagle("Eddie")
    
    animals = [duck, penguin, eagle]
    
    # Show initial status
    print("Initial status:")
    for animal in animals:
        print(f"  {animal.get_status()}")
    
    # Test flying abilities
    print(f"\n=== Flying Tests ===")
    print(f"Duck: {duck.take_off()}")
    print(f"Duck: {duck.fly_higher(200)}")
    print(f"Eagle: {eagle.take_off()}")
    print(f"Eagle: {eagle.fly_higher(500)}")
    
    try:
        # Penguin doesn't have flying ability
        print(f"Penguin: {penguin.take_off()}")
    except AttributeError as e:
        print(f"Penguin can't fly: {e}")
    
    # Test swimming abilities
    print(f"\n=== Swimming Tests ===")
    print(f"Duck: {duck.dive()}")
    print(f"Duck: {duck.swim_deeper(5)}")
    print(f"Penguin: {penguin.dive()}")
    print(f"Penguin: {penguin.swim_deeper(20)}")
    
    try:
        # Eagle doesn't have swimming ability
        print(f"Eagle: {eagle.dive()}")
    except AttributeError as e:
        print(f"Eagle can't swim: {e}")
    
    # Test movement (overridden in each class)
    print(f"\n=== Movement Tests ===")
    for animal in animals:
        print(f"  {animal.move()}")
    
    # Test specific abilities
    print(f"\n=== Specific Abilities ===")
    print(f"Duck: {duck.quack()}")
    print(f"Duck: {duck.migrate()}")
    print(f"Penguin: {penguin.join_colony(50)}")
    print(f"Eagle: {eagle.hunt()}")
    print(f"Eagle: {eagle.establish_territory(25)}")
    
    return duck, penguin, eagle

def demonstrate_mro():
    """Demonstrate Method Resolution Order."""
    print(f"\n=== Method Resolution Order (MRO) ===")
    
    # Show MRO for each class
    classes = [Duck, Penguin, Eagle]
    
    for cls in classes:
        print(f"\n{cls.__name__} MRO:")
        for i, base in enumerate(cls.__mro__):
            print(f"  {i + 1}. {base.__name__}")
    
    # Show how MRO affects method calls
    duck = Duck("MRO Test Duck")
    
    print(f"\nMethod resolution for duck.move():")
    print(f"  Calls: {Duck.move.__qualname__}")
    print(f"  Which calls: {Animal.move.__qualname__}")
    
    print(f"\nMethod resolution for duck.__init__():")
    print(f"  Duck.__init__ -> Animal.__init__ -> Flyable.__init__ -> Swimmable.__init__ -> object.__init__")

# Test the classes
if __name__ == "__main__":
    # Test multiple inheritance
    animals = create_multiple_inheritance()
    
    # Demonstrate MRO
    demonstrate_mro()
    
    # Final status
    print(f"\n=== Final Status ===")
    duck, penguin, eagle = animals
    
    for animal in animals:
        print(f"  {animal.get_status()}")
    
    # Show that super() works correctly
    print(f"\n=== Testing super() behavior ===")
    print(f"Duck energy before eating: {duck.energy}")
    print(f"Duck: {duck.eat()}")
    print(f"Duck energy after eating: {duck.energy}")
```

## Hints

- Use `super().__init__()` in all classes that participate in multiple inheritance
- MRO follows C3 linearization algorithm
- Use `ClassName.__mro__` to see method resolution order
- Mixin classes should call `super().__init__()`
- Design classes to work well together

## Test Cases

Your multiple inheritance should:

- Create classes that inherit from multiple parents
- Show correct method resolution order
- Use `super()` properly to call parent methods
- Handle cases where not all animals have all abilities
- Demonstrate method overriding with multiple inheritance

## Bonus Challenge

Create a `Robot` class hierarchy with `Movable`, `Rechargeable`, and `Programmable` mixins, and show how different robot types can combine different abilities!
