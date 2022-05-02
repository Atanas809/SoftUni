# Задача 7:

def output(my_dict):

    for key, value in my_dict.items():
        print(f"{key} - {', '.join(value)}")

def synonyms():

    number = int(input())

    my_dict = dict()

    for x in range(number):
        key = input()
        value = input()

        if key not in my_dict.keys():
            my_dict[key] = list()

        my_dict[key].append(value)

    output(my_dict)

synonyms()

