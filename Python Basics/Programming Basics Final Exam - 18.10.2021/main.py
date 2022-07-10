price_for_page = float(input())
price_for_cover = float(input())
discount = int(input())
total_sum_percent = int(input())

price_for_printing = (price_for_page * 899) + (price_for_cover * 2)
total_sum_for_printing = (price_for_printing - (price_for_printing * (discount / 100))) + price_for_designer
