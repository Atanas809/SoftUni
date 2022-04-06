trip_price = float(input())
current_money = float(input())
days_elapsed = 0
days_spend = 0

while trip_price > current_money:
    command = input()
    sum_used = float(input())
    days_elapsed += 1
    if command == "spend":
        current_money -= sum_used
        days_spend += 1
        if days_spend >= 5:
            break
        if current_money < 0:
            current_money = 0
    if command == "save":
        days_spend = 0
        current_money += sum_used
if current_money >= trip_price:
    print(f"You saved the money for {days_elapsed} days.")
if days_spend == 5:
    print(f"You can't save the money.")
    print(f"{days_elapsed}")
