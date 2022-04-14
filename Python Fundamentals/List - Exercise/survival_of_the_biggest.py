numbers = list(map(int, input().split()))

counter = int(input())

for x in range(counter):
    current_min = min(numbers)

    numbers.remove(current_min)

result = list(map(str, numbers))

print(', '.join(result))
