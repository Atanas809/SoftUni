kg_food = float(input()) * 1000
kg_hay = float(input()) * 1000
kg_cover = float(input()) * 1000

weight_in_grams = float(input()) * 1000

for x in range(1, 30 + 1):

    kg_food -= 300

    if x % 2 == 0:
