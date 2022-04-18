def filtered():

    numbers = list(map(int, input().split()))

    even_nums = list(filter(lambda x: x % 2 == 0, numbers))

    return even_nums

print(filtered())


