def output(standings):
_dic.values():
            sort_dic[name] = points
    nums = sorted(sort_dic.values(), reverse=True)
    counter = 1
    for x in nums:
        for item in sort_dic.items():
            if item[1] == x:
                print(f"{counter}. {item[0]} -> {item[1]}")
                counter += 1
                del sort_dic[item[0]]
                break



def result(my_dict):

    for key, value in my_dict.items():
        print(f"{key}: {len(value) // 2} participants")
        sort_dic = dict()
        for x in range(0, len(value), 2):
            name = value[x]
            points = value[x + 1]
            if name not in sort_dic.values():
                sort_dic[name] = points
        output = sorted(sort_dic.values(), reverse=True)
        counter = 1
        for y in output:
            for item in sort_dic.items():
                if item[1] == y:
                    print(f"{counter}. {item[0]} <::> {item[1]}")
                    counter += 1
                    del sort_dic[item[0]]
                    break


def judge():
    data = input().split(" -> ")

    my_dict = dict()
    individual_standings = dict()
    names = list()

    while data[0] != "no more time":
        name = data[0]
        course = data[1]
        points = int(data[2])

        if course in my_dict.keys() and name in names:
            for key, value in my_dict.items():
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

