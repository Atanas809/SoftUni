from math import ceil

budget = float(input())
students = int(input())
price_flour = float(input())
price_single_egg = float(input())
price_apron = float(input())

all_aprons = price_apron * (students + ceil(students * 0.2))

total_price = all_aprons
count_flour = 0

for s in range(1, students + 1):
    needed_eggs = price_single_egg * 10
    count_flour += 1
    if count_flour % 5 == 0:
        total_price += needed_eggs
    else:
        total_price += needed_eggs + price_flour

if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
