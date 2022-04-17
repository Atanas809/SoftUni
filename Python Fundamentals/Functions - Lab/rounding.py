def rounding():

    numbers = (list(map(float, input().split())))

    new_list = list(map(lambda a: round(a), numbers))

    print(new_list)

rounding()
