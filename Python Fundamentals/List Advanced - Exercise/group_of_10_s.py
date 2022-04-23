numbers = list(map(int, input().split(", ")))

group = 10

while len(numbers) != 0:
    current_group = [x for x in numbers if x <= group]

    for x in current_group:
        numbers.remove(x)

    print(f"Group of {group}'s: {current_group}")

    group += 10

