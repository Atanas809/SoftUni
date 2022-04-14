coins = list(map(int, input().split(", ")))

count_beggars = int(input())

my_list = [0] * count_beggars

index = 0

for i in coins:
    my_list[index] += i
    if index + 1 == count_beggars:
        index = 0
    else:
        index += 1


print(my_list)
