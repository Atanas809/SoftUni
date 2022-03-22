# задача 6:
nylon_needed = int(input())
paint_needed = int(input())
diluent_needed = int(input())
hours_needed = int(input())

price_nylon = (nylon_needed + 2) * 1.50
price_paint = (paint_needed + (paint_needed * 0.1)) * 14.50
price_diluent = diluent_needed * 5
total_price = price_nylon + price_paint + price_diluent + 0.40

sum_for_workers = (total_price * 0.3) * hours_needed

final_sum = total_price + sum_for_workers

print(final_sum)