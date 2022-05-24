prices = input()

net_price = 0
taxes = 0
total_price = 0

while prices != "special" and prices != "regular":
    current_price = float(prices)
    if current_price <= 0:
        print("Invalid price!")
    else:
        net_price += current_price
        taxes += current_price * 0.2
