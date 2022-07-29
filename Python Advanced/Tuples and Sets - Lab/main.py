counter = int(input())

names = [input() for _ in range(counter)]

my_set = {x for x in names}
