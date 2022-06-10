import re

data = input()

expression = r"(#|\|)(?P<food>[a-zA-Z\s]+)\1(?P<ex_date>[\d]{2}\/[\d]{2}\/[\d]{2})\1(?P<calories>[\d]{1,5})\1"
