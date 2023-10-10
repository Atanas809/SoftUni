"""
OCP stands for - Open-Closed Principle
"""

# Fixed code without OCP violation:
# Below you can see the original code with OCP violation

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "meow"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "woof-woof"


class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Hoot-hoot"


def animal_sound(animals_type: list):
    for animal in animals_type:
        print(f"{animal.__class__.__name__} with name {animal.name} make sound '{animal.make_sound()}'")


cat = Cat("Kitty")
dog = Dog("Poppy")
chicken = Chicken("Pepi")
animals = [cat, dog, chicken]

animal_sound(animals)

# Try to add a new animal without making changes to the code, just extend it! - Fixed!

# Original code with OCP violation

# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)
