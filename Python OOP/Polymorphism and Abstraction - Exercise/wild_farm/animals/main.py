from wild_farm.animals.animal import Bird


class Owl(Bird):
    INCREASE_WEIGHT = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
