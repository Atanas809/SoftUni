number_of_cats = int(input())

small_cats = 0
big_cats = 0
huge_cats = 0
needed_food = 0

for cat in range(1, number_of_cats + 1):
    food_in_grams = float(input())
    needed_food += food_in_grams
    if 100 <= food_in_grams < 200:
        small_cats += 1
    elif 200 <= food_in_grams < 300:
        big_cats += 1
    else:
        huge_cats += 1
