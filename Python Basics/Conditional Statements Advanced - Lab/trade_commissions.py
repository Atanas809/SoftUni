city = input()
sales = float(input())
city_is_valid = False
sales_is_valid = True
commissions = 0

if city == "Sofia":
    city_is_valid = True
    if 0 <= sales <= 500:
        commissions += sales * 0.05
    elif 500 < sales <= 1000:
        commissions += sales * 0.07
    elif 1000 < sales <= 10000:
        commissions += sales * 0.08
    else:
        commissions += sales * 0.12
if city == "Varna":
    city_is_valid = True
    if 0 <= sales <= 500:
        commissions += sales * 0.045
    elif 500 < sales <= 1000:
        commissions += sales * 0.075
    elif 1000 < sales <= 10000:
        commissions += sales * 0.1
    else:
        commissions += sales * 0.13
if city == "Plovdiv":
    city_is_valid = True
    if 0 <= sales <= 500:
        commissions += sales * 0.055
    elif 500 < sales <= 1000:
        commissions += sales * 0.08
    elif 1000 < sales <= 10000:
        commissions += sales * 0.12
    else:
        commissions += sales * 0.145
if sales < 0:
    sales_is_valid = False

if sales_is_valid and city_is_valid:
    print(f"{commissions:.2f}")
else:
    print("error")
