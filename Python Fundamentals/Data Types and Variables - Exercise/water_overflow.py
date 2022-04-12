number_of_liters = float(input())

liters_added = 0
capacity = 255

for liters in range(1, number_of_liters + 1):
    current_liter = int(input())
    if liters_added + current_liter <= capacity:
        liters_added += current_liter
    else:
        print("Insufficient capacity!")

print(liters_added)
