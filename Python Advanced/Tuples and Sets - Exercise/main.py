def result(even, odd):
    even_sum = sum(even)
    odd_sum = sum(odd)

    if even_sum == odd_sum:
        union_set = even.union(odd)
        print(*union_set, sep=", ")
    elif odd_sum > even_sum:
        difference_set = odd.difference(even)
        print(*difference_set, sep=", ")
    else:
        symmetric_difference_set = even.symmetric_difference(odd)
        print(*symmetric_difference_set, sep=", ")


def battle():
    counter = int(input())

    even = set()
    odd = set()

    for x in range(1, counter + 1):
