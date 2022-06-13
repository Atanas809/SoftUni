import re

num = int(input())
expression = r"@(#)+(?P<valid>[A-Z][a-zA-Z0-9]{4,}[A-Z])@(#)+"

for _ in range(num):
    is_valid = False
    data = input()
