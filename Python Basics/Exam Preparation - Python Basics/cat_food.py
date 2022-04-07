number_of_cats = int(input())

small_cats = 0
big_cats = 0
huge_cats = 0
needed_food = 0

for cat in range(number_of_cats):
    food_in_grams = float(input())
    needed_food += food_in_grams
    if 100 <= food_in_grams < 200:
        small_cats += 1
    elif 200 <= food_in_grams < 300:
        big_cats += 1
    else:
        huge_cats += 1
price_food_per_day = (needed_food / 1000) * 12.45

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {huge_cats} cats.")
print(f"Price for food per day: {price_food_per_day:.2f} lv.")
