data = input().split()

my_dict = dict()

for x in range(0, len(data) - 1, 2):

    product = data[x]
    quantity = int(data[x + 1])

    my_dict[product] = quantity

print(my_dict)
