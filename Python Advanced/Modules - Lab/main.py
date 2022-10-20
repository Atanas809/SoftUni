from packages.math_operations import *


def operations(num1, sign, num2):
    if sign == "+":
        add(num1, num2)
    elif sign == "-":
        subtract(num1, num2)
    elif sign == "/":
        divide(num1, num2)
    elif sign == "*":
        multiply(num1, num2)
    elif sign == "^":
        power(num1, num2)


first_number, operator, second_number = input().split()
operations(float(first_number), operator, int(second_number))
