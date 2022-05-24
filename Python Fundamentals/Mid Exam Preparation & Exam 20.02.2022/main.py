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

    prices = input()

total_price += net_price + taxes

if total_price == 0:
    print("Invalid order!")
else:
    if prices == "special":
        total_price -= total_price * 0.1
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {net_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
