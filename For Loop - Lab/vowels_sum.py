# Задача 6:
text = input()

sum = 0

for char in text:
    if char == "a":
        sum += 1
    if char == "e":
        sum += 2
    if char == "i":
        sum += 3
    if char == "o":
        sum += 4
    if char == "u":
        sum += 5

print(sum)