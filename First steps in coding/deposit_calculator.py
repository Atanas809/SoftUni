# задача 3:
deposited_sum = float(input())
months = int(input())
interest = float(input())

sum_interests = deposited_sum * (interest / 100)
interest_for_one_month = sum_interests / 12
total_sum = deposited_sum + (months * interest_for_one_month)

print(total_sum)