def result(occurrences):
    for char, value in sorted(occurrences.items()):
        print(f"{char}: {value} time/s")


def counter():
    text = input()

    occurrences = dict()

    for ch in text:
