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
