from wild_farm.animals.animal import Mammal


class Mouse(Mammal):
    INCREASE_WEIGHT = 0.10

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def eats(self):
        return ["Vegetable", "Fruit"]

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    INCREASE_WEIGHT = 0.40

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def eats(self):
        return ["Meat"]

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    INCREASE_WEIGHT = 0.30

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def eats(self):
        return ["Vegetable", "Meat"]

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    INCREASE_WEIGHT = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def eats(self):
        return ["Meat"]

    def make_sound(self):
        return "ROAR!!!"
