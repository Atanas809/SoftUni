# pi = 3.14
from math import pi

type_of_figure = input()
a = float(input())

if type_of_figure == "square":
    area = a * a
elif type_of_figure == "rectangle":
    b = float(input())
    area = a * b
elif type_of_figure == "circle":
    area = pi * (a ** 2)
else:
    b = float(input())
    area = (a * b)/ 2
print(f"{area:.3f}")
