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
