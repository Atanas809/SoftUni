from abc import ABC, abstractmethod


class Animal(ABC):
    INCREASE_WEIGHT = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0
