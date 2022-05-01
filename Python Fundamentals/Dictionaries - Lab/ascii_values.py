chars = input().split(", ")

my_dict = dict()

for x in chars:
  my_dict[x] = ord(x)

print(my_dict)
