# Задача 1:
numbers = (list(map(float, input().split())))

absolute_values = list()

for a in numbers:
    absolute_values.append(abs(a))

print(absolute_values)