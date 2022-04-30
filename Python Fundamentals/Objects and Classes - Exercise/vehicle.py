class Vehicle:

    def __init__(self, type, model, price):

        self.type = type
        self.model = model
        self.price = price
        self.owner = None
        
    def buy(self, money: int, owner: str):

            if money >= self.price and self.owner == None:
                change = money - self.price
                self.owner = owner
                return f"Successfully bought a {self.type}. Change: {change:.2f}"

            elif money < self.price:
                return "Sorry, not enough money"

            else:
                return "Car already sold"
            
    def sell(self):
        if self.owner != None:
            self.owner = None
        else:
            return "Vehicle has no owner"
