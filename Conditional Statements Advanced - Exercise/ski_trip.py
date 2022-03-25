days_for_stay = int(input())
room_type = input()
feedback = input()

price = 0

if room_type == "room for one person":
    price += (days_for_stay - 1) * 18
elif room_type == "apartment":
    if days_for_stay < 10:
        price += (days_for_stay - 1) * 25 - (((days_for_stay - 1) * 25) * 0.3)
    elif 10 <= days_for_stay <= 15:
        price += (days_for_stay - 1) * 25 - (((days_for_stay - 1) * 25) * 0.35)
    else:
        price += (days_for_stay - 1) * 25 - (((days_for_stay - 1) * 25) * 0.5)
elif room_type == "president apartment":
    if days_for_stay < 10:
        price += (days_for_stay - 1) * 35 - (((days_for_stay - 1) * 35) * 0.1)
    elif 10 <= days_for_stay <= 15:
        price += (days_for_stay - 1) * 35 - (((days_for_stay - 1) * 35) * 0.15)
    else:
        price += (days_for_stay - 1) * 35 - (((days_for_stay - 1) * 35) * 0.2)

if feedback == "positive":
    price += price * 0.25
else:
    price -= price * 0.1

print(f"{price:.2f}")
