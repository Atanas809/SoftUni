def division(number):

    fact = 1

    for x in range(1, number + 1):
        fact *= x

    return fact

f_num = int(input())
s_num = int(input())

result = division(f_num) / division(s_num)

print(f"{result:.2f}")
