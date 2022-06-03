kg_food = float(input()) * 1000
kg_hay = float(input()) * 1000
kg_cover = float(input()) * 1000

weight_in_grams = float(input()) * 1000

for x in range(1, 30 + 1):

    kg_food -= 300

    if x % 2 == 0:
        five_percent = kg_food * 0.05

        kg_hay -= five_percent

    if x % 3 == 0:
        one_third = weight_in_grams / 3

        kg_cover -= one_third

if kg_food > 0 and kg_hay > 0 and kg_cover > 0:
