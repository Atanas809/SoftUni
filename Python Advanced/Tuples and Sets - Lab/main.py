def avg(grades):
    return sum(grades) / len(grades)


def output(statistics):
    for name, grades in statistics.items():
        average_grade = avg(grades)
        string_grades = [str(f"{g:.2f}") for g in grades]
        print(f"{name} -> {' '.join(string_grades)} (avg: {average_grade:.2f})")


def students():
