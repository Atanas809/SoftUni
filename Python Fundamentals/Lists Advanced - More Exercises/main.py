def battle(my_list, attacked):

    destroyed = 0

    for x in attacked:
        data = x.split("-")
        row = int(data[0])
        col = int(data[1])
        if my_list[row][col] - 1 == 0:
            my_list[row][col] = 0
            destroyed += 1
        else:
            my_list[row][col] -= 1

    print(destroyed)

def ships():

    counter = int(input())

    my_list = list()

    for _ in range(counter):

        current_ships = list(map(int, input().split()))

        my_list.append(current_ships)
