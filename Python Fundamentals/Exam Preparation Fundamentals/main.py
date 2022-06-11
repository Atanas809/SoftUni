
            individual_standings[name].append(points)
        else:
            for key, value in my_dict.items():
                if course == key and name in my_dict[course]:
                    if individual_standings[name][0] < points:
                        individual_standings[name][0] = points
                        break
                else:
                    if course != key and name in my_dict[course]:
                        individual_standings[name][0] += points
                        break



        data = input().split(" -> ")

    my_dict = result(my_dict)
    individual_standings = output(individual_standings)

judge()

