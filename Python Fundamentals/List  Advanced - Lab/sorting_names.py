# 1: Sorting names by ascending order
# 2: Sorting names by their length

names = sorted(input().split(", "))

print(sorted(names, key=len, reverse=True))
