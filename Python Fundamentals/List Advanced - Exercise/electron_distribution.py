# Задача 6:

electrons = int(input())

position = 1

my_list = list()

while electrons > 0:
    formula = 2 * (position ** 2)

    if electrons - formula > 0:
        electrons -= formula
        my_list.append(formula)

    else:
        my_list.append(electrons)
        electrons = 0

    position += 1

print(my_list)