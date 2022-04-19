def factorial(num):
    f = 1
    if num >= 1:
        for i in range(1, num + 1):
            f = f * i
#     return f

# number1 = int(input())
# number2 = int(input())

result = factorial(number1) / factorial(number2)

print(f"{result:.2f}")
