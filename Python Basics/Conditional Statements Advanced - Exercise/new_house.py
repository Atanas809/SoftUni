flower_type = input()
count_flowers = int(input())
budget = int(input())

price = 0

if flower_type == "Roses":
    price += 5 * count_flowers
elif flower_type == "Dahlias":
    price += 3.8 * count_flowers
elif flower_type == "Tulips":
    price += 2.8 * count_flowers
elif flower_type == "Narcissus":
    price += 3 * count_flowers
elif flower_type == "Gladiolus":
    price += 2.5 * count_flowers

if flower_type == "Roses" and count_flowers > 80:
    price -= (5 * count_flowers) * 0.1
elif flower_type == "Dahlias" and count_flowers > 90:
    price -= (3.8 * count_flowers) * 0.15
elif flower_type == "Tulips" and count_flowers > 80:
    price -= (2.8 * count_flowers) * 0.15
elif flower_type == "Narcissus" and count_flowers < 120:
    price += (3 * count_flowers) * 0.15
elif flower_type == "Gladiolus" and count_flowers < 80:
    price += (2.5 * count_flowers) * 0.2

difference = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
