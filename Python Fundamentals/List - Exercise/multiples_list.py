factor = int(input())
count = int(input())

my_list = list()

for x in range(factor, factor * count + 1, factor):
    my_list.append(x)

print(f"Output: {my_list}")
