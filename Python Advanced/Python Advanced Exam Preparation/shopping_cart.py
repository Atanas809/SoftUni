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
        elif meal == "Soup":
            if len(meals["Soup"]) < soup_limit and product not in meals["Soup"]:
                meals["Soup"].append(product)
        elif meal == "Dessert":
            if len(meals["Dessert"]) < dessert_limit and product not in meals["Dessert"]:
                meals["Dessert"].append(product)

    sorted_meals = dict(sorted(meals.items(), key=lambda x: (-len(x[1]), x[0])))

    if is_valid(sorted_meals):

        result = []

        for x, y in sorted_meals.items():
            sorted_values = sorted(y)
            result.append(f"{x}:")
            for j in sorted_values:
                result.append(f" - {j}")

        return '\n'.join(result)

    return "No products in the cart!"


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
# print("-" * 20)
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print("-" * 20)
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
