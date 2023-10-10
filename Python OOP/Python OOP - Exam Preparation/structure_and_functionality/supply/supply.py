from abc import ABC, abstractmethod


class Supply(ABC):
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        self.__validate_energy(value)
        self.__energy = value

    @staticmethod
    def __validate_name(value):
        if not value:
            raise ValueError("Name cannot be an empty string.")

    @staticmethod
    def __validate_energy(value):
        if value < 0:
            raise ValueError("Energy cannot be less than zero.")

    @abstractmethod
    def type_of_supply(self):
        pass

    def details(self):
        return f"{self.type_of_supply()}: {self.name}, {self.energy}"

