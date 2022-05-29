from math import ceil

budget = float(input())
students = int(input())
price_flour = float(input())
price_single_egg = float(input())
price_apron = float(input())

all_aprons = price_apron * (students + ceil(students * 0.2))

total_price = all_aprons
count_flour = 0
