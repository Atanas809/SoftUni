price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
type_items = input()

right = price_ratings[entry_point + 1:]
left = price_ratings[:entry_point]

left_sum = 0
right_sum = 0

for x in right:
    if type_items == "cheap":
        if x < price_ratings[entry_point]:
            right_sum += x
    elif type_items == "expensive":
        if x >= price_ratings[entry_point]:
            right_sum += x
for y in left:
    if type_items == "cheap":
        if y < price_ratings[entry_point]:
            left_sum += y
    elif type_items == "expensive":
        if y >= price_ratings[entry_point]:
