trip_price = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

count_toys = count_puzzles + count_dolls + count_bears + count_minions + count_trucks

price_puzzles = count_puzzles * 2.60
price_dolls = count_dolls * 3
price_bears = count_bears * 4.10
price_minions = count_minions * 8.20
price_trucks = count_trucks * 2

total_price = price_puzzles + price_dolls + price_bears + price_minions + price_trucks

if count_toys >= 50:
    total_price -= total_price * 0.25

final_sum = total_price - (total_price * 0.1)
difference = abs(final_sum - trip_price)

if final_sum >= trip_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
