nums = list(map(int, input().split(", ")))

indices = list()

index = 0

for x in nums:
    if x % 2 == 0:
        indices.append(index)
    index += 1

print(indices)
