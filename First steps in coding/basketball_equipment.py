# задача 8:
annual_price = int(input())

sneakers_price = annual_price - (annual_price * 0.4)
equipment_price = sneakers_price - (sneakers_price * 0.2)
ball_price = equipment_price * 0.25
accessories_price = ball_price * 0.2

total_price = annual_price + sneakers_price + equipment_price + ball_price + accessories_price

print(total_price)