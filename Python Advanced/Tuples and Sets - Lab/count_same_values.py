def output(occurrences):
    for key, value in occurrences.items():
        print(f"{key:.1f} - {value} times")


def values():
    numbers = (float(x) for x in input().split())

    occurrences = dict()
