from abc import ABC, abstractmethod


class Vehicle(ABC):
    ADDITIONAL_LITERS = 0

    @abstractmethod
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
