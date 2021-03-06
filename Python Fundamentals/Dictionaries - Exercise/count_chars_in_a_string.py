# Solution without library:

text = input()

my_dict = dict()

for i in text:
    if i != " ":
        if i not in my_dict.keys():
            my_dict[i] = 1
        else:
            my_dict[i] += 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")

# Solution with library collections (Counter):

from collections import Counter

info = input()

my_dict = dict(Counter(info))

for key, value in my_dict.items():
    if key != " ":
        print(f"{key} -> {value}")
