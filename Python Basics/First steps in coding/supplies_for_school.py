# задача 5:
count_pens = int(input())
count_markers = int(input())
litres_cleaner = float(input())
discount = int(input())

price_pens = count_pens * 5.80
price_markers = count_markers * 7.20
price_cleaner = litres_cleaner * 1.20
total_price = price_pens + price_markers + price_cleaner

final_sum = total_price - (total_price * (discount / 100))

print(final_sum)