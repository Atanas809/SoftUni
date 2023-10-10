from abc import ABC, abstractmethod


class Meal(ABC):
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__validate_price(value)
        self.__price = value

    @staticmethod
    def __validate_name(value):
        if not value:
            raise ValueError("Name cannot be an empty string!")

    @staticmethod
    def __validate_price(value):
        if value <= 0.0:
            raise ValueError("Invalid price!")

    @abstractmethod
    def details(self):
        pass

    @abstractmethod
    def type(self):
        pass
