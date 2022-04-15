# Задача 7:
def output(gifts):

    result = list()

    for x in gifts:
        if x != "None":
            result.append(x)

    print(' '.join(result))


def easter():
    gifts = input().split()

    command = input().split()

    while command[0] != "No" and command[1] != "Money":

        if command[0] == "OutOfStock":
            item = command[1]

            if item in gifts:
                for x in range(len(gifts)):
                    if gifts[x] == item:
                        gifts[x] = "None"

        elif command[0] == "Required":
            item = command[1]
            index = int(command[2])

            if 0 <= index <= len(gifts) - 1:
                gifts.pop(index)
                gifts.insert(index, item)

        elif command[0] == "JustInCase":
            item = command[1]

            gifts[-1] = item

        command = input().split()

    output(gifts)

easter()