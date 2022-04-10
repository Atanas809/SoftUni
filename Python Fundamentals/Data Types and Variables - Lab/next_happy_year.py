# Задача 6:
year = int(input())

is_happy_year = False

while not is_happy_year:
    year += 1
    str_year = str(year)
    set_year = set()
    for char in range(len(str_year)):
        set_year.add(str_year[char])

    if len(str_year) == len(set_year):
        is_happy_year = True

print(year)