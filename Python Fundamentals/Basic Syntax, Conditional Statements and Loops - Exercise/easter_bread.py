# Задача 9:
budget = float(input())
price_for_kg_flour = float(input())

count_eggs = 0
count_bread = 0
easter_bread = 0
total_price = 0

price_for_pack_eggs = price_for_kg_flour * 0.75
price_for_250ml_milk = (price_for_kg_flour + (price_for_kg_flour * 0.25)) / 4

total_price += price_for_pack_eggs + price_for_kg_flour + price_for_250ml_milk

while budget > total_price:
    count_bread += 1
    easter_bread += 1
    count_eggs += 3
    easter_bread -= 1
    if count_bread % 3 == 0:
        count_eggs -= count_bread - 2
    budget -= total_price

print(f"You made {count_bread} loaves of Easter bread! Now you have {count_eggs} eggs and {budget:.2f}BGN left.")
