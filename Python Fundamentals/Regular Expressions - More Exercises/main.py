import re

def output(my_dict):

    sorted_dict = sorted(my_dict)

    for x in sorted_dict:
        print(f"{x} - {my_dict[x][0]} health, {my_dict[x][1]:.2f} damage")

def damage(name):
    
    expression = r"(?P<digits>[\-\+]?(\d+\.?\d+|\d+))"

    matches = re.finditer(expression, name)

    nums = 0

    for match in matches:
        nums += float(match.group("digits"))
