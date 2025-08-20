# Class Attributes vs Instance Attributes - Practice 5

**Difficulty:** ⭐ (Very Easy)

## Description

Learn the difference between class attributes (shared by all instances) and instance attributes (unique to each object).

## Objectives

- Understand class attributes vs instance attributes
- Learn when to use each type
- Practice accessing both types of attributes
- See how changes affect different instances

## Your Tasks

1. **create_animal_class()** - Create Animal class with both attribute types
2. **demonstrate_class_attributes()** - Show shared class attributes
3. **demonstrate_instance_attributes()** - Show unique instance attributes
4. **test_attribute_changes()** - Practice how changes affect instances

## Example

```python
class Animal:
    """An animal class demonstrating class and instance attributes."""
    
    # Class attributes (shared by all instances)
    kingdom = "Animalia"
    total_animals = 0  # Counter for all animals created
    species_list = []  # List of all species created
    
    def __init__(self, name, species, age):
        """Initialize an Animal instance."""
        # Instance attributes (unique to each object)
        self.name = name
        self.species = species
        self.age = age
        self.is_sleeping = False
        
        # Update class attributes
        Animal.total_animals += 1
        if species not in Animal.species_list:
            Animal.species_list.append(species)
    
    def sleep(self):
        """Make the animal sleep."""
        self.is_sleeping = True
        return f"{self.name} is now sleeping"
    
    def wake_up(self):
        """Wake up the animal."""
        self.is_sleeping = False
        return f"{self.name} is now awake"
    
    def get_info(self):
        """Get animal information."""
        status = "sleeping" if self.is_sleeping else "awake"
        return f"{self.name} the {self.species} ({self.age} years old) - {status}"
    
    @classmethod
    def get_total_animals(cls):
        """Get total number of animals created."""
        return cls.total_animals
    
    @classmethod
    def get_all_species(cls):
        """Get list of all species."""
        return cls.species_list.copy()  # Return a copy to prevent modification

# Example usage
def create_animal_class():
    """Create and use Animal objects to demonstrate attributes."""
    print(f"Initial total animals: {Animal.get_total_animals()}")
    print(f"Initial species list: {Animal.get_all_species()}")
    
    # Create animals
    animal1 = Animal("Buddy", "Dog", 5)
    animal2 = Animal("Whiskers", "Cat", 3)
    animal3 = Animal("Rex", "Dog", 7)
    
    print(f"\nAfter creating animals:")
    print(f"Total animals: {Animal.get_total_animals()}")
    print(f"Species list: {Animal.get_all_species()}")
    
    # Show individual animals
    print(f"\nIndividual animals:")
    animals = [animal1, animal2, animal3]
    for animal in animals:
        print(f"- {animal.get_info()}")
        print(f"  Kingdom: {animal.kingdom}")  # Accessing class attribute through instance
    
    # Demonstrate instance attributes are unique
    print(f"\nTesting instance attributes:")
    print(animal1.sleep())
    print(animal2.wake_up())  # Was already awake
    
    for animal in animals:
        print(f"- {animal.get_info()}")
    
    # Demonstrate class attribute changes affect all instances
    print(f"\nChanging class attribute:")
    print(f"Before: {animal1.kingdom}, {animal2.kingdom}, {animal3.kingdom}")
    
    Animal.kingdom = "Modified Animalia"
    print(f"After:  {animal1.kingdom}, {animal2.kingdom}, {animal3.kingdom}")
    
    return animals

# Practice the class
if __name__ == "__main__":
    animals = create_animal_class()
    
    # Final statistics
    print(f"\nFinal statistics:")
    print(f"Total animals created: {Animal.total_animals}")
    print(f"Different species: {len(Animal.species_list)}")
    print(f"Species: {', '.join(Animal.species_list)}")
```

## Hints

- Class attributes are defined outside `__init__`
- Instance attributes are defined with `self.attribute`
- Class attributes are shared by all instances
- Use `@classmethod` for methods that work with class attributes

## Practice Cases

Your Animal class should:

- Track the total number of animals created
- Maintain a list of unique species
- Allow each animal to have individual attributes
- Show that class attribute changes affect all instances

## Bonus Challenge

Add a class attribute for endangered species and methods to mark/unmark species as endangered!