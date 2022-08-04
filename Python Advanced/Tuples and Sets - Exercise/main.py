def result(longest_intersection):
    output = [str(i) for i in longest_intersection]

    print(f"Longest intersection is [{', '.join(output)}] with length {len(longest_intersection)}")


def intersections():
    counter = int(input())

    longest_intersection = []

    for _ in range(counter):
        data = input().split("-")

        first_start, first_end = [int(i) for i in data[0].split(",")]
