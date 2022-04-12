n = int(input())

final_sum = 0

for number in range(1, n + 1):
    letter = input()
    final_sum += ord(letter)

print(f"The sum equals: {final_sum}")
