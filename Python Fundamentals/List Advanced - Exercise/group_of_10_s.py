numbers = list(map(int, input().split(", ")))

group = 10

while len(numbers) != 0:
    current_group = [i for i in numbers if i <= group]

    for x in current_group:
        numbers.remove(x)

    print(f"Group of {group}'s: {current_group}")

    group += 10

