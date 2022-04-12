# Задача 6:
n = int(input())

for x in range(n):
    for y in range(n):
        for z in range(n):
            print(f"{chr(x + 97)}{chr(y + 97)}{chr(z + 97)}")