def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    shopping_bag = []

    for key, value in kwargs.items():
        product = key
        price = value[0]
        quantity = value[1]
        if len(shopping_bag) == 5:
            break
