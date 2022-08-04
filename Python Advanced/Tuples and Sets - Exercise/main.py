def result(longest_intersection):
    output = [str(i) for i in longest_intersection]

    print(f"Longest intersection is [{', '.join(output)}] with length {len(longest_intersection)}")


def intersections():
    counter = int(input())

    longest_intersection = []

    for _ in range(counter):
