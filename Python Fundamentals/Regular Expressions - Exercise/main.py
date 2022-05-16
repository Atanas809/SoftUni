import re

expression = r"^>>(?P<item>(\w+))<<(?P<price>(0|[0-9]+).?(0|[0-9]+))!(?P<quantity>(\d+))$"

data = input()

total_price = 0
