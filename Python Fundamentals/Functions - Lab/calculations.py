def calc(operator, first_num, second_num):

    if operator == "multiply":
        return first_num * s_num
    elif operator == "divide":
        return first_num // s_num
    elif operator == "add":
        return first_num + s_num
    elif operator == "subtract":
        return first_num - s_num

operator = input()
f_num = int(input())
s_num = int(input())

print(calc(operator, first_num, s_num))
