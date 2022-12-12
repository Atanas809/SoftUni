class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients.keys():
            self.ingredients[ingredient] = quantity

        else:
            self.ingredients[ingredient] += quantity

        self.price += price_per_quantity * quantity
