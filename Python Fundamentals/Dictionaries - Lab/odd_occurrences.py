data = input().lower().split()

my_dict = dict()

for x in data:

    if x not in my_dict.keys():
        my_dict[x] = 1
    else:
        my_dict[x] += 1

for key, value in my_dict.items():

    if value % 2 != 0:
        print(key, end=" ")
