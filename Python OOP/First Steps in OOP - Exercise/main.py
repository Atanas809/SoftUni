class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if self.status() >= milliliters:
            self.quantity += milliliters

    def status(self):
        return self.size - self.quantity
