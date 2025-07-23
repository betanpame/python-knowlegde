# Dynamic Module Loading - Test 11

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Learn advanced techniques for loading modules dynamically at runtime.

## Objectives
- Master importlib for dynamic imports
- Implement conditional module loading
- Handle module loading errors gracefully
- Create flexible, runtime-configurable imports

## Your Tasks

1. **dynamic_import_by_name()** - Load modules by string names
2. **conditional_feature_loading()** - Load optional features
3. **plugin_system_basics()** - Create a simple plugin loader
4. **module_factory_pattern()** - Build modules based on conditions
5. **safe_import_wrapper()** - Handle import failures gracefully
6. **reload_modified_modules()** - Detect and reload changed modules
7. **lazy_loading_system()** - Implement deferred module loading
8. **runtime_dependency_resolver()** - Resolve dependencies dynamically

## Example
```python
import importlib

def load_plugin(plugin_name):
    try:
        module = importlib.import_module(f"plugins.{plugin_name}")
        return module.get_plugin_instance()
    except ImportError:
        return None
```

## Hints
- Use importlib.import_module() for dynamic imports
- Consider using try/except for optional dependencies
- sys.modules can help track loaded modules
- importlib.reload() for module reloading

## Test Cases
Your functions should handle:
- Valid and invalid module names
- Missing optional dependencies
- Module reloading scenarios
- Plugin discovery and loading

## Bonus Challenge
Create a configuration-driven module loader that can load different implementations based on settings!

Remember: Dynamic imports add flexibility but require careful error handling!
