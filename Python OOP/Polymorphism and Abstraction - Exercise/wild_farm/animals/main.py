from wild_farm.animals.animal import Bird


class Owl(Bird):
    INCREASE_WEIGHT = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def eats(self):
        return ["Meat"]

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    INCREASE_WEIGHT = 0.35
