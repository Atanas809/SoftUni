from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
