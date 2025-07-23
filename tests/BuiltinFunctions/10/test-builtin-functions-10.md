# Memory and Performance Functions - Test 10

**Difficulty:** ⭐⭐⭐⭐ (Medium-Hard)

## Description

Master Python's built-in functions for memory management and performance optimization including `id()`, `hash()`, `sys.getsizeof()`, `weakref`, `gc`, and advanced memory profiling techniques.

## Objectives

- Understand object identity and memory allocation with `id()`
- Use `hash()` for efficient data structures and caching
- Monitor memory usage with `sys.getsizeof()` and profiling tools
- Implement weak references to avoid memory leaks
- Optimize performance with caching and memory-efficient patterns

## Your Tasks

1. **object_identity()** - Work with object identity and memory addresses
2. **hashing_mechanisms()** - Master hash functions and hash-based collections
3. **memory_profiling()** - Monitor and optimize memory usage
4. **weak_references()** - Implement weak references for memory management
5. **performance_optimization()** - Apply caching and optimization patterns

## Example

```python
import sys
import gc
import weakref
import functools
import time
import tracemalloc
from typing import Any, Dict, List, Optional, Callable
import hashlib
import pickle

def object_identity():
    """Demonstrate object identity and memory allocation patterns."""
    print("=== Object Identity ===")
    
    # Basic identity checking
    print("Basic Identity Checking:")
    
    # Small integers are cached
    a = 5
    b = 5
    c = 10
    d = 10
    
    print(f"Small integers:")
    print(f"  a = 5, b = 5: a is b = {a is b} (id(a)={id(a)}, id(b)={id(b)})")
    print(f"  c = 10, d = 10: c is d = {c is d} (id(c)={id(c)}, id(d)={id(d)})")
    
    # Large integers are not cached
    x = 1000
    y = 1000
    z = 500 + 500  # Still creates new object
    
    print(f"\\nLarge integers:")
    print(f"  x = 1000, y = 1000: x is y = {x is y}")
    print(f"  x = 1000, z = 500+500: x is z = {x is z}")
    print(f"  id(x)={id(x)}, id(y)={id(y)}, id(z)={id(z)}")
    
    # String interning
    print(f"\\nString Interning:")
    
    str1 = "hello"
    str2 = "hello"
    str3 = "hello world"
    str4 = "hello world"
    str5 = "hello" + " world"  # Runtime concatenation
    
    print(f"  str1 = 'hello', str2 = 'hello': str1 is str2 = {str1 is str2}")
    print(f"  str3 = 'hello world', str4 = 'hello world': str3 is str4 = {str3 is str4}")
    print(f"  str3 = 'hello world', str5 = 'hello' + ' world': str3 is str5 = {str3 is str5}")
    
    # List and mutable object identity
    print(f"\\nMutable Object Identity:")
    
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1  # Same object
    list4 = list1.copy()  # Different object, same content
    
    print(f"  list1 = [1,2,3], list2 = [1,2,3]: list1 is list2 = {list1 is list2}")
    print(f"  list3 = list1: list1 is list3 = {list1 is list3}")
    print(f"  list4 = list1.copy(): list1 is list4 = {list1 is list4}")
    print(f"  list1 == list4 = {list1 == list4} (content equal)")
    
    # Modify list1 and observe effects
    list1.append(4)
    print(f"  After list1.append(4):")
    print(f"    list1: {list1}")
    print(f"    list3: {list3} (same object, changed)")
    print(f"    list4: {list4} (different object, unchanged)")
    
    # Function identity
    print(f"\\nFunction Identity:")
    
    def func1():
        return "function 1"
    
    def func2():
        return "function 1"  # Same body, different function
    
    func3 = func1  # Same function object
    
    print(f"  func1 is func2: {func1 is func2} (different functions)")
    print(f"  func1 is func3: {func1 is func3} (same function object)")
    print(f"  id(func1)={id(func1)}, id(func2)={id(func2)}")
    
    # Class and instance identity
    print(f"\\nClass and Instance Identity:")
    
    class MyClass:
        class_var = "shared"
        
        def __init__(self, value):
            self.value = value
    
    obj1 = MyClass(10)
    obj2 = MyClass(10)
    obj3 = obj1
    
    print(f"  obj1 is obj2: {obj1 is obj2} (different instances)")
    print(f"  obj1 is obj3: {obj1 is obj3} (same instance)")
    print(f"  obj1.value == obj2.value: {obj1.value == obj2.value} (same values)")
    print(f"  obj1.__class__ is obj2.__class__: {obj1.__class__ is obj2.__class__} (same class)")
    
    # Identity tracking
    print(f"\\nIdentity Tracking:")
    
    class IdentityTracker:
        def __init__(self):
            self.objects = set()
            self.id_map = {}
        
        def track(self, obj, name=None):
            obj_id = id(obj)
            self.objects.add(obj_id)
            if name:
                self.id_map[obj_id] = name
            return obj_id
        
        def is_tracked(self, obj):
            return id(obj) in self.objects
        
        def get_name(self, obj):
            return self.id_map.get(id(obj), "unnamed")
        
        def get_stats(self):
            return {
                "tracked_count": len(self.objects),
                "named_count": len(self.id_map),
                "tracked_ids": list(self.objects)
            }
    
    tracker = IdentityTracker()
    
    # Track various objects
    test_objects = [
        ([1, 2, 3], "list"),
        ({"key": "value"}, "dict"),
        ("test string", "string"),
        (MyClass(42), "instance")
    ]
    
    for obj, name in test_objects:
        obj_id = tracker.track(obj, name)
        print(f"  Tracked {name}: id={obj_id}")
    
    # Test tracking
    test_list = [1, 2, 3]
    is_tracked_before = tracker.is_tracked(test_list)
    tracker.track(test_list, "test_list")
    is_tracked_after = tracker.is_tracked(test_list)
    
    print(f"  test_list tracked before: {is_tracked_before}")
    print(f"  test_list tracked after: {is_tracked_after}")
    print(f"  Tracker stats: {tracker.get_stats()}")
    
    # Memory address patterns
    print(f"\\nMemory Address Patterns:")
    
    def analyze_memory_pattern(obj_type, count=10):
        objects = []
        addresses = []
        
        for i in range(count):
            if obj_type == list:
                obj = [i]
            elif obj_type == dict:
                obj = {f"key_{i}": i}
            elif obj_type == str:
                obj = f"string_{i}"
            else:
                obj = obj_type()
            
            objects.append(obj)
            addresses.append(id(obj))
        
        # Analyze patterns
        gaps = [addresses[i+1] - addresses[i] for i in range(len(addresses)-1)]
        avg_gap = sum(abs(gap) for gap in gaps) / len(gaps) if gaps else 0
        
        return {
            "type": obj_type.__name__,
            "addresses": addresses,
            "gaps": gaps,
            "avg_gap": avg_gap,
            "min_addr": min(addresses),
            "max_addr": max(addresses)
        }
    
    # Analyze different object types
    for obj_type in [list, dict, str]:
        pattern = analyze_memory_pattern(obj_type, 5)
        print(f"  {pattern['type']} pattern:")
        print(f"    Average gap: {pattern['avg_gap']:.0f}")
        print(f"    Address range: {pattern['min_addr']} - {pattern['max_addr']}")
    
    return {
        "small_int_cached": a is b,
        "large_int_cached": x is y,
        "string_interned": str1 is str2,
        "runtime_string_interned": str3 is str5,
        "list_identity": list1 is list3,
        "list_copy_identity": list1 is list4,
        "function_identity": func1 is func2,
        "class_identity": obj1.__class__ is obj2.__class__,
        "tracker_stats": tracker.get_stats(),
        "memory_patterns": {obj_type.__name__: analyze_memory_pattern(obj_type, 3) 
                           for obj_type in [list, dict]}
    }

def hashing_mechanisms():
    """Demonstrate hash functions and hash-based collections."""
    print("\\n=== Hashing Mechanisms ===")
    
    # Basic hashing
    print("Basic Hashing:")
    
    hashable_objects = [
        42,
        3.14,
        "hello",
        (1, 2, 3),
        frozenset([1, 2, 3]),
        True,
        None
    ]
    
    hash_values = {}
    for obj in hashable_objects:
        hash_val = hash(obj)
        hash_values[repr(obj)] = hash_val
        print(f"  hash({repr(obj)}) = {hash_val}")
    
    # Hash consistency
    print(f"\\nHash Consistency:")
    
    test_string = "python"
    hash1 = hash(test_string)
    hash2 = hash(test_string)
    identical_string = "pyt" + "hon"
    hash3 = hash(identical_string)
    
    print(f"  hash('python') = {hash1}")
    print(f"  hash('python') again = {hash2}")
    print(f"  hash('pyt' + 'hon') = {hash3}")
    print(f"  Consistent: {hash1 == hash2 == hash3}")
    
    # Unhashable objects
    print(f"\\nUnhashable Objects:")
    
    unhashable_objects = [
        [1, 2, 3],
        {"key": "value"},
        {1, 2, 3}
    ]
    
    for obj in unhashable_objects:
        try:
            hash_val = hash(obj)
            print(f"  hash({repr(obj)}) = {hash_val}")
        except TypeError as e:
            print(f"  hash({type(obj).__name__}) failed: {e}")
    
    # Custom hashable class
    print(f"\\nCustom Hashable Class:")
    
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __hash__(self):
            return hash((self.x, self.y))
        
        def __eq__(self, other):
            if not isinstance(other, Point):
                return False
            return self.x == other.x and self.y == other.y
        
        def __repr__(self):
            return f"Point({self.x}, {self.y})"
    
    # Test custom hashing
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(2, 3)
    
    print(f"  Point(1, 2) hash: {hash(p1)}")
    print(f"  Point(1, 2) hash (different instance): {hash(p2)}")
    print(f"  Point(2, 3) hash: {hash(p3)}")
    print(f"  p1 == p2: {p1 == p2}")
    print(f"  hash(p1) == hash(p2): {hash(p1) == hash(p2)}")
    
    # Using points in hash-based collections
    point_set = {p1, p2, p3}
    point_dict = {p1: "first", p2: "second", p3: "third"}
    
    print(f"  Point set length: {len(point_set)} (should be 2)")
    print(f"  Point dict: {point_dict}")
    
    # Hash distribution analysis
    print(f"\\nHash Distribution Analysis:")
    
    def analyze_hash_distribution(data, hash_func=hash):
        \"\"\"Analyze hash distribution for given data.\"\"\"
        hashes = [hash_func(item) for item in data]
        
        # Basic statistics
        unique_hashes = len(set(hashes))
        total_items = len(data)
        collision_rate = (total_items - unique_hashes) / total_items
        
        # Distribution in buckets (simulate hash table)
        bucket_count = 16
        bucket_distribution = [0] * bucket_count
        
        for hash_val in hashes:
            bucket = hash_val % bucket_count
            bucket_distribution[bucket] += 1
        
        # Calculate variance to measure distribution quality
        avg_per_bucket = total_items / bucket_count
        variance = sum((count - avg_per_bucket) ** 2 for count in bucket_distribution) / bucket_count
        
        return {
            "total_items": total_items,
            "unique_hashes": unique_hashes,
            "collision_rate": collision_rate,
            "bucket_distribution": bucket_distribution,
            "distribution_variance": variance
        }
    
    # Test hash distribution with different data types
    datasets = [
        ("integers", list(range(100))),
        ("strings", [f"string_{i}" for i in range(100)]),
        ("points", [Point(i % 10, i // 10) for i in range(100)])
    ]
    
    distribution_results = {}
    for name, dataset in datasets:
        analysis = analyze_hash_distribution(dataset)
        distribution_results[name] = analysis
        
        print(f"  {name}:")
        print(f"    Collision rate: {analysis['collision_rate']:.2%}")
        print(f"    Distribution variance: {analysis['distribution_variance']:.2f}")
        print(f"    Bucket fill: {analysis['bucket_distribution']}")
    
    # Custom hash functions
    print(f"\\nCustom Hash Functions:")
    
    def simple_string_hash(s):
        \"\"\"Simple string hash function.\"\"\"
        hash_val = 0
        for char in s:
            hash_val = (hash_val * 31 + ord(char)) % (2**32)
        return hash_val
    
    def fnv_hash(data):
        \"\"\"FNV-1a hash function.\"\"\"
        hash_val = 2166136261  # FNV offset basis
        for byte in data.encode('utf-8') if isinstance(data, str) else data:
            hash_val ^= byte if isinstance(byte, int) else ord(byte)
            hash_val *= 16777619  # FNV prime
            hash_val &= 0xffffffff  # Keep 32-bit
        return hash_val
    
    # Compare hash functions
    test_strings = ["hello", "world", "python", "hashing", "functions"]
    
    print(f"  Hash function comparison:")
    for string in test_strings:
        builtin_hash = hash(string) & 0xffffffff  # Mask to 32-bit for comparison
        simple_hash = simple_string_hash(string)
        fnv_hash_val = fnv_hash(string)
        
        print(f"    '{string}':")
        print(f"      Built-in: {builtin_hash}")
        print(f"      Simple:   {simple_hash}")
        print(f"      FNV-1a:   {fnv_hash_val}")
    
    # Hash-based caching
    print(f"\\nHash-based Caching:")
    
    class HashCache:
        def __init__(self, max_size=100):
            self.cache = {}
            self.max_size = max_size
            self.hits = 0
            self.misses = 0
        
        def get(self, key, compute_func):
            \"\"\"Get value from cache or compute it.\"\"\"
            try:
                key_hash = hash(key)
            except TypeError:
                # Unhashable key, compute directly
                self.misses += 1
                return compute_func(key)
            
            if key_hash in self.cache:
                self.hits += 1
                return self.cache[key_hash]
            
            # Cache miss, compute value
            self.misses += 1
            value = compute_func(key)
            
            # Add to cache (simple eviction: remove oldest if full)
            if len(self.cache) >= self.max_size:
                oldest_key = next(iter(self.cache))
                del self.cache[oldest_key]
            
            self.cache[key_hash] = value
            return value
        
        def get_stats(self):
            total_requests = self.hits + self.misses
            hit_rate = self.hits / total_requests if total_requests > 0 else 0
            return {
                "hits": self.hits,
                "misses": self.misses,
                "hit_rate": hit_rate,
                "cache_size": len(self.cache)
            }
    
    # Test hash cache
    cache = HashCache(max_size=5)
    
    def expensive_computation(x):
        \"\"\"Simulate expensive computation.\"\"\"
        time.sleep(0.001)  # Simulate work
        return x ** 2
    
    # Test caching with repeated access
    test_keys = [1, 2, 3, 1, 2, 4, 5, 6, 1, 2]
    
    results = []
    for key in test_keys:
        result = cache.get(key, expensive_computation)
        results.append(result)
    
    cache_stats = cache.get_stats()
    print(f"  Cache statistics:")
    print(f"    Hits: {cache_stats['hits']}")
    print(f"    Misses: {cache_stats['misses']}")
    print(f"    Hit rate: {cache_stats['hit_rate']:.2%}")
    print(f"    Cache size: {cache_stats['cache_size']}")
    
    return {
        "hash_values": hash_values,
        "hash_consistency": hash1 == hash2 == hash3,
        "point_set_size": len(point_set),
        "point_dict_size": len(point_dict),
        "distribution_results": distribution_results,
        "custom_hash_comparison": {
            string: {
                "builtin": hash(string) & 0xffffffff,
                "simple": simple_string_hash(string),
                "fnv": fnv_hash(string)
            } for string in test_strings[:2]  # Limit for readability
        },
        "cache_stats": cache_stats,
        "cached_results": results
    }

def memory_profiling():
    """Demonstrate memory monitoring and optimization techniques."""
    print("\\n=== Memory Profiling ===")
    
    # Basic memory size analysis
    print("Basic Memory Size Analysis:")
    
    test_objects = [
        ("empty list", []),
        ("list with 10 ints", list(range(10))),
        ("list with 100 ints", list(range(100))),
        ("empty dict", {}),
        ("dict with 10 items", {i: i for i in range(10)}),
        ("string 'hello'", "hello"),
        ("string 100 chars", "a" * 100),
        ("integer 42", 42),
        ("float 3.14", 3.14),
        ("tuple (1,2,3)", (1, 2, 3))
    ]
    
    size_analysis = {}
    for name, obj in test_objects:
        size = sys.getsizeof(obj)
        size_analysis[name] = size
        print(f"  {name}: {size} bytes")
    
    # Deep size calculation
    print(f"\\nDeep Memory Size Analysis:")
    
    def get_deep_size(obj, seen=None):
        \"\"\"Calculate deep memory size of object including referenced objects.\"\"\"
        if seen is None:
            seen = set()
        
        obj_id = id(obj)
        if obj_id in seen:
            return 0
        
        seen.add(obj_id)
        size = sys.getsizeof(obj)
        
        if hasattr(obj, '__dict__'):
            size += get_deep_size(obj.__dict__, seen)
        
        if hasattr(obj, '__slots__'):
            size += sum(get_deep_size(getattr(obj, attr), seen) 
                       for attr in obj.__slots__ if hasattr(obj, attr))
        
        if isinstance(obj, (list, tuple)):
            size += sum(get_deep_size(item, seen) for item in obj)
        elif isinstance(obj, dict):
            size += sum(get_deep_size(key, seen) + get_deep_size(value, seen)
                       for key, value in obj.items())
        elif isinstance(obj, set):
            size += sum(get_deep_size(item, seen) for item in obj)
        
        return size
    
    # Test deep size calculation
    nested_data = {
        "numbers": list(range(10)),
        "nested": {
            "inner_list": [{"key": "value"} for _ in range(5)],
            "inner_dict": {f"key_{i}": [i] * 3 for i in range(3)}
        }
    }
    
    shallow_size = sys.getsizeof(nested_data)
    deep_size = get_deep_size(nested_data)
    
    print(f"  Nested data structure:")
    print(f"    Shallow size: {shallow_size} bytes")
    print(f"    Deep size: {deep_size} bytes")
    print(f"    Ratio: {deep_size / shallow_size:.1f}x")
    
    # Memory growth tracking
    print(f"\\nMemory Growth Tracking:")
    
    class MemoryTracker:
        def __init__(self):
            self.snapshots = []
            self.start_size = self._get_memory_usage()
        
        def _get_memory_usage(self):
            \"\"\"Get current memory usage (simplified).\"\"\"
            return len(gc.get_objects())
        
        def snapshot(self, label=""):
            \"\"\"Take a memory snapshot.\"\"\"
            current_size = self._get_memory_usage()
            growth = current_size - self.start_size
            
            snapshot = {
                "label": label,
                "objects": current_size,
                "growth": growth,
                "growth_percent": (growth / self.start_size * 100) if self.start_size > 0 else 0
            }
            
            self.snapshots.append(snapshot)
            print(f"    {label}: {current_size} objects (+{growth}, {snapshot['growth_percent']:.1f}%)")
            return snapshot
    
    # Track memory during operations
    tracker = MemoryTracker()
    tracker.snapshot("Initial")
    
    # Create various data structures
    large_list = list(range(1000))
    tracker.snapshot("After creating 1000-item list")
    
    large_dict = {i: f"value_{i}" for i in range(500)}
    tracker.snapshot("After creating 500-item dict")
    
    nested_structure = [[i] * 10 for i in range(100)]
    tracker.snapshot("After creating nested structure")
    
    # Clean up and measure
    del large_list, large_dict, nested_structure
    gc.collect()
    tracker.snapshot("After cleanup and gc.collect()")
    
    # Memory-efficient alternatives
    print(f"\\nMemory-Efficient Alternatives:")
    
    # Generator vs list
    def list_approach(n):
        return [i**2 for i in range(n)]
    
    def generator_approach(n):
        return (i**2 for i in range(n))
    
    n = 1000
    
    # Measure list approach
    list_result = list_approach(n)
    list_size = sys.getsizeof(list_result)
    
    # Measure generator approach
    gen_result = generator_approach(n)
    gen_size = sys.getsizeof(gen_result)
    
    print(f"  List of {n} squares: {list_size} bytes")
    print(f"  Generator of {n} squares: {gen_size} bytes")
    print(f"  Memory savings: {(list_size - gen_size) / list_size:.1%}")
    
    # Slots vs regular class
    class RegularClass:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c
    
    class SlotsClass:
        __slots__ = ['a', 'b', 'c']
        
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c
    
    # Compare instance sizes
    regular_instance = RegularClass(1, 2, 3)
    slots_instance = SlotsClass(1, 2, 3)
    
    regular_size = sys.getsizeof(regular_instance) + sys.getsizeof(regular_instance.__dict__)
    slots_size = sys.getsizeof(slots_instance)
    
    print(f"  Regular class instance: {regular_size} bytes")
    print(f"  Slots class instance: {slots_size} bytes")
    print(f"  Memory savings with __slots__: {(regular_size - slots_size) / regular_size:.1%}")
    
    # Memory profiling with tracemalloc
    print(f"\\nAdvanced Memory Profiling:")
    
    def memory_intensive_function():
        \"\"\"Function that allocates significant memory.\"\"\"
        data = []
        for i in range(100):
            data.append([j for j in range(100)])
        return data
    
    # Start memory tracing
    tracemalloc.start()
    
    # Run memory-intensive function
    result = memory_intensive_function()
    
    # Get memory statistics
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"  Current memory usage: {current / 1024 / 1024:.2f} MB")
    print(f"  Peak memory usage: {peak / 1024 / 1024:.2f} MB")
    
    # Memory pool analysis
    print(f"\\nMemory Pool Analysis:")
    
    def analyze_object_pools():
        \"\"\"Analyze object allocation patterns.\"\"\"
        # Get all objects and group by type
        all_objects = gc.get_objects()
        type_counts = {}
        
        for obj in all_objects:
            obj_type = type(obj).__name__
            type_counts[obj_type] = type_counts.get(obj_type, 0) + 1
        
        # Sort by count
        sorted_types = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)
        
        return sorted_types[:10]  # Top 10 types
    
    object_pools = analyze_object_pools()
    
    print(f"  Top object types by count:")
    for obj_type, count in object_pools:
        print(f"    {obj_type}: {count}")
    
    return {
        "size_analysis": size_analysis,
        "nested_data_sizes": {"shallow": shallow_size, "deep": deep_size},
        "memory_snapshots": tracker.snapshots,
        "generator_vs_list": {"list_size": list_size, "gen_size": gen_size},
        "slots_vs_regular": {"regular_size": regular_size, "slots_size": slots_size},
        "tracemalloc_stats": {"current_mb": current / 1024 / 1024, "peak_mb": peak / 1024 / 1024},
        "top_object_types": object_pools[:5]
    }

def weak_references():
    """Demonstrate weak references for memory management."""
    print("\\n=== Weak References ===")
    
    # Basic weak references
    print("Basic Weak References:")
    
    class MyClass:
        def __init__(self, name):
            self.name = name
        
        def __repr__(self):
            return f"MyClass('{self.name}')"
        
        def __del__(self):
            print(f"    MyClass('{self.name}') is being deleted")
    
    # Create object and weak reference
    obj = MyClass("test_object")
    weak_ref = weakref.ref(obj)
    
    print(f"  Original object: {obj}")
    print(f"  Weak reference: {weak_ref}")
    print(f"  Weak ref target: {weak_ref()}")
    print(f"  Object exists: {weak_ref() is not None}")
    
    # Delete original object
    print(f"  Deleting original object...")
    del obj
    gc.collect()  # Force garbage collection
    
    print(f"  After deletion:")
    print(f"    Weak ref target: {weak_ref()}")
    print(f"    Object exists: {weak_ref() is not None}")
    
    # Weak reference callbacks
    print(f"\\nWeak Reference Callbacks:")
    
    def cleanup_callback(weak_ref):
        print(f"    Callback: Object referenced by {weak_ref} has been deleted")
    
    obj2 = MyClass("callback_test")
    weak_ref2 = weakref.ref(obj2, cleanup_callback)
    
    print(f"  Created object with callback: {obj2}")
    print(f"  Deleting object...")
    del obj2
    gc.collect()
    
    # WeakKeyDictionary and WeakValueDictionary
    print(f"\\nWeak Dictionaries:")
    
    # WeakValueDictionary - values are weakly referenced
    weak_value_dict = weakref.WeakValueDictionary()
    
    obj3 = MyClass("weak_value")
    obj4 = MyClass("another_weak_value")
    
    weak_value_dict['key1'] = obj3
    weak_value_dict['key2'] = obj4
    
    print(f"  WeakValueDictionary before deletion:")
    print(f"    Keys: {list(weak_value_dict.keys())}")
    print(f"    Values: {list(weak_value_dict.values())}")
    
    # Delete one object
    del obj3
    gc.collect()
    
    print(f"  WeakValueDictionary after deleting obj3:")
    print(f"    Keys: {list(weak_value_dict.keys())}")
    print(f"    Values: {list(weak_value_dict.values())}")
    
    # WeakKeyDictionary - keys are weakly referenced
    weak_key_dict = weakref.WeakKeyDictionary()
    
    key1 = MyClass("key1")
    key2 = MyClass("key2")
    
    weak_key_dict[key1] = "value1"
    weak_key_dict[key2] = "value2"
    
    print(f"  \\nWeakKeyDictionary before deletion:")
    print(f"    Keys: {list(weak_key_dict.keys())}")
    print(f"    Values: {list(weak_key_dict.values())}")
    
    # Delete one key
    del key1
    gc.collect()
    
    print(f"  WeakKeyDictionary after deleting key1:")
    print(f"    Keys: {list(weak_key_dict.keys())}")
    print(f"    Values: {list(weak_key_dict.values())}")
    
    # Weak sets
    print(f"\\nWeak Sets:")
    
    weak_set = weakref.WeakSet()
    
    obj5 = MyClass("set_member1")
    obj6 = MyClass("set_member2")
    obj7 = MyClass("set_member3")
    
    weak_set.add(obj5)
    weak_set.add(obj6)
    weak_set.add(obj7)
    
    print(f"  WeakSet before deletion: {len(weak_set)} members")
    print(f"    Members: {list(weak_set)}")
    
    # Delete some objects
    del obj5, obj6
    gc.collect()
    
    print(f"  WeakSet after deletion: {len(weak_set)} members")
    print(f"    Members: {list(weak_set)}")
    
    # Avoiding circular references
    print(f"\\nAvoiding Circular References:")
    
    class Parent:
        def __init__(self, name):
            self.name = name
            self.children = []
        
        def add_child(self, child):
            self.children.append(child)
            child.parent = weakref.ref(self)  # Weak reference to parent
        
        def __repr__(self):
            return f"Parent('{self.name}')"
        
        def __del__(self):
            print(f"    Parent('{self.name}') deleted")
    
    class Child:
        def __init__(self, name):
            self.name = name
            self.parent = None
        
        def get_parent(self):
            return self.parent() if self.parent else None
        
        def __repr__(self):
            return f"Child('{self.name}')"
        
        def __del__(self):
            print(f"    Child('{self.name}') deleted")
    
    # Create parent-child relationship
    parent = Parent("Parent1")
    child1 = Child("Child1")
    child2 = Child("Child2")
    
    parent.add_child(child1)
    parent.add_child(child2)
    
    print(f"  Created parent-child relationships:")
    print(f"    Parent: {parent}")
    print(f"    Children: {parent.children}")
    print(f"    Child1's parent: {child1.get_parent()}")
    
    # Delete parent - children should still be able to detect this
    print(f"  Deleting parent...")
    del parent
    gc.collect()
    
    print(f"    Child1's parent after deletion: {child1.get_parent()}")
    
    # Observer pattern with weak references
    print(f"\\nObserver Pattern with Weak References:")
    
    class Observable:
        def __init__(self):
            self._observers = weakref.WeakSet()
        
        def add_observer(self, observer):
            self._observers.add(observer)
        
        def remove_observer(self, observer):
            self._observers.discard(observer)
        
        def notify(self, message):
            # Create a copy of the set to avoid issues during iteration
            observers = list(self._observers)
            print(f"    Notifying {len(observers)} observers: {message}")
            for observer in observers:
                observer.update(message)
        
        def observer_count(self):
            return len(self._observers)
    
    class Observer:
        def __init__(self, name):
            self.name = name
        
        def update(self, message):
            print(f"      {self.name} received: {message}")
        
        def __del__(self):
            print(f"    Observer '{self.name}' deleted")
    
    # Test observer pattern
    observable = Observable()
    
    observer1 = Observer("Observer1")
    observer2 = Observer("Observer2")
    observer3 = Observer("Observer3")
    
    observable.add_observer(observer1)
    observable.add_observer(observer2)
    observable.add_observer(observer3)
    
    print(f"  Initial observer count: {observable.observer_count()}")
    observable.notify("First message")
    
    # Delete one observer
    del observer2
    gc.collect()
    
    print(f"  Observer count after deletion: {observable.observer_count()}")
    observable.notify("Second message")
    
    # Cache with weak references
    print(f"\\nCache with Weak References:")
    
    class WeakCache:
        def __init__(self):
            self._cache = weakref.WeakValueDictionary()
            self._hits = 0
            self._misses = 0
        
        def get(self, key, factory):
            if key in self._cache:
                self._hits += 1
                return self._cache[key]
            
            self._misses += 1
            value = factory()
            self._cache[key] = value
            return value
        
        def get_stats(self):
            return {
                "hits": self._hits,
                "misses": self._misses,
                "cache_size": len(self._cache)
            }
    
    # Test weak cache
    cache = WeakCache()
    
    def create_expensive_object(name):
        return MyClass(f"expensive_{name}")
    
    # Get objects from cache
    obj_a = cache.get("a", lambda: create_expensive_object("a"))
    obj_b = cache.get("b", lambda: create_expensive_object("b"))
    obj_a_again = cache.get("a", lambda: create_expensive_object("a"))  # Should be cached
    
    print(f"  Cache stats after operations: {cache.get_stats()}")
    print(f"  obj_a is obj_a_again: {obj_a is obj_a_again}")
    
    # Delete objects and see cache shrink
    del obj_a, obj_a_again
    gc.collect()
    
    print(f"  Cache stats after deletion: {cache.get_stats()}")
    
    return {
        "weak_ref_exists_before": True,  # We know this was True
        "weak_ref_exists_after": weak_ref() is not None,
        "weak_value_dict_keys_after": list(weak_value_dict.keys()),
        "weak_key_dict_keys_after": list(weak_key_dict.keys()),
        "weak_set_size_before": 3,
        "weak_set_size_after": len(weak_set),
        "child_parent_exists": child1.get_parent() is not None,
        "observer_count_initial": 3,
        "observer_count_after_deletion": observable.observer_count(),
        "cache_stats": cache.get_stats()
    }

def performance_optimization():
    """Demonstrate caching and performance optimization patterns."""
    print("\\n=== Performance Optimization ===")
    
    # Function memoization
    print("Function Memoization:")
    
    def fibonacci_naive(n):
        \"\"\"Naive fibonacci implementation.\"\"\"
        if n <= 1:
            return n
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)
    
    @functools.lru_cache(maxsize=128)
    def fibonacci_cached(n):
        \"\"\"Cached fibonacci implementation.\"\"\"
        if n <= 1:
            return n
        return fibonacci_cached(n-1) + fibonacci_cached(n-2)
    
    def fibonacci_manual_cache(n, cache={}):
        \"\"\"Manually cached fibonacci implementation.\"\"\"
        if n in cache:
            return cache[n]
        if n <= 1:
            cache[n] = n
            return n
        cache[n] = fibonacci_manual_cache(n-1, cache) + fibonacci_manual_cache(n-2, cache)
        return cache[n]
    
    # Performance comparison
    import time
    
    test_n = 30
    
    # Time naive approach
    start = time.time()
    naive_result = fibonacci_naive(test_n)
    naive_time = time.time() - start
    
    # Time cached approach
    start = time.time()
    cached_result = fibonacci_cached(test_n)
    cached_time = time.time() - start
    
    # Time manual cache approach
    start = time.time()
    manual_result = fibonacci_manual_cache(test_n)
    manual_time = time.time() - start
    
    print(f"  Fibonacci({test_n}):")
    print(f"    Naive: {naive_result} ({naive_time:.4f}s)")
    print(f"    LRU cached: {cached_result} ({cached_time:.4f}s)")
    print(f"    Manual cache: {manual_result} ({manual_time:.4f}s)")
    print(f"    Speedup (LRU): {naive_time/cached_time:.1f}x")
    print(f"    Speedup (manual): {naive_time/manual_time:.1f}x")
    
    # Cache info
    cache_info = fibonacci_cached.cache_info()
    print(f"    LRU cache info: {cache_info}")
    
    # Custom caching decorator
    print(f"\\nCustom Caching Decorator:")
    
    def memory_efficient_cache(maxsize=128):
        \"\"\"Custom caching decorator with memory management.\"\"\"
        def decorator(func):
            cache = {}
            access_order = []
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # Create cache key
                key = str(args) + str(sorted(kwargs.items()))
                
                if key in cache:
                    # Move to end (most recently used)
                    access_order.remove(key)
                    access_order.append(key)
                    return cache[key]
                
                # Compute result
                result = func(*args, **kwargs)
                
                # Add to cache
                cache[key] = result
                access_order.append(key)
                
                # Evict if necessary
                if len(cache) > maxsize:
                    oldest_key = access_order.pop(0)
                    del cache[oldest_key]
                
                return result
            
            def cache_info():
                return {
                    "cache_size": len(cache),
                    "max_size": maxsize,
                    "access_order": len(access_order)
                }
            
            wrapper.cache_info = cache_info
            wrapper.cache_clear = lambda: (cache.clear(), access_order.clear())
            
            return wrapper
        return decorator
    
    @memory_efficient_cache(maxsize=50)
    def expensive_computation(x, y):
        \"\"\"Simulate expensive computation.\"\"\"
        time.sleep(0.001)  # Simulate work
        return x ** y + y ** x
    
    # Test custom cache
    test_pairs = [(2, 3), (3, 4), (2, 3), (4, 5), (3, 4), (5, 6)]
    
    results = []
    for x, y in test_pairs:
        result = expensive_computation(x, y)
        results.append(result)
    
    custom_cache_info = expensive_computation.cache_info()
    print(f"  Custom cache info: {custom_cache_info}")
    
    # Memory-sensitive caching
    print(f"\\nMemory-Sensitive Caching:")
    
    class MemorySensitiveCache:
        def __init__(self, max_memory_mb=10):
            self.cache = {}
            self.max_memory = max_memory_mb * 1024 * 1024  # Convert to bytes
            self.current_memory = 0
        
        def get(self, key, compute_func):
            if key in self.cache:
                return self.cache[key]
            
            result = compute_func()
            result_size = sys.getsizeof(result)
            
            # Check if we need to evict
            while self.current_memory + result_size > self.max_memory and self.cache:
                # Simple eviction: remove first item
                evicted_key = next(iter(self.cache))
                evicted_value = self.cache.pop(evicted_key)
                self.current_memory -= sys.getsizeof(evicted_value)
            
            # Add new result
            self.cache[key] = result
            self.current_memory += result_size
            
            return result
        
        def get_stats(self):
            return {
                "cache_entries": len(self.cache),
                "memory_used_mb": self.current_memory / 1024 / 1024,
                "memory_limit_mb": self.max_memory / 1024 / 1024
            }
    
    # Test memory-sensitive cache
    memory_cache = MemorySensitiveCache(max_memory_mb=1)  # Very small limit
    
    def create_large_data(size):
        return list(range(size * 1000))  # Create large list
    
    # Add data to cache
    for i in range(5):
        data = memory_cache.get(f"data_{i}", lambda i=i: create_large_data(i+1))
    
    memory_stats = memory_cache.get_stats()
    print(f"  Memory cache stats: {memory_stats}")
    
    # Lazy evaluation patterns
    print(f"\\nLazy Evaluation Patterns:")
    
    class LazyProperty:
        \"\"\"Descriptor for lazy property evaluation.\"\"\"
        def __init__(self, func):
            self.func = func
            self.name = func.__name__
        
        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            
            # Check if already computed
            if hasattr(obj, f'_lazy_{self.name}'):
                return getattr(obj, f'_lazy_{self.name}')
            
            # Compute and cache
            value = self.func(obj)
            setattr(obj, f'_lazy_{self.name}', value)
            return value
    
    class ExpensiveObject:
        def __init__(self, data):
            self.data = data
        
        @LazyProperty
        def expensive_calculation(self):
            print(f"      Computing expensive calculation...")
            time.sleep(0.001)  # Simulate expensive work
            return sum(x**2 for x in self.data)
        
        @LazyProperty
        def another_calculation(self):
            print(f"      Computing another calculation...")
            time.sleep(0.001)  # Simulate expensive work
            return max(self.data) - min(self.data)
    
    # Test lazy properties
    obj = ExpensiveObject([1, 2, 3, 4, 5])
    
    print(f"  Object created (no calculations yet)")
    print(f"  First access to expensive_calculation:")
    result1 = obj.expensive_calculation
    print(f"    Result: {result1}")
    
    print(f"  Second access to expensive_calculation (should be cached):")
    result2 = obj.expensive_calculation
    print(f"    Result: {result2}")
    
    print(f"  Access to another_calculation:")
    result3 = obj.another_calculation
    print(f"    Result: {result3}")
    
    # Performance monitoring
    print(f"\\nPerformance Monitoring:")
    
    class PerformanceMonitor:
        def __init__(self):
            self.call_counts = {}
            self.total_times = {}
        
        def monitor(self, func):
            \"\"\"Decorator to monitor function performance.\"\"\"
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                func_name = func.__name__
                
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                
                execution_time = end_time - start_time
                
                self.call_counts[func_name] = self.call_counts.get(func_name, 0) + 1
                self.total_times[func_name] = self.total_times.get(func_name, 0) + execution_time
                
                return result
            return wrapper
        
        def get_stats(self):
            stats = {}
            for func_name in self.call_counts:
                stats[func_name] = {
                    "call_count": self.call_counts[func_name],
                    "total_time": self.total_times[func_name],
                    "avg_time": self.total_times[func_name] / self.call_counts[func_name]
                }
            return stats
    
    # Test performance monitoring
    monitor = PerformanceMonitor()
    
    @monitor.monitor
    def fast_function(x):
        return x * 2
    
    @monitor.monitor
    def slow_function(x):
        time.sleep(0.001)
        return x ** 2
    
    # Run monitored functions
    for i in range(10):
        fast_function(i)
    
    for i in range(5):
        slow_function(i)
    
    perf_stats = monitor.get_stats()
    print(f"  Performance statistics:")
    for func_name, stats in perf_stats.items():
        print(f"    {func_name}:")
        print(f"      Calls: {stats['call_count']}")
        print(f"      Total time: {stats['total_time']:.4f}s")
        print(f"      Average time: {stats['avg_time']:.4f}s")
    
    return {
        "fibonacci_performance": {
            "naive_time": naive_time,
            "cached_time": cached_time,
            "manual_time": manual_time,
            "speedup_cached": naive_time / cached_time,
            "speedup_manual": naive_time / manual_time
        },
        "lru_cache_info": cache_info._asdict(),
        "custom_cache_info": custom_cache_info,
        "memory_cache_stats": memory_stats,
        "lazy_property_results": [result1, result2, result3],
        "performance_stats": perf_stats
    }

# Main execution
if __name__ == "__main__":
    print("=== Built-in Memory and Performance Functions ===")
    
    print("\\n1. Object Identity:")
    identity_results = object_identity()
    
    print("\\n2. Hashing Mechanisms:")
    hashing_results = hashing_mechanisms()
    
    print("\\n3. Memory Profiling:")
    memory_results = memory_profiling()
    
    print("\\n4. Weak References:")
    weakref_results = weak_references()
    
    print("\\n5. Performance Optimization:")
    performance_results = performance_optimization()
    
    print("\\n" + "="*60)
    print("=== MEMORY AND PERFORMANCE FUNCTIONS COMPLETE ===")
    print("✓ Object identity and memory allocation")
    print("✓ Hash functions and distribution analysis")
    print("✓ Memory profiling and optimization")
    print("✓ Weak references for memory management")
    print("✓ Performance optimization with caching")
    print("✓ Lazy evaluation and monitoring")
```

## Hints

- Use `id()` to check object identity, not equality
- `hash()` enables efficient lookups in sets and dict keys
- `sys.getsizeof()` gives shallow size - calculate deep size for nested structures
- Weak references prevent circular reference memory leaks
- `@functools.lru_cache` provides built-in memoization

## Test Cases

Your functions should handle:

1. Object identity comparisons across different data types
2. Hash function analysis and custom hashable classes
3. Memory usage tracking and optimization techniques
4. Weak reference patterns for avoiding memory leaks
5. Performance optimization with various caching strategies

## Bonus Challenge

Build a comprehensive memory profiler, implement an adaptive caching system, and create a performance monitoring framework with automatic optimization suggestions!
