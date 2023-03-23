from abc import ABC, abstractmethod


class Animal(ABC):
    INCREASE_WEIGHT = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def eats(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        food_name = food.__class__.__name__

        if food_name not in self.eats():
            return f"{self.__class__.__name__} does not eat {food_name}!"
        self.weight += food.quantity * self.INCREASE_WEIGHT
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    INCREASE_WEIGHT = 0

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size
