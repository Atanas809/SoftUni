import re

data = input()
expression = r"(=|\/)(?P<valid>[A-Z][a-zA-Z]{2,})\1"
matches = re.finditer(expression, data)
destinations = list()

for match in matches:
    city = match.group("valid")
    destinations.append(city)

points = 0

for x in destinations:
    for y in x:
        points += 1
        
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")
