counter = int(input())
stack = list()

for _ in range(counter):
    query = list(map(int, input().split()))

    if query[0] == 1:
        stack.append(query[1])
    elif query[0] == 2 and stack:
        stack.pop()
    elif query[0] == 3 and stack:
        print(max(stack))
    elif query[0] == 4 and stack:
        print(min(stack))
