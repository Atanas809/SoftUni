# Задача 2:
import re

def bar():

    expression = r"%(?P<customer>([A-Z][a-z]+))%([^\$\|\.\%]+)?" \
                 r"<(?P<product>(\w+))>([^\$\|\.\%]+)?" \
                 r"\|(?P<count>(\d+))\|([^\$\|\.\%]+)?" \
                 r"(?P<price>([1-9][0-9]*|[1-9][0-9]*\.[0-9]+))\$"

    command = input()

    total_income = 0

    while command != "end of shift":

        matches = re.finditer(expression, command)
        
        for match in matches:
            customer = match.group("customer")
            product = match.group("product")
            quantity = int(match.group("count"))
            price = float(match.group("price"))

            total_price = quantity * price

            print(f"{customer}: {product} - {total_price:.2f}")

            total_income += total_price

        command = input()

    print(f"Total income: {total_income:.2f}")

bar()
