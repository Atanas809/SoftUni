# Задача 1:

# Test input:
"""
one
1
two
2
Search
one
Remove
two
End
"""

# Wrong code:
numbers_dictionary = {}
line = input()

while line != "Search":
    number_as_string = line
    number = int(input())
    numbers_dictionary[number_as_string] = number

line = input()

while line != "Remove":
    searched = line
    print(numbers_dictionary[searched])

line = input()

while line != "End":
