def result(my_dict):

    print("Plants for the exhibition:")

    for key, value in my_dict.items():
        plant = key
        rarity = my_dict[plant][0]
        average_rating = 0
        if len(value) != 1:
            average_rating += sum(value[1:]) / len(value[1:])

        print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")


def output(my_dict):

    command = input().split(": ")

    while command[0] != "Exhibition":

        data = command[1]
        info = data.split(" - ")

        if command[0] == "Rate":
            plant = info[0]
            rating = int(info[1])

            if plant in my_dict.keys():
                my_dict[plant].append(rating)
            else:
                print("error")

        elif command[0] == "Update":

            plant = info[0]
            new_rarity = int(info[1])
