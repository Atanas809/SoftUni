def output(my_set):
    if my_set:
        [print(x) for x in my_set]
    else:
        print("Parking Lot is Empty")


def parking():
    counter = int(input())

    my_set = set()

    for _ in range(counter):

        command, number_plate = input().split(", ")

        if command == "IN":
            my_set.add(number_plate)
        else:
