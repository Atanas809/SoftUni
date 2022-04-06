budget = float(input())
season = input()

accommodation = ""
destination = ""
price = 0

if season == "summer":
    accommodation = "Camp"
elif season == "winter":
    accommodation = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price += budget * 0.3
    elif season == "winter":
        price = budget * 0.7
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price += budget * 0.4
    elif season == "winter":
        price += budget * 0.8
else:
    destination = "Europe"
    accommodation = "Hotel"
    price += budget * 0.9

print(f"Somewhere in {destination}")
print(f"{accommodation} - {price:.2f}")
