# Задача 2:

expression = input()

my_stack = list()

for x in range(len(expression)):
    if expression[x] == "(":
        my_stack.append(x)
    elif expression[x] == ")":
