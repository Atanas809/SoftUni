def result(my_dict):

    print("Plants for the exhibition:")

    for key, value in my_dict.items():
        plant = key
        rarity = my_dict[plant][0]
        average_rating = 0
        if len(value) != 1:
            average_rating += sum(value[1:]) / len(value[1:])
