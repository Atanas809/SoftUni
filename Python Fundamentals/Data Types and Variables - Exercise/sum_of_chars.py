# Задача 4:
n = int(input())

total_sum = 0

for number in range(1, n + 1):
    letter = input()
    total_sum += ord(letter)

print(f"The sum equals: {total_sum}")