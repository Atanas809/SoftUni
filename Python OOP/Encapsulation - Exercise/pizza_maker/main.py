

    p.add_topping(mozzarella_topping)
    print(p.calculate_total_weight())

    p.add_topping(mozzarella_topping)
except ValueError as error:
    print(f'ValueError: {error}')
