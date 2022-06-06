def results(individuals):
    print("Individual standings:")

    sorted_dict = sorted(individuals.values(), reverse=True)

    counter = 1

    for x in sorted_dict:
        for key, value in individuals.items():
            if value == x:
                print(f"{counter}. {key} -> {x[0]}")
                counter += 1
                del individuals[key]
                break
