
                if key == course and name in value:
                    for x in range(0, len(value), 2):
                        user = value[x]
                        num = value[x + 1]
                        if user == name:
                            if num < points:
                                my_dict[course][x + 1] = points
                                break

        if course not in my_dict.keys():
            my_dict[course] = list()
            my_dict[course].append(name)
            my_dict[course].append(points)
        else:
            if name not in my_dict[course]:
                my_dict[course].append(name)
                my_dict[course].append(points)

        if name not in names:
            names.append(name)

        if name not in individual_standings.keys():
            individual_standings[name] = list()
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

