# Задача 3:

def calc(operator, f_num, s_num):

    if operator == "multiply":
        return f_num * s_num
    elif operator == "divide":
        return f_num // s_num
    elif operator == "add":
        return f_num + s_num
    elif operator == "subtract":
        return f_num - s_num

operator = input()
f_num = int(input())
s_num = int(input())

print(calc(operator, f_num, s_num))
