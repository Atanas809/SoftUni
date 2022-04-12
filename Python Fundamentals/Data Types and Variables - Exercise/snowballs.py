number_of_snowballs = int(input())

best_snowball = 0
best_data = ""

for snowball in range(1, number_of_snowballs + 1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    value = (weight / time_needed) ** quality

    if value > best_snowball:
        best_snowball = value
        best_data = f"{weight} : {time_needed} = {best_snowball:.0f} ({quality})"

print(best_data)
