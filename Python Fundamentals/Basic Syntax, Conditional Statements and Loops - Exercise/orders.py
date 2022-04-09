# Задача 6:
number_of_orders = int(input())

total_price = 0

for order in range(1, number_of_orders + 1):
    price_per_order = 0
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    price_per_order += price_per_capsule * capsules_count * days
    print(f"The price for the coffee is: ${price_per_order:.2f}")
    total_price += price_per_order

print(f"Total: ${total_price:.2f}")