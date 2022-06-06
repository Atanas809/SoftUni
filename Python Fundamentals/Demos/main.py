def results(individuals):
    print("Individual standings:")

    sorted_dict = sorted(individuals.values(), reverse=True)

    counter = 1

    for x in sorted_dict:
        for key, value in individuals.items():
