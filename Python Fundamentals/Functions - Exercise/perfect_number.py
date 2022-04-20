# Задача 10:

def perfect_num():

    number = int(input())

    divisors = list()

    for x in range(1, number + 1):
        if number % x == 0:
            divisors.append(x)

    if sum(divisors) / 2 == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

perfect_num()
