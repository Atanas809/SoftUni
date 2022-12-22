from itertools import permutations


def possible_permutations(obj):
    perm = permutations(obj)

    for i in list(perm):
        yield list(i)


[print(n) for n in possible_permutations([1, 2, 3])]
