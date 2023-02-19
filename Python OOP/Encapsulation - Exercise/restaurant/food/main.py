

    whole_wheat_dough = Dough("Whole Wheat Flour", "Mixing", 200)
    print(whole_wheat_dough.weight)
    print(whole_wheat_dough.flour_type)
    print(whole_wheat_dough.baking_technique)

    p = Pizza("Margherita", whole_wheat_dough, 2)

    p.add_topping(tomato_topping)
    print(p.calculate_total_weight())

    p.add_topping(mozzarella_topping)
    print(p.calculate_total_weight())

    p.add_topping(mozzarella_topping)
except ValueError as error:
    print(f'ValueError: {error}')
