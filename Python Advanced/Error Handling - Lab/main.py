# Test input:
"""
1
4
-5
3
10
"""


class ValueCannotBeNegative(Exception):
    pass


while True:
    number = int(input())

    if number < 0:
        raise ValueCannotBeNegative
