first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    odd_numbers = 0
    even_numbers = 0
    number_in_string = str(current_number)
    for index, digit in enumerate(number_in_string):
        if int(index) % 2 == 0:
            even_numbers += int(digit)
        if int(index) % 2 != 0:
            odd_numbers += int(digit)
    if odd_numbers == even_numbers:
        print(current_number, end = " ")
