# Property Decorators - Practice 8

**Difficulty:** ⭐ (Very Easy)

## Description

Learn to use the `@property` decorator to create getter and setter methods that work like attributes.

## Objectives

- Use `@property` decorator for getter methods
- Use `@property_name.setter` for setter methods
- Create read-only and read-write properties
- Understand the benefits of properties over direct attribute access

## Your Tasks

1. **create_temperature_class()** - Create Temperature class with properties
2. **implement_getter_setter()** - Use property decorators
3. **add_validation()** - Add validation in setter methods
4. **create_readonly_properties()** - Create calculated read-only properties

## Example

```python
class Temperature:
    """Temperature class demonstrating property decorators."""
    
    def __init__(self, celsius=0):
        """Initialize temperature in Celsius."""
        self._celsius = 0  # Private attribute
        self.celsius = celsius  # Use setter for validation
    
    @property
    def celsius(self):
        """Get temperature in Celsius (getter)."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius with validation (setter)."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = float(value)
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit (calculated property)."""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature using Fahrenheit value."""
        if value < -459.67:
            raise ValueError("Temperature cannot be below absolute zero (-459.67°F)")
        self._celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Get temperature in Kelvin (read-only calculated property)."""
        return self._celsius + 273.15
    
    @property
    def is_freezing(self):
        """Check if temperature is at or below freezing point (read-only)."""
        return self._celsius <= 0
    
    @property
    def is_boiling(self):
        """Check if temperature is at or above boiling point (read-only)."""
        return self._celsius >= 100
    
    @property
    def state_of_water(self):
        """Get the state of water at this temperature (read-only)."""
        if self._celsius < 0:
            return "Ice"
        elif self._celsius >= 100:
            return "Steam"
        else:
            return "Liquid"
    
    def __str__(self):
        """String representation of temperature."""
        return f"{self._celsius:.1f}°C ({self.fahrenheit:.1f}°F, {self.kelvin:.1f}K) - Water: {self.state_of_water}"

# Example usage
def create_temperature_class():
    """Create and use Temperature class with properties."""
    # Create temperature objects
    temp1 = Temperature(25)  # Room temperature
    temp2 = Temperature()    # Default (0°C)
    
    print("Initial temperatures:")
    print(f"Temp1: {temp1}")
    print(f"Temp2: {temp2}")
    
    # Practice property getters
    print(f"\nProperty getters:")
    print(f"Temp1 Celsius: {temp1.celsius}")
    print(f"Temp1 Fahrenheit: {temp1.fahrenheit:.1f}")
    print(f"Temp1 Kelvin: {temp1.kelvin:.1f}")
    
    # Practice property setters
    print(f"\nSetting temperatures:")
    temp1.celsius = 0
    print(f"After setting temp1 to 0°C: {temp1}")
    
    temp2.fahrenheit = 212  # Boiling point in Fahrenheit
    print(f"After setting temp2 to 212°F: {temp2}")
    
    # Practice read-only properties
    print(f"\nRead-only properties:")
    print(f"Temp1 is freezing: {temp1.is_freezing}")
    print(f"Temp1 is boiling: {temp1.is_boiling}")
    print(f"Temp2 is freezing: {temp2.is_freezing}")
    print(f"Temp2 is boiling: {temp2.is_boiling}")
    
    # Practice different temperature ranges
    temperatures = [-10, 0, 25, 50, 100, 150]
    print(f"\nTesting different temperatures:")
    
    for temp_c in temperatures:
        temp = Temperature(temp_c)
        print(f"{temp_c:3}°C -> {temp.state_of_water:6} "
              f"(Freezing: {temp.is_freezing}, Boiling: {temp.is_boiling})")
    
    # Practice validation
    print(f"\nTesting validation:")
    try:
        temp_invalid = Temperature(-300)  # Below absolute zero
    except ValueError as e:
        print(f"Caught error: {e}")
    
    try:
        temp1.fahrenheit = -500  # Below absolute zero in Fahrenheit
    except ValueError as e:
        print(f"Caught error: {e}")
    
    return temp1, temp2

# Practice the class
if __name__ == "__main__":
    t1, t2 = create_temperature_class()
    
    # Demonstrate that properties work like attributes
    print(f"\nFinal demonstration:")
    print(f"Setting t1.celsius = 37 (body temperature)")
    t1.celsius = 37
    print(f"Result: {t1}")
    
    print(f"Setting t1.fahrenheit = 32 (freezing point)")
    t1.fahrenheit = 32
    print(f"Result: {t1}")
```

## Hints

- Use `@property` decorator before getter methods
- Use `@property_name.setter` for setter methods
- Store actual data in "private" attributes (prefix with `_`)
- Properties can perform calculations and validation
- Read-only properties only have getters, no setters

## Practice Cases

Your Temperature class should:

- Allow setting temperature in Celsius or Fahrenheit
- Automatically convert between temperature scales
- Validate that temperatures are not below absolute zero
- Provide read-only properties for water state and conditions
- Work seamlessly like regular attributes

## Bonus Challenge

Add properties for Rankine scale and create a `TemperatureConverter` class that works with multiple Temperature objects!