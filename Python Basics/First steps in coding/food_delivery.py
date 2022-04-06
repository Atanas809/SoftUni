count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegetarian_menu = int(input())

price_chicken_menu = count_chicken_menu * 10.35
price_fish_menu = count_fish_menu * 12.40
price_vegetarian_menu = count_vegetarian_menu * 8.15

total_sum = price_chicken_menu + price_fish_menu + price_vegetarian_menu
dessert_price = total_sum * 0.2

final_price = total_sum + dessert_price + 2.50

print(final_price)
