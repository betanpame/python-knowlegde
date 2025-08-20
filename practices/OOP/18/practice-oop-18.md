# Design Patterns Implementation - Practice 18

**Difficulty:** ⭐⭐⭐⭐ (Medium-Hard)

## Description

Implement classic design patterns using Python's object-oriented features. Learn Singleton, Factory, Observer, Strategy, and Decorator patterns.

## Objectives

- Implement Singleton pattern for unique instances
- Create Factory patterns for object creation
- Build Observer pattern for event handling
- Implement Strategy pattern for algorithm selection
- Use Decorator pattern for behavior extension

## Your Tasks

1. **implement_singleton_pattern()** - Create thread-safe Singleton
2. **create_factory_patterns()** - Implement Abstract Factory
3. **build_observer_pattern()** - Create event notification system
4. **implement_strategy_pattern()** - Build algorithm selection system
5. **create_decorator_pattern()** - Implement behavior decoration

## Example

```python
import threading
import time
import abc
from typing import List, Dict, Any, Callable, Protocol
from enum import Enum
from dataclasses import dataclass
from datetime import datetime
import weakref

# Singleton Pattern Implementation
class SingletonMeta(type):
    """Thread-safe Singleton metaclass."""
    
    _instances = {}
    _lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        """Create or return existing instance."""
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    """Singleton database connection."""
    
    def __init__(self):
        """Initialize database connection (only called once)."""
        if hasattr(self, 'initialized'):
            return
        
        self.initialized = True
        self.connection_id = id(self)
        self.queries_executed = 0
        self.connected_at = datetime.now()
        print(f"Database connection established: {self.connection_id}")
    
    def execute_query(self, query: str) -> str:
        """Execute a database query."""
        self.queries_executed += 1
        return f"Query executed: {query} (Total: {self.queries_executed})"
    
    def get_stats(self) -> Dict[str, Any]:
        """Get connection statistics."""
        return {
            'connection_id': self.connection_id,
            'queries_executed': self.queries_executed,
            'connected_at': self.connected_at,
            'uptime': datetime.now() - self.connected_at
        }

class ConfigManager(metaclass=SingletonMeta):
    """Singleton configuration manager."""
    
    def __init__(self):
        """Initialize configuration."""
        if hasattr(self, 'initialized'):
            return
        
        self.initialized = True
        self._config = {
            'database_url': 'localhost:5432',
            'api_key': 'secret-key-123',
            'debug_mode': True,
            'max_connections': 100
        }
        print("Configuration manager initialized")
    
    def get(self, key: str, default=None):
        """Get configuration value."""
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set configuration value."""
        self._config[key] = value
    
    def get_all(self) -> Dict[str, Any]:
        """Get all configuration."""
        return self._config.copy()

# Factory Pattern Implementation
class VehicleType(Enum):
    """Vehicle types for factory."""
    CAR = "car"
    MOTORCYCLE = "motorcycle"
    TRUCK = "truck"

class Vehicle(abc.ABC):
    """Abstract vehicle class."""
    
    def __init__(self, make: str, model: str):
        """Initialize vehicle."""
        self.make = make
        self.model = model
        self.created_at = datetime.now()
    
    @abc.abstractmethod
    def start_engine(self) -> str:
        """Start the vehicle engine."""
        pass
    
    @abc.abstractmethod
    def get_max_speed(self) -> int:
        """Get maximum speed in mph."""
        pass
    
    @abc.abstractmethod
    def get_fuel_efficiency(self) -> float:
        """Get fuel efficiency in mpg."""
        pass
    
    def get_info(self) -> str:
        """Get vehicle information."""
        return f"{self.make} {self.model}"

class Car(Vehicle):
    """Car implementation."""
    
    def __init__(self, make: str, model: str, doors: int = 4):
        """Initialize car."""
        super().__init__(make, model)
        self.doors = doors
    
    def start_engine(self) -> str:
        """Start car engine."""
        return f"Car engine started: {self.get_info()}"
    
    def get_max_speed(self) -> int:
        """Get car max speed."""
        return 120
    
    def get_fuel_efficiency(self) -> float:
        """Get car fuel efficiency."""
        return 25.0

class Motorcycle(Vehicle):
    """Motorcycle implementation."""
    
    def __init__(self, make: str, model: str, engine_size: int = 600):
        """Initialize motorcycle."""
        super().__init__(make, model)
        self.engine_size = engine_size
    
    def start_engine(self) -> str:
        """Start motorcycle engine."""
        return f"Motorcycle engine roared: {self.get_info()}"
    
    def get_max_speed(self) -> int:
        """Get motorcycle max speed."""
        return 180
    
    def get_fuel_efficiency(self) -> float:
        """Get motorcycle fuel efficiency."""
        return 45.0

class Truck(Vehicle):
    """Truck implementation."""
    
    def __init__(self, make: str, model: str, payload_capacity: int = 2000):
        """Initialize truck."""
        super().__init__(make, model)
        self.payload_capacity = payload_capacity
    
    def start_engine(self) -> str:
        """Start truck engine."""
        return f"Truck engine rumbled: {self.get_info()}"
    
    def get_max_speed(self) -> int:
        """Get truck max speed."""
        return 80
    
    def get_fuel_efficiency(self) -> float:
        """Get truck fuel efficiency."""
        return 12.0

class VehicleFactory:
    """Factory for creating vehicles."""
    
    @staticmethod
    def create_vehicle(vehicle_type: VehicleType, make: str, model: str, **kwargs) -> Vehicle:
        """Create vehicle based on type."""
        if vehicle_type == VehicleType.CAR:
            return Car(make, model, **kwargs)
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle(make, model, **kwargs)
        elif vehicle_type == VehicleType.TRUCK:
            return Truck(make, model, **kwargs)
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

class VehicleRegistry:
    """Registry for managing vehicle creation with additional features."""
    
    def __init__(self):
        """Initialize vehicle registry."""
        self._creators = {}
        self._vehicles = []
    
    def register_creator(self, vehicle_type: VehicleType, creator: Callable):
        """Register a vehicle creator function."""
        self._creators[vehicle_type] = creator
    
    def create_vehicle(self, vehicle_type: VehicleType, **kwargs) -> Vehicle:
        """Create vehicle using registered creator."""
        if vehicle_type not in self._creators:
            raise ValueError(f"No creator registered for {vehicle_type}")
        
        vehicle = self._creators[vehicle_type](**kwargs)
        self._vehicles.append(vehicle)
        return vehicle
    
    def get_all_vehicles(self) -> List[Vehicle]:
        """Get all created vehicles."""
        return self._vehicles.copy()

# Observer Pattern Implementation
class Observer(abc.ABC):
    """Abstract observer interface."""
    
    @abc.abstractmethod
    def update(self, subject: 'Subject', event_type: str, data: Any):
        """Handle notification from subject."""
        pass

class Subject:
    """Subject that can be observed."""
    
    def __init__(self):
        """Initialize subject."""
        self._observers = weakref.WeakSet()
    
    def attach(self, observer: Observer):
        """Attach an observer."""
        self._observers.add(observer)
    
    def detach(self, observer: Observer):
        """Detach an observer."""
        self._observers.discard(observer)
    
    def notify(self, event_type: str, data: Any = None):
        """Notify all observers."""
        for observer in self._observers:
            try:
                observer.update(self, event_type, data)
            except Exception as e:
                print(f"Error notifying observer: {e}")

class StockPrice(Subject):
    """Stock price that can be observed."""
    
    def __init__(self, symbol: str, initial_price: float):
        """Initialize stock price."""
        super().__init__()
        self.symbol = symbol
        self._price = initial_price
        self.history = [(datetime.now(), initial_price)]
    
    @property
    def price(self) -> float:
        """Get current price."""
        return self._price
    
    @price.setter
    def price(self, new_price: float):
        """Set new price and notify observers."""
        old_price = self._price
        self._price = new_price
        self.history.append((datetime.now(), new_price))
        
        # Determine event type
        if new_price > old_price:
            event_type = "price_increase"
        elif new_price < old_price:
            event_type = "price_decrease"
        else:
            event_type = "price_unchanged"
        
        self.notify(event_type, {
            'old_price': old_price,
            'new_price': new_price,
            'change': new_price - old_price,
            'change_percent': ((new_price - old_price) / old_price) * 100
        })

class StockAlert(Observer):
    """Observer that alerts on stock price changes."""
    
    def __init__(self, name: str, threshold_percent: float = 5.0):
        """Initialize stock alert."""
        self.name = name
        self.threshold_percent = threshold_percent
        self.alerts_sent = 0
    
    def update(self, subject: StockPrice, event_type: str, data: Dict[str, Any]):
        """Handle stock price updates."""
        if abs(data['change_percent']) >= self.threshold_percent:
            direction = "increased" if data['change'] > 0 else "decreased"
            self.alerts_sent += 1
            print(f"ALERT ({self.name}): {subject.symbol} {direction} by "
                  f"{abs(data['change_percent']):.2f}% to ${data['new_price']:.2f}")

class StockLogger(Observer):
    """Observer that logs all stock price changes."""
    
    def __init__(self):
        """Initialize stock logger."""
        self.log_entries = []
    
    def update(self, subject: StockPrice, event_type: str, data: Dict[str, Any]):
        """Log stock price updates."""
        entry = {
            'timestamp': datetime.now(),
            'symbol': subject.symbol,
            'event_type': event_type,
            'old_price': data['old_price'],
            'new_price': data['new_price'],
            'change': data['change']
        }
        self.log_entries.append(entry)

# Strategy Pattern Implementation
class SortingStrategy(abc.ABC):
    """Abstract sorting strategy."""
    
    @abc.abstractmethod
    def sort(self, data: List[Any]) -> List[Any]:
        """Sort the data."""
        pass
    
    @abc.abstractmethod
    def get_name(self) -> str:
        """Get strategy name."""
        pass

class BubbleSortStrategy(SortingStrategy):
    """Bubble sort implementation."""
    
    def sort(self, data: List[Any]) -> List[Any]:
        """Sort using bubble sort."""
        data = data.copy()
        n = len(data)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        
        return data
    
    def get_name(self) -> str:
        """Get strategy name."""
        return "Bubble Sort"

class QuickSortStrategy(SortingStrategy):
    """Quick sort implementation."""
    
    def sort(self, data: List[Any]) -> List[Any]:
        """Sort using quick sort."""
        if len(data) <= 1:
            return data.copy()
        
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        
        return self.sort(left) + middle + self.sort(right)
    
    def get_name(self) -> str:
        """Get strategy name."""
        return "Quick Sort"

class PythonSortStrategy(SortingStrategy):
    """Python built-in sort implementation."""
    
    def sort(self, data: List[Any]) -> List[Any]:
        """Sort using Python's built-in sort."""
        return sorted(data)
    
    def get_name(self) -> str:
        """Get strategy name."""
        return "Python Built-in Sort"

class SortingContext:
    """Context for sorting strategies."""
    
    def __init__(self, strategy: SortingStrategy = None):
        """Initialize sorting context."""
        self._strategy = strategy or PythonSortStrategy()
        self.sort_history = []
    
    def set_strategy(self, strategy: SortingStrategy):
        """Set the sorting strategy."""
        self._strategy = strategy
    
    def sort_data(self, data: List[Any]) -> List[Any]:
        """Sort data using current strategy."""
        start_time = time.perf_counter()
        result = self._strategy.sort(data)
        end_time = time.perf_counter()
        
        sort_info = {
            'strategy': self._strategy.get_name(),
            'input_size': len(data),
            'execution_time': end_time - start_time,
            'timestamp': datetime.now()
        }
        self.sort_history.append(sort_info)
        
        return result
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """Get performance statistics."""
        if not self.sort_history:
            return {}
        
        by_strategy = {}
        for entry in self.sort_history:
            strategy = entry['strategy']
            if strategy not in by_strategy:
                by_strategy[strategy] = []
            by_strategy[strategy].append(entry['execution_time'])
        
        stats = {}
        for strategy, times in by_strategy.items():
            stats[strategy] = {
                'count': len(times),
                'avg_time': sum(times) / len(times),
                'min_time': min(times),
                'max_time': max(times)
            }
        
        return stats

# Decorator Pattern Implementation
class Component(abc.ABC):
    """Abstract component interface."""
    
    @abc.abstractmethod
    def operation(self) -> str:
        """Perform the component operation."""
        pass
    
    @abc.abstractmethod
    def get_cost(self) -> float:
        """Get component cost."""
        pass

class Coffee(Component):
    """Basic coffee component."""
    
    def operation(self) -> str:
        """Get coffee description."""
        return "Simple Coffee"
    
    def get_cost(self) -> float:
        """Get coffee cost."""
        return 2.00

class CoffeeDecorator(Component):
    """Base decorator for coffee."""
    
    def __init__(self, component: Component):
        """Initialize decorator."""
        self._component = component
    
    def operation(self) -> str:
        """Delegate to component."""
        return self._component.operation()
    
    def get_cost(self) -> float:
        """Delegate to component."""
        return self._component.get_cost()

class MilkDecorator(CoffeeDecorator):
    """Milk decorator."""
    
    def operation(self) -> str:
        """Add milk to description."""
        return f"{self._component.operation()} + Milk"
    
    def get_cost(self) -> float:
        """Add milk cost."""
        return self._component.get_cost() + 0.50

class SugarDecorator(CoffeeDecorator):
    """Sugar decorator."""
    
    def operation(self) -> str:
        """Add sugar to description."""
        return f"{self._component.operation()} + Sugar"
    
    def get_cost(self) -> float:
        """Add sugar cost."""
        return self._component.get_cost() + 0.25

class WhipCreamDecorator(CoffeeDecorator):
    """Whip cream decorator."""
    
    def operation(self) -> str:
        """Add whip cream to description."""
        return f"{self._component.operation()} + Whip Cream"
    
    def get_cost(self) -> float:
        """Add whip cream cost."""
        return self._component.get_cost() + 0.75

class CinnamonDecorator(CoffeeDecorator):
    """Cinnamon decorator."""
    
    def operation(self) -> str:
        """Add cinnamon to description."""
        return f"{self._component.operation()} + Cinnamon"
    
    def get_cost(self) -> float:
        """Add cinnamon cost."""
        return self._component.get_cost() + 0.30

# Example usage and tests
def implement_singleton_pattern():
    """Demonstrate Singleton pattern."""
    print("=== Singleton Pattern ===")
    
    # Practice database connection singleton
    print("1. Database Connection Singleton:")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    print(f"db1 is db2: {db1 is db2}")
    print(f"db1 ID: {id(db1)}")
    print(f"db2 ID: {id(db2)}")
    
    print(db1.execute_query("SELECT * FROM users"))
    print(db2.execute_query("SELECT * FROM products"))
    
    stats = db1.get_stats()
    print(f"Connection stats: {stats}")
    
    # Practice configuration manager singleton
    print("\n2. Configuration Manager Singleton:")
    config1 = ConfigManager()
    config2 = ConfigManager()
    
    print(f"config1 is config2: {config1 is config2}")
    
    config1.set('new_setting', 'test_value')
    print(f"Config from config2: {config2.get('new_setting')}")
    
    return db1, config1

def create_factory_patterns():
    """Demonstrate Factory patterns."""
    print("\n=== Factory Patterns ===")
    
    # Practice simple factory
    print("1. Simple Vehicle Factory:")
    factory = VehicleFactory()
    
    vehicles = [
        factory.create_vehicle(VehicleType.CAR, "Toyota", "Camry", doors=4),
        factory.create_vehicle(VehicleType.MOTORCYCLE, "Honda", "CBR600", engine_size=600),
        factory.create_vehicle(VehicleType.TRUCK, "Ford", "F-150", payload_capacity=2500)
    ]
    
    for vehicle in vehicles:
        print(f"  {vehicle.start_engine()}")
        print(f"    Max Speed: {vehicle.get_max_speed()} mph")
        print(f"    Fuel Efficiency: {vehicle.get_fuel_efficiency()} mpg")
    
    # Practice registry factory
    print("\n2. Registry Factory:")
    registry = VehicleRegistry()
    
    # Register creators
    registry.register_creator(VehicleType.CAR, 
                            lambda **kwargs: Car(kwargs.get('make', 'Generic'), 
                                                kwargs.get('model', 'Car')))
    registry.register_creator(VehicleType.MOTORCYCLE,
                            lambda **kwargs: Motorcycle(kwargs.get('make', 'Generic'),
                                                       kwargs.get('model', 'Bike')))
    
    registry_vehicles = [
        registry.create_vehicle(VehicleType.CAR, make="BMW", model="X5"),
        registry.create_vehicle(VehicleType.MOTORCYCLE, make="Yamaha", model="R1")
    ]
    
    print(f"Registry created {len(registry.get_all_vehicles())} vehicles")
    
    return vehicles, registry

def build_observer_pattern():
    """Demonstrate Observer pattern."""
    print("\n=== Observer Pattern ===")
    
    # Create stock and observers
    stock = StockPrice("AAPL", 150.00)
    
    alert1 = StockAlert("Email Alert", threshold_percent=3.0)
    alert2 = StockAlert("SMS Alert", threshold_percent=5.0)
    logger = StockLogger()
    
    # Attach observers
    stock.attach(alert1)
    stock.attach(alert2)
    stock.attach(logger)
    
    print("1. Stock price changes:")
    
    # Simulate price changes
    price_changes = [152.00, 148.50, 145.00, 147.75, 155.20]
    
    for new_price in price_changes:
        print(f"Setting price to ${new_price:.2f}")
        stock.price = new_price
        time.sleep(0.1)  # Small delay for realism
    
    print(f"\nAlert statistics:")
    print(f"  Email alerts sent: {alert1.alerts_sent}")
    print(f"  SMS alerts sent: {alert2.alerts_sent}")
    print(f"  Log entries: {len(logger.log_entries)}")
    
    return stock, [alert1, alert2, logger]

def implement_strategy_pattern():
    """Demonstrate Strategy pattern."""
    print("\n=== Strategy Pattern ===")
    
    # Create test data
    test_data = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    print(f"Original data: {test_data}")
    
    # Create sorting context
    sorter = SortingContext()
    
    # Practice different strategies
    strategies = [
        BubbleSortStrategy(),
        QuickSortStrategy(),
        PythonSortStrategy()
    ]
    
    results = {}
    for strategy in strategies:
        sorter.set_strategy(strategy)
        sorted_data = sorter.sort_data(test_data)
        results[strategy.get_name()] = sorted_data
        print(f"{strategy.get_name()}: {sorted_data}")
    
    # Show performance stats
    print("\nPerformance Statistics:")
    stats = sorter.get_performance_stats()
    for strategy, stat in stats.items():
        print(f"  {strategy}: {stat['avg_time']:.6f}s avg, {stat['count']} runs")
    
    return sorter, results

def create_decorator_pattern():
    """Demonstrate Decorator pattern."""
    print("\n=== Decorator Pattern ===")
    
    # Create different coffee combinations
    print("1. Building different coffee orders:")
    
    # Simple coffee
    simple_coffee = Coffee()
    print(f"  {simple_coffee.operation()} - ${simple_coffee.get_cost():.2f}")
    
    # Coffee with milk
    milk_coffee = MilkDecorator(Coffee())
    print(f"  {milk_coffee.operation()} - ${milk_coffee.get_cost():.2f}")
    
    # Coffee with multiple decorators
    fancy_coffee = WhipCreamDecorator(
        CinnamonDecorator(
            SugarDecorator(
                MilkDecorator(Coffee())
            )
        )
    )
    print(f"  {fancy_coffee.operation()} - ${fancy_coffee.get_cost():.2f}")
    
    # Another combination
    sweet_coffee = SugarDecorator(
        SugarDecorator(  # Double sugar
            MilkDecorator(Coffee())
        )
    )
    print(f"  {sweet_coffee.operation()} - ${sweet_coffee.get_cost():.2f}")
    
    return [simple_coffee, milk_coffee, fancy_coffee, sweet_coffee]

# Practice all patterns
if __name__ == "__main__":
    # Practice Singleton pattern
    singletons = implement_singleton_pattern()
    
    # Practice Factory patterns
    factory_results = create_factory_patterns()
    
    # Practice Observer pattern
    observer_results = build_observer_pattern()
    
    # Practice Strategy pattern
    strategy_results = implement_strategy_pattern()
    
    # Practice Decorator pattern
    decorator_results = create_decorator_pattern()
    
    print("\n=== Pattern Implementation Complete ===")
    print("All major design patterns demonstrated:")
    print("  ✓ Singleton - Unique instance management")
    print("  ✓ Factory - Object creation abstraction")
    print("  ✓ Observer - Event notification system")
    print("  ✓ Strategy - Algorithm selection")
    print("  ✓ Decorator - Behavior extension")
```

## Hints

- Use metaclasses for thread-safe Singleton implementation
- Make Factory methods return abstract interfaces
- Use weak references in Observer to avoid memory leaks
- Strategy pattern allows runtime algorithm switching
- Decorator pattern builds functionality incrementally

## Practice Cases

Your design patterns should:

- Singleton: Ensure only one instance exists globally
- Factory: Create objects without exposing instantiation logic
- Observer: Notify multiple objects of state changes
- Strategy: Allow algorithm selection at runtime
- Decorator: Add functionality without modifying original classes

## Bonus Challenge

Implement a Command pattern for undo/redo functionality and a Chain of Responsibility pattern for request processing pipeline!