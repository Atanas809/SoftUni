def nested_loop(indx, number, array):
    if indx == len(array):
        print(*array, sep=" ")
        return

    for n in range(1, number + 1):
        array[indx] = n
        nested_loop(indx + 1, number, array)


n = int(input())
array = [None] * n
nested_loop(0, n, array)
