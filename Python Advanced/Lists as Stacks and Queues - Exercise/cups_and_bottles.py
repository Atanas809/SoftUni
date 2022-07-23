counter = int(input())
stack = list()

for _ in range(counter):
    query = list(map(int, input().split()))

    if query[0] == 1:
        stack.append(query[1])
