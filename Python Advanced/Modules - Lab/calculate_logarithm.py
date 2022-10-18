from math import log

number = int(input())
base = input()

if base.isdigit():
    base = int(base)
    print(f"{log(number, base):.2f}")
else:
    print(f"{log(number):.2f}")
