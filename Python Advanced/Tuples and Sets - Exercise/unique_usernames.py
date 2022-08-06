counter = int(input())

unique = set([input() for _ in range(counter)])

print(*unique, sep="\n")
