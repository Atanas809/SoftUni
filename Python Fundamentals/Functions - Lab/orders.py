def orders():

    product = input()
    quantity = int(input())

    if product == "coffee":
        return 1.5 * quantity
    elif product == "water":
        return 1 * quantity
    elif product == "coke":
        return 1.4 * quantity
    elif product == "snacks":
        return 2 * quantity

print(f"{orders():.2f}")
