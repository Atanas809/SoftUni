def is_valid(sorted_meals):

    if len(sorted_meals["Pizza"]) == 0 and len(sorted_meals["Soup"]) == 0 and len(sorted_meals["Dessert"]) == 0:
        return False

    return True


def shopping_cart(*args):
    meals = {"Pizza": [], "Soup": [], "Dessert": []}
    pizza_limit = 4
    soup_limit = 3
    dessert_limit = 2

    for data in args:
        if data == "Stop":
            break

        meal = data[0]
        product = data[1]

        if meal == "Pizza":
            if len(meals["Pizza"]) < pizza_limit and product not in meals["Pizza"]:
                meals["Pizza"].append(product)
