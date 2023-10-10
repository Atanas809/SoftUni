from structure_and_functionality.supply.supply import Supply


class Drink(Supply):
    DEFAULT_ENERGY = 15

    def __init__(self, name):
        super().__init__(name, self.DEFAULT_ENERGY)

    def type_of_supply(self):
        return "Drink"
