# Class and Object Creation Functions - Test 9

**Difficulty:** ⭐⭐⭐ (Medium)

## Description

Master Python's built-in functions for creating and working with classes and objects including `type()`, `isinstance()`, `issubclass()`, `super()`, `property()`, `staticmethod()`, `classmethod()`, and advanced object-oriented programming patterns.

## Objectives

- Use `type()` for type checking and dynamic class creation
- Apply `isinstance()` and `issubclass()` for type relationships
- Understand `super()` for method resolution and inheritance
- Create properties using `property()`, `staticmethod()`, and `classmethod()`
- Build advanced OOP patterns with metaclasses and descriptors

## Your Tasks

1. **type_operations()** - Master type() for checking and creating types
2. **inheritance_checking()** - Use isinstance() and issubclass() effectively
3. **method_decorators()** - Work with staticmethod, classmethod, and property
4. **super_mechanics()** - Understand super() and method resolution
5. **advanced_oop()** - Build metaclasses and descriptors

## Example

```python
import functools
from typing import Any, Dict, List, Type, Union
import weakref

def type_operations():
    """Demonstrate type() function for checking and creating types."""
    print("=== Type Operations ===")
    
    # Basic type checking
    print("Basic Type Checking:")
    
    test_objects = [
        42,
        3.14,
        "hello",
        [1, 2, 3],
        {"key": "value"},
        (1, 2, 3),
        {1, 2, 3},
        lambda x: x,
        print,
        type
    ]
    
    for obj in test_objects:
        obj_type = type(obj)
        type_name = obj_type.__name__
        module = obj_type.__module__
        
        print(f"  {repr(obj)[:20]:<20} -> {type_name} (from {module})")
    
    # Type vs isinstance
    print("\\nType vs isinstance:")
    
    class Parent:
        pass
    
    class Child(Parent):
        pass
    
    child_instance = Child()
    
    print(f"Child instance: {child_instance}")
    print(f"type(child_instance) == Child: {type(child_instance) == Child}")
    print(f"type(child_instance) == Parent: {type(child_instance) == Parent}")
    print(f"isinstance(child_instance, Child): {isinstance(child_instance, Child)}")
    print(f"isinstance(child_instance, Parent): {isinstance(child_instance, Parent)}")
    
    # Dynamic class creation with type()
    print("\\nDynamic Class Creation:")
    
    # Method 1: Basic class creation
    def init_method(self, name, value):
        self.name = name
        self.value = value
    
    def str_method(self):
        return f"DynamicClass(name='{self.name}', value={self.value})"
    
    def add_method(self, other):
        if isinstance(other, type(self)):
            return self.value + other.value
        return self.value + other
    
    # Create class using type()
    DynamicClass = type('DynamicClass', (), {
        '__init__': init_method,
        '__str__': str_method,
        '__add__': add_method,
        'class_attribute': 'I am dynamic!'
    })
    
    # Test dynamic class
    obj1 = DynamicClass("first", 10)
    obj2 = DynamicClass("second", 20)
    
    print(f"Dynamic object 1: {obj1}")
    print(f"Dynamic object 2: {obj2}")
    print(f"Addition: {obj1 + obj2}")
    print(f"Class attribute: {DynamicClass.class_attribute}")
    
    # Method 2: Class with inheritance
    class BaseClass:
        def base_method(self):
            return "Base method called"
    
    DerivedDynamic = type('DerivedDynamic', (BaseClass,), {
        'derived_attribute': 'derived value',
        'derived_method': lambda self: f"Derived method: {self.derived_attribute}"
    })
    
    derived_obj = DerivedDynamic()
    print(f"\\nDerived object base method: {derived_obj.base_method()}")
    print(f"Derived object derived method: {derived_obj.derived_method()}")
    
    # Method 3: Complex dynamic class with multiple methods
    def create_data_class(class_name, fields):
        \"\"\"Create a data class with specified fields.\"\"\"
        
        def init(self, **kwargs):
            for field in fields:
                setattr(self, field, kwargs.get(field))
        
        def repr_method(self):
            field_values = [f"{field}={getattr(self, field, None)}" for field in fields]
            return f"{class_name}({', '.join(field_values)})"
        
        def eq_method(self, other):
            if not isinstance(other, self.__class__):
                return False
            return all(getattr(self, field) == getattr(other, field) for field in fields)
        
        def to_dict(self):
            return {field: getattr(self, field) for field in fields}
        
        def from_dict(cls, data):
            return cls(**data)
        
        class_dict = {
            '__init__': init,
            '__repr__': repr_method,
            '__eq__': eq_method,
            'to_dict': to_dict,
            'from_dict': classmethod(from_dict),
            'fields': fields
        }
        
        return type(class_name, (), class_dict)
    
    # Create and test data classes
    Person = create_data_class('Person', ['name', 'age', 'email'])
    Product = create_data_class('Product', ['name', 'price', 'category'])
    
    person1 = Person(name="Alice", age=30, email="alice@example.com")
    person2 = Person(name="Alice", age=30, email="alice@example.com")
    person3 = Person(name="Bob", age=25, email="bob@example.com")
    
    print(f"\\nPerson 1: {person1}")
    print(f"Person 2: {person2}")
    print(f"Person 1 == Person 2: {person1 == person2}")
    print(f"Person 1 == Person 3: {person1 == person3}")
    print(f"Person 1 dict: {person1.to_dict()}")
    
    # Recreate from dict
    person_data = {'name': 'Charlie', 'age': 35, 'email': 'charlie@example.com'}
    person4 = Person.from_dict(person_data)
    print(f"Person from dict: {person4}")
    
    # Type checking with dynamic classes
    print("\\nType Checking with Dynamic Classes:")
    
    print(f"Type of person1: {type(person1)}")
    print(f"person1 is instance of Person: {isinstance(person1, Person)}")
    print(f"Person is subclass of object: {issubclass(Person, object)}")
    
    # Class factory
    print("\\nClass Factory:")
    
    class ClassFactory:
        @staticmethod
        def create_enum_class(name, values):
            \"\"\"Create an enum-like class.\"\"\"
            
            class_dict = {}
            
            for i, value in enumerate(values):
                class_dict[value.upper()] = i
            
            def get_name(cls, value):
                for name, val in cls.__dict__.items():
                    if val == value and not name.startswith('_'):
                        return name
                return None
            
            def get_values(cls):
                return [val for name, val in cls.__dict__.items() 
                       if not name.startswith('_') and isinstance(val, int)]
            
            class_dict['get_name'] = classmethod(get_name)
            class_dict['get_values'] = classmethod(get_values)
            
            return type(name, (), class_dict)
        
        @staticmethod
        def create_singleton_class(name, base_class=None):
            \"\"\"Create a singleton class.\"\"\"
            
            _instance = None
            
            def new(cls):
                nonlocal _instance
                if _instance is None:
                    _instance = super(cls, cls).__new__(cls)
                return _instance
            
            bases = (base_class,) if base_class else ()
            
            return type(name, bases, {'__new__': new})
    
    # Test enum class
    Color = ClassFactory.create_enum_class('Color', ['red', 'green', 'blue'])
    
    print(f"Color.RED: {Color.RED}")
    print(f"Color.GREEN: {Color.GREEN}")
    print(f"Color.BLUE: {Color.BLUE}")
    print(f"Color values: {Color.get_values()}")
    print(f"Name for 1: {Color.get_name(1)}")
    
    # Test singleton class
    Database = ClassFactory.create_singleton_class('Database')
    
    db1 = Database()
    db2 = Database()
    
    print(f"\\nSingleton test:")
    print(f"db1 is db2: {db1 is db2}")
    print(f"id(db1): {id(db1)}")
    print(f"id(db2): {id(db2)}")
    
    return {
        "test_objects_types": [type(obj).__name__ for obj in test_objects],
        "inheritance_checks": {
            "exact_type": type(child_instance) == Child,
            "isinstance_child": isinstance(child_instance, Child),
            "isinstance_parent": isinstance(child_instance, Parent)
        },
        "dynamic_class_test": {
            "obj1_str": str(obj1),
            "addition_result": obj1 + obj2,
            "class_attribute": DynamicClass.class_attribute
        },
        "data_class_test": {
            "person1_dict": person1.to_dict(),
            "equality_test": person1 == person2,
            "person_from_dict": str(person4)
        },
        "enum_values": Color.get_values(),
        "singleton_test": db1 is db2
    }

def inheritance_checking():
    """Demonstrate isinstance() and issubclass() for type relationships."""
    print("\\n=== Inheritance Checking ===")
    
    # Create class hierarchy
    print("Class Hierarchy:")
    
    class Animal:
        def speak(self):
            return "Some sound"
    
    class Mammal(Animal):
        def give_birth(self):
            return "Gives birth to live young"
    
    class Bird(Animal):
        def lay_eggs(self):
            return "Lays eggs"
    
    class Dog(Mammal):
        def speak(self):
            return "Woof!"
        
        def fetch(self):
            return "Fetching the ball"
    
    class Cat(Mammal):
        def speak(self):
            return "Meow!"
        
        def purr(self):
            return "Purring contentedly"
    
    class Eagle(Bird):
        def hunt(self):
            return "Hunting from above"
    
    # Create instances
    animal = Animal()
    mammal = Mammal()
    bird = Bird()
    dog = Dog()
    cat = Cat()
    eagle = Eagle()
    
    instances = [
        ("animal", animal),
        ("mammal", mammal),
        ("bird", bird),
        ("dog", dog),
        ("cat", cat),
        ("eagle", eagle)
    ]
    
    classes = [Animal, Mammal, Bird, Dog, Cat, Eagle]
    
    # isinstance checking
    print("isinstance() Checking:")
    
    isinstance_matrix = {}
    
    for inst_name, instance in instances:
        isinstance_matrix[inst_name] = {}
        print(f"\\n{inst_name} ({type(instance).__name__}):")
        
        for cls in classes:
            is_instance = isinstance(instance, cls)
            isinstance_matrix[inst_name][cls.__name__] = is_instance
            print(f"  isinstance({inst_name}, {cls.__name__}): {is_instance}")
    
    # issubclass checking
    print("\\nissubclass() Checking:")
    
    issubclass_matrix = {}
    
    for child_cls in classes:
        issubclass_matrix[child_cls.__name__] = {}
        print(f"\\n{child_cls.__name__}:")
        
        for parent_cls in classes:
            is_subclass = issubclass(child_cls, parent_cls)
            issubclass_matrix[child_cls.__name__][parent_cls.__name__] = is_subclass
            print(f"  issubclass({child_cls.__name__}, {parent_cls.__name__}): {is_subclass}")
    
    # Multiple inheritance
    print("\\nMultiple Inheritance:")
    
    class Flyable:
        def fly(self):
            return "Flying through the air"
    
    class Swimmable:
        def swim(self):
            return "Swimming in water"
    
    class Duck(Bird, Flyable, Swimmable):
        def speak(self):
            return "Quack!"
    
    class Bat(Mammal, Flyable):
        def speak(self):
            return "Screech!"
        
        def echolocate(self):
            return "Using echolocation"
    
    duck = Duck()
    bat = Bat()
    
    # Test multiple inheritance
    multi_instances = [("duck", duck), ("bat", bat)]
    multi_classes = [Animal, Mammal, Bird, Flyable, Swimmable, Duck, Bat]
    
    for inst_name, instance in multi_instances:
        print(f"\\n{inst_name} ({type(instance).__name__}):")
        for cls in multi_classes:
            is_instance = isinstance(instance, cls)
            print(f"  isinstance({inst_name}, {cls.__name__}): {is_instance}")
    
    # Built-in type checking
    print("\\nBuilt-in Type Checking:")
    
    test_values = [
        ("integer", 42),
        ("float", 3.14),
        ("string", "hello"),
        ("list", [1, 2, 3]),
        ("tuple", (1, 2, 3)),
        ("dict", {"key": "value"}),
        ("set", {1, 2, 3}),
        ("boolean", True)
    ]
    
    builtin_types = [int, float, str, list, tuple, dict, set, bool, object]
    
    for value_name, value in test_values:
        print(f"\\n{value_name}: {value}")
        for builtin_type in builtin_types:
            is_instance = isinstance(value, builtin_type)
            if is_instance:
                print(f"  isinstance({value_name}, {builtin_type.__name__}): {is_instance}")
    
    # Multiple types checking
    print("\\nMultiple Types Checking:")
    
    def check_multiple_types(value, type_tuple, value_name="value"):
        \"\"\"Check if value is instance of any type in tuple.\"\"\"
        result = isinstance(value, type_tuple)
        type_names = [t.__name__ for t in type_tuple]
        print(f"  isinstance({value_name}, ({', '.join(type_names)})): {result}")
        return result
    
    test_multiple = [
        (42, (int, float)),
        (3.14, (int, float)),
        ("hello", (str, bytes)),
        ([1, 2, 3], (list, tuple)),
        ({1, 2, 3}, (set, frozenset)),
        (True, (bool, int)),
        (None, (type(None),))
    ]
    
    for value, types in test_multiple:
        check_multiple_types(value, types, repr(value))
    
    # Abstract base classes
    print("\\nAbstract Base Classes:")
    
    from collections.abc import Iterable, Container, Sized, Callable
    
    abc_test_objects = [
        ("list", [1, 2, 3]),
        ("string", "hello"),
        ("dict", {"a": 1}),
        ("function", lambda x: x),
        ("method", str.upper)
    ]
    
    abcs = [Iterable, Container, Sized, Callable]
    
    for obj_name, obj in abc_test_objects:
        print(f"\\n{obj_name}:")
        for abc in abcs:
            is_instance = isinstance(obj, abc)
            if is_instance:
                print(f"  isinstance({obj_name}, {abc.__name__}): {is_instance}")
    
    # Custom type checking
    print("\\nCustom Type Checking:")
    
    def safe_isinstance(obj, class_or_tuple):
        \"\"\"Safe isinstance that handles potential errors.\"\"\"
        try:
            return isinstance(obj, class_or_tuple)
        except TypeError:
            return False
    
    def type_info(obj):
        \"\"\"Get comprehensive type information.\"\"\"
        obj_type = type(obj)
        
        info = {
            'type': obj_type.__name__,
            'module': obj_type.__module__,
            'mro': [cls.__name__ for cls in obj_type.__mro__],
            'is_callable': callable(obj),
            'is_iterable': safe_isinstance(obj, Iterable),
            'is_container': safe_isinstance(obj, Container),
            'is_sized': safe_isinstance(obj, Sized)
        }
        
        return info
    
    # Test type info
    info_test_objects = [dog, [1, 2, 3], {"key": "value"}, lambda x: x]
    
    type_information = {}
    for obj in info_test_objects:
        obj_repr = repr(obj)[:30]
        info = type_info(obj)
        type_information[obj_repr] = info
        
        print(f"\\nType info for {obj_repr}:")
        for key, value in info.items():
            print(f"  {key}: {value}")
    
    return {
        "isinstance_results": isinstance_matrix,
        "issubclass_results": issubclass_matrix,
        "multiple_inheritance": {
            "duck_is_bird": isinstance(duck, Bird),
            "duck_is_flyable": isinstance(duck, Flyable),
            "duck_is_swimmable": isinstance(duck, Swimmable),
            "bat_is_mammal": isinstance(bat, Mammal),
            "bat_is_flyable": isinstance(bat, Flyable)
        },
        "builtin_type_checks": {value_name: [bt.__name__ for bt in builtin_types 
                                           if isinstance(value, bt)]
                              for value_name, value in test_values},
        "multiple_type_results": [check_multiple_types(value, types, repr(value))
                                for value, types in test_multiple],
        "abc_results": {obj_name: [abc.__name__ for abc in abcs if isinstance(obj, abc)]
                       for obj_name, obj in abc_test_objects},
        "type_information": type_information
    }

def method_decorators():
    """Demonstrate staticmethod, classmethod, and property decorators."""
    print("\\n=== Method Decorators ===")
    
    # Basic method types
    print("Basic Method Types:")
    
    class Calculator:
        class_name = "Calculator"
        precision = 2
        
        def __init__(self, name):
            self.name = name
            self._history = []
        
        # Instance method
        def add(self, a, b):
            \"\"\"Instance method - operates on instance data.\"\"\"
            result = a + b
            self._history.append(f"add({a}, {b}) = {result}")
            return round(result, self.precision)
        
        # Static method
        @staticmethod
        def multiply(a, b):
            \"\"\"Static method - doesn't access instance or class data.\"\"\"
            return a * b
        
        # Class method
        @classmethod
        def get_class_info(cls):
            \"\"\"Class method - operates on class data.\"\"\"
            return f"Class: {cls.class_name}, Precision: {cls.precision}"
        
        @classmethod
        def create_scientific(cls, name):
            \"\"\"Class method factory - creates instances with specific settings.\"\"\"
            instance = cls(name)
            instance.precision = 6
            return instance
        
        # Property
        @property
        def history(self):
            \"\"\"Property getter - read-only access to history.\"\"\"
            return self._history.copy()
        
        @property
        def history_count(self):
            \"\"\"Property - computed value.\"\"\"
            return len(self._history)
        
        # Property with setter and deleter
        @property
        def precision(self):
            \"\"\"Property getter for precision.\"\"\"
            return self._precision
        
        @precision.setter
        def precision(self, value):
            \"\"\"Property setter with validation.\"\"\"
            if not isinstance(value, int) or value < 0:
                raise ValueError("Precision must be a non-negative integer")
            self._precision = value
        
        @precision.deleter
        def precision(self):
            \"\"\"Property deleter - reset to default.\"\"\"
            self._precision = 2
    
    # Test calculator
    calc = Calculator("Standard Calculator")
    
    print(f"Calculator name: {calc.name}")
    print(f"Initial precision: {calc.precision}")
    
    # Test instance method
    result1 = calc.add(10, 5)
    result2 = calc.add(3.14159, 2.71828)
    
    print(f"\\nInstance method results:")
    print(f"  10 + 5 = {result1}")
    print(f"  π + e = {result2}")
    print(f"  History: {calc.history}")
    print(f"  History count: {calc.history_count}")
    
    # Test static method
    static_result = Calculator.multiply(6, 7)
    instance_static = calc.multiply(8, 9)
    
    print(f"\\nStatic method results:")
    print(f"  Class call: Calculator.multiply(6, 7) = {static_result}")
    print(f"  Instance call: calc.multiply(8, 9) = {instance_static}")
    
    # Test class method
    class_info = Calculator.get_class_info()
    instance_class_info = calc.get_class_info()
    
    print(f"\\nClass method results:")
    print(f"  Class call: {class_info}")
    print(f"  Instance call: {instance_class_info}")
    
    # Test class method factory
    scientific_calc = Calculator.create_scientific("Scientific Calculator")
    
    print(f"\\nFactory method:")
    print(f"  Scientific calc name: {scientific_calc.name}")
    print(f"  Scientific calc precision: {scientific_calc.precision}")
    
    # Test property setter
    print(f"\\nProperty manipulation:")
    print(f"  Original precision: {calc.precision}")
    
    calc.precision = 4
    print(f"  After setting to 4: {calc.precision}")
    
    result3 = calc.add(1, 3)
    print(f"  1/3 with precision 4: {result3}")
    
    # Test property deleter
    del calc.precision
    print(f"  After deletion (reset): {calc.precision}")
    
    # Advanced property usage
    print("\\nAdvanced Property Usage:")
    
    class Temperature:
        def __init__(self, celsius=0):
            self._celsius = celsius
        
        @property
        def celsius(self):
            return self._celsius
        
        @celsius.setter
        def celsius(self, value):
            if value < -273.15:
                raise ValueError("Temperature cannot be below absolute zero")
            self._celsius = value
        
        @property
        def fahrenheit(self):
            return (self._celsius * 9/5) + 32
        
        @fahrenheit.setter
        def fahrenheit(self, value):
            self.celsius = (value - 32) * 5/9
        
        @property
        def kelvin(self):
            return self._celsius + 273.15
        
        @kelvin.setter
        def kelvin(self, value):
            self.celsius = value - 273.15
        
        def __str__(self):
            return f"Temperature: {self.celsius:.2f}°C, {self.fahrenheit:.2f}°F, {self.kelvin:.2f}K"
    
    # Test temperature conversions
    temp = Temperature(25)  # 25°C
    print(f"Initial: {temp}")
    
    temp.fahrenheit = 100  # Set to 100°F
    print(f"After setting 100°F: {temp}")
    
    temp.kelvin = 300  # Set to 300K
    print(f"After setting 300K: {temp}")
    
    # Descriptor protocol
    print("\\nDescriptor Protocol:")
    
    class ValidatedAttribute:
        def __init__(self, validator, default=None):
            self.validator = validator
            self.default = default
            self.name = None
        
        def __set_name__(self, owner, name):
            self.name = name
            self.private_name = f'_{name}'
        
        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            return getattr(obj, self.private_name, self.default)
        
        def __set__(self, obj, value):
            if not self.validator(value):
                raise ValueError(f"Invalid value for {self.name}: {value}")
            setattr(obj, self.private_name, value)
        
        def __delete__(self, obj):
            setattr(obj, self.private_name, self.default)
    
    # Validators
    def positive_number(value):
        return isinstance(value, (int, float)) and value > 0
    
    def non_empty_string(value):
        return isinstance(value, str) and len(value.strip()) > 0
    
    class Product:
        name = ValidatedAttribute(non_empty_string, "Unnamed Product")
        price = ValidatedAttribute(positive_number, 0.0)
        
        def __init__(self, name, price):
            self.name = name
            self.price = price
        
        def __str__(self):
            return f"Product(name='{self.name}', price=${self.price:.2f})"
    
    # Test descriptor
    product = Product("Laptop", 999.99)
    print(f"\\nProduct: {product}")
    
    # Test validation
    try:
        product.price = -100
    except ValueError as e:
        print(f"Validation error: {e}")
    
    try:
        product.name = ""
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Cached property
    print("\\nCached Property:")
    
    class ExpensiveComputation:
        def __init__(self, data):
            self.data = data
            self._cache = {}
        
        @property
        def expensive_calculation(self):
            if 'expensive' not in self._cache:
                print("  Computing expensive result...")
                # Simulate expensive computation
                result = sum(x**2 for x in self.data)
                self._cache['expensive'] = result
            return self._cache['expensive']
        
        def clear_cache(self):
            self._cache.clear()
    
    # Test cached property
    computer = ExpensiveComputation([1, 2, 3, 4, 5])
    
    print("First access:")
    result1 = computer.expensive_calculation
    print(f"Result: {result1}")
    
    print("\\nSecond access (cached):")
    result2 = computer.expensive_calculation
    print(f"Result: {result2}")
    
    print("\\nAfter clearing cache:")
    computer.clear_cache()
    result3 = computer.expensive_calculation
    print(f"Result: {result3}")
    
    return {
        "calculator_history": calc.history,
        "static_method_results": {
            "class_call": static_result,
            "instance_call": instance_static
        },
        "class_method_info": class_info,
        "scientific_calc_precision": scientific_calc.precision,
        "temperature_conversions": {
            "celsius": temp.celsius,
            "fahrenheit": temp.fahrenheit,
            "kelvin": temp.kelvin
        },
        "product_validation": str(product),
        "cached_computation_calls": 3,  # First, second (cached), third (after clear)
        "cached_result": result3
    }

def super_mechanics():
    """Demonstrate super() and method resolution order."""
    print("\\n=== Super Mechanics ===")
    
    # Basic inheritance with super()
    print("Basic Inheritance with super():")
    
    class Animal:
        def __init__(self, name, species):
            self.name = name
            self.species = species
            print(f"Animal.__init__: Creating {species} named {name}")
        
        def speak(self):
            return f"{self.name} makes a sound"
        
        def info(self):
            return f"{self.name} is a {self.species}"
    
    class Mammal(Animal):
        def __init__(self, name, species, fur_color):
            print(f"Mammal.__init__: Adding fur_color={fur_color}")
            super().__init__(name, species)  # Call parent __init__
            self.fur_color = fur_color
        
        def speak(self):
            base_sound = super().speak()  # Call parent speak
            return f"{base_sound} (mammal sound)"
        
        def info(self):
            base_info = super().info()  # Call parent info
            return f"{base_info}, fur color: {self.fur_color}"
    
    class Dog(Mammal):
        def __init__(self, name, breed, fur_color="brown"):
            print(f"Dog.__init__: Adding breed={breed}")
            super().__init__(name, "dog", fur_color)
            self.breed = breed
        
        def speak(self):
            # Override completely or call super
            return f"{self.name} barks: Woof!"
        
        def fetch(self):
            return f"{self.name} fetches the ball"
        
        def info(self):
            base_info = super().info()
            return f"{base_info}, breed: {self.breed}"
    
    # Create instances and test
    print("\\nCreating Dog instance:")
    dog = Dog("Buddy", "Golden Retriever", "golden")
    
    print(f"\\nDog speaks: {dog.speak()}")
    print(f"Dog info: {dog.info()}")
    print(f"Dog fetches: {dog.fetch()}")
    
    # Method Resolution Order (MRO)
    print("\\nMethod Resolution Order:")
    
    mro = Dog.__mro__
    print(f"Dog MRO: {[cls.__name__ for cls in mro]}")
    
    for cls in mro:
        print(f"  {cls.__name__}: {cls}")
    
    # Multiple inheritance with super()
    print("\\nMultiple Inheritance with super():")
    
    class Flyable:
        def __init__(self, **kwargs):
            print("Flyable.__init__: Adding flight capability")
            super().__init__(**kwargs)  # Cooperative inheritance
            self.can_fly = True
        
        def fly(self):
            return "Flying through the air"
        
        def info(self):
            base_info = super().info()
            return f"{base_info}, can fly: {self.can_fly}"
    
    class Swimmable:
        def __init__(self, **kwargs):
            print("Swimmable.__init__: Adding swimming capability")
            super().__init__(**kwargs)
            self.can_swim = True
        
        def swim(self):
            return "Swimming in water"
        
        def info(self):
            base_info = super().info()
            return f"{base_info}, can swim: {self.can_swim}"
    
    class Bird(Animal, Flyable):
        def __init__(self, name, wingspan, **kwargs):
            print(f"Bird.__init__: Adding wingspan={wingspan}")
            super().__init__(name=name, species="bird", **kwargs)
            self.wingspan = wingspan
        
        def speak(self):
            return f"{self.name} chirps: Tweet!"
        
        def info(self):
            base_info = super().info()
            return f"{base_info}, wingspan: {self.wingspan}cm"
    
    class Duck(Bird, Swimmable):
        def __init__(self, name, wingspan=50, **kwargs):
            print(f"Duck.__init__: Creating a duck")
            super().__init__(name=name, wingspan=wingspan, **kwargs)
        
        def speak(self):
            return f"{self.name} quacks: Quack!"
        
        def migrate(self):
            return f"{self.name} migrates south for winter"
    
    # Create duck with multiple inheritance
    print("\\nCreating Duck instance:")
    duck = Duck("Daffy")
    
    print(f"\\nDuck MRO: {[cls.__name__ for cls in Duck.__mro__]}")
    print(f"Duck speaks: {duck.speak()}")
    print(f"Duck flies: {duck.fly()}")
    print(f"Duck swims: {duck.swim()}")
    print(f"Duck info: {duck.info()}")
    
    # Complex inheritance diamond problem
    print("\\nDiamond Inheritance Problem:")
    
    class A:
        def __init__(self):
            print("A.__init__")
        
        def method(self):
            print("A.method")
            return "A"
    
    class B(A):
        def __init__(self):
            print("B.__init__")
            super().__init__()
        
        def method(self):
            print("B.method")
            result = super().method()
            return f"B -> {result}"
    
    class C(A):
        def __init__(self):
            print("C.__init__")
            super().__init__()
        
        def method(self):
            print("C.method")
            result = super().method()
            return f"C -> {result}"
    
    class D(B, C):
        def __init__(self):
            print("D.__init__")
            super().__init__()
        
        def method(self):
            print("D.method")
            result = super().method()
            return f"D -> {result}"
    
    print(f"\\nD MRO: {[cls.__name__ for cls in D.__mro__]}")
    
    print("\\nCreating D instance:")
    d = D()
    
    print("\\nCalling d.method():")
    result = d.method()
    print(f"Final result: {result}")
    
    # Super with explicit class and instance
    print("\\nExplicit super() usage:")
    
    class Parent:
        def greet(self):
            return "Hello from Parent"
    
    class Child(Parent):
        def greet(self):
            # Different ways to call super
            
            # Method 1: Modern Python (recommended)
            result1 = super().greet()
            
            # Method 2: Explicit class and instance
            result2 = super(Child, self).greet()
            
            # Method 3: Calling specific parent class
            result3 = Parent.greet(self)
            
            return {
                "modern_super": result1,
                "explicit_super": result2,
                "direct_parent": result3
            }
    
    child = Child()
    super_results = child.greet()
    
    print("Super call results:")
    for method, result in super_results.items():
        print(f"  {method}: {result}")
    
    # Cooperative inheritance pattern
    print("\\nCooperative Inheritance Pattern:")
    
    class LoggingMixin:
        def __init__(self, *args, **kwargs):
            print(f"LoggingMixin: Initializing with args={args}, kwargs={kwargs}")
            super().__init__(*args, **kwargs)
            self._log = []
        
        def log(self, message):
            self._log.append(message)
            print(f"LOG: {message}")
        
        def get_log(self):
            return self._log.copy()
    
    class TimestampMixin:
        def __init__(self, *args, **kwargs):
            print(f"TimestampMixin: Initializing")
            super().__init__(*args, **kwargs)
            from datetime import datetime
            self.created_at = datetime.now()
        
        def get_age(self):
            from datetime import datetime
            return (datetime.now() - self.created_at).total_seconds()
    
    class BaseClass:
        def __init__(self, name):
            print(f"BaseClass: Initializing with name={name}")
            self.name = name
    
    class EnhancedClass(LoggingMixin, TimestampMixin, BaseClass):
        def __init__(self, name, extra_data=None):
            print(f"EnhancedClass: Initializing")
            super().__init__(name)
            self.extra_data = extra_data
            self.log(f"Created EnhancedClass instance: {name}")
    
    print("\\nCreating EnhancedClass instance:")
    enhanced = EnhancedClass("TestObject", {"version": "1.0"})
    
    print(f"\\nEnhancedClass MRO: {[cls.__name__ for cls in EnhancedClass.__mro__]}")
    print(f"Instance name: {enhanced.name}")
    print(f"Instance age: {enhanced.get_age():.4f} seconds")
    print(f"Instance log: {enhanced.get_log()}")
    
    return {
        "dog_creation_order": ["Dog.__init__", "Mammal.__init__", "Animal.__init__"],
        "dog_mro": [cls.__name__ for cls in Dog.__mro__],
        "duck_mro": [cls.__name__ for cls in Duck.__mro__],
        "diamond_mro": [cls.__name__ for cls in D.__mro__],
        "diamond_method_result": result,
        "super_call_methods": super_results,
        "enhanced_class_mro": [cls.__name__ for cls in EnhancedClass.__mro__],
        "enhanced_instance_name": enhanced.name,
        "enhanced_log_count": len(enhanced.get_log())
    }

def advanced_oop():
    """Demonstrate metaclasses and advanced OOP patterns."""
    print("\\n=== Advanced OOP ===")
    
    # Basic metaclass
    print("Basic Metaclass:")
    
    class SingletonMeta(type):
        \"\"\"Metaclass that creates singleton instances.\"\"\"
        _instances = {}
        
        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]
    
    class Database(metaclass=SingletonMeta):
        def __init__(self, connection_string="default"):
            self.connection_string = connection_string
            self.connections = 0
        
        def connect(self):
            self.connections += 1
            return f"Connected to {self.connection_string} (connection #{self.connections})"
    
    # Test singleton
    db1 = Database("postgres://localhost:5432/db1")
    db2 = Database("mysql://localhost:3306/db2")  # Same instance!
    
    print(f"db1 is db2: {db1 is db2}")
    print(f"db1.connection_string: {db1.connection_string}")
    print(f"db2.connection_string: {db2.connection_string}")
    print(f"db1 connect: {db1.connect()}")
    print(f"db2 connect: {db2.connect()}")
    
    # Attribute validation metaclass
    print("\\nAttribute Validation Metaclass:")
    
    class ValidatedMeta(type):
        \"\"\"Metaclass that adds validation to class attributes.\"\"\"
        
        def __new__(mcs, name, bases, attrs):
            # Find validation rules
            validations = {}
            for key, value in list(attrs.items()):
                if key.startswith('_validate_'):
                    attr_name = key[10:]  # Remove '_validate_' prefix
                    validations[attr_name] = value
                    del attrs[key]
            
            # Create class
            cls = super().__new__(mcs, name, bases, attrs)
            cls._validations = validations
            
            # Override __setattr__ to add validation
            original_setattr = cls.__setattr__ if hasattr(cls, '__setattr__') else object.__setattr__
            
            def validated_setattr(self, name, value):
                if name in cls._validations:
                    validator = cls._validations[name]
                    if not validator(value):
                        raise ValueError(f"Invalid value for {name}: {value}")
                original_setattr(self, name, value)
            
            cls.__setattr__ = validated_setattr
            return cls
    
    class Person(metaclass=ValidatedMeta):
        def _validate_age(value):
            return isinstance(value, int) and 0 <= value <= 150
        
        def _validate_name(value):
            return isinstance(value, str) and len(value.strip()) > 0
        
        def _validate_email(value):
            return isinstance(value, str) and '@' in value
        
        def __init__(self, name, age, email):
            self.name = name
            self.age = age
            self.email = email
        
        def __str__(self):
            return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"
    
    # Test validation
    person = Person("Alice", 30, "alice@example.com")
    print(f"Valid person: {person}")
    
    try:
        person.age = -5
    except ValueError as e:
        print(f"Validation error: {e}")
    
    try:
        person.email = "invalid-email"
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Auto-property metaclass
    print("\\nAuto-Property Metaclass:")
    
    class AutoPropertyMeta(type):
        \"\"\"Metaclass that automatically creates properties for private attributes.\"\"\"
        
        def __new__(mcs, name, bases, attrs):
            # Find attributes that should become properties
            properties = {}
            for key, value in list(attrs.items()):
                if key.startswith('_') and not key.startswith('__'):
                    prop_name = key[1:]  # Remove leading underscore
                    
                    # Create getter
                    def make_getter(attr_name):
                        def getter(self):
                            return getattr(self, attr_name)
                        return getter
                    
                    # Create setter
                    def make_setter(attr_name):
                        def setter(self, value):
                            setattr(self, attr_name, value)
                        return setter
                    
                    # Create property
                    prop = property(make_getter(key), make_setter(key))
                    properties[prop_name] = prop
            
            # Add properties to class
            attrs.update(properties)
            
            return super().__new__(mcs, name, bases, attrs)
    
    class AutoPropClass(metaclass=AutoPropertyMeta):
        def __init__(self, name, value):
            self._name = name      # Will become 'name' property
            self._value = value    # Will become 'value' property
            self._computed = None  # Will become 'computed' property
        
        def calculate(self):
            self._computed = self._value * 2
            return self._computed
    
    # Test auto-properties
    auto_obj = AutoPropClass("test", 42)
    
    print(f"Auto object name: {auto_obj.name}")
    print(f"Auto object value: {auto_obj.value}")
    
    auto_obj.name = "updated"
    auto_obj.value = 100
    result = auto_obj.calculate()
    
    print(f"Updated name: {auto_obj.name}")
    print(f"Updated value: {auto_obj.value}")
    print(f"Computed result: {auto_obj.computed}")
    
    # Registry metaclass
    print("\\nRegistry Metaclass:")
    
    class RegistryMeta(type):
        \"\"\"Metaclass that maintains a registry of all created classes.\"\"\"
        registry = {}
        
        def __new__(mcs, name, bases, attrs):
            cls = super().__new__(mcs, name, bases, attrs)
            mcs.registry[name] = cls
            return cls
        
        @classmethod
        def get_registered_classes(mcs):
            return mcs.registry.copy()
        
        @classmethod
        def get_class_by_name(mcs, name):
            return mcs.registry.get(name)
    
    class BasePlugin(metaclass=RegistryMeta):
        pass
    
    class TextPlugin(BasePlugin):
        def process(self, text):
            return text.upper()
    
    class NumberPlugin(BasePlugin):
        def process(self, number):
            return number * 2
    
    class DatePlugin(BasePlugin):
        def process(self, date):
            return f"Processed: {date}"
    
    # Test registry
    registered = RegistryMeta.get_registered_classes()
    print(f"Registered classes: {list(registered.keys())}")
    
    # Get class by name and use it
    TextPluginClass = RegistryMeta.get_class_by_name('TextPlugin')
    if TextPluginClass:
        plugin = TextPluginClass()
        result = plugin.process("hello world")
        print(f"TextPlugin result: {result}")
    
    # Debugging metaclass
    print("\\nDebugging Metaclass:")
    
    class DebugMeta(type):
        \"\"\"Metaclass that adds debugging to method calls.\"\"\"
        
        def __new__(mcs, name, bases, attrs):
            # Wrap methods with debugging
            for key, value in attrs.items():
                if callable(value) and not key.startswith('__'):
                    attrs[key] = mcs.debug_wrapper(value, key)
            
            return super().__new__(mcs, name, bases, attrs)
        
        @staticmethod
        def debug_wrapper(func, name):
            def wrapper(*args, **kwargs):
                print(f"DEBUG: Calling {name} with args={args[1:]} kwargs={kwargs}")
                result = func(*args, **kwargs)
                print(f"DEBUG: {name} returned {result}")
                return result
            return wrapper
    
    class DebuggedClass(metaclass=DebugMeta):
        def __init__(self, value):
            self.value = value
        
        def add(self, other):
            return self.value + other
        
        def multiply(self, other):
            return self.value * other
    
    # Test debugging
    debug_obj = DebuggedClass(10)
    add_result = debug_obj.add(5)
    mult_result = debug_obj.multiply(3)
    
    print(f"Final results: add={add_result}, multiply={mult_result}")
    
    # Class decorator as alternative to metaclass
    print("\\nClass Decorator Alternative:")
    
    def add_logging(cls):
        \"\"\"Class decorator that adds logging to methods.\"\"\"
        original_methods = {}
        
        for name in dir(cls):
            attr = getattr(cls, name)
            if callable(attr) and not name.startswith('__'):
                original_methods[name] = attr
                
                def make_logged_method(method, method_name):
                    def logged_method(*args, **kwargs):
                        print(f"LOG: Calling {method_name}")
                        result = method(*args, **kwargs)
                        print(f"LOG: {method_name} completed")
                        return result
                    return logged_method
                
                setattr(cls, name, make_logged_method(attr, name))
        
        cls._original_methods = original_methods
        return cls
    
    @add_logging
    class LoggedClass:
        def __init__(self, name):
            self.name = name
        
        def greet(self):
            return f"Hello, I'm {self.name}"
        
        def farewell(self):
            return f"Goodbye from {self.name}"
    
    # Test class decorator
    logged_obj = LoggedClass("Alice")
    greeting = logged_obj.greet()
    farewell = logged_obj.farewell()
    
    return {
        "singleton_test": db1 is db2,
        "singleton_connections": db1.connections,
        "validation_class_name": Person.__name__,
        "auto_property_name": auto_obj.name,
        "auto_property_computed": auto_obj.computed,
        "registered_classes": list(registered.keys()),
        "text_plugin_result": result,
        "debug_add_result": add_result,
        "debug_multiply_result": mult_result,
        "logged_greeting": greeting
    }

# Main execution
if __name__ == "__main__":
    print("=== Built-in Class and Object Creation Functions ===")
    
    print("\\n1. Type Operations:")
    type_results = type_operations()
    
    print("\\n2. Inheritance Checking:")
    inheritance_results = inheritance_checking()
    
    print("\\n3. Method Decorators:")
    decorator_results = method_decorators()
    
    print("\\n4. Super Mechanics:")
    super_results = super_mechanics()
    
    print("\\n5. Advanced OOP:")
    advanced_results = advanced_oop()
    
    print("\\n" + "="*60)
    print("=== CLASS AND OBJECT CREATION FUNCTIONS COMPLETE ===")
    print("✓ Dynamic type checking and class creation")
    print("✓ Inheritance relationship validation")
    print("✓ Method decorators and property management")
    print("✓ Super() mechanics and method resolution")
    print("✓ Metaclasses and advanced OOP patterns")
    print("✓ Plugin systems and class registries")
    print("✓ Debugging and logging decorators")
```

## Hints

- Use `type(obj, (), {})` syntax for dynamic class creation with three arguments
- `isinstance()` is preferred over `type()` checking for inheritance hierarchies
- Use `super()` without arguments in Python 3 for cleaner inheritance code
- Property decorators create descriptors for controlled attribute access
- Metaclasses control class creation itself, not just instances

## Test Cases

Your functions should handle:

1. Dynamic class creation with methods, properties, and inheritance
2. Type checking with complex inheritance hierarchies and multiple inheritance
3. Property creation with getters, setters, deleters, and validation
4. Method resolution order in complex inheritance scenarios
5. Metaclass implementation for singletons, validation, and registries

## Bonus Challenge

Create a dynamic ORM framework using metaclasses, implement a plugin architecture with automatic registration, and build a debugging toolkit with method interception!
