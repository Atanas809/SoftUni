# Задача 8:

def output(my_dict):

    for key, value in my_dict.items():
        print(f"{key}: {len(value)}")
        for name in value:
            print(f"-- {name}")

def softuni_courses():

    command = input().split(" : ")

    my_dict = dict()

    while command[0] != "end":

        course = command[0]
        name = command[1]

        if course not in my_dict.keys():
            my_dict[course] = list()

        my_dict[course].append(name)

        command = input().split(" : ")

    output(my_dict)

softuni_courses()
