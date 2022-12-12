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

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif self.ingredients[ingredient] < quantity:

            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_quantity

    def make_order(self):
        if not self.ordered:
            self.ordered = True
            ingredients = ', '.join([f"{key}: {value}" for key, value in self.ingredients.items()])
            return f"You've ordered pizza {self.name} prepared with {ingredients} and the price will be {self.price}lv."

        return f"Pizza {self.name} already prepared, and we can't make any changes!"


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
