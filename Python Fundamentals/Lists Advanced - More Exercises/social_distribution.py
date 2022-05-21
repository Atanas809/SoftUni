def distribution():

    data = list(map(int, input().split(", ")))

    minimum = int(input())

    condition = True

    for x in range(0, len(data)):
        richest = max(data)
        index = data.index(richest)
        if data[x] < minimum:
            needed = minimum - data[x]
            if richest - needed >= minimum:
                data[index] -= needed
                data[x] += needed
            else:
                condition = False
                print("No equal distribution possible")
                break

    if condition:
        print(data)

distribution()
