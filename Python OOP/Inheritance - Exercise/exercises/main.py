class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
