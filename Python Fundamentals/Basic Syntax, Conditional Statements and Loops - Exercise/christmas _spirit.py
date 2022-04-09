quantity = int(input())
days = int(input())

christmas_spirit = 0
total_sum = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        total_sum += 2 * quantity
        christmas_spirit += 5

    if day % 3 == 0:
        total_sum += 8 * quantity
        christmas_spirit += 13

    if day % 5 == 0:
        total_sum += 15 * quantity
        christmas_spirit += 17

        if day % 3 == 0:
            christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        total_sum += 5 + 3 + 15
        if days == day:
            christmas_spirit -= 30

print(f"Total cost: {total_sum}")
print(f"Total spirit: {christmas_spirit}")
