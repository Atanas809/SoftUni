from abc import ABC, abstractmethod


class Horse(ABC):
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__validate_speed(value)
        self.__speed = value

    @staticmethod
    def __validate_name(value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")

    def __validate_speed(self, value):
        if value > self.max_speed():
            raise ValueError("Horse speed is too high!")

    @abstractmethod
    def max_speed(self):
        pass

    @abstractmethod
    def train(self):
        # TODO
        """
        Each horse can be additionally trained during the race days. When a horse is trained,
        it increases its speed by a value depending on its type. During training, a horse cannot exceed its
        maximum speed (just set its speed to the maximum one without raising an error).
        :return:
        """
        pass
