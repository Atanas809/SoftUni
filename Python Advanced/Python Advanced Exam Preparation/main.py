def is_valid(sorted_meals):

    if len(sorted_meals["Pizza"]) == 0 and len(sorted_meals["Soup"]) == 0 and len(sorted_meals["Dessert"]) == 0:
        return False

    return True


def shopping_cart(*args):
    meals = {"Pizza": [], "Soup": [], "Dessert": []}
    pizza_limit = 4
    soup_limit = 3
    dessert_limit = 2
