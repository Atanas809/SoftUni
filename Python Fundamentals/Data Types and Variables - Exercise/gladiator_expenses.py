lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_price = 0
broken_shield = 0

for lost in range(1, lost_fights_count + 1):
    if lost % 2 == 0:
        total_price += helmet_price
    if lost % 3 == 0:
        total_price += sword_price
        if lost % 2 == 0:
            broken_shield += 1
            price += shield_price
            if broken_shield % 2 == 0:
                price += armor_price

print(f"Gladiator expenses: {price:.2f} aureus")
