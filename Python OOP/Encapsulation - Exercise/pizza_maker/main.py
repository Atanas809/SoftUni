from pizza_maker.topping import Topping


class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = dict()

    @property
    def name(self):
        return self.__name
