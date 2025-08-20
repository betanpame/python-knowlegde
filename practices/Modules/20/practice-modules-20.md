# Advanced Module Compiler and Runtime System - Practice 20

**Difficulty:** ⭐⭐⭐⭐⭐ (Hard)

## Description

Create a sophisticated module compiler and runtime system that can optimize, transform, and execute Python modules with advanced features like JIT compilation, custom bytecode generation, and runtime optimization.

## Objectives

- Build a complete module compilation pipeline
- Implement JIT compilation for hot code paths
- Create custom bytecode optimization passes
- Design adaptive runtime optimization systems

## Your Tasks

1. **module_ast_optimizer()** - Advanced AST optimization passes
2. **custom_bytecode_compiler()** - Generate optimized bytecode
3. **jit_compilation_engine()** - Just-in-time compilation for performance
4. **runtime_profiling_system()** - Profile and optimize at runtime
5. **adaptive_optimization_framework()** - Self-optimizing module system
6. **cross_module_inlining()** - Optimize across module boundaries
7. **memory_layout_optimizer()** - Optimize memory usage patterns
8. **dynamic_recompilation_system()** - Recompile modules based on usage

## Example

```python
import ast
import dis
import sys
import types
import marshal
import threading
import time
from typing import Dict, List, Any, Optional, Callable, Set
from dataclasses import dataclass, field
from collections import defaultdict, Counter
import cProfile
import pstats
from contextlib import contextmanager

@dataclass
class OptimizationProfile:
    """Profile data for module optimization."""
    function_call_counts: Dict[str, int] = field(default_factory=Counter)
    execution_times: Dict[str, List[float]] = field(default_factory=lambda: defaultdict(list))
    memory_usage: Dict[str, List[int]] = field(default_factory=lambda: defaultdict(list))
    hot_paths: Set[str] = field(default_factory=set)
    cold_paths: Set[str] = field(default_factory=set)
    optimization_candidates: List[str] = field(default_factory=list)

class AdvancedASTOptimizer(ast.NodeTransformer):
    """Advanced AST optimization passes."""
    
    def __init__(self, profile: OptimizationProfile = None):
        self.profile = profile or OptimizationProfile()
        self.optimizations_applied = []
        self.constant_table = {}
        self.inline_candidates = set()
    
    def optimize(self, tree: ast.AST) -> ast.AST:
        """Apply all optimization passes."""
        
        # Pass 1: Constant folding and propagation
        tree = self.visit(tree)
        self.optimizations_applied.append("constant_folding")
        
        # Pass 2: Dead code elimination
        tree = self._eliminate_dead_code(tree)
        self.optimizations_applied.append("dead_code_elimination")
        
        # Pass 3: Loop optimization
        tree = self._optimize_loops(tree)
        self.optimizations_applied.append("loop_optimization")
        
        # Pass 4: Function inlining for hot paths
        tree = self._inline_hot_functions(tree)
        self.optimizations_applied.append("function_inlining")
        
        # Pass 5: Strength reduction
        tree = self._strength_reduction(tree)
        self.optimizations_applied.append("strength_reduction")
        
        return tree
    
    def visit_BinOp(self, node):
        """Optimize binary operations."""
        self.generic_visit(node)
        
        # Constant folding for arithmetic operations
        if isinstance(node.left, ast.Constant) and isinstance(node.right, ast.Constant):
            try:
                if isinstance(node.op, ast.Add):
                    result = node.left.value + node.right.value
                elif isinstance(node.op, ast.Sub):
                    result = node.left.value - node.right.value
                elif isinstance(node.op, ast.Mult):
                    result = node.left.value * node.right.value
                elif isinstance(node.op, ast.Div):
                    result = node.left.value / node.right.value
                elif isinstance(node.op, ast.Pow):
                    result = node.left.value ** node.right.value
                else:
                    return node
                
                return ast.Constant(value=result)
            except:
                return node
        
        # Strength reduction: x * 2 -> x + x
        if (isinstance(node.op, ast.Mult) and 
            isinstance(node.right, ast.Constant) and 
            node.right.value == 2):
            return ast.BinOp(
                left=node.left,
                op=ast.Add(),
                right=node.left
            )
        
        return node
    
    def visit_For(self, node):
        """Optimize for loops."""
        self.generic_visit(node)
        
        # Convert range-based loops to while loops for better control
        if (isinstance(node.iter, ast.Call) and 
            isinstance(node.iter.func, ast.Name) and 
            node.iter.func.id == 'range'):
            
            # Extract range parameters
            args = node.iter.args
            if len(args) == 1:  # range(n)
                start, stop, step = ast.Constant(0), args[0], ast.Constant(1)
            elif len(args) == 2:  # range(start, stop)
                start, stop, step = args[0], args[1], ast.Constant(1)
            elif len(args) == 3:  # range(start, stop, step)
                start, stop, step = args[0], args[1], args[2]
            else:
                return node
            
            # Create optimized while loop
            iter_var = node.target.id
            init_assign = ast.Assign(
                targets=[ast.Name(id=iter_var, ctx=ast.Store())],
                value=start
            )
            
            condition = ast.Compare(
                left=ast.Name(id=iter_var, ctx=ast.Load()),
                ops=[ast.Lt()],
                comparators=[stop]
            )
            
            increment = ast.AugAssign(
                target=ast.Name(id=iter_var, ctx=ast.Store()),
                op=ast.Add(),
                value=step
            )
            
            while_body = node.body + [increment]
            
            return [
                init_assign,
                ast.While(
                    test=condition,
                    body=while_body,
                    orelse=node.orelse
                )
            ]
        
        return node
    
    def _eliminate_dead_code(self, tree: ast.AST) -> ast.AST:
        """Remove unreachable code."""
        class DeadCodeEliminator(ast.NodeTransformer):
            def visit_If(self, node):
                self.generic_visit(node)
                
                # Remove if False: blocks
                if isinstance(node.test, ast.Constant) and not node.test.value:
                    return node.orelse
                
                # Remove else: blocks after if True:
                if isinstance(node.test, ast.Constant) and node.test.value:
                    return node.body
                
                return node
        
        return DeadCodeEliminator().visit(tree)
    
    def _optimize_loops(self, tree: ast.AST) -> ast.AST:
        """Apply loop optimizations."""
        class LoopOptimizer(ast.NodeTransformer):
            def visit_For(self, node):
                self.generic_visit(node)
                
                # Loop unrolling for small constant ranges
                if (isinstance(node.iter, ast.Call) and 
                    isinstance(node.iter.func, ast.Name) and 
                    node.iter.func.id == 'range' and
                    len(node.iter.args) == 1 and
                    isinstance(node.iter.args[0], ast.Constant) and
                    node.iter.args[0].value <= 4):  # Only unroll small loops
                    
                    unrolled_body = []
                    for i in range(node.iter.args[0].value):
                        # Replace loop variable with constant
                        replacer = ConstantReplacer(node.target.id, i)
                        for stmt in node.body:
                            unrolled_body.append(replacer.visit(stmt))
                    
                    return unrolled_body
                
                return node
        
        return LoopOptimizer().visit(tree)
    
    def _inline_hot_functions(self, tree: ast.AST) -> ast.AST:
        """Inline frequently called small functions."""
        if not self.profile.hot_paths:
            return tree
        
        # This is a simplified implementation
        # Real inlining would need sophisticated analysis
        return tree
    
    def _strength_reduction(self, tree: ast.AST) -> ast.AST:
        """Apply strength reduction optimizations."""
        class StrengthReducer(ast.NodeTransformer):
            def visit_BinOp(self, node):
                self.generic_visit(node)
                
                # x ** 2 -> x * x
                if (isinstance(node.op, ast.Pow) and 
                    isinstance(node.right, ast.Constant) and 
                    node.right.value == 2):
                    return ast.BinOp(
                        left=node.left,
                        op=ast.Mult(),
                        right=node.left
                    )
                
                # x * 0 -> 0
                if (isinstance(node.op, ast.Mult) and
                    isinstance(node.right, ast.Constant) and
                    node.right.value == 0):
                    return ast.Constant(value=0)
                
                return node
        
        return StrengthReducer().visit(tree)

class ConstantReplacer(ast.NodeTransformer):
    """Replace variable references with constants."""
    
    def __init__(self, var_name: str, value: Any):
        self.var_name = var_name
        self.value = value
    
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load) and node.id == self.var_name:
            return ast.Constant(value=self.value)
        return node

class JITCompiler:
    """Just-in-time compiler for hot code paths."""
    
    def __init__(self):
        self.compiled_functions: Dict[str, Callable] = {}
        self.compilation_threshold = 100
        self.call_counts: Counter = Counter()
        self.native_code_cache: Dict[str, bytes] = {}
    
    def maybe_compile(self, func: Callable) -> Callable:
        """Compile function if it's called frequently enough."""
        func_id = f"{func.__module__}.{func.__qualname__}"
        self.call_counts[func_id] += 1
        
        if (self.call_counts[func_id] >= self.compilation_threshold and 
            func_id not in self.compiled_functions):
            
            # Simulate JIT compilation
            compiled_func = self._compile_function(func)
            self.compiled_functions[func_id] = compiled_func
            return compiled_func
        
        return self.compiled_functions.get(func_id, func)
    
    def _compile_function(self, func: Callable) -> Callable:
        """Compile function to optimized bytecode."""
        import inspect
        
        # Get function source and AST
        source = inspect.getsource(func)
        tree = ast.parse(source)
        
        # Optimize AST
        optimizer = AdvancedASTOptimizer()
        optimized_tree = optimizer.optimize(tree)
        
        # Compile to bytecode
        code = compile(optimized_tree, f"<jit_{func.__name__}>", "exec")
        
        # Create optimized function
        namespace = func.__globals__.copy()
        exec(code, namespace)
        
        # Return the compiled function
        compiled_func = namespace[func.__name__]
        compiled_func.__jit_compiled__ = True
        
        return compiled_func

class RuntimeProfiler:
    """Profile module execution at runtime."""
    
    def __init__(self):
        self.profiles: Dict[str, OptimizationProfile] = {}
        self.active_profiling = threading.local()
        self.profiling_enabled = True
    
    @contextmanager
    def profile_module(self, module_name: str):
        """Context manager for profiling module execution."""
        if not self.profiling_enabled:
            yield
            return
        
        if module_name not in self.profiles:
            self.profiles[module_name] = OptimizationProfile()
        
        profile = self.profiles[module_name]
        
        # Start profiling
        profiler = cProfile.Profile()
        start_time = time.time()
        profiler.enable()
        
        try:
            yield profile
        finally:
            profiler.disable()
            end_time = time.time()
            
            # Analyze profile data
            stats = pstats.Stats(profiler)
            self._update_profile(profile, stats, end_time - start_time)
    
    def _update_profile(self, profile: OptimizationProfile, stats: pstats.Stats, total_time: float):
        """Update optimization profile with new data."""
        
        # Extract function call counts and timing
        for func_info, (call_count, _, cumulative_time, _, _) in stats.stats.items():
            func_name = f"{func_info[0]}:{func_info[2]}"
            profile.function_call_counts[func_name] += call_count
            profile.execution_times[func_name].append(cumulative_time)
            
            # Identify hot and cold paths
            if cumulative_time > total_time * 0.1:  # Hot if >10% of total time
                profile.hot_paths.add(func_name)
            elif cumulative_time < total_time * 0.001:  # Cold if <0.1% of total time
                profile.cold_paths.add(func_name)

class AdaptiveModuleSystem:
    """Self-optimizing module system."""
    
    def __init__(self):
        self.profiler = RuntimeProfiler()
        self.jit_compiler = JITCompiler()
        self.optimization_scheduler = threading.Thread(target=self._optimization_loop, daemon=True)
        self.running = True
        self.recompilation_queue = []
        
        # Start optimization scheduler
        self.optimization_scheduler.start()
    
    def load_module(self, module_name: str) -> types.ModuleType:
        """Load and optimize module adaptively."""
        
        # Load module normally first
        module = __import__(module_name)
        
        # Wrap module functions for profiling and JIT compilation
        self._instrument_module(module)
        
        return module
    
    def _instrument_module(self, module: types.ModuleType):
        """Instrument module for profiling and optimization."""
        
        for name, obj in vars(module).items():
            if callable(obj) and not name.startswith('_'):
                # Create instrumented wrapper
                def create_wrapper(func, func_name):
                    def wrapper(*args, **kwargs):
                        with self.profiler.profile_module(module.__name__):
                            # Check if function should be JIT compiled
                            optimized_func = self.jit_compiler.maybe_compile(func)
                            return optimized_func(*args, **kwargs)
                    
                    wrapper.__wrapped__ = func
                    wrapper.__name__ = func_name
                    return wrapper
                
                setattr(module, name, create_wrapper(obj, name))
    
    def _optimization_loop(self):
        """Background optimization loop."""
        while self.running:
            time.sleep(5)  # Check every 5 seconds
            
            # Analyze profiles and schedule recompilations
            for module_name, profile in self.profiler.profiles.items():
                if self._should_reoptimize(profile):
                    self.recompilation_queue.append(module_name)
            
            # Process recompilation queue
            while self.recompilation_queue:
                module_name = self.recompilation_queue.pop(0)
                self._reoptimize_module(module_name)
    
    def _should_reoptimize(self, profile: OptimizationProfile) -> bool:
        """Determine if module should be reoptimized."""
        
        # Check if hot paths have changed significantly
        total_calls = sum(profile.function_call_counts.values())
        if total_calls > 1000:  # Only after sufficient data
            
            # Find functions that became hot
            for func_name, call_count in profile.function_call_counts.items():
                if (call_count / total_calls > 0.1 and  # >10% of calls
                    func_name not in profile.hot_paths):
                    return True
        
        return False
    
    def _reoptimize_module(self, module_name: str):
        """Reoptimize module based on runtime profile."""
        print(f"Reoptimizing module {module_name} based on runtime profile")
        
        # In a real implementation, this would:
        # 1. Reload module source
        # 2. Apply profile-guided optimizations
        # 3. Recompile with new optimizations
        # 4. Hot-swap the module
    
    def shutdown(self):
        """Shutdown the adaptive system."""
        self.running = False
        self.optimization_scheduler.join()

class ModuleCompilerFramework:
    """Complete framework for advanced module compilation."""
    
    def __init__(self):
        self.ast_optimizer = AdvancedASTOptimizer()
        self.jit_compiler = JITCompiler()
        self.adaptive_system = AdaptiveModuleSystem()
        self.compiled_modules: Dict[str, types.ModuleType] = {}
    
    def compile_module(self, 
                      source_code: str, 
                      module_name: str,
                      optimization_level: int = 2) -> types.ModuleType:
        """Compile module with specified optimization level."""
        
        # Parse source to AST
        tree = ast.parse(source_code, module_name)
        
        # Apply optimizations based on level
        if optimization_level >= 1:
            tree = self.ast_optimizer.optimize(tree)
        
        # Compile to bytecode
        code = compile(tree, module_name, "exec")
        
        # Create module and execute
        module = types.ModuleType(module_name)
        module.__file__ = f"<compiled_{module_name}>"
        
        exec(code, module.__dict__)
        
        # Enable adaptive optimization if level >= 2
        if optimization_level >= 2:
            self.adaptive_system._instrument_module(module)
        
        self.compiled_modules[module_name] = module
        return module
    
    def get_compilation_stats(self) -> Dict[str, Any]:
        """Get detailed compilation and optimization statistics."""
        return {
            "total_modules_compiled": len(self.compiled_modules),
            "jit_compiled_functions": len(self.jit_compiler.compiled_functions),
            "optimization_profiles": len(self.adaptive_system.profiler.profiles),
            "ast_optimizations_applied": self.ast_optimizer.optimizations_applied
        }
```

## Hints

- Study Python's bytecode format and compilation process
- Implement proper AST analysis for optimization opportunities
- Use profiling data to guide optimization decisions
- Consider memory management and garbage collection implications

## Practice Cases

Your compiler system should handle:
- Complex AST transformations and optimizations
- Just-in-time compilation of hot code paths
- Runtime profiling and adaptive optimization
- Memory-efficient bytecode generation
- Cross-module optimization scenarios

## Bonus Challenge

Create a complete Python-to-native compiler that can generate machine code with LLVM integration and achieve performance competitive with compiled languages!

Remember: Compiler construction requires deep understanding of language semantics, runtime systems, and performance optimization techniques!