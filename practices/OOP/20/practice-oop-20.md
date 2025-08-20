# Enterprise OOP Architecture System - Practice 20

**Difficulty:** ⭐⭐⭐⭐⭐ (Hard)

## Description

Build a comprehensive enterprise-level object-oriented architecture system with advanced patterns, microservices simulation, dependency injection, event sourcing, and distributed computing patterns.

## Objectives

- Implement dependency injection container
- Create event sourcing and CQRS patterns
- Build microservices communication system
- Implement distributed object patterns
- Create enterprise-level architectural components

## Your Tasks

1. **create_dependency_injection_system()** - Build IoC container with scopes
2. **implement_event_sourcing()** - Create event store and projections
3. **build_microservices_architecture()** - Design service mesh simulation
4. **create_distributed_objects()** - Implement proxy and remote patterns
5. **implement_enterprise_patterns()** - Build saga, circuit breaker, and more

## Example

```python
import abc
import asyncio
import threading
import time
import uuid
import json
import pickle
import weakref
from typing import Any, Dict, List, Type, Callable, Optional, Union, Tuple, Protocol
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict, deque
from concurrent.futures import ThreadPoolExecutor, Future
import functools
import logging
import copy
import inspect

# Dependency Injection System
class Scope(Enum):
    """Dependency injection scopes."""
    SINGLETON = "singleton"
    TRANSIENT = "transient"
    SCOPED = "scoped"
    PROTOTYPE = "prototype"

class Injectable:
    """Decorator for marking injectable classes."""
    
    def __init__(self, scope: Scope = Scope.SINGLETON, name: str = None):
        """Initialize injectable decorator."""
        self.scope = scope
        self.name = name
    
    def __call__(self, cls):
        """Mark class as injectable."""
        cls._injectable_scope = self.scope
        cls._injectable_name = self.name or cls.__name__
        return cls

class DependencyInjectionContainer:
    """Advanced dependency injection container."""
    
    def __init__(self):
        """Initialize DI container."""
        self._registrations = {}
        self._singletons = {}
        self._scoped_instances = defaultdict(dict)
        self._factories = {}
        self._decorators = []
        self._current_scope = None
        self._creation_stack = []
    
    def register(self, interface: Type, implementation: Type = None, 
                 scope: Scope = Scope.SINGLETON, name: str = None):
        """Register a type in the container."""
        if implementation is None:
            implementation = interface
        
        registration_key = name or interface.__name__
        self._registrations[registration_key] = {
            'interface': interface,
            'implementation': implementation,
            'scope': scope,
            'name': name
        }
        
        return self
    
    def register_factory(self, interface: Type, factory: Callable, 
                        scope: Scope = Scope.SINGLETON, name: str = None):
        """Register a factory function."""
        registration_key = name or interface.__name__
        self._factories[registration_key] = {
            'interface': interface,
            'factory': factory,
            'scope': scope,
            'name': name
        }
        
        return self
    
    def register_instance(self, interface: Type, instance: Any, name: str = None):
        """Register a specific instance."""
        registration_key = name or interface.__name__
        self._singletons[registration_key] = instance
        self._registrations[registration_key] = {
            'interface': interface,
            'implementation': type(instance),
            'scope': Scope.SINGLETON,
            'name': name
        }
        
        return self
    
    def add_decorator(self, decorator: Callable):
        """Add a decorator to be applied to all resolved instances."""
        self._decorators.append(decorator)
        return self
    
    def create_scope(self):
        """Create a new dependency resolution scope."""
        return DependencyScope(self)
    
    def resolve(self, interface: Type, name: str = None) -> Any:
        """Resolve a dependency."""
        registration_key = name or interface.__name__
        
        # Check for circular dependencies
        if registration_key in self._creation_stack:
            raise ValueError(f"Circular dependency detected: {' -> '.join(self._creation_stack + [registration_key])}")
        
        self._creation_stack.append(registration_key)
        
        try:
            # Check if it's a factory
            if registration_key in self._factories:
                return self._resolve_factory(registration_key)
            
            # Check if it's registered
            if registration_key not in self._registrations:
                # Try to auto-register if it has injectable metadata
                if hasattr(interface, '_injectable_scope'):
                    self.register(interface, interface, interface._injectable_scope, 
                                interface._injectable_name)
                else:
                    raise ValueError(f"Type {registration_key} is not registered")
            
            registration = self._registrations[registration_key]
            scope = registration['scope']
            implementation = registration['implementation']
            
            # Handle different scopes
            if scope == Scope.SINGLETON:
                if registration_key not in self._singletons:
                    self._singletons[registration_key] = self._create_instance(implementation)
                instance = self._singletons[registration_key]
            
            elif scope == Scope.SCOPED:
                if self._current_scope is None:
                    raise ValueError("No active scope for scoped dependency")
                scope_id = id(self._current_scope)
                if registration_key not in self._scoped_instances[scope_id]:
                    self._scoped_instances[scope_id][registration_key] = self._create_instance(implementation)
                instance = self._scoped_instances[scope_id][registration_key]
            
            elif scope in [Scope.TRANSIENT, Scope.PROTOTYPE]:
                instance = self._create_instance(implementation)
            
            else:
                raise ValueError(f"Unknown scope: {scope}")
            
            # Apply decorators
            for decorator in self._decorators:
                instance = decorator(instance)
            
            return instance
        
        finally:
            self._creation_stack.pop()
    
    def _resolve_factory(self, registration_key: str) -> Any:
        """Resolve using a factory function."""
        factory_info = self._factories[registration_key]
        factory = factory_info['factory']
        scope = factory_info['scope']
        
        if scope == Scope.SINGLETON:
            if registration_key not in self._singletons:
                self._singletons[registration_key] = factory(self)
            return self._singletons[registration_key]
        else:
            return factory(self)
    
    def _create_instance(self, implementation: Type) -> Any:
        """Create an instance with dependency injection."""
        # Get constructor parameters
        sig = inspect.signature(implementation.__init__)
        kwargs = {}
        
        for param_name, param in sig.parameters.items():
            if param_name == 'self':
                continue
            
            # Try to resolve parameter by type annotation
            if param.annotation != inspect.Parameter.empty:
                try:
                    kwargs[param_name] = self.resolve(param.annotation)
                except ValueError:
                    # If we can't resolve, use default if available
                    if param.default != inspect.Parameter.empty:
                        kwargs[param_name] = param.default
                    else:
                        raise ValueError(f"Cannot resolve parameter {param_name} of type {param.annotation}")
        
        return implementation(**kwargs)
    
    def dispose(self):
        """Dispose of all managed instances."""
        for instance in self._singletons.values():
            if hasattr(instance, 'dispose'):
                instance.dispose()
        
        self._singletons.clear()
        self._scoped_instances.clear()

class DependencyScope:
    """Dependency resolution scope."""
    
    def __init__(self, container: DependencyInjectionContainer):
        """Initialize scope."""
        self.container = container
        self.scope_id = id(self)
    
    def __enter__(self):
        """Enter scope."""
        self.container._current_scope = self
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit scope."""
        # Dispose scoped instances
        if self.scope_id in self.container._scoped_instances:
            for instance in self.container._scoped_instances[self.scope_id].values():
                if hasattr(instance, 'dispose'):
                    instance.dispose()
            del self.container._scoped_instances[self.scope_id]
        
        self.container._current_scope = None

# Event Sourcing System
@dataclass
class Event:
    """Base event class."""
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    event_type: str = field(default="")
    aggregate_id: str = field(default="")
    version: int = field(default=0)
    timestamp: datetime = field(default_factory=datetime.now)
    data: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

class EventStore:
    """Event store for event sourcing."""
    
    def __init__(self):
        """Initialize event store."""
        self._events = defaultdict(list)  # aggregate_id -> events
        self._snapshots = {}  # aggregate_id -> snapshot
        self._subscriptions = defaultdict(list)  # event_type -> handlers
        self._global_subscriptions = []
    
    def append_events(self, aggregate_id: str, events: List[Event], expected_version: int = None):
        """Append events to the store."""
        current_events = self._events[aggregate_id]
        
        if expected_version is not None and len(current_events) != expected_version:
            raise ValueError(f"Concurrency conflict. Expected version {expected_version}, "
                           f"but current version is {len(current_events)}")
        
        # Set version numbers
        for i, event in enumerate(events):
            event.version = len(current_events) + i + 1
            event.aggregate_id = aggregate_id
        
        # Append events
        self._events[aggregate_id].extend(events)
        
        # Notify subscribers
        for event in events:
            self._notify_subscribers(event)
    
    def get_events(self, aggregate_id: str, from_version: int = 0) -> List[Event]:
        """Get events for an aggregate."""
        events = self._events[aggregate_id]
        return [e for e in events if e.version > from_version]
    
    def get_all_events(self, from_timestamp: datetime = None) -> List[Event]:
        """Get all events, optionally from a timestamp."""
        all_events = []
        for events in self._events.values():
            all_events.extend(events)
        
        if from_timestamp:
            all_events = [e for e in all_events if e.timestamp >= from_timestamp]
        
        return sorted(all_events, key=lambda e: e.timestamp)
    
    def save_snapshot(self, aggregate_id: str, snapshot: Any, version: int):
        """Save a snapshot of an aggregate."""
        self._snapshots[aggregate_id] = {
            'data': snapshot,
            'version': version,
            'timestamp': datetime.now()
        }
    
    def get_snapshot(self, aggregate_id: str) -> Optional[Tuple[Any, int]]:
        """Get the latest snapshot for an aggregate."""
        if aggregate_id in self._snapshots:
            snapshot_info = self._snapshots[aggregate_id]
            return snapshot_info['data'], snapshot_info['version']
        return None
    
    def subscribe(self, event_type: str, handler: Callable[[Event], None]):
        """Subscribe to specific event types."""
        self._subscriptions[event_type].append(handler)
    
    def subscribe_all(self, handler: Callable[[Event], None]):
        """Subscribe to all events."""
        self._global_subscriptions.append(handler)
    
    def _notify_subscribers(self, event: Event):
        """Notify event subscribers."""
        # Notify specific event type subscribers
        for handler in self._subscriptions[event.event_type]:
            try:
                handler(event)
            except Exception as e:
                print(f"Error in event handler: {e}")
        
        # Notify global subscribers
        for handler in self._global_subscriptions:
            try:
                handler(event)
            except Exception as e:
                print(f"Error in global event handler: {e}")

class AggregateRoot:
    """Base aggregate root for event sourcing."""
    
    def __init__(self, aggregate_id: str = None):
        """Initialize aggregate root."""
        self.aggregate_id = aggregate_id or str(uuid.uuid4())
        self.version = 0
        self._uncommitted_events = []
    
    def apply_event(self, event: Event):
        """Apply an event to the aggregate."""
        # Set event metadata
        event.aggregate_id = self.aggregate_id
        event.version = self.version + 1
        
        # Apply the event
        self._handle_event(event)
        
        # Add to uncommitted events
        self._uncommitted_events.append(event)
        self.version += 1
    
    def mark_events_as_committed(self):
        """Mark all uncommitted events as committed."""
        self._uncommitted_events.clear()
    
    def get_uncommitted_events(self) -> List[Event]:
        """Get uncommitted events."""
        return self._uncommitted_events.copy()
    
    def load_from_history(self, events: List[Event]):
        """Load aggregate state from event history."""
        for event in events:
            self._handle_event(event)
            self.version = event.version
    
    def _handle_event(self, event: Event):
        """Handle an event. Override in subclasses."""
        handler_name = f"_handle_{event.event_type.lower()}"
        handler = getattr(self, handler_name, None)
        if handler:
            handler(event)

# CQRS Implementation
class Command:
    """Base command class."""
    
    def __init__(self, command_id: str = None):
        """Initialize command."""
        self.command_id = command_id or str(uuid.uuid4())
        self.timestamp = datetime.now()

class Query:
    """Base query class."""
    
    def __init__(self, query_id: str = None):
        """Initialize query."""
        self.query_id = query_id or str(uuid.uuid4())
        self.timestamp = datetime.now()

class CommandHandler(abc.ABC):
    """Abstract command handler."""
    
    @abc.abstractmethod
    def handle(self, command: Command) -> Any:
        """Handle a command."""
        pass

class QueryHandler(abc.ABC):
    """Abstract query handler."""
    
    @abc.abstractmethod
    def handle(self, query: Query) -> Any:
        """Handle a query."""
        pass

class MessageBus:
    """CQRS message bus."""
    
    def __init__(self, event_store: EventStore):
        """Initialize message bus."""
        self.event_store = event_store
        self._command_handlers = {}
        self._query_handlers = {}
        self._middleware = []
    
    def register_command_handler(self, command_type: Type[Command], handler: CommandHandler):
        """Register a command handler."""
        self._command_handlers[command_type] = handler
    
    def register_query_handler(self, query_type: Type[Query], handler: QueryHandler):
        """Register a query handler."""
        self._query_handlers[query_type] = handler
    
    def add_middleware(self, middleware: Callable):
        """Add middleware to the message bus."""
        self._middleware.append(middleware)
    
    def send_command(self, command: Command) -> Any:
        """Send a command."""
        command_type = type(command)
        
        if command_type not in self._command_handlers:
            raise ValueError(f"No handler registered for command {command_type.__name__}")
        
        handler = self._command_handlers[command_type]
        
        # Apply middleware
        result = command
        for middleware in self._middleware:
            result = middleware(result, handler.handle) or result
        
        if result is command:  # No middleware intercepted
            return handler.handle(command)
        else:
            return result
    
    def send_query(self, query: Query) -> Any:
        """Send a query."""
        query_type = type(query)
        
        if query_type not in self._query_handlers:
            raise ValueError(f"No handler registered for query {query_type.__name__}")
        
        handler = self._query_handlers[query_type]
        return handler.handle(query)

# Microservices Architecture Simulation
class ServiceRegistry:
    """Service registry for microservices."""
    
    def __init__(self):
        """Initialize service registry."""
        self._services = {}
        self._health_checks = {}
        self._load_balancers = defaultdict(list)
    
    def register_service(self, service_name: str, service_instance: Any, 
                        health_check: Callable = None):
        """Register a service instance."""
        if service_name not in self._services:
            self._services[service_name] = []
        
        service_info = {
            'instance': service_instance,
            'id': str(uuid.uuid4()),
            'registered_at': datetime.now(),
            'last_heartbeat': datetime.now()
        }
        
        self._services[service_name].append(service_info)
        
        if health_check:
            self._health_checks[service_info['id']] = health_check
        
        print(f"Registered service: {service_name} (ID: {service_info['id']})")
        return service_info['id']
    
    def discover_service(self, service_name: str) -> Optional[Any]:
        """Discover a healthy service instance."""
        if service_name not in self._services:
            return None
        
        healthy_services = []
        for service_info in self._services[service_name]:
            service_id = service_info['id']
            if service_id in self._health_checks:
                try:
                    if self._health_checks[service_id]():
                        healthy_services.append(service_info)
                except Exception:
                    continue  # Service is unhealthy
            else:
                healthy_services.append(service_info)  # No health check, assume healthy
        
        if not healthy_services:
            return None
        
        # Simple round-robin load balancing
        if service_name not in self._load_balancers:
            self._load_balancers[service_name] = [0]
        
        index = self._load_balancers[service_name][0] % len(healthy_services)
        self._load_balancers[service_name][0] = (index + 1) % len(healthy_services)
        
        selected_service = healthy_services[index]
        selected_service['last_heartbeat'] = datetime.now()
        
        return selected_service['instance']
    
    def get_all_services(self, service_name: str) -> List[Any]:
        """Get all instances of a service."""
        if service_name not in self._services:
            return []
        
        return [info['instance'] for info in self._services[service_name]]
    
    def unregister_service(self, service_name: str, service_id: str):
        """Unregister a service instance."""
        if service_name in self._services:
            self._services[service_name] = [
                info for info in self._services[service_name] 
                if info['id'] != service_id
            ]
        
        if service_id in self._health_checks:
            del self._health_checks[service_id]

class ServiceProxy:
    """Proxy for calling remote services."""
    
    def __init__(self, service_registry: ServiceRegistry, service_name: str):
        """Initialize service proxy."""
        self.service_registry = service_registry
        self.service_name = service_name
        self._circuit_breaker = CircuitBreaker()
    
    def call_method(self, method_name: str, *args, **kwargs) -> Any:
        """Call a method on the remote service."""
        def _call():
            service = self.service_registry.discover_service(self.service_name)
            if service is None:
                raise ConnectionError(f"No healthy instances of {self.service_name} available")
            
            method = getattr(service, method_name)
            return method(*args, **kwargs)
        
        return self._circuit_breaker.call(_call)

class CircuitBreaker:
    """Circuit breaker pattern implementation."""
    
    def __init__(self, failure_threshold: int = 5, timeout: int = 60):
        """Initialize circuit breaker."""
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
    
    def call(self, func: Callable) -> Any:
        """Execute function with circuit breaker."""
        if self.state == "OPEN":
            if self._should_attempt_reset():
                self.state = "HALF_OPEN"
            else:
                raise ConnectionError("Circuit breaker is OPEN")
        
        try:
            result = func()
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise
    
    def _should_attempt_reset(self) -> bool:
        """Check if circuit breaker should attempt reset."""
        return (self.last_failure_time and 
                datetime.now() - self.last_failure_time > timedelta(seconds=self.timeout))
    
    def _on_success(self):
        """Handle successful call."""
        self.failure_count = 0
        self.state = "CLOSED"
    
    def _on_failure(self):
        """Handle failed call."""
        self.failure_count += 1
        self.last_failure_time = datetime.now()
        
        if self.failure_count >= self.failure_threshold:
            self.state = "OPEN"

# Distributed Object Patterns
class RemoteObjectProxy:
    """Proxy for remote objects."""
    
    def __init__(self, target_id: str, object_registry: 'DistributedObjectRegistry'):
        """Initialize remote object proxy."""
        self.target_id = target_id
        self.object_registry = object_registry
        self._cache = {}
        self._cache_timeout = 30  # seconds
    
    def __getattr__(self, name: str) -> Any:
        """Handle attribute access."""
        # Check cache first
        cache_key = f"{self.target_id}.{name}"
        if cache_key in self._cache:
            cached_value, timestamp = self._cache[cache_key]
            if datetime.now() - timestamp < timedelta(seconds=self._cache_timeout):
                return cached_value
        
        # Get remote attribute
        result = self.object_registry.call_remote_method(self.target_id, '__getattribute__', name)
        
        # Cache result if it's not callable
        if not callable(result):
            self._cache[cache_key] = (result, datetime.now())
        
        return result
    
    def __call__(self, *args, **kwargs) -> Any:
        """Handle method calls."""
        return self.object_registry.call_remote_method(self.target_id, '__call__', *args, **kwargs)

class DistributedObjectRegistry:
    """Registry for distributed objects."""
    
    def __init__(self):
        """Initialize distributed object registry."""
        self._objects = {}
        self._proxies = {}
        self._serializers = {
            'json': (json.dumps, json.loads),
            'pickle': (pickle.dumps, pickle.loads)
        }
        self._default_serializer = 'pickle'
    
    def register_object(self, obj: Any, object_id: str = None) -> str:
        """Register an object for distributed access."""
        if object_id is None:
            object_id = str(uuid.uuid4())
        
        self._objects[object_id] = {
            'object': obj,
            'registered_at': datetime.now(),
            'access_count': 0
        }
        
        print(f"Registered object: {object_id} ({type(obj).__name__})")
        return object_id
    
    def create_proxy(self, object_id: str) -> RemoteObjectProxy:
        """Create a proxy for a remote object."""
        if object_id not in self._objects:
            raise ValueError(f"Object {object_id} not found")
        
        proxy = RemoteObjectProxy(object_id, self)
        self._proxies[object_id] = proxy
        return proxy
    
    def call_remote_method(self, object_id: str, method_name: str, *args, **kwargs) -> Any:
        """Call a method on a remote object."""
        if object_id not in self._objects:
            raise ValueError(f"Object {object_id} not found")
        
        obj_info = self._objects[object_id]
        obj = obj_info['object']
        obj_info['access_count'] += 1
        
        # Serialize arguments (simulate network transfer)
        serializer = self._serializers[self._default_serializer]
        serialized_args = serializer[0]((args, kwargs))
        deserialized_args, deserialized_kwargs = serializer[1](serialized_args)
        
        # Call method
        if method_name == '__getattribute__':
            result = getattr(obj, deserialized_args[0])
        elif method_name == '__call__':
            result = obj(*deserialized_args, **deserialized_kwargs)
        else:
            method = getattr(obj, method_name)
            result = method(*deserialized_args, **deserialized_kwargs)
        
        # Serialize result (simulate network transfer)
        try:
            serialized_result = serializer[0](result)
            return serializer[1](serialized_result)
        except (TypeError, pickle.PicklingError):
            # Can't serialize, return a new proxy
            if hasattr(result, '__dict__'):
                result_id = self.register_object(result)
                return self.create_proxy(result_id)
            else:
                return str(result)  # Fallback to string representation
    
    def get_object_stats(self, object_id: str) -> Dict[str, Any]:
        """Get statistics for an object."""
        if object_id not in self._objects:
            raise ValueError(f"Object {object_id} not found")
        
        obj_info = self._objects[object_id]
        return {
            'object_id': object_id,
            'object_type': type(obj_info['object']).__name__,
            'registered_at': obj_info['registered_at'],
            'access_count': obj_info['access_count']
        }

# Enterprise Patterns Implementation
class SagaOrchestrator:
    """Saga pattern for distributed transactions."""
    
    def __init__(self):
        """Initialize saga orchestrator."""
        self._sagas = {}
        self._compensations = defaultdict(list)
        self._step_results = defaultdict(list)
    
    def start_saga(self, saga_id: str, steps: List[Tuple[Callable, Callable]]) -> str:
        """Start a new saga."""
        if saga_id is None:
            saga_id = str(uuid.uuid4())
        
        self._sagas[saga_id] = {
            'steps': steps,
            'current_step': 0,
            'status': 'RUNNING',
            'started_at': datetime.now(),
            'completed_steps': []
        }
        
        return saga_id
    
    def execute_saga(self, saga_id: str) -> bool:
        """Execute a saga."""
        if saga_id not in self._sagas:
            raise ValueError(f"Saga {saga_id} not found")
        
        saga = self._sagas[saga_id]
        steps = saga['steps']
        
        try:
            # Execute steps
            for i, (step_func, compensation_func) in enumerate(steps):
                if i < saga['current_step']:
                    continue  # Skip already completed steps
                
                print(f"Executing saga step {i + 1}/{len(steps)}")
                result = step_func()
                
                saga['completed_steps'].append({
                    'step_index': i,
                    'result': result,
                    'completed_at': datetime.now()
                })
                
                self._compensations[saga_id].append(compensation_func)
                saga['current_step'] = i + 1
            
            saga['status'] = 'COMPLETED'
            return True
        
        except Exception as e:
            print(f"Saga step failed: {e}")
            saga['status'] = 'FAILED'
            self._compensate(saga_id)
            return False
    
    def _compensate(self, saga_id: str):
        """Execute compensation actions for a failed saga."""
        print(f"Compensating saga {saga_id}")
        compensations = self._compensations[saga_id]
        
        # Execute compensations in reverse order
        for compensation in reversed(compensations):
            try:
                compensation()
            except Exception as e:
                print(f"Compensation failed: {e}")
        
        self._sagas[saga_id]['status'] = 'COMPENSATED'

class RetryPolicy:
    """Retry policy implementation."""
    
    def __init__(self, max_attempts: int = 3, delay: float = 1.0, 
                 backoff_factor: float = 2.0, exceptions: Tuple = (Exception,)):
        """Initialize retry policy."""
        self.max_attempts = max_attempts
        self.delay = delay
        self.backoff_factor = backoff_factor
        self.exceptions = exceptions
    
    def execute(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function with retry policy."""
        last_exception = None
        
        for attempt in range(self.max_attempts):
            try:
                return func(*args, **kwargs)
            except self.exceptions as e:
                last_exception = e
                if attempt < self.max_attempts - 1:
                    sleep_time = self.delay * (self.backoff_factor ** attempt)
                    print(f"Attempt {attempt + 1} failed, retrying in {sleep_time}s...")
                    time.sleep(sleep_time)
                else:
                    print(f"All {self.max_attempts} attempts failed")
        
        raise last_exception

class BulkheadPattern:
    """Bulkhead pattern for resource isolation."""
    
    def __init__(self, pool_name: str, max_workers: int = 5):
        """Initialize bulkhead."""
        self.pool_name = pool_name
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.active_tasks = 0
        self.max_workers = max_workers
    
    def execute(self, func: Callable, *args, **kwargs) -> Future:
        """Execute function in isolated thread pool."""
        if self.active_tasks >= self.max_workers:
            raise ResourceWarning(f"Bulkhead {self.pool_name} at capacity")
        
        self.active_tasks += 1
        
        def wrapped_func():
            try:
                return func(*args, **kwargs)
            finally:
                self.active_tasks -= 1
        
        return self.executor.submit(wrapped_func)
    
    def shutdown(self):
        """Shutdown the bulkhead."""
        self.executor.shutdown(wait=True)

# Example usage and comprehensive tests
@Injectable(scope=Scope.SINGLETON)
class UserRepository:
    """User repository service."""
    
    def __init__(self, database_connection: 'DatabaseConnection'):
        """Initialize user repository."""
        self.db = database_connection
        self.users = {}
    
    def save_user(self, user_id: str, user_data: Dict[str, Any]):
        """Save a user."""
        self.users[user_id] = user_data
        return f"User {user_id} saved to {self.db.connection_string}"
    
    def get_user(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get a user."""
        return self.users.get(user_id)

@Injectable(scope=Scope.SINGLETON)
class DatabaseConnection:
    """Database connection service."""
    
    def __init__(self):
        """Initialize database connection."""
        self.connection_string = "postgresql://localhost:5432/enterprise_db"
        self.is_connected = True
        print(f"Database connected: {self.connection_string}")
    
    def dispose(self):
        """Dispose of connection."""
        self.is_connected = False
        print("Database connection disposed")

class UserCreatedEvent(Event):
    """User created event."""
    
    def __init__(self, user_id: str, user_data: Dict[str, Any]):
        """Initialize user created event."""
        super().__init__(
            event_type="UserCreated",
            data={'user_id': user_id, 'user_data': user_data}
        )

class UserAggregate(AggregateRoot):
    """User aggregate for event sourcing."""
    
    def __init__(self, aggregate_id: str = None):
        """Initialize user aggregate."""
        super().__init__(aggregate_id)
        self.user_data = {}
        self.is_active = False
    
    def create_user(self, user_data: Dict[str, Any]):
        """Create a new user."""
        event = UserCreatedEvent(self.aggregate_id, user_data)
        self.apply_event(event)
    
    def _handle_usercreated(self, event: Event):
        """Handle user created event."""
        self.user_data = event.data['user_data']
        self.is_active = True

def create_dependency_injection_system():
    """Demonstrate dependency injection system."""
    print("=== Dependency Injection System ===")
    
    # Create container
    container = DependencyInjectionContainer()
    
    # Register services
    container.register(DatabaseConnection, DatabaseConnection, Scope.SINGLETON)
    container.register(UserRepository, UserRepository, Scope.SINGLETON)
    
    # Add logging decorator
    def logging_decorator(instance):
        original_class = instance.__class__
        
        class LoggingWrapper:
            def __init__(self, wrapped_instance):
                self._wrapped = wrapped_instance
            
            def __getattr__(self, name):
                attr = getattr(self._wrapped, name)
                if callable(attr):
                    def logged_method(*args, **kwargs):
                        print(f"[LOG] Calling {original_class.__name__}.{name}")
                        result = attr(*args, **kwargs)
                        print(f"[LOG] Completed {original_class.__name__}.{name}")
                        return result
                    return logged_method
                return attr
        
        return LoggingWrapper(instance)
    
    container.add_decorator(logging_decorator)
    
    # Resolve services
    user_repo = container.resolve(UserRepository)
    db_conn = container.resolve(DatabaseConnection)
    
    print(f"Resolved UserRepository: {type(user_repo)}")
    print(f"Database connection: {db_conn.connection_string}")
    
    # Practice service calls
    result = user_repo.save_user("user123", {"name": "Alice", "email": "alice@example.com"})
    print(f"Save result: {result}")
    
    user = user_repo.get_user("user123")
    print(f"Retrieved user: {user}")
    
    # Practice scoped dependencies
    with container.create_scope():
        scoped_repo = container.resolve(UserRepository)
        print(f"Scoped repository: {type(scoped_repo)}")
    
    container.dispose()
    return container

def implement_event_sourcing():
    """Demonstrate event sourcing system."""
    print("\n=== Event Sourcing System ===")
    
    # Create event store
    event_store = EventStore()
    
    # Subscribe to events
    def user_created_handler(event: Event):
        print(f"[HANDLER] User created: {event.data['user_id']}")
    
    def all_events_logger(event: Event):
        print(f"[LOG] Event: {event.event_type} for aggregate {event.aggregate_id}")
    
    event_store.subscribe("UserCreated", user_created_handler)
    event_store.subscribe_all(all_events_logger)
    
    # Create user aggregate
    user_aggregate = UserAggregate("user123")
    user_aggregate.create_user({"name": "Bob", "email": "bob@example.com"})
    
    # Save events
    uncommitted_events = user_aggregate.get_uncommitted_events()
    event_store.append_events(user_aggregate.aggregate_id, uncommitted_events)
    user_aggregate.mark_events_as_committed()
    
    print(f"User aggregate state: {user_aggregate.user_data}")
    print(f"User is active: {user_aggregate.is_active}")
    
    # Load from history
    new_aggregate = UserAggregate("user123")
    events = event_store.get_events("user123")
    new_aggregate.load_from_history(events)
    
    print(f"Loaded aggregate state: {new_aggregate.user_data}")
    
    # Save snapshot
    event_store.save_snapshot("user123", new_aggregate.user_data, new_aggregate.version)
    
    return event_store, user_aggregate

def build_microservices_architecture():
    """Demonstrate microservices architecture."""
    print("\n=== Microservices Architecture ===")
    
    # Create service registry
    registry = ServiceRegistry()
    
    # Create services
    class OrderService:
        def __init__(self, service_id: str):
            self.service_id = service_id
            self.processed_orders = 0
        
        def create_order(self, order_data: Dict[str, Any]) -> str:
            self.processed_orders += 1
            order_id = f"order_{self.processed_orders}_{self.service_id}"
            print(f"[{self.service_id}] Created order: {order_id}")
            return order_id
        
        def get_order(self, order_id: str) -> Dict[str, Any]:
            return {"order_id": order_id, "status": "created", "service": self.service_id}
        
        def health_check(self) -> bool:
            return True
    
    class PaymentService:
        def __init__(self, service_id: str):
            self.service_id = service_id
            self.is_healthy = True
        
        def process_payment(self, order_id: str, amount: float) -> str:
            if not self.is_healthy:
                raise Exception("Payment service is down")
            
            payment_id = f"payment_{order_id}_{self.service_id}"
            print(f"[{self.service_id}] Processed payment: {payment_id} (${amount})")
            return payment_id
        
        def health_check(self) -> bool:
            return self.is_healthy
    
    # Register service instances
    order_service1 = OrderService("order-1")
    order_service2 = OrderService("order-2")
    payment_service1 = PaymentService("payment-1")
    
    registry.register_service("order-service", order_service1, order_service1.health_check)
    registry.register_service("order-service", order_service2, order_service2.health_check)
    registry.register_service("payment-service", payment_service1, payment_service1.health_check)
    
    # Create service proxies
    order_proxy = ServiceProxy(registry, "order-service")
    payment_proxy = ServiceProxy(registry, "payment-service")
    
    # Practice load balancing
    print("\nTesting load balancing:")
    for i in range(4):
        order_id = order_proxy.call_method("create_order", {"item": f"item_{i}"})
        order_details = order_proxy.call_method("get_order", order_id)
        print(f"  Order details: {order_details}")
    
    # Practice payment processing
    print("\nTesting payment processing:")
    try:
        payment_id = payment_proxy.call_method("process_payment", "order_123", 99.99)
        print(f"  Payment successful: {payment_id}")
    except Exception as e:
        print(f"  Payment failed: {e}")
    
    # Practice circuit breaker
    print("\nTesting circuit breaker (simulating failures):")
    payment_service1.is_healthy = False
    
    for i in range(7):  # Should trigger circuit breaker
        try:
            payment_proxy.call_method("process_payment", f"order_{i}", 50.0)
        except Exception as e:
            print(f"  Attempt {i + 1}: {e}")
    
    return registry, [order_proxy, payment_proxy]

def create_distributed_objects():
    """Demonstrate distributed object patterns."""
    print("\n=== Distributed Objects ===")
    
    # Create distributed object registry
    registry = DistributedObjectRegistry()
    
    # Create objects to distribute
    class CalculatorService:
        def __init__(self):
            self.history = []
        
        def add(self, a: float, b: float) -> float:
            result = a + b
            self.history.append(f"add({a}, {b}) = {result}")
            return result
        
        def multiply(self, a: float, b: float) -> float:
            result = a * b
            self.history.append(f"multiply({a}, {b}) = {result}")
            return result
        
        def get_history(self) -> List[str]:
            return self.history.copy()
    
    class DataProcessor:
        def __init__(self, name: str):
            self.name = name
            self.processed_items = 0
        
        def process_data(self, data: List[Any]) -> Dict[str, Any]:
            self.processed_items += len(data)
            return {
                "processor": self.name,
                "items_processed": len(data),
                "total_processed": self.processed_items,
                "summary": f"Processed {len(data)} items"
            }
    
    # Register objects
    calc_service = CalculatorService()
    data_processor = DataProcessor("processor-1")
    
    calc_id = registry.register_object(calc_service)
    processor_id = registry.register_object(data_processor)
    
    # Create proxies
    calc_proxy = registry.create_proxy(calc_id)
    processor_proxy = registry.create_proxy(processor_id)
    
    # Practice remote method calls
    print("Testing remote calculator:")
    result1 = calc_proxy.add(10, 20)
    result2 = calc_proxy.multiply(5, 6)
    history = calc_proxy.get_history()
    
    print(f"  10 + 20 = {result1}")
    print(f"  5 * 6 = {result2}")
    print(f"  History: {history}")
    
    print("\nTesting remote data processor:")
    test_data = [1, 2, 3, 4, 5]
    result = processor_proxy.process_data(test_data)
    print(f"  Processing result: {result}")
    
    # Show object statistics
    calc_stats = registry.get_object_stats(calc_id)
    processor_stats = registry.get_object_stats(processor_id)
    
    print(f"\nObject statistics:")
    print(f"  Calculator: {calc_stats}")
    print(f"  Processor: {processor_stats}")
    
    return registry, [calc_proxy, processor_proxy]

def implement_enterprise_patterns():
    """Demonstrate enterprise patterns."""
    print("\n=== Enterprise Patterns ===")
    
    # Practice Saga pattern
    print("1. Saga Pattern:")
    saga_orchestrator = SagaOrchestrator()
    
    # Simulate distributed transaction steps
    order_created = False
    payment_processed = False
    inventory_reserved = False
    
    def create_order():
        global order_created
        print("  Creating order...")
        order_created = True
        return "order_123"
    
    def process_payment():
        global payment_processed
        print("  Processing payment...")
        payment_processed = True
        return "payment_456"
    
    def reserve_inventory():
        global inventory_reserved
        print("  Reserving inventory...")
        inventory_reserved = True
        return "reservation_789"
    
    def compensate_order():
        global order_created
        print("  Compensating order...")
        order_created = False
    
    def compensate_payment():
        global payment_processed
        print("  Compensating payment...")
        payment_processed = False
    
    def compensate_inventory():
        global inventory_reserved
        print("  Compensating inventory...")
        inventory_reserved = False
    
    # Execute successful saga
    saga_steps = [
        (create_order, compensate_order),
        (process_payment, compensate_payment),
        (reserve_inventory, compensate_inventory)
    ]
    
    saga_id = saga_orchestrator.start_saga("order_saga_1", saga_steps)
    success = saga_orchestrator.execute_saga(saga_id)
    print(f"  Saga completed successfully: {success}")
    
    # Practice Retry pattern
    print("\n2. Retry Pattern:")
    retry_policy = RetryPolicy(max_attempts=3, delay=0.1)
    
    attempt_count = 0
    def unreliable_service():
        global attempt_count
        attempt_count += 1
        if attempt_count < 3:
            raise ConnectionError(f"Service unavailable (attempt {attempt_count})")
        return "Service call successful!"
    
    try:
        result = retry_policy.execute(unreliable_service)
        print(f"  Retry result: {result}")
    except Exception as e:
        print(f"  Retry failed: {e}")
    
    # Practice Bulkhead pattern
    print("\n3. Bulkhead Pattern:")
    bulkhead = BulkheadPattern("api_pool", max_workers=3)
    
    def cpu_intensive_task(task_id: int) -> str:
        time.sleep(0.1)  # Simulate work
        return f"Task {task_id} completed"
    
    # Submit tasks
    futures = []
    for i in range(5):
        try:
            future = bulkhead.execute(cpu_intensive_task, i)
            futures.append(future)
            print(f"  Submitted task {i}")
        except ResourceWarning as e:
            print(f"  {e}")
    
    # Wait for results
    for i, future in enumerate(futures):
        result = future.result()
        print(f"  {result}")
    
    bulkhead.shutdown()
    
    return saga_orchestrator, retry_policy, bulkhead

# Comprehensive test execution
if __name__ == "__main__":
    # Practice dependency injection
    di_results = create_dependency_injection_system()
    
    # Practice event sourcing
    es_results = implement_event_sourcing()
    
    # Practice microservices architecture
    ms_results = build_microservices_architecture()
    
    # Practice distributed objects
    do_results = create_distributed_objects()
    
    # Practice enterprise patterns
    ep_results = implement_enterprise_patterns()
    
    print("\n" + "="*60)
    print("=== ENTERPRISE OOP ARCHITECTURE COMPLETE ===")
    print("="*60)
    print("✓ Dependency Injection - IoC container with multiple scopes")
    print("✓ Event Sourcing - Event store with snapshots and projections")
    print("✓ Microservices - Service registry with load balancing")
    print("✓ Distributed Objects - Remote proxies with caching")
    print("✓ Enterprise Patterns - Saga, circuit breaker, retry, bulkhead")
    print("✓ CQRS - Command/query separation with message bus")
    print("✓ Advanced OOP - Metaclasses, proxies, and decorators")
    print("\nThis system demonstrates enterprise-level architecture")
    print("patterns suitable for large-scale distributed applications!")
```

## Hints

- Use metaclasses for framework-level functionality like DI containers
- Event sourcing requires careful event versioning and schema evolution
- Circuit breakers prevent cascade failures in distributed systems
- Saga pattern ensures data consistency across microservices
- Proxy patterns enable transparent remote object access

## Practice Cases

Your enterprise system should:

- DI Container: Resolve dependencies with proper scope management
- Event Store: Store/replay events with snapshot support
- Service Registry: Discover services with health checks and load balancing
- Distributed Objects: Provide transparent remote method calls
- Enterprise Patterns: Implement saga, circuit breaker, retry, and bulkhead

## Bonus Challenge

Add distributed caching, message queues, distributed locks, and a complete monitoring/logging system with metrics collection!