def output(my_dict):

    if len(my_dict.keys()) > 0:
        print(f"Ahoy, Captain! There are {len(my_dict.keys())} wealthy settlements to go to:")
        for key, value in my_dict.items():
            print(f"{key} -> Population: {my_dict[key][0]} citizens, Gold: {my_dict[key][1]} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")
