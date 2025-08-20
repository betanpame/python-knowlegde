# Advanced Module Architectures - Practice 16

**Difficulty:** ⭐⭐⭐ (Medium)

## Description

Design and implement sophisticated module architectures for complex applications.

## Objectives

- Implement plugin architecture systems
- Create modular application frameworks
- Design extensible module hierarchies
- Build configuration-driven module systems

## Your Tasks

1. **plugin_discovery_system()** - Automatically discover and load plugins
2. **modular_application_framework()** - Build extensible app architecture
3. **dependency_injection_modules()** - Implement DI for loose coupling
4. **event_driven_module_system()** - Create pub/sub module communication
5. **hot_reload_architecture()** - Enable runtime module replacement
6. **module_lifecycle_management()** - Handle module initialization/cleanup
7. **cross_module_communication()** - Design inter-module messaging
8. **configuration_driven_loading()** - Load modules based on config files

## Example

```python
import importlib
import inspect
from typing import Dict, List, Type, Any
from abc import ABC, abstractmethod

class PluginInterface(ABC):
    """Base interface for all plugins."""
    
    @abstractmethod
    def initialize(self) -> None:
        """Initialize the plugin."""
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """Return plugin name."""
        pass
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """Execute plugin functionality."""
        pass

class PluginManager:
    """Manages plugin discovery, loading, and lifecycle."""
    
    def __init__(self):
        self.plugins: Dict[str, PluginInterface] = {}
        self.plugin_configs: Dict[str, Dict] = {}
    
    def discover_plugins(self, plugin_dir: str) -> List[str]:
        """Discover available plugins in directory."""
        import os
        import pkgutil
        
        discovered = []
        for importer, modname, ispkg in pkgutil.iter_modules([plugin_dir]):
            if not ispkg:  # Only load modules, not packages
                discovered.append(modname)
        return discovered
    
    def load_plugin(self, plugin_name: str, plugin_dir: str = "plugins") -> bool:
        """Load a specific plugin."""
        try:
            # Import the plugin module
            spec = importlib.util.spec_from_file_location(
                plugin_name, 
                f"{plugin_dir}/{plugin_name}.py"
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Find plugin class that implements PluginInterface
            for name, obj in inspect.getmembers(module):
                if (inspect.isclass(obj) and 
                    issubclass(obj, PluginInterface) and 
                    obj != PluginInterface):
                    
                    plugin_instance = obj()
                    plugin_instance.initialize()
                    self.plugins[plugin_instance.get_name()] = plugin_instance
                    return True
            
            return False
        except Exception as e:
            print(f"Failed to load plugin {plugin_name}: {e}")
            return False
    
    def execute_plugin(self, plugin_name: str, *args, **kwargs) -> Any:
        """Execute a loaded plugin."""
        if plugin_name in self.plugins:
            return self.plugins[plugin_name].execute(*args, **kwargs)
        else:
            raise ValueError(f"Plugin {plugin_name} not loaded")
    
    def unload_plugin(self, plugin_name: str) -> bool:
        """Unload a plugin."""
        if plugin_name in self.plugins:
            # Call cleanup if available
            if hasattr(self.plugins[plugin_name], 'cleanup'):
                self.plugins[plugin_name].cleanup()
            del self.plugins[plugin_name]
            return True
        return False

class ModuleRegistry:
    """Central registry for module dependencies and communication."""
    
    def __init__(self):
        self.modules: Dict[str, Any] = {}
        self.dependencies: Dict[str, List[str]] = {}
        self.event_handlers: Dict[str, List[callable]] = {}
    
    def register_module(self, name: str, module: Any, deps: List[str] = None):
        """Register a module with optional dependencies."""
        self.modules[name] = module
        self.dependencies[name] = deps or []
    
    def get_module(self, name: str) -> Any:
        """Get a registered module."""
        return self.modules.get(name)
    
    def emit_event(self, event_name: str, data: Any = None):
        """Emit an event to all registered handlers."""
        if event_name in self.event_handlers:
            for handler in self.event_handlers[event_name]:
                handler(data)
    
    def subscribe_to_event(self, event_name: str, handler: callable):
        """Subscribe to an event."""
        if event_name not in self.event_handlers:
            self.event_handlers[event_name] = []
        self.event_handlers[event_name].append(handler)
```

## Hints

- Use abstract base classes for plugin interfaces
- Implement proper error handling for dynamic loading
- Consider using dependency injection containers
- Design clear module communication protocols

## Practice Cases

Your architecture should support:
- Plugin discovery and dynamic loading
- Module dependency resolution
- Event-driven communication
- Hot reloading of modules
- Graceful error handling

## Bonus Challenge

Create a complete microframework that can load plugins, manage dependencies, and provide inter-module communication with a configuration file!

Remember: Good architecture makes complex systems manageable and extensible!