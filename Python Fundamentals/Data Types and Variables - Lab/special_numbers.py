n = int(input())

for numbers in range(1, n + 1):
    is_special = False
    sum_digits = 0
    digit = numbers
    while digit > 0:
        sum_digits += digit % 10
        digit = int(digit / 10)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_special = True

    if is_special:
        print(f"{numbers} -> True")
    else:
        print(f"{numbers} -> False")
