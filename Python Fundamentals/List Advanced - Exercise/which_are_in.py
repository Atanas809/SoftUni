substrings = input().split(", ")

text = input()

my_list = list()

for x in substrings:
    if x in text:
        my_list.append(x)

print(my_list)
