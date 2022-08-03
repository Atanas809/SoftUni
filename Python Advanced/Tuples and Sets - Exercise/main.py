def result(even, odd):
    even_sum = sum(even)
    odd_sum = sum(odd)

    if even_sum == odd_sum:
        union_set = even.union(odd)
        print(*union_set, sep=", ")
    elif odd_sum > even_sum:
        difference_set = odd.difference(even)
