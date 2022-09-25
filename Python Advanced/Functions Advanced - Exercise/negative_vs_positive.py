def positives_vs_negatives(*args):
    positive_sum = sum([x for x in args if x > 0])
    negative_sum = sum(x for x in args if x < 0)

    if positive_sum > abs(negative_sum):
        return f"{negative_sum}\n{positive_sum}\nThe positives are stronger than the negatives"
    else:
        return f"{negative_sum}\n{positive_sum}\nThe negatives are stronger than the positives"


# Test input: "1 2 -3 -4 65 -98 12 57 -84"
numbers = [int(x) for x in input().split()]

print(positives_vs_negatives(*numbers))
