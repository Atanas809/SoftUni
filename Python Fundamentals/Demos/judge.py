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

def participants(my_dict):

    for key, value in my_dict.items():
        new_dict = dict()
        print(f"{key}: {len(value) // 2} participants")
        for x in range(0, len(value), 2):
            name = value[x]
            points = value[x + 1]
            if points not in new_dict.keys():
                new_dict[points] = list()
                new_dict[points].append(name)
            else:
                new_dict[points].append(name)

        sorted_dict = sorted(new_dict, reverse=True)

        counter = 1

        for y in sorted_dict:
            values = sorted(new_dict[y])
            for p in values:
                print(f"{counter}. {p} <::> {y}")
                counter += 1


def judge_system():

    data = input().split(" -> ")

    my_dict = dict()
    individuals = dict()

    while data[0] != "no more time":

        username = data[0]
        contest = data[1]
        points = int(data[2])

        if contest not in my_dict.keys():
            my_dict[contest] = list()
            my_dict[contest].append(username)
            my_dict[contest].append(points)
        else:
            if username in my_dict[contest]:
                index = my_dict[contest].index(username)
                if my_dict[contest][index + 1] < points:
                    my_dict[contest][index + 1] = points
            else:
                my_dict[contest].append(username)
                my_dict[contest].append(points)

        if username not in individuals.keys():
            individuals[username] = list()
            individuals[username].append(points)
        else:
            individuals[username][0] += points

        data = input().split(" -> ")

    participants(my_dict)
    results(individuals)

judge_system()
