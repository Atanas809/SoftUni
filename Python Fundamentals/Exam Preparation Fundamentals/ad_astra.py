import re

data = input()
expression = r"(#|\|)(?P<food>[a-zA-Z\s]+)\1(?P<ex_date>[\d]{2}\/[\d]{2}\/[\d]{2})\1(?P<calories>[\d]{1,5})\1"
matches = re.finditer(expression, data)
total_calories = 0

output = list()

for match in matches:
    food = match.group("food")
    ex_date = match.group("ex_date")
    calories = int(match.group("calories"))
    
    total_calories += calories
    
    output.append(f"Item: {food}, Best before: {ex_date}, Nutrition: {calories}")

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")

for item in output:
    print(item)
