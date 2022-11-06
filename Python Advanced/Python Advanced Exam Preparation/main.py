def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    shopping_bag = []
