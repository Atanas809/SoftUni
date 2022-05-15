

while data != "Purchase":

    matches = re.finditer(expression, data)

    for match in matches:
        item = match.group("item")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))

        furniture.append(item)

        total_price += price * quantity

    data = input()

print("Bought furniture:")

for item in furniture:
    print(item)

print(f"Total money spend: {total_price:.2f}")
