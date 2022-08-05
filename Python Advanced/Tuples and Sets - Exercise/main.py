counters = [int(x) for x in input().split()]

first_set = set(int(input()) for _ in range(counters[0]))
second_set = set(int(input()) for _ in range(counters[1]))

result = first_set.intersection(second_set)

print(*result)
