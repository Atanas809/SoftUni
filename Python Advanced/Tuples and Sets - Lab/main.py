numbers = [int(x) for x in input().split()]

target = int(input())

unique = set()

iterations = 0

for n1 in range(0, len(numbers)):
    for n2 in range(n1 + 1, len(numbers)):
        if numbers[n1] + numbers[n2] == target:
            print(f"{numbers[n1]} + {numbers[n2]} = {target}")
            unique.add(f"{(numbers[n1], numbers[n2])}")
