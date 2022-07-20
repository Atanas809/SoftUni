clothes = [int(x) for x in input().split()]

capacity = int(input())

racks_used = 1

current_weight = capacity

while clothes:
    current_piece = clothes[-1]

    if current_piece <= current_weight:
        current_weight -= current_piece
        clothes.pop()
    else:
        racks_used += 1
        current_weight = capacity

print(racks_used)
