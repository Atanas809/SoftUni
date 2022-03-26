# Задача 10:
count_numbers = int(input())

odd_sum = 0
even_sum = 0

for position in range(1, count_numbers + 1):
    current_number = int(input())
    if position % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    difference = abs(odd_sum - even_sum)
    print("No")
    print(f"Diff = {difference}")