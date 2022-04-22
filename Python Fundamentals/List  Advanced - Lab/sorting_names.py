# 1: Sorting names by ascending order

names = sorted(input().split(", "))

print(sorted(names, key=len, reverse=True))
