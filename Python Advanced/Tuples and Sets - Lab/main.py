def avg(grades):
    return sum(grades) / len(grades)


def output(statistics):
    for name, grades in statistics.items():
        average_grade = avg(grades)
