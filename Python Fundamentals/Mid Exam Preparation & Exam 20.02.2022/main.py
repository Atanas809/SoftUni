number = int(input())

is_prime = True

if number > 1:
    for x in range(2, number):
        if number % x == 0:
            is_prime = False
            print("False")
            break
    if number / 1 != 0 and number / number != 0:
        if is_prime:
            print("True")
else:
    print("False")
