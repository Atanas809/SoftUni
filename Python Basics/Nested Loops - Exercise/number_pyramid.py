number = int(input())
counter = 1
all_numbers_printed = False

for rows in range(1, number + 1):
    for cols in range(1, rows + 1):
        if counter == 1 and counter <= number:
            print(counter, end = " ")
            counter += 1
        elif counter != 1 and counter <= number:
            print(counter, end = " ")
            counter += 1
        elif counter == number:
            all_numbers_printed = True
            break
    if all_numbers_printed:
        break
    print()

