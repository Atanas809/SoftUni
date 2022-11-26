def is_valid(sorted_meals):

    if len(sorted_meals["Pizza"]) == 0 and len(sorted_meals["Soup"]) == 0 and len(sorted_meals["Dessert"]) == 0:
        return False

    return True
