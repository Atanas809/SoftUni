def output(my_dict):

    for key, value in my_dict.items():
        print(f"{key} -> {value}")

def resources():

    info = input()

    my_dict = dict()

    while info != "stop":

        quantity = int(input())

        if info not in my_dict.keys():
            my_dict[info] = quantity
        else:
            my_dict[info] += quantity

        info = input()

    output(my_dict)

resources()
