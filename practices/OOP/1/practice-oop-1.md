# Practice OOP 1: Classes, Objects, and Inheritance

**Difficulty:** ⭐⭐⭐☆☆ (Medium)

**Related Topics:** Class definition, inheritance, encapsulation, polymorphism

## Objective

Master object-oriented programming concepts including class creation, inheritance, and encapsulation.

## Requirements

Create a class hierarchy that demonstrates OOP principles:

1. `Vehicle` (base class) - Define common vehicle attributes and methods
2. `Car(Vehicle)` - Inherit from Vehicle, add car-specific features
3. `ElectricCar(Car)` - Multiple inheritance levels, electric-specific features
4. `Garage` - Composition example, manages multiple vehicles
5. Demonstrate encapsulation with private attributes

## Class Structure Requirements

### Vehicle (Base Class)
- Attributes: brand, model, year, _mileage (protected)
- Methods: start(), stop(), get_info(), __str__()

### Car(Vehicle)
- Additional attributes: fuel_type, doors
- Override methods where appropriate
- Add car-specific methods

### ElectricCar(Car)
- Additional attributes: battery_capacity, charging_status
- Override fuel-related methods
- Add electric-specific methods

## Examples

```python
# Creating objects and demonstrating inheritance
car = Car("Toyota", "Camry", 2023, fuel_type="gasoline", doors=4)
electric = ElectricCar("Tesla", "Model 3", 2023, battery_capacity=75)

# Demonstrating polymorphism
vehicles = [car, electric]
for vehicle in vehicles:
    print(vehicle.start())  # Different behavior for each type
```

## Hints

- Use `super()` to call parent class methods
- Implement `__init__()` constructors properly
- Use single underscore `_` for protected attributes
- Use double underscore `__` for private attributes (name mangling)
- Override `__str__()` and `__repr__()` for better object representation
- Demonstrate method overriding and polymorphism

## Practice Cases

Your implementation should handle:

1. Creating objects with proper initialization
2. Inheritance chain working correctly
3. Method overriding and polymorphism
4. Encapsulation with protected/private attributes
5. Composition with the Garage class