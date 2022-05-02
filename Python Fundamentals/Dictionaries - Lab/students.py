# Задача 4:

def output(my_dict, command):

    searched_course = command.replace("_", " ")

    for key, value in my_dict.items():
        if key == searched_course:
            for i in range(0, len(value) - 1, 2):
                print(f"{value[i]} - {value[i + 1]}")


def courses():

    data = input().split(":")

    my_dict = dict()

    while len(data) > 1:

        name = data[0]
        id = data[1]
        course = data[2]

        if course not in my_dict.keys():
            my_dict[course] = list()

        my_dict[course].append(name)
        my_dict[course].append(id)

        data = input().split(":")

    output(my_dict, data[0])

courses()
