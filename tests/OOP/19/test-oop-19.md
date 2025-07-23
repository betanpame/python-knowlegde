# Advanced Metaclasses and Class Creation - Test 19

**Difficulty:** ⭐⭐⭐⭐ (Medium-Hard)

## Description

Master Python's metaclasses, custom class creation, and advanced object instantiation. Build systems that create and modify classes dynamically.

## Objectives

- Create custom metaclasses for class control
- Implement dynamic class generation
- Build attribute validation systems
- Create ORM-like class systems
- Implement class registration and discovery

## Your Tasks

1. **create_validation_metaclass()** - Build automatic validation system
2. **implement_dynamic_classes()** - Create classes at runtime
3. **build_orm_system()** - Create simple ORM with metaclasses
4. **create_plugin_system()** - Build plugin registration system
5. **implement_class_tracking()** - Track and manage class creation

## Example

```python
import abc
import inspect
import weakref
from typing import Any, Dict, List, Type, Callable, Optional, Union
from datetime import datetime
from collections import defaultdict
import functools
import json

# Validation Metaclass System
class ValidationError(Exception):
    """Custom validation error."""
    pass

class Validator:
    """Base validator class."""
    
    def __init__(self, message: str = None):
        """Initialize validator."""
        self.message = message or "Validation failed"
    
    def validate(self, value: Any) -> bool:
        """Validate a value."""
        raise NotImplementedError
    
    def __call__(self, value: Any) -> Any:
        """Validate and return value."""
        if not self.validate(value):
            raise ValidationError(f"{self.message}: {value}")
        return value

class TypeValidator(Validator):
    """Type validation."""
    
    def __init__(self, expected_type: Type, message: str = None):
        """Initialize type validator."""
        self.expected_type = expected_type
        super().__init__(message or f"Expected {expected_type.__name__}")
    
    def validate(self, value: Any) -> bool:
        """Check if value is correct type."""
        return isinstance(value, self.expected_type)

class RangeValidator(Validator):
    """Range validation for numbers."""
    
    def __init__(self, min_val: float = None, max_val: float = None, message: str = None):
        """Initialize range validator."""
        self.min_val = min_val
        self.max_val = max_val
        super().__init__(message or f"Value must be between {min_val} and {max_val}")
    
    def validate(self, value: Any) -> bool:
        """Check if value is in range."""
        if self.min_val is not None and value < self.min_val:
            return False
        if self.max_val is not None and value > self.max_val:
            return False
        return True

class LengthValidator(Validator):
    """Length validation for sequences."""
    
    def __init__(self, min_len: int = None, max_len: int = None, message: str = None):
        """Initialize length validator."""
        self.min_len = min_len
        self.max_len = max_len
        super().__init__(message or f"Length must be between {min_len} and {max_len}")
    
    def validate(self, value: Any) -> bool:
        """Check if value length is valid."""
        if not hasattr(value, '__len__'):
            return False
        length = len(value)
        if self.min_len is not None and length < self.min_len:
            return False
        if self.max_len is not None and length > self.max_len:
            return False
        return True

class ValidatedMeta(type):
    """Metaclass that adds automatic validation to classes."""
    
    def __new__(mcs, name, bases, namespace, **kwargs):
        """Create new class with validation."""
        
        # Extract validation rules
        validators = {}
        for key, value in list(namespace.items()):
            if key.startswith('_validate_'):
                attr_name = key[10:]  # Remove '_validate_' prefix
                validators[attr_name] = value
                del namespace[key]
        
        # Store validators in class
        namespace['_validators'] = validators
        
        # Create the class
        cls = super().__new__(mcs, name, bases, namespace)
        
        # Override __setattr__ to add validation
        original_setattr = cls.__setattr__
        
        def validated_setattr(self, name, value):
            """Setattr with validation."""
            if name in cls._validators:
                validator = cls._validators[name]
                if isinstance(validator, (list, tuple)):
                    for v in validator:
                        value = v(value)
                else:
                    value = validator(value)
            
            # Call original setattr
            if hasattr(original_setattr, '__func__'):
                original_setattr.__func__(self, name, value)
            else:
                object.__setattr__(self, name, value)
        
        cls.__setattr__ = validated_setattr
        
        return cls

class Person(metaclass=ValidatedMeta):
    """Person class with automatic validation."""
    
    # Validation rules
    _validate_name = [
        TypeValidator(str, "Name must be a string"),
        LengthValidator(min_len=1, max_len=100, "Name must be 1-100 characters")
    ]
    
    _validate_age = [
        TypeValidator(int, "Age must be an integer"),
        RangeValidator(min_val=0, max_val=150, "Age must be 0-150")
    ]
    
    _validate_email = [
        TypeValidator(str, "Email must be a string"),
        LengthValidator(min_len=5, max_len=254, "Email must be 5-254 characters")
    ]
    
    def __init__(self, name: str, age: int, email: str):
        """Initialize person."""
        self.name = name
        self.age = age
        self.email = email
        self.created_at = datetime.now()
    
    def __repr__(self):
        """String representation."""
        return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"

class Product(metaclass=ValidatedMeta):
    """Product class with validation."""
    
    _validate_name = [
        TypeValidator(str),
        LengthValidator(min_len=1, max_len=200)
    ]
    
    _validate_price = [
        TypeValidator((int, float)),
        RangeValidator(min_val=0)
    ]
    
    _validate_quantity = [
        TypeValidator(int),
        RangeValidator(min_val=0)
    ]
    
    def __init__(self, name: str, price: float, quantity: int = 0):
        """Initialize product."""
        self.name = name
        self.price = price
        self.quantity = quantity

# Dynamic Class Creation System
class ClassBuilder:
    """Builder for creating classes dynamically."""
    
    def __init__(self, class_name: str):
        """Initialize class builder."""
        self.class_name = class_name
        self.bases = (object,)
        self.namespace = {}
        self.metaclass = type
    
    def add_base(self, base_class: Type):
        """Add a base class."""
        self.bases = self.bases + (base_class,)
        return self
    
    def add_method(self, name: str, method: Callable):
        """Add a method to the class."""
        self.namespace[name] = method
        return self
    
    def add_attribute(self, name: str, value: Any):
        """Add an attribute to the class."""
        self.namespace[name] = value
        return self
    
    def add_property(self, name: str, getter: Callable, setter: Callable = None):
        """Add a property to the class."""
        if setter:
            self.namespace[name] = property(getter, setter)
        else:
            self.namespace[name] = property(getter)
        return self
    
    def set_metaclass(self, metaclass: Type):
        """Set the metaclass."""
        self.metaclass = metaclass
        return self
    
    def build(self) -> Type:
        """Build and return the class."""
        return self.metaclass(self.class_name, self.bases, self.namespace)

class DynamicClassFactory:
    """Factory for creating dynamic classes."""
    
    def __init__(self):
        """Initialize factory."""
        self.created_classes = {}
    
    def create_data_class(self, class_name: str, fields: Dict[str, Type]) -> Type:
        """Create a data class with specified fields."""
        
        def __init__(self, **kwargs):
            """Initialize data class instance."""
            for field_name, field_type in fields.items():
                value = kwargs.get(field_name)
                if value is not None and not isinstance(value, field_type):
                    raise TypeError(f"{field_name} must be {field_type.__name__}")
                setattr(self, field_name, value)
        
        def __repr__(self):
            """String representation."""
            field_strs = [f"{name}={getattr(self, name)}" for name in fields.keys()]
            return f"{class_name}({', '.join(field_strs)})"
        
        def __eq__(self, other):
            """Equality comparison."""
            if not isinstance(other, self.__class__):
                return False
            return all(getattr(self, name) == getattr(other, name) for name in fields.keys())
        
        namespace = {
            '__init__': __init__,
            '__repr__': __repr__,
            '__eq__': __eq__,
            '_fields': fields
        }
        
        cls = type(class_name, (object,), namespace)
        self.created_classes[class_name] = cls
        return cls
    
    def create_enum_class(self, class_name: str, values: List[str]) -> Type:
        """Create an enum-like class."""
        
        def __init__(self, value):
            """Initialize enum instance."""
            if value not in values:
                raise ValueError(f"Invalid value: {value}")
            self.value = value
        
        def __repr__(self):
            """String representation."""
            return f"{class_name}.{self.value}"
        
        def __eq__(self, other):
            """Equality comparison."""
            if isinstance(other, str):
                return self.value == other
            if isinstance(other, self.__class__):
                return self.value == other.value
            return False
        
        namespace = {
            '__init__': __init__,
            '__repr__': __repr__,
            '__eq__': __eq__,
            '_values': values
        }
        
        # Add class attributes for each value
        for value in values:
            namespace[value] = value
        
        cls = type(class_name, (object,), namespace)
        self.created_classes[class_name] = cls
        return cls

# Simple ORM System with Metaclasses
class Field:
    """Base field class for ORM."""
    
    def __init__(self, field_type: Type, default=None, nullable=True):
        """Initialize field."""
        self.field_type = field_type
        self.default = default
        self.nullable = nullable
        self.name = None  # Set by metaclass
    
    def validate(self, value):
        """Validate field value."""
        if value is None:
            if not self.nullable:
                raise ValueError(f"Field {self.name} cannot be None")
            return value
        
        if not isinstance(value, self.field_type):
            raise TypeError(f"Field {self.name} must be {self.field_type.__name__}")
        
        return value
    
    def __get__(self, obj, objtype=None):
        """Get field value."""
        if obj is None:
            return self
        return obj.__dict__.get(self.name, self.default)
    
    def __set__(self, obj, value):
        """Set field value."""
        validated_value = self.validate(value)
        obj.__dict__[self.name] = validated_value

class CharField(Field):
    """Character field with length validation."""
    
    def __init__(self, max_length=255, **kwargs):
        """Initialize char field."""
        super().__init__(str, **kwargs)
        self.max_length = max_length
    
    def validate(self, value):
        """Validate string field."""
        value = super().validate(value)
        if value is not None and len(value) > self.max_length:
            raise ValueError(f"Field {self.name} exceeds max length {self.max_length}")
        return value

class IntegerField(Field):
    """Integer field with range validation."""
    
    def __init__(self, min_value=None, max_value=None, **kwargs):
        """Initialize integer field."""
        super().__init__(int, **kwargs)
        self.min_value = min_value
        self.max_value = max_value
    
    def validate(self, value):
        """Validate integer field."""
        value = super().validate(value)
        if value is not None:
            if self.min_value is not None and value < self.min_value:
                raise ValueError(f"Field {self.name} below minimum {self.min_value}")
            if self.max_value is not None and value > self.max_value:
                raise ValueError(f"Field {self.name} above maximum {self.max_value}")
        return value

class ModelMeta(type):
    """Metaclass for ORM models."""
    
    def __new__(mcs, name, bases, namespace, **kwargs):
        """Create new model class."""
        
        # Extract fields
        fields = {}
        for key, value in list(namespace.items()):
            if isinstance(value, Field):
                fields[key] = value
                value.name = key
        
        # Store fields in class
        namespace['_fields'] = fields
        
        # Add save/load methods
        def save(self, storage: Dict[str, List]):
            """Save instance to storage."""
            if name not in storage:
                storage[name] = []
            
            instance_data = {}
            for field_name in self._fields:
                instance_data[field_name] = getattr(self, field_name)
            
            storage[name].append(instance_data)
            return len(storage[name]) - 1  # Return index as ID
        
        def load(cls, storage: Dict[str, List], index: int):
            """Load instance from storage."""
            if name not in storage or index >= len(storage[name]):
                raise ValueError(f"No {name} at index {index}")
            
            data = storage[name][index]
            instance = cls()
            for field_name, value in data.items():
                setattr(instance, field_name, value)
            return instance
        
        namespace['save'] = save
        namespace['load'] = classmethod(load)
        
        return super().__new__(mcs, name, bases, namespace)

class Model(metaclass=ModelMeta):
    """Base model class."""
    
    def __init__(self, **kwargs):
        """Initialize model instance."""
        for field_name, field in self._fields.items():
            value = kwargs.get(field_name, field.default)
            setattr(self, field_name, value)
    
    def __repr__(self):
        """String representation."""
        field_strs = []
        for field_name in self._fields:
            value = getattr(self, field_name)
            field_strs.append(f"{field_name}={value}")
        return f"{self.__class__.__name__}({', '.join(field_strs)})"

class User(Model):
    """User model example."""
    
    username = CharField(max_length=50, nullable=False)
    email = CharField(max_length=254, nullable=False)
    age = IntegerField(min_value=0, max_value=150)
    is_active = Field(bool, default=True)

class Article(Model):
    """Article model example."""
    
    title = CharField(max_length=200, nullable=False)
    content = CharField(max_length=5000)
    author = CharField(max_length=100)
    published = Field(bool, default=False)

# Plugin Registration System
class PluginMeta(type):
    """Metaclass for automatic plugin registration."""
    
    _registry = defaultdict(list)
    
    def __new__(mcs, name, bases, namespace, **kwargs):
        """Create new plugin class."""
        cls = super().__new__(mcs, name, bases, namespace)
        
        # Register plugin if it has a plugin_type
        plugin_type = getattr(cls, 'plugin_type', None)
        if plugin_type:
            mcs._registry[plugin_type].append(cls)
            print(f"Registered plugin: {name} (type: {plugin_type})")
        
        return cls
    
    @classmethod
    def get_plugins(mcs, plugin_type: str) -> List[Type]:
        """Get all plugins of a specific type."""
        return mcs._registry[plugin_type].copy()
    
    @classmethod
    def get_all_plugins(mcs) -> Dict[str, List[Type]]:
        """Get all registered plugins."""
        return dict(mcs._registry)

class Plugin(metaclass=PluginMeta):
    """Base plugin class."""
    
    plugin_type = None  # Override in subclasses
    
    def execute(self):
        """Execute the plugin."""
        raise NotImplementedError

class DataProcessor(Plugin):
    """Data processing plugin."""
    
    plugin_type = "data_processor"
    
    def process_data(self, data):
        """Process data."""
        raise NotImplementedError

class CSVProcessor(DataProcessor):
    """CSV data processor."""
    
    def execute(self):
        """Execute CSV processing."""
        return "Processing CSV data"
    
    def process_data(self, data):
        """Process CSV data."""
        return f"Processed {len(data)} CSV records"

class JSONProcessor(DataProcessor):
    """JSON data processor."""
    
    def execute(self):
        """Execute JSON processing."""
        return "Processing JSON data"
    
    def process_data(self, data):
        """Process JSON data."""
        return f"Processed JSON with {len(data)} keys"

class ReportGenerator(Plugin):
    """Report generation plugin."""
    
    plugin_type = "report_generator"
    
    def generate_report(self, data):
        """Generate report."""
        raise NotImplementedError

class PDFReportGenerator(ReportGenerator):
    """PDF report generator."""
    
    def execute(self):
        """Execute PDF generation."""
        return "Generating PDF report"
    
    def generate_report(self, data):
        """Generate PDF report."""
        return f"Generated PDF report with {len(data)} pages"

class HTMLReportGenerator(ReportGenerator):
    """HTML report generator."""
    
    def execute(self):
        """Execute HTML generation."""
        return "Generating HTML report"
    
    def generate_report(self, data):
        """Generate HTML report."""
        return f"Generated HTML report with {len(data)} sections"

# Class Tracking System
class TrackedMeta(type):
    """Metaclass that tracks class creation and usage."""
    
    _class_registry = {}
    _instance_counts = defaultdict(int)
    _creation_log = []
    
    def __new__(mcs, name, bases, namespace, **kwargs):
        """Track class creation."""
        cls = super().__new__(mcs, name, bases, namespace)
        
        # Register class
        mcs._class_registry[name] = {
            'class': cls,
            'bases': bases,
            'created_at': datetime.now(),
            'namespace_size': len(namespace)
        }
        
        # Log creation
        mcs._creation_log.append({
            'class_name': name,
            'timestamp': datetime.now(),
            'base_count': len(bases),
            'method_count': len([k for k, v in namespace.items() if callable(v)])
        })
        
        # Override __call__ to track instantiation
        original_call = cls.__call__
        
        def tracked_call(*args, **kwargs):
            """Track instance creation."""
            mcs._instance_counts[name] += 1
            return original_call(*args, **kwargs)
        
        cls.__call__ = tracked_call
        
        print(f"Tracked class created: {name}")
        return cls
    
    @classmethod
    def get_class_info(mcs, class_name: str) -> Dict[str, Any]:
        """Get information about a tracked class."""
        return mcs._class_registry.get(class_name, {})
    
    @classmethod
    def get_instance_count(mcs, class_name: str) -> int:
        """Get instance count for a class."""
        return mcs._instance_counts[class_name]
    
    @classmethod
    def get_creation_log(mcs) -> List[Dict[str, Any]]:
        """Get class creation log."""
        return mcs._creation_log.copy()
    
    @classmethod
    def get_statistics(mcs) -> Dict[str, Any]:
        """Get overall statistics."""
        total_classes = len(mcs._class_registry)
        total_instances = sum(mcs._instance_counts.values())
        
        return {
            'total_classes': total_classes,
            'total_instances': total_instances,
            'avg_instances_per_class': total_instances / total_classes if total_classes else 0,
            'most_instantiated': max(mcs._instance_counts.items(), key=lambda x: x[1]) if mcs._instance_counts else None
        }

class TrackedClass(metaclass=TrackedMeta):
    """Base class for tracked classes."""
    
    def __init__(self, name: str):
        """Initialize tracked instance."""
        self.name = name
        self.created_at = datetime.now()

class Employee(TrackedClass):
    """Employee class that's automatically tracked."""
    
    def __init__(self, name: str, department: str):
        """Initialize employee."""
        super().__init__(name)
        self.department = department

class Customer(TrackedClass):
    """Customer class that's automatically tracked."""
    
    def __init__(self, name: str, email: str):
        """Initialize customer."""
        super().__init__(name)
        self.email = email

# Example usage and tests
def create_validation_metaclass():
    """Demonstrate validation metaclass."""
    print("=== Validation Metaclass ===")
    
    # Test valid person creation
    try:
        person1 = Person("Alice Smith", 30, "alice@example.com")
        print(f"Created: {person1}")
        
        # Test valid updates
        person1.age = 31
        person1.name = "Alice Johnson"
        print(f"Updated: {person1}")
        
    except ValidationError as e:
        print(f"Validation error: {e}")
    
    # Test invalid data
    try:
        invalid_person = Person("", -5, "invalid")  # Should fail
    except ValidationError as e:
        print(f"Expected validation error: {e}")
    
    # Test product validation
    try:
        product = Product("Laptop", 999.99, 10)
        print(f"Created: {product}")
        
        product.price = -100  # Should fail
    except ValidationError as e:
        print(f"Expected validation error: {e}")
    
    return person1

def implement_dynamic_classes():
    """Demonstrate dynamic class creation."""
    print("\n=== Dynamic Class Creation ===")
    
    # Test class builder
    print("1. Using ClassBuilder:")
    
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    def get_age(self):
        return getattr(self, '_age', 0)
    
    def set_age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
    
    DynamicPerson = (ClassBuilder("DynamicPerson")
                     .add_method("greet", greet)
                     .add_property("age", get_age, set_age)
                     .add_attribute("species", "Human")
                     .build())
    
    dp = DynamicPerson()
    dp.name = "Bob"
    dp.age = 25
    print(f"  {dp.greet()}")
    print(f"  Age: {dp.age}")
    print(f"  Species: {dp.species}")
    
    # Test dynamic class factory
    print("\n2. Using DynamicClassFactory:")
    factory = DynamicClassFactory()
    
    # Create data class
    Point = factory.create_data_class("Point", {
        'x': int,
        'y': int,
        'label': str
    })
    
    point1 = Point(x=10, y=20, label="Origin")
    point2 = Point(x=10, y=20, label="Origin")
    print(f"  Point 1: {point1}")
    print(f"  Point 1 == Point 2: {point1 == point2}")
    
    # Create enum class
    Status = factory.create_enum_class("Status", ["PENDING", "APPROVED", "REJECTED"])
    status = Status("PENDING")
    print(f"  Status: {status}")
    print(f"  Status == 'PENDING': {status == 'PENDING'}")
    
    return DynamicPerson, factory

def build_orm_system():
    """Demonstrate ORM system."""
    print("\n=== ORM System ===")
    
    # Create storage
    storage = {}
    
    # Create and save users
    user1 = User(username="john_doe", email="john@example.com", age=28)
    user2 = User(username="jane_smith", email="jane@example.com", age=32)
    
    user1_id = user1.save(storage)
    user2_id = user2.save(storage)
    
    print(f"Saved users: {user1_id}, {user2_id}")
    print(f"User 1: {user1}")
    print(f"User 2: {user2}")
    
    # Load user from storage
    loaded_user = User.load(storage, user1_id)
    print(f"Loaded user: {loaded_user}")
    
    # Create and save articles
    article1 = Article(
        title="Introduction to Python", 
        content="Python is a great language...",
        author="john_doe",
        published=True
    )
    
    article1_id = article1.save(storage)
    print(f"Saved article: {article1}")
    
    # Test validation
    try:
        invalid_user = User(username="", email="invalid", age=-1)
    except (ValueError, TypeError) as e:
        print(f"Expected error: {e}")
    
    return storage, [user1, user2, article1]

def create_plugin_system():
    """Demonstrate plugin system."""
    print("\n=== Plugin System ===")
    
    # Show registered plugins
    all_plugins = PluginMeta.get_all_plugins()
    print("Registered plugins by type:")
    for plugin_type, plugins in all_plugins.items():
        print(f"  {plugin_type}: {[p.__name__ for p in plugins]}")
    
    # Test data processors
    print("\nTesting data processors:")
    processors = PluginMeta.get_plugins("data_processor")
    test_data = [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]
    
    for processor_class in processors:
        processor = processor_class()
        print(f"  {processor.execute()}")
        print(f"  {processor.process_data(test_data)}")
    
    # Test report generators
    print("\nTesting report generators:")
    generators = PluginMeta.get_plugins("report_generator")
    report_data = ["Page 1", "Page 2", "Page 3"]
    
    for generator_class in generators:
        generator = generator_class()
        print(f"  {generator.execute()}")
        print(f"  {generator.generate_report(report_data)}")
    
    return all_plugins

def implement_class_tracking():
    """Demonstrate class tracking."""
    print("\n=== Class Tracking ===")
    
    # Create instances
    employees = [
        Employee("Alice Johnson", "Engineering"),
        Employee("Bob Smith", "Marketing"),
        Employee("Carol Davis", "Engineering")
    ]
    
    customers = [
        Customer("David Wilson", "david@email.com"),
        Customer("Eve Brown", "eve@email.com")
    ]
    
    print(f"Created {len(employees)} employees and {len(customers)} customers")
    
    # Show statistics
    stats = TrackedMeta.get_statistics()
    print(f"\nTracking Statistics:")
    print(f"  Total classes: {stats['total_classes']}")
    print(f"  Total instances: {stats['total_instances']}")
    print(f"  Average instances per class: {stats['avg_instances_per_class']:.1f}")
    if stats['most_instantiated']:
        print(f"  Most instantiated: {stats['most_instantiated'][0]} ({stats['most_instantiated'][1]} instances)")
    
    # Show instance counts
    print(f"\nInstance counts:")
    for class_name in ['Employee', 'Customer']:
        count = TrackedMeta.get_instance_count(class_name)
        info = TrackedMeta.get_class_info(class_name)
        print(f"  {class_name}: {count} instances (created at {info.get('created_at')})")
    
    # Show creation log
    print(f"\nCreation log:")
    for entry in TrackedMeta.get_creation_log():
        print(f"  {entry['class_name']}: {entry['method_count']} methods, {entry['base_count']} bases")
    
    return employees, customers

# Test all metaclass features
if __name__ == "__main__":
    # Test validation metaclass
    validation_result = create_validation_metaclass()
    
    # Test dynamic class creation
    dynamic_results = implement_dynamic_classes()
    
    # Test ORM system
    orm_results = build_orm_system()
    
    # Test plugin system
    plugin_results = create_plugin_system()
    
    # Test class tracking
    tracking_results = implement_class_tracking()
    
    print("\n=== Metaclass System Complete ===")
    print("Advanced metaclass features demonstrated:")
    print("  ✓ Validation metaclass - Automatic attribute validation")
    print("  ✓ Dynamic classes - Runtime class creation")
    print("  ✓ ORM system - Database-like model classes")
    print("  ✓ Plugin system - Automatic registration")
    print("  ✓ Class tracking - Instance and creation monitoring")
```

## Hints

- Metaclasses control class creation through `__new__` method
- Use `type()` function to create classes dynamically
- Store metadata in class attributes for later use
- Weak references prevent memory leaks in registries
- Override `__setattr__` for attribute validation

## Test Cases

Your metaclass system should:

- ValidationMeta: Automatically validate attribute assignments
- DynamicFactory: Create classes with specified attributes/methods
- ORMMeta: Add save/load methods to model classes
- PluginMeta: Register classes automatically by type
- TrackedMeta: Monitor class creation and instance counts

## Bonus Challenge

Create a metaclass that implements automatic caching, method timing, and access logging for all class methods!
