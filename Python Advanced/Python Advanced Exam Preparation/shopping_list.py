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

        current_price = quantity * price

        if budget >= current_price:
            budget -= current_price
            shopping_bag.append(f"You bought {product} for {current_price:.2f} leva.")

    return '\n'.join(shopping_bag)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
