from structure_and_functionality.supply.supply import Supply


class Food(Supply):
    def __init__(self, name, energy=25):
        super().__init__(name, energy)

    def type_of_supply(self):
        return "Food"
