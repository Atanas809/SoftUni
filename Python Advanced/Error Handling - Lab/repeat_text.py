# Test inputs:
"""
1 : Hello
    Bye

2: Hello
   2
"""

try:
    text = input()
    number = int(input())
    print(text * number)
except ValueError:
    print("Variable times must be an integer")
