class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity):
        self.is_happy = False

        if quantity >= self.water_requirements:
            self.is_happy = True
