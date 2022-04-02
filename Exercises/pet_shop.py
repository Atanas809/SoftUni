# price per one dog food -> 2.50
# price per one cat food -> 4.00

food_for_dogs = int(input())
food_for_cats = int(input())

price_food_for_dogs = food_for_dogs * 2.50
price_food_for_cats = food_for_cats * 4

total_price = price_food_for_dogs + price_food_for_cats

print(f"{total_price} lv.")
