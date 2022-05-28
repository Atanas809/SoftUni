number = int(input())

is_prime = True

if number > 1:
    for x in range(2, number):
        if number % x == 0:
            is_prime = False
            print("False")
            break
