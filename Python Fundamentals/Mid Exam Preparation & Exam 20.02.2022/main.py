price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
type_items = input()

right = price_ratings[entry_point + 1:]
left = price_ratings[:entry_point]

left_sum = 0
