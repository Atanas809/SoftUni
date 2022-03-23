budget = float(input())
count_statists = int(input())
price_per_dress = float(input())

decor = budget * 0.1

if count_statists > 150:
    price_per_dress -= price_per_dress * 0.1

price_dresses = count_statists * price_per_dress

total_money = decor + price_dresses

difference = abs(total_money - budget)

if budget >= total_money:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
