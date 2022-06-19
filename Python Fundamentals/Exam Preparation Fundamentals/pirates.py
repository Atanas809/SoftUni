def output(my_dict):

    if len(my_dict.keys()) > 0:
        print(f"Ahoy, Captain! There are {len(my_dict.keys())} wealthy settlements to go to:")
        for key, value in my_dict.items():
            print(f"{key} -> Population: {my_dict[key][0]} citizens, Gold: {my_dict[key][1]} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


def targets(my_dict):

    command = input().split("=>")

    while command[0] != "End":

        if command[0] == "Plunder":
            town = command[1]
            people = int(command[2])
            gold = int(command[3])

            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

            if my_dict[town][0] - people <= 0 or my_dict[town][1] - gold <= 0:
                del my_dict[town]
                print(f"{town} has been wiped off the map!")

            else:
                my_dict[town][0] -= people
                my_dict[town][1] -= gold
        else:
            town = command[1]
            gold = int(command[2])

            if gold < 0:
                print("Gold added cannot be a negative number!")
            else:
                my_dict[town][1] += gold
                print(f"{gold} gold added to the city treasury. {town} now has {my_dict[town][1]} gold.")

        command = input().split("=>")

    output(my_dict)


def cities():

    data = input().split("||")
    my_dict = dict()

    while data[0] != "Sail":

        city = data[0]
        population = int(data[1])
        gold = int(data[2])

        if city not in my_dict.keys():
            my_dict[city] = list()
            my_dict[city].append(population)
            my_dict[city].append(gold)

        else:
            my_dict[city][0] += population
            my_dict[city][1] += gold

        data = input().split("||")

    targets(my_dict)

cities()
