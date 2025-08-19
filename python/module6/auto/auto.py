class Vehicle:
    """Base class representing a general vehicle."""

    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def start(self):
        """Start the vehicle."""
        return f"{self.brand} is starting."

    def stop(self):
        """Stop the vehicle."""
        return f"{self.brand} is stopping."


class Car(Vehicle):
    """Intermediate class representing a car, inherits from Vehicle."""

    def __init__(self, brand: str, year: int, doors: int):
        super().__init__(brand, year)
        self.doors = doors

    def honk(self):
        """Honk the car horn."""
        return f"{self.brand} goes 'beep beep!'"

class ElectricCar(Car):

    def __init__(self, brand: str, year: int, doors: int, battery_capacity: int):
        super().__init__(brand, year, doors)
        self.battery_capacity = battery_capacity

    def charge(self):
        """Recharge the electric car's battery."""
        return f"{self.brand} is charging with {self.battery_capacity} kWh capacity."