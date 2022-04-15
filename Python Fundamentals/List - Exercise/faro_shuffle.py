cards = input().split()

shuffles = int(input())

length = len(cards)
mid = length // 2

for x in range(shuffles):
    my_list = []
    for y in range(0, mid):
        my_list.append(cards[y])
        my_list.append(cards[mid])
        mid += 1
    cards = my_list
    mid = length // 2

print(cards)
