def battle(my_list, attacked):

    destroyed = 0

    for x in attacked:
        data = x.split("-")
        row = int(data[0])
        col = int(data[1])
        if my_list[row][col] - 1 == 0:
            my_list[row][col] = 0
            destroyed += 1
