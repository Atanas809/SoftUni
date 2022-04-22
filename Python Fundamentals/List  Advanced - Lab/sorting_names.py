# Задача 5:

names = sorted(input().split(", "))

print(sorted(names, key=len, reverse=True))
