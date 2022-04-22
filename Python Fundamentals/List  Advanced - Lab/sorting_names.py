# 1: Sorting names by ascending order
# 2: Sorting names by their length
# 3: If two or more names are the same length, they need to be sorted in ascending order.

names = sorted(input().split(", "))

print(sorted(names, key=len, reverse=True))
