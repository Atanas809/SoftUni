def distribution():

    data = list(map(int, input().split(", ")))

    minimum = int(input())

    condition = True

    for x in range(0, len(data)):
        richest = max(data)
        index = data.index(richest)
