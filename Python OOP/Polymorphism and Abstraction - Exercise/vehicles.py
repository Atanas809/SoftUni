from abc import ABC, abstractmethod


class Vehicle(ABC):
    ADDITIONAL_LITERS = 0

    @abstractmethod
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + self.ADDITIONAL_LITERS)

        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, amount):
        self.fuel_quantity += amount
        return self.fuel_quantity


class Car(Vehicle):
    ADDITIONAL_LITERS = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)


class Truck(Vehicle):
    ADDITIONAL_LITERS = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def refuel(self, amount):
        self.fuel_quantity += amount * 0.95
        return self.fuel_quantity


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
