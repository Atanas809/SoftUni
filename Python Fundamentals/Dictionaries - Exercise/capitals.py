# Задача 3:

country = input().split(", ")
capital = input().split(", ")

my_dict = dict(zip(country, capital))

for key, value in my_dict.items():
    print(f"{key} -> {value}")