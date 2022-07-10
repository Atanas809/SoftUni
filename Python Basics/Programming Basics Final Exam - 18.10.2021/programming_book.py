price_for_page = float(input())
price_for_cover = float(input())
discount = int(input())
total_sum_percent = int(input())

price_for_printing = (price_for_page * 899) + (price_for_cover * 2)
total_sum_for_printing = (price_for_printing - (price_for_printing * (discount / 100))) + price_for_designer

total_sum_with_discount = total_sum_for_printing - (total_sum_for_printing * (total_sum_percent / 100))

print(f"Ivan should pay {total_sum_with_discount:.2f} BGN.")
