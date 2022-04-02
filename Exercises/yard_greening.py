# задача 9:
metres_for_greening = float(input())

price_for_all_metres = metres_for_greening * 7.61
discount = price_for_all_metres * 0.18

final_sum = price_for_all_metres - discount

print(f"The final price is: {final_sum} lv.")
print(f"The discount is: {discount} lv.")