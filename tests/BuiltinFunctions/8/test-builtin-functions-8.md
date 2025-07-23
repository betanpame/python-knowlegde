# Attribute and Introspection Functions - Test 8

**Difficulty:** ⭐⭐⭐ (Medium)

## Description

Master Python's built-in introspection functions including `getattr()`, `setattr()`, `hasattr()`, `delattr()`, `dir()`, `vars()`, `globals()`, `locals()`, and advanced object inspection techniques.

## Objectives

- Use attribute functions for dynamic object manipulation
- Perform introspection with `dir()`, `vars()`, and inspection functions
- Work with namespaces using `globals()` and `locals()`
- Understand Python's attribute lookup mechanism
- Build dynamic systems using introspection capabilities

## Your Tasks

1. **attribute_operations()** - Master getattr, setattr, hasattr, delattr
2. **introspection_basics()** - Use dir(), vars(), and basic inspection
3. **namespace_exploration()** - Work with globals(), locals(), and scopes
4. **dynamic_programming()** - Build systems using introspection
5. **advanced_inspection()** - Deep object inspection and analysis

## Example

```python
import inspect
import types
import sys
from typing import Any, Dict, List, Callable
import json

def attribute_operations():
    """Demonstrate getattr, setattr, hasattr, and delattr functions."""
    print("=== Attribute Operations ===")
    
    # Basic attribute operations
    print("Basic Attribute Operations:")
    
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            self.active = True
        
        def greet(self):
            return f"Hello, I'm {self.name}"
        
        def __str__(self):
            return f"Person(name='{self.name}', age={self.age})"
    
    person = Person("Alice", 30)
    
    # hasattr - check if attribute exists
    print(f"Person object: {person}")
    print(f"Has 'name' attribute: {hasattr(person, 'name')}")
    print(f"Has 'email' attribute: {hasattr(person, 'email')}")
    print(f"Has 'greet' method: {hasattr(person, 'greet')}")
    print(f"Has '__str__' method: {hasattr(person, '__str__')}")
    
    # getattr - get attribute value
    print("\\nGetting Attributes:")
    
    name = getattr(person, 'name')
    age = getattr(person, 'age', 0)  # Default value
    email = getattr(person, 'email', 'Not provided')  # Default for missing attr
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    
    # Get method and call it
    greet_method = getattr(person, 'greet')
    greeting = greet_method()
    print(f"Greeting: {greeting}")
    
    # setattr - set attribute value
    print("\\nSetting Attributes:")
    
    setattr(person, 'email', 'alice@example.com')
    setattr(person, 'department', 'Engineering')
    setattr(person, 'salary', 75000)
    
    print(f"After setting attributes: {vars(person)}")
    
    # Dynamic attribute setting
    attributes_to_set = {
        'city': 'New York',
        'country': 'USA',
        'phone': '+1-555-0123'
    }
    
    for attr_name, attr_value in attributes_to_set.items():
        setattr(person, attr_name, attr_value)
    
    print(f"After dynamic setting: {vars(person)}")
    
    # delattr - delete attribute
    print("\\nDeleting Attributes:")
    
    print(f"Before deletion - has phone: {hasattr(person, 'phone')}")
    delattr(person, 'phone')
    print(f"After deletion - has phone: {hasattr(person, 'phone')}")
    
    # Safe attribute deletion
    def safe_delattr(obj, attr_name):
        if hasattr(obj, attr_name):
            delattr(obj, attr_name)
            return True
        return False
    
    deleted_city = safe_delattr(person, 'city')
    deleted_nonexistent = safe_delattr(person, 'nonexistent')
    
    print(f"Deleted 'city': {deleted_city}")
    print(f"Deleted 'nonexistent': {deleted_nonexistent}")
    print(f"Final attributes: {list(vars(person).keys())}")
    
    # Attribute operations with classes
    print("\\nClass Attribute Operations:")
    
    class DynamicClass:
        class_var = "I'm a class variable"
    
    # Check class attributes
    print(f"Has 'class_var': {hasattr(DynamicClass, 'class_var')}")
    print(f"Class var value: {getattr(DynamicClass, 'class_var')}")
    
    # Add class attributes dynamically
    setattr(DynamicClass, 'new_class_var', 'I was added dynamically')
    setattr(DynamicClass, 'class_method', classmethod(lambda cls: f"Called from {cls.__name__}"))
    
    print(f"New class var: {getattr(DynamicClass, 'new_class_var')}")
    
    # Create instance and test
    obj = DynamicClass()
    print(f"Instance access to class var: {obj.class_var}")
    print(f"Instance access to new var: {obj.new_class_var}")
    
    # Property-like behavior with getattr
    print("\\nProperty-like Behavior:")
    
    class SmartObject:
        def __init__(self):
            self._data = {}
        
        def __getattr__(self, name):
            if name.startswith('get_'):
                key = name[4:]  # Remove 'get_' prefix
                return lambda: self._data.get(key, f"No data for {key}")
            elif name.startswith('set_'):
                key = name[4:]  # Remove 'set_' prefix
                return lambda value: self._data.update({key: value})
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        
        def __setattr__(self, name, value):
            if name.startswith('_'):
                super().__setattr__(name, value)
            else:
                self._data[name] = value
        
        def __hasattr__(self, name):
            return name.startswith(('get_', 'set_')) or name in self._data
    
    smart_obj = SmartObject()
    
    # Test dynamic methods
    smart_obj.username = "alice"
    smart_obj.age = 30
    
    get_username = getattr(smart_obj, 'get_username')
    set_email = getattr(smart_obj, 'set_email')
    
    print(f"Username: {get_username()}")
    set_email('alice@example.com')
    
    get_email = getattr(smart_obj, 'get_email')
    print(f"Email: {get_email()}")
    print(f"Data: {smart_obj._data}")
    
    return {
        "person_attributes": list(vars(person).keys()),
        "has_name": hasattr(person, 'name'),
        "has_email": hasattr(person, 'email'),
        "email_value": getattr(person, 'email', 'Not found'),
        "deleted_attributes": ["phone", "city"],
        "class_attributes": list(vars(DynamicClass).keys()),
        "smart_object_data": smart_obj._data
    }

def introspection_basics():
    """Demonstrate dir(), vars(), and basic introspection functions."""
    print("\\n=== Introspection Basics ===")
    
    # dir() function
    print("dir() Function:")
    
    # Basic types
    basic_objects = [
        42,
        "hello",
        [1, 2, 3],
        {"key": "value"},
        lambda x: x * 2
    ]
    
    for obj in basic_objects:
        obj_dir = dir(obj)
        obj_type = type(obj).__name__
        print(f"{obj_type} has {len(obj_dir)} attributes/methods")
        
        # Show some interesting methods
        interesting = [attr for attr in obj_dir if not attr.startswith('_')][:5]
        if interesting:
            print(f"  Non-dunder methods: {interesting}")
        
        # Show dunder methods
        dunder = [attr for attr in obj_dir if attr.startswith('__') and attr.endswith('__')][:3]
        print(f"  Sample dunder methods: {dunder}")
        print()
    
    # Custom class introspection
    print("Custom Class Introspection:")
    
    class ExampleClass:
        class_variable = "I'm a class variable"
        
        def __init__(self, value):
            self.instance_variable = value
            self._private_var = "private"
        
        def public_method(self):
            return "public method called"
        
        def _private_method(self):
            return "private method called"
        
        @staticmethod
        def static_method():
            return "static method called"
        
        @classmethod
        def class_method(cls):
            return f"class method called on {cls.__name__}"
        
        @property
        def computed_property(self):
            return f"computed: {self.instance_variable}"
    
    # Class introspection
    class_dir = dir(ExampleClass)
    print(f"ExampleClass has {len(class_dir)} attributes")
    
    # Categorize attributes
    methods = []
    properties = []
    variables = []
    dunder = []
    
    for attr_name in class_dir:
        if attr_name.startswith('__') and attr_name.endswith('__'):
            dunder.append(attr_name)
        else:
            attr = getattr(ExampleClass, attr_name)
            if callable(attr):
                methods.append(attr_name)
            elif isinstance(attr, property):
                properties.append(attr_name)
            else:
                variables.append(attr_name)
    
    print(f"  Methods: {methods}")
    print(f"  Properties: {properties}")
    print(f"  Variables: {variables}")
    print(f"  Dunder methods: {len(dunder)}")
    
    # Instance introspection
    instance = ExampleClass("test value")
    instance_dir = dir(instance)
    
    print(f"\\nInstance has {len(instance_dir)} attributes")
    
    # vars() function
    print("\\nvars() Function:")
    
    # Class vars
    class_vars = vars(ExampleClass)
    print(f"Class vars: {list(class_vars.keys())}")
    
    # Instance vars
    instance_vars = vars(instance)
    print(f"Instance vars: {instance_vars}")
    
    # Add more instance variables
    instance.new_attr = "dynamically added"
    instance.another_attr = [1, 2, 3]
    
    updated_vars = vars(instance)
    print(f"Updated instance vars: {updated_vars}")
    
    # Introspection with modules
    print("\\nModule Introspection:")
    
    import math
    import datetime
    
    modules_to_inspect = [math, datetime]
    
    for module in modules_to_inspect:
        module_dir = dir(module)
        module_name = module.__name__
        
        # Get callable functions
        functions = [name for name in module_dir 
                    if callable(getattr(module, name)) and not name.startswith('_')]
        
        # Get constants/variables
        constants = [name for name in module_dir 
                    if not callable(getattr(module, name)) and not name.startswith('_')]
        
        print(f"Module {module_name}:")
        print(f"  Functions: {len(functions)} (examples: {functions[:5]})")
        print(f"  Constants: {len(constants)} (examples: {constants[:5]})")
    
    # Object inspection helpers
    print("\\nObject Inspection Helpers:")
    
    def inspect_object(obj, name="object"):
        """Comprehensive object inspection."""
        print(f"\\nInspecting {name} ({type(obj).__name__}):")
        
        # Basic info
        obj_dir = dir(obj)
        print(f"  Total attributes: {len(obj_dir)}")
        
        # Categorize
        public_attrs = [attr for attr in obj_dir if not attr.startswith('_')]
        private_attrs = [attr for attr in obj_dir if attr.startswith('_') and not attr.startswith('__')]
        dunder_attrs = [attr for attr in obj_dir if attr.startswith('__') and attr.endswith('__')]
        
        print(f"  Public: {len(public_attrs)}")
        print(f"  Private: {len(private_attrs)}")
        print(f"  Dunder: {len(dunder_attrs)}")
        
        # Show callable vs non-callable
        callable_attrs = [attr for attr in public_attrs if callable(getattr(obj, attr, None))]
        non_callable_attrs = [attr for attr in public_attrs if not callable(getattr(obj, attr, None))]
        
        print(f"  Public methods: {callable_attrs}")
        print(f"  Public variables: {non_callable_attrs}")
        
        # Show instance variables if available
        if hasattr(obj, '__dict__'):
            instance_vars = vars(obj)
            print(f"  Instance variables: {list(instance_vars.keys())}")
        
        return {
            "total": len(obj_dir),
            "public": len(public_attrs),
            "private": len(private_attrs),
            "dunder": len(dunder_attrs),
            "methods": callable_attrs,
            "variables": non_callable_attrs
        }
    
    # Inspect various objects
    objects_to_inspect = [
        (instance, "ExampleClass instance"),
        (ExampleClass, "ExampleClass"),
        ([1, 2, 3], "list"),
        ({"a": 1}, "dict")
    ]
    
    inspection_results = {}
    for obj, name in objects_to_inspect:
        inspection_results[name] = inspect_object(obj, name)
    
    return {
        "basic_object_attrs": {type(obj).__name__: len(dir(obj)) for obj in basic_objects},
        "example_class_methods": methods,
        "example_class_properties": properties,
        "instance_vars": updated_vars,
        "module_functions": {mod.__name__: len([name for name in dir(mod) 
                                               if callable(getattr(mod, name)) and not name.startswith('_')])
                            for mod in modules_to_inspect},
        "inspection_results": inspection_results
    }

def namespace_exploration():
    """Demonstrate globals(), locals(), and namespace operations."""
    print("\\n=== Namespace Exploration ===")
    
    # Global namespace
    print("Global Namespace:")
    
    # Get current globals
    current_globals = globals()
    
    # Filter out built-ins and imports for cleaner display
    user_globals = {k: v for k, v in current_globals.items() 
                   if not k.startswith('__') and not inspect.ismodule(v)}
    
    print(f"Total global names: {len(current_globals)}")
    print(f"User-defined globals: {len(user_globals)}")
    print(f"Sample user globals: {list(user_globals.keys())[:10]}")
    
    # Add global variables dynamically
    globals()['dynamic_global'] = "I was added dynamically"
    globals()['global_counter'] = 0
    
    print(f"Added dynamic globals: dynamic_global = {dynamic_global}")
    
    # Local namespace
    print("\\nLocal Namespace:")
    
    def demonstrate_locals():
        local_var1 = "I'm local"
        local_var2 = 42
        local_var3 = [1, 2, 3]
        
        current_locals = locals()
        print(f"  Local variables: {list(current_locals.keys())}")
        print(f"  Local values: {current_locals}")
        
        # Modify locals (note: changes may not persist)
        current_locals['new_local'] = "added to locals dict"
        print(f"  After modification: {list(current_locals.keys())}")
        
        # Try to access the new variable (may not work)
        try:
            print(f"  new_local value: {new_local}")
        except NameError:
            print("  new_local not accessible (locals() modification doesn't create variables)")
        
        return current_locals
    
    local_namespace = demonstrate_locals()
    
    # Nested scopes
    print("\\nNested Scopes:")
    
    def outer_function(outer_param):
        outer_var = "I'm in outer scope"
        
        def inner_function(inner_param):
            inner_var = "I'm in inner scope"
            
            print(f"    Inner locals: {list(locals().keys())}")
            print(f"    Inner can see outer_var: {outer_var}")
            print(f"    Inner can see outer_param: {outer_param}")
            
            # Access to different scopes
            scopes = {
                'local': locals(),
                'global': globals()
            }
            
            return scopes
        
        print(f"  Outer locals: {list(locals().keys())}")
        return inner_function("inner_value")
    
    nested_scopes = outer_function("outer_value")
    
    # Namespace modifications
    print("\\nNamespace Modifications:")
    
    def modify_namespaces():
        # Local modifications
        local_dict = locals()
        print(f"  Before: {list(local_dict.keys())}")
        
        # Add variables normally
        new_var = "normal assignment"
        another_var = 123
        
        updated_locals = locals()
        print(f"  After normal assignment: {list(updated_locals.keys())}")
        
        # Global modifications
        global global_counter
        global_counter += 1
        
        # Add new global
        globals()['function_global'] = f"Set from function {global_counter}"
        
        return updated_locals
    
    modified_locals = modify_namespaces()
    
    print(f"Global counter after modification: {global_counter}")
    print(f"Function global: {globals().get('function_global', 'Not found')}")
    
    # Variable lookup order (LEGB)
    print("\\nLEGB Rule Demonstration:")
    
    builtin_len = len  # Built-in
    
    global_var = "I'm global"
    
    def demonstrate_legb():
        enclosing_var = "I'm enclosing"
        
        def inner_legb():
            local_var = "I'm local"
            
            # Demonstrate lookup order
            print(f"    Local variable: {local_var}")
            print(f"    Enclosing variable: {enclosing_var}")
            print(f"    Global variable: {global_var}")
            print(f"    Built-in function: {builtin_len([1, 2, 3])}")
            
            # Show what's in each namespace
            return {
                'local': list(locals().keys()),
                'enclosing': 'enclosing_var',
                'global': 'global_var' in globals(),
                'builtin': 'len' in dir(__builtins__)
            }
        
        return inner_legb()
    
    legb_demo = demonstrate_legb()
    
    # Exec and eval with namespaces
    print("\\nExec and Eval with Namespaces:")
    
    # Custom namespace for exec
    custom_namespace = {
        'x': 10,
        'y': 20,
        'math': __import__('math')
    }
    
    # Execute code in custom namespace
    code = """
result = x + y
squared = x ** 2
pi_value = math.pi
computed = math.sqrt(x * y)
"""
    
    exec(code, custom_namespace)
    
    print(f"  Custom namespace after exec:")
    for key, value in custom_namespace.items():
        if not key.startswith('__'):
            print(f"    {key}: {value}")
    
    # Eval with custom namespace
    expression = "x * y + math.sqrt(result)"
    eval_result = eval(expression, custom_namespace)
    print(f"  Eval result: {eval_result}")
    
    # Namespace inspection utilities
    print("\\nNamespace Utilities:")
    
    def compare_namespaces(ns1, ns2, name1="ns1", name2="ns2"):
        """Compare two namespaces."""
        keys1 = set(ns1.keys())
        keys2 = set(ns2.keys())
        
        common = keys1 & keys2
        only_in_1 = keys1 - keys2
        only_in_2 = keys2 - keys1
        
        print(f"  Comparing {name1} and {name2}:")
        print(f"    Common keys: {len(common)}")
        print(f"    Only in {name1}: {len(only_in_1)}")
        print(f"    Only in {name2}: {len(only_in_2)}")
        
        return {
            'common': len(common),
            'only_in_first': len(only_in_1),
            'only_in_second': len(only_in_2)
        }
    
    # Compare different namespaces
    comparison = compare_namespaces(
        globals(), 
        vars(__builtins__) if hasattr(__builtins__, '__dict__') else __builtins__, 
        "globals", "builtins"
    )
    
    return {
        "total_globals": len(current_globals),
        "user_globals": len(user_globals),
        "local_vars_count": len(local_namespace),
        "nested_scopes_keys": list(nested_scopes['local'].keys()),
        "global_counter": global_counter,
        "legb_demo": legb_demo,
        "custom_namespace_vars": [k for k in custom_namespace.keys() if not k.startswith('__')],
        "eval_result": eval_result,
        "namespace_comparison": comparison
    }

def dynamic_programming():
    """Demonstrate dynamic programming using introspection."""
    print("\\n=== Dynamic Programming ===")
    
    # Dynamic method calling
    print("Dynamic Method Calling:")
    
    class Calculator:
        def add(self, a, b):
            return a + b
        
        def subtract(self, a, b):
            return a - b
        
        def multiply(self, a, b):
            return a * b
        
        def divide(self, a, b):
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
        
        def power(self, a, b):
            return a ** b
        
        def get_operations(self):
            """Get all available operations."""
            return [method for method in dir(self) 
                   if callable(getattr(self, method)) and not method.startswith('_')]
    
    calc = Calculator()
    
    # Get available operations
    operations = calc.get_operations()
    print(f"Available operations: {operations}")
    
    # Dynamic method calling
    operation_tests = [
        ('add', 10, 5),
        ('subtract', 10, 5),
        ('multiply', 10, 5),
        ('divide', 10, 5),
        ('power', 2, 3)
    ]
    
    results = {}
    for op_name, arg1, arg2 in operation_tests:
        if hasattr(calc, op_name):
            method = getattr(calc, op_name)
            try:
                result = method(arg1, arg2)
                results[op_name] = result
                print(f"  {op_name}({arg1}, {arg2}) = {result}")
            except Exception as e:
                print(f"  {op_name}({arg1}, {arg2}) failed: {e}")
    
    # Dynamic class creation
    print("\\nDynamic Class Creation:")
    
    def create_data_class(name, fields):
        """Create a data class dynamically."""
        
        def __init__(self, **kwargs):
            for field in fields:
                setattr(self, field, kwargs.get(field))
        
        def __str__(self):
            field_strs = [f"{field}={getattr(self, field)}" for field in fields]
            return f"{name}({', '.join(field_strs)})"
        
        def __repr__(self):
            return self.__str__()
        
        def to_dict(self):
            return {field: getattr(self, field) for field in fields}
        
        # Create class dynamically
        attrs = {
            '__init__': __init__,
            '__str__': __str__,
            '__repr__': __repr__,
            'to_dict': to_dict,
            'fields': fields
        }
        
        return type(name, (), attrs)
    
    # Create different data classes
    Person = create_data_class('Person', ['name', 'age', 'email'])
    Product = create_data_class('Product', ['name', 'price', 'category'])
    
    # Test dynamic classes
    person = Person(name="Alice", age=30, email="alice@example.com")
    product = Product(name="Laptop", price=999.99, category="Electronics")
    
    print(f"Person: {person}")
    print(f"Product: {product}")
    print(f"Person dict: {person.to_dict()}")
    
    # Plugin system using introspection
    print("\\nPlugin System:")
    
    class PluginManager:
        def __init__(self):
            self.plugins = {}
        
        def register_plugin(self, plugin_class):
            """Register a plugin class."""
            plugin_name = plugin_class.__name__.lower().replace('plugin', '')
            self.plugins[plugin_name] = plugin_class
            print(f"  Registered plugin: {plugin_name}")
        
        def get_plugin(self, name):
            """Get a plugin instance."""
            if name in self.plugins:
                return self.plugins[name]()
            else:
                raise ValueError(f"Plugin '{name}' not found")
        
        def list_plugins(self):
            """List all available plugins."""
            return list(self.plugins.keys())
        
        def execute_plugin_method(self, plugin_name, method_name, *args, **kwargs):
            """Execute a specific method on a plugin."""
            plugin = self.get_plugin(plugin_name)
            if hasattr(plugin, method_name):
                method = getattr(plugin, method_name)
                return method(*args, **kwargs)
            else:
                raise AttributeError(f"Plugin '{plugin_name}' has no method '{method_name}'")
    
    # Define some plugins
    class TextPlugin:
        def process(self, text):
            return text.upper()
        
        def reverse(self, text):
            return text[::-1]
    
    class MathPlugin:
        def process(self, numbers):
            return sum(numbers)
        
        def average(self, numbers):
            return sum(numbers) / len(numbers) if numbers else 0
    
    class FilePlugin:
        def process(self, filename):
            return f"Processing file: {filename}"
        
        def get_extension(self, filename):
            return filename.split('.')[-1] if '.' in filename else ''
    
    # Use plugin system
    manager = PluginManager()
    
    # Register plugins
    for plugin_class in [TextPlugin, MathPlugin, FilePlugin]:
        manager.register_plugin(plugin_class)
    
    print(f"Available plugins: {manager.list_plugins()}")
    
    # Test plugins
    plugin_tests = [
        ('text', 'process', 'hello world'),
        ('text', 'reverse', 'python'),
        ('math', 'process', [1, 2, 3, 4, 5]),
        ('math', 'average', [10, 20, 30]),
        ('file', 'process', 'document.pdf'),
        ('file', 'get_extension', 'image.jpg')
    ]
    
    plugin_results = {}
    for plugin_name, method, arg in plugin_tests:
        try:
            result = manager.execute_plugin_method(plugin_name, method, arg)
            plugin_results[f"{plugin_name}_{method}"] = result
            print(f"  {plugin_name}.{method}({arg}) = {result}")
        except Exception as e:
            print(f"  {plugin_name}.{method}({arg}) failed: {e}")
    
    # Dynamic configuration
    print("\\nDynamic Configuration:")
    
    class ConfigurableObject:
        def __init__(self, **config):
            self.config = config
            self._apply_config()
        
        def _apply_config(self):
            """Apply configuration as object attributes."""
            for key, value in self.config.items():
                setattr(self, key, value)
        
        def update_config(self, **new_config):
            """Update configuration."""
            self.config.update(new_config)
            self._apply_config()
        
        def get_config(self):
            """Get current configuration."""
            return self.config.copy()
        
        def has_config(self, key):
            """Check if configuration key exists."""
            return key in self.config
    
    # Test configurable object
    obj = ConfigurableObject(
        name="TestObject",
        debug=True,
        timeout=30,
        retries=3
    )
    
    print(f"Initial config: {obj.get_config()}")
    print(f"Object name: {obj.name}")
    print(f"Debug mode: {obj.debug}")
    
    # Update configuration
    obj.update_config(debug=False, timeout=60, new_feature=True)
    print(f"Updated config: {obj.get_config()}")
    print(f"New feature: {obj.new_feature}")
    
    # Reflection-based serialization
    print("\\nReflection-based Serialization:")
    
    def serialize_object(obj):
        """Serialize object using reflection."""
        if hasattr(obj, '__dict__'):
            # Get instance variables
            data = {}
            for key, value in vars(obj).items():
                if not key.startswith('_'):
                    # Simple types only for this example
                    if isinstance(value, (str, int, float, bool, list, dict)):
                        data[key] = value
                    else:
                        data[key] = str(value)
            return {
                'type': obj.__class__.__name__,
                'data': data
            }
        else:
            return {'type': type(obj).__name__, 'value': obj}
    
    # Test serialization
    serializable_objects = [person, product, obj]
    
    serialized_data = {}
    for i, obj in enumerate(serializable_objects):
        serialized = serialize_object(obj)
        serialized_data[f"object_{i}"] = serialized
        print(f"  Serialized {serialized['type']}: {serialized}")
    
    return {
        "calculator_operations": operations,
        "operation_results": results,
        "dynamic_classes": [Person.__name__, Product.__name__],
        "person_data": person.to_dict(),
        "product_data": product.to_dict(),
        "plugins": manager.list_plugins(),
        "plugin_results": plugin_results,
        "configurable_config": obj.get_config(),
        "serialized_objects": serialized_data
    }

def advanced_inspection():
    """Demonstrate advanced object inspection and analysis."""
    print("\\n=== Advanced Inspection ===")
    
    # inspect module usage
    print("Inspect Module Usage:")
    
    class InspectionTarget:
        """A class for demonstrating inspection capabilities."""
        
        class_attribute = "I'm a class attribute"
        
        def __init__(self, name, value):
            """Initialize the inspection target."""
            self.name = name
            self.value = value
            self._private = "private data"
        
        def instance_method(self, arg):
            """An instance method."""
            return f"Instance method called with {arg}"
        
        @classmethod
        def class_method(cls, arg):
            """A class method."""
            return f"Class method called with {arg}"
        
        @staticmethod
        def static_method(arg):
            """A static method."""
            return f"Static method called with {arg}"
        
        @property
        def computed_property(self):
            """A computed property."""
            return f"Computed: {self.value}"
        
        def _private_method(self):
            """A private method."""
            return "Private method called"
    
    target = InspectionTarget("test", 42)
    
    # Inspect members
    members = inspect.getmembers(target)
    print(f"Total members: {len(members)}")
    
    # Categorize members
    methods = inspect.getmembers(target, inspect.ismethod)
    functions = inspect.getmembers(target, inspect.isfunction)
    properties = []
    
    for name, member in members:
        if isinstance(member, property):
            properties.append((name, member))
    
    print(f"Methods: {[name for name, _ in methods]}")
    print(f"Functions: {[name for name, _ in functions]}")
    
    # Inspect specific methods
    print("\\nMethod Inspection:")
    
    method = target.instance_method
    
    # Get method signature
    sig = inspect.signature(method)
    print(f"Method signature: {sig}")
    print(f"Parameters: {list(sig.parameters.keys())}")
    
    # Get source (if available)
    try:
        source = inspect.getsource(target.instance_method)
        print(f"Method source available: {len(source)} characters")
    except:
        print("Source not available")
    
    # Get docstring
    doc = inspect.getdoc(target.instance_method)
    print(f"Docstring: '{doc}'")
    
    # Class inspection
    print("\\nClass Inspection:")
    
    # Get class hierarchy
    mro = inspect.getmro(InspectionTarget)
    print(f"Method Resolution Order: {[cls.__name__ for cls in mro]}")
    
    # Get class members by type
    class_members = inspect.getmembers(InspectionTarget)
    
    categorized = {
        'methods': [],
        'functions': [],
        'properties': [],
        'data': []
    }
    
    for name, member in class_members:
        if name.startswith('__'):
            continue
        elif inspect.ismethod(member) or inspect.isfunction(member):
            if hasattr(member, '__self__'):
                categorized['methods'].append(name)
            else:
                categorized['functions'].append(name)
        elif isinstance(member, property):
            categorized['properties'].append(name)
        else:
            categorized['data'].append(name)
    
    for category, items in categorized.items():
        print(f"  {category.title()}: {items}")
    
    # Function signature analysis
    print("\\nFunction Signature Analysis:")
    
    def complex_function(pos_arg, pos_default=10, *args, kw_only=None, **kwargs):
        """A function with complex signature for inspection."""
        return f"Called with: pos_arg={pos_arg}, pos_default={pos_default}, args={args}, kw_only={kw_only}, kwargs={kwargs}"
    
    sig = inspect.signature(complex_function)
    
    for name, param in sig.parameters.items():
        print(f"  Parameter: {name}")
        print(f"    Kind: {param.kind}")
        print(f"    Default: {param.default if param.default != param.empty else 'No default'}")
        print(f"    Annotation: {param.annotation if param.annotation != param.empty else 'No annotation'}")
    
    # Type inspection
    print("\\nType Inspection:")
    
    objects_to_inspect = [
        ("integer", 42),
        ("float", 3.14),
        ("string", "hello"),
        ("list", [1, 2, 3]),
        ("dict", {"key": "value"}),
        ("function", lambda x: x),
        ("method", target.instance_method),
        ("class", InspectionTarget),
        ("instance", target)
    ]
    
    for name, obj in objects_to_inspect:
        obj_type = type(obj)
        print(f"  {name}:")
        print(f"    Type: {obj_type}")
        print(f"    MRO: {[cls.__name__ for cls in obj_type.__mro__]}")
        print(f"    Is callable: {callable(obj)}")
        print(f"    Has __dict__: {hasattr(obj, '__dict__')}")
    
    # Module inspection
    print("\\nModule Inspection:")
    
    import json
    import math
    
    modules = [json, math]
    
    for module in modules:
        print(f"  Module: {module.__name__}")
        
        # Get module members
        module_members = inspect.getmembers(module)
        
        # Categorize
        functions = [name for name, obj in module_members 
                    if inspect.isfunction(obj) and not name.startswith('_')]
        classes = [name for name, obj in module_members 
                  if inspect.isclass(obj) and not name.startswith('_')]
        constants = [name for name, obj in module_members 
                    if not callable(obj) and not name.startswith('_') and name.isupper()]
        
        print(f"    Functions: {len(functions)} (examples: {functions[:3]})")
        print(f"    Classes: {len(classes)} (examples: {classes[:3]})")
        print(f"    Constants: {len(constants)} (examples: {constants[:3]})")
    
    # Performance inspection
    print("\\nPerformance Inspection:")
    
    def profile_function_calls(func, *args, **kwargs):
        """Profile function calls and inspect the function."""
        import time
        
        # Get function info
        sig = inspect.signature(func)
        doc = inspect.getdoc(func) or "No documentation"
        
        # Time the execution
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        
        return {
            'function_name': func.__name__,
            'signature': str(sig),
            'docstring': doc[:50] + "..." if len(doc) > 50 else doc,
            'execution_time': execution_time,
            'result_type': type(result).__name__,
            'result': result
        }
    
    # Test function profiling
    test_functions = [
        (sum, [1, 2, 3, 4, 5]),
        (sorted, [5, 2, 8, 1, 9]),
        (len, "hello world"),
        (max, [10, 5, 8, 3, 1])
    ]
    
    profiles = {}
    for func, args in test_functions:
        profile = profile_function_calls(func, *args)
        profiles[func.__name__] = profile
        print(f"  {profile['function_name']}: {profile['execution_time']:.6f}s -> {profile['result']}")
    
    # Custom inspection framework
    print("\\nCustom Inspection Framework:")
    
    class ObjectAnalyzer:
        @staticmethod
        def analyze(obj):
            """Comprehensive object analysis."""
            analysis = {
                'basic_info': {
                    'type': type(obj).__name__,
                    'id': id(obj),
                    'size': sys.getsizeof(obj),
                    'callable': callable(obj)
                },
                'attributes': {
                    'total': len(dir(obj)),
                    'public': len([attr for attr in dir(obj) if not attr.startswith('_')]),
                    'private': len([attr for attr in dir(obj) if attr.startswith('_') and not attr.startswith('__')]),
                    'dunder': len([attr for attr in dir(obj) if attr.startswith('__')])
                },
                'methods': [],
                'properties': [],
                'data_attributes': []
            }
            
            # Analyze each attribute
            for attr_name in dir(obj):
                if attr_name.startswith('__'):
                    continue
                
                try:
                    attr_value = getattr(obj, attr_name)
                    if callable(attr_value):
                        analysis['methods'].append(attr_name)
                    elif isinstance(attr_value, property):
                        analysis['properties'].append(attr_name)
                    else:
                        analysis['data_attributes'].append(attr_name)
                except:
                    pass
            
            return analysis
    
    # Analyze different objects
    analyzer = ObjectAnalyzer()
    
    analysis_targets = [target, InspectionTarget, [1, 2, 3], {"key": "value"}]
    
    analyses = {}
    for obj in analysis_targets:
        analysis = analyzer.analyze(obj)
        obj_name = getattr(obj, '__name__', type(obj).__name__)
        analyses[obj_name] = analysis
        
        print(f"  Analysis of {obj_name}:")
        print(f"    Type: {analysis['basic_info']['type']}")
        print(f"    Size: {analysis['basic_info']['size']} bytes")
        print(f"    Methods: {len(analysis['methods'])}")
        print(f"    Properties: {len(analysis['properties'])}")
        print(f"    Data attributes: {len(analysis['data_attributes'])}")
    
    return {
        "target_members": len(members),
        "method_count": len(methods),
        "class_mro": [cls.__name__ for cls in mro],
        "categorized_members": categorized,
        "signature_params": list(sig.parameters.keys()),
        "type_inspection": [(name, type(obj).__name__) for name, obj in objects_to_inspect],
        "module_stats": {mod.__name__: len([name for name, obj in inspect.getmembers(mod) 
                                           if not name.startswith('_')]) for mod in modules},
        "function_profiles": profiles,
        "object_analyses": analyses
    }

# Main execution
if __name__ == "__main__":
    print("=== Built-in Attribute and Introspection Functions ===")
    
    print("\\n1. Attribute Operations:")
    attr_results = attribute_operations()
    
    print("\\n2. Introspection Basics:")
    introspection_results = introspection_basics()
    
    print("\\n3. Namespace Exploration:")
    namespace_results = namespace_exploration()
    
    print("\\n4. Dynamic Programming:")
    dynamic_results = dynamic_programming()
    
    print("\\n5. Advanced Inspection:")
    inspection_results = advanced_inspection()
    
    print("\\n" + "="*60)
    print("=== ATTRIBUTE AND INTROSPECTION FUNCTIONS COMPLETE ===")
    print("✓ Dynamic attribute manipulation")
    print("✓ Object introspection and analysis")
    print("✓ Namespace exploration and modification")
    print("✓ Dynamic programming patterns")
    print("✓ Advanced inspection techniques")
    print("✓ Plugin systems and configuration")
    print("✓ Performance profiling and analysis")
```

## Hints

- Use `hasattr()` to safely check for attributes before accessing them
- `getattr()` with default values prevents AttributeError exceptions
- `dir()` shows available attributes, `vars()` shows instance variables only
- `globals()` and `locals()` return dictionaries you can modify
- The `inspect` module provides advanced introspection capabilities

## Test Cases

Your functions should handle:

1. Safe attribute access with default values and error handling
2. Comprehensive object introspection including methods and properties
3. Namespace manipulation and variable lookup in different scopes
4. Dynamic class creation and plugin system implementation
5. Advanced inspection with signature analysis and performance profiling

## Bonus Challenge

Build a dynamic ORM system, create a comprehensive debugging toolkit, and implement a reflection-based serialization framework using introspection functions!
