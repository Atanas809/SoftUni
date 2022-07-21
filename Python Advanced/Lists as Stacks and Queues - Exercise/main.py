from collections import deque

food_quantity = int(input())

orders = deque(int(x) for x in input().split())

print(max(orders))
condition = True

for _ in range(len(orders)):
    order_quantity = orders[0]

    if order_quantity <= food_quantity:
        food_quantity -= order_quantity
        orders.popleft()
    else:
        condition = False
        break

if condition:
