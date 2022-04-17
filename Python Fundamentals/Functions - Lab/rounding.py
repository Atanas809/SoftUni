def rounding():

    numbers = (list(map(float, input().split())))

    new_list = list(map(lambda a: round(a), numbers))

    return new_list

print(rounding())
