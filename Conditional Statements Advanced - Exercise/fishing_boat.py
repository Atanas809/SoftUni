budget = int(input())
season = input()
fisherman = int(input())

boat_rent = 0

if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if fisherman <= 6:
    boat_rent -= boat_rent * 0.1
elif 7 <= fisherman <= 11:
    boat_rent -= boat_rent * 0.15
else:
    boat_rent -= boat_rent * 0.25

if fisherman % 2 == 0 and season != "Autumn":
    boat_rent -= boat_rent * 0.05

difference = abs(budget - boat_rent)

if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
