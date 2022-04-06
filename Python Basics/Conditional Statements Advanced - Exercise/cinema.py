ticket_type = input()
rows = int(input())
cows = int(input())

income = 0

hall_volume = rows * cows

if ticket_type == "Premiere":
    income += hall_volume * 12
elif ticket_type == "Normal":
    income += hall_volume * 7.5
else:
    income += hall_volume * 5

print(f"{income:.2f} leva")
