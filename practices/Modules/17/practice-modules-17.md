# Module Metaprogramming and Code Generation - Practice 17

**Difficulty:** ⭐⭐⭐ (Medium)

## Description

Master advanced metaprogramming techniques for dynamic module creation and code generation.

## Objectives

- Generate modules programmatically
- Create dynamic module factories
- Implement module transformation systems
- Build code generation pipelines

## Your Tasks

1. **dynamic_module_creation()** - Create modules from scratch at runtime
2. **code_template_system()** - Generate modules from templates
3. **module_transformation_pipeline()** - Transform existing modules
4. **ast_based_code_generation()** - Use AST for sophisticated code gen
5. **module_composition_system()** - Combine modules programmatically
6. **metaclass_driven_modules()** - Use metaclasses for module behavior
7. **bytecode_module_generation()** - Generate modules at bytecode level
8. **adaptive_module_interfaces()** - Create self-modifying module APIs

## Example

```python
import ast
import types
import importlib.util
from typing import Any, Dict, List

class ModuleFactory:
    """Factory for creating modules dynamically."""
    
    def create_module_from_template(self, name: str, template: str, **kwargs) -> types.ModuleType:
        """Create a module from a code template."""
        # Replace template variables
        code = template.format(**kwargs)
        
        # Create module spec
        spec = importlib.util.spec_from_loader(name, loader=None)
        module = importlib.util.module_from_spec(spec)
        
        # Execute code in module namespace
        exec(code, module.__dict__)
        
        return module
    
    def create_data_class_module(self, class_name: str, fields: Dict[str, type]) -> types.ModuleType:
        """Generate a module containing a data class."""
        # Build class definition using AST
        field_assignments = []
        init_params = []
        
        for field_name, field_type in fields.items():
            # Add to __init__ parameters
            init_params.append(ast.arg(arg=field_name, annotation=ast.Name(id=field_type.__name__, ctx=ast.Load())))
            # Add assignment in __init__
            field_assignments.append(
                ast.Assign(
                    targets=[ast.Attribute(value=ast.Name(id='self', ctx=ast.Load()), attr=field_name, ctx=ast.Store())],
                    value=ast.Name(id=field_name, ctx=ast.Load())
                )
            )
        
        # Create __init__ method
        init_method = ast.FunctionDef(
            name='__init__',
            args=ast.arguments(
                posonlyargs=[],
                args=[ast.arg(arg='self')] + init_params,
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[]
            ),
            body=field_assignments,
            decorator_list=[],
            returns=None
        )
        
        # Create class definition
        class_def = ast.ClassDef(
            name=class_name,
            bases=[],
            keywords=[],
            decorator_list=[],
            body=[init_method]
        )
        
        # Create module
        module_ast = ast.Module(body=[class_def], type_ignores=[])
        
        # Compile and execute
        code = compile(module_ast, f"<generated_{class_name.lower()}>", "exec")
        module = types.ModuleType(f"{class_name.lower()}_module")
        exec(code, module.__dict__)
        
        return module
    
    def create_api_wrapper_module(self, base_url: str, endpoints: List[Dict[str, str]]) -> types.ModuleType:
        """Generate a module that wraps a REST API."""
        module_code = f'''
import requests
from typing import Dict, Any

BASE_URL = "{base_url}"

class APIClient:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({{"Authorization": f"Bearer {{api_key}}"}})
'''
        
        # Generate methods for each endpoint
        for endpoint in endpoints:
            method_name = endpoint['name']
            http_method = endpoint.get('method', 'GET').upper()
            path = endpoint['path']
            
            method_code = f'''
    def {method_name}(self, **kwargs) -> Dict[str, Any]:
        """Auto-generated method for {path}"""
        url = BASE_URL + "{path}"
        response = self.session.{http_method.lower()}(url, **kwargs)
        response.raise_for_status()
        return response.json()
'''
            module_code += method_code
        
        # Create the module
        module = types.ModuleType("api_client")
        exec(module_code, module.__dict__)
        return module

class ModuleTransformer:
    """Transform existing modules using AST manipulation."""
    
    def add_logging_to_functions(self, module: types.ModuleType) -> types.ModuleType:
        """Add logging statements to all functions in a module."""
        import inspect
        
        # Get module source
        source = inspect.getsource(module)
        tree = ast.parse(source)
        
        # Transform the AST
        transformer = LoggingTransformer()
        new_tree = transformer.visit(tree)
        
        # Compile and create new module
        code = compile(new_tree, module.__name__, "exec")
        new_module = types.ModuleType(f"{module.__name__}_logged")
        exec(code, new_module.__dict__)
        
        return new_module

class LoggingTransformer(ast.NodeTransformer):
    """AST transformer that adds logging to functions."""
    
    def visit_FunctionDef(self, node):
        # Add logging statement at the beginning of function
        log_stmt = ast.Expr(
            value=ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id='logging', ctx=ast.Load()),
                    attr='info',
                    ctx=ast.Load()
                ),
                args=[ast.Constant(value=f"Calling function {node.name}")],
                keywords=[]
            )
        )
        
        # Insert logging import if not present
        if not any(isinstance(stmt, ast.Import) and 
                  any(alias.name == 'logging' for alias in stmt.names) 
                  for stmt in ast.walk(node)):
            node.body.insert(0, log_stmt)
        
        return self.generic_visit(node)
```

## Hints

- Use the ast module for sophisticated code generation
- types.ModuleType creates new module objects
- exec() can execute code in a specific namespace
- Consider using importlib.util for proper module creation

## Practice Cases

Your metaprogramming should handle:
- Template-based module generation
- AST manipulation and transformation
- Dynamic class and function creation
- Module composition and inheritance

## Bonus Challenge

Create a domain-specific language (DSL) that compiles to Python modules with custom syntax and semantics!

Remember: Metaprogramming is powerful but should be used judiciously for maintainable code!