# Задача 6:

numbers = list(map(int, input().split()))

counter = int(input())

for x in range(counter):
    current_min = min(numbers)

    numbers.remove(current_min)

output = list(map(str, numbers))

print(', '.join(output))
