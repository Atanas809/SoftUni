# Задача 4:

def even_odd():

    number = input()

    even_sum = 0
    odd_sum = 0

    for x in number:
        if int(x) % 2 == 0:
            even_sum += int(x)
        else:
            odd_sum += int(x)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

print(even_odd())
