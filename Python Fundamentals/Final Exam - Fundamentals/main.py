import re

number = int(input())

expression = r"^(\W+|\w+)(>)(?P<valid>[0-9]{3,}[|][a-z]{3,}[|][A-Z]{3,}[|][^\<\>]{3,})(<)\1$"
