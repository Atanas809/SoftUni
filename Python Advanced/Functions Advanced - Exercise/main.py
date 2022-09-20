def even_odd(*args):
    command = args[-1]

    if command == "even":
        return [x for x in args[:-1] if x % 2 == 0]
    else:
        return [x for x in args[:-1] if x % 2 != 0]


# Test inputs:
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
