# TODO: Implement OOP classes with inheritance and encapsulation
# Starter code for OOP Practice 1

class Vehicle:
    """Base class for all vehicles."""
    
    def __init__(self, brand, model, year):
        """
        Initialize a vehicle.
        
        Args:
            brand (str): Vehicle brand
            model (str): Vehicle model
            year (int): Manufacturing year
        """
        # Your implementation here
        # Initialize attributes including protected _mileage
        pass
    
    def start(self):
        """Start the vehicle."""
        # Your implementation here
        pass
    
    def stop(self):
        """Stop the vehicle."""
        # Your implementation here
        pass
    
    def get_info(self):
        """Get vehicle information."""
        # Your implementation here
        pass
    
    def __str__(self):
        """String representation of the vehicle."""
        # Your implementation here
        pass

class Car(Vehicle):
    """Car class inheriting from Vehicle."""
    
    def __init__(self, brand, model, year, fuel_type="gasoline", doors=4):
        """
        Initialize a car.
        
        Args:
            brand (str): Car brand
            model (str): Car model
            year (int): Manufacturing year
            fuel_type (str): Type of fuel
            doors (int): Number of doors
        """
        # Your implementation here
        # Use super() to call parent constructor
        pass
    
    def refuel(self):
        """Refuel the car."""
        # Your implementation here
        pass
    
    # Override parent methods as needed

class ElectricCar(Car):
    """Electric car class inheriting from Car."""
    
    def __init__(self, brand, model, year, battery_capacity, doors=4):
        """
        Initialize an electric car.
        
        Args:
            brand (str): Car brand
            model (str): Car model
            year (int): Manufacturing year
            battery_capacity (int): Battery capacity in kWh
            doors (int): Number of doors
        """
        # Your implementation here
        # Call parent constructor with appropriate fuel_type
        pass
    
    def charge(self):
        """Charge the electric car."""
        # Your implementation here
        pass
    
    def get_range(self):
        """Get estimated range based on battery."""
        # Your implementation here
        pass
    
    # Override refuel method since electric cars don't use traditional fuel

class Garage:
    """Garage class to manage multiple vehicles (composition example)."""
    
    def __init__(self, name, capacity=5):
        """
        Initialize a garage.
        
        Args:
            name (str): Garage name
            capacity (int): Maximum number of vehicles
        """
        # Your implementation here
        pass
    
    def add_vehicle(self, vehicle):
        """Add a vehicle to the garage."""
        # Your implementation here
        pass
    
    def remove_vehicle(self, vehicle):
        """Remove a vehicle from the garage."""
        # Your implementation here
        pass
    
    def list_vehicles(self):
        """List all vehicles in the garage."""
        # Your implementation here
        pass
    
    def start_all_vehicles(self):
        """Start all vehicles in the garage (demonstrate polymorphism)."""
        # Your implementation here
        pass

# Practice your implementations
if __name__ == "__main__":
    # Practice Vehicle creation
    print("=== Testing Vehicle Classes ===")
    
    # Create different types of vehicles
    regular_car = Car("Toyota", "Camry", 2023, "gasoline", 4)
    electric_car = ElectricCar("Tesla", "Model 3", 2023, 75)
    
    print(f"Regular car: {regular_car}")
    print(f"Electric car: {electric_car}")
    
    # Practice inheritance and polymorphism
    print("\n=== Testing Inheritance and Polymorphism ===")
    vehicles = [regular_car, electric_car]
    
    for vehicle in vehicles:
        print(f"Starting {vehicle.get_info()}: {vehicle.start()}")
    
    # Practice encapsulation
    print("\n=== Testing Encapsulation ===")
    print(f"Regular car mileage: {regular_car._mileage}")  # Protected access
    
    # Practice composition with Garage
    print("\n=== Testing Composition (Garage) ===")
    my_garage = Garage("My Garage", 3)
    my_garage.add_vehicle(regular_car)
    my_garage.add_vehicle(electric_car)
    
    print("Vehicles in garage:")
    my_garage.list_vehicles()
    
    print("\nStarting all vehicles:")
    my_garage.start_all_vehicles()
    
    # Practice electric car specific methods
    print("\n=== Testing Electric Car Specific Features ===")
    electric_car.charge()
    print(f"Electric car range: {electric_car.get_range()} miles")