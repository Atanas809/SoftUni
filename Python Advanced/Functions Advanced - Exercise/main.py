def positives_vs_negatives(*args):
    positive_sum = sum([x for x in args if x > 0])
    negative_sum = sum(x for x in args if x < 0)

    if positive_sum > abs(negative_sum):
