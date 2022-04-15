my_list = list(map(int, input().split()))

new_list = list()

for x in my_list:

    if x <= 0:
        x = abs(x)
        new_list.append(x)

    else:
        x = f"-{x}"
        new_list.append(int(x))


print(new_list)
