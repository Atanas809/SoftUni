# Задача 9:
def output(academy_grades):

    for key, value in academy_grades.items():
        average_grade = sum(value) / len(value)

        if average_grade >= 4.50:
            print(f"{key} -> {average_grade:.2f}")

def academy():

    counter = int(input())

    academy_grades = dict()

    for _ in range(counter):

        name = input()
        grade = float(input())

        if name not in academy_grades.keys():
            academy_grades[name] = list()

        academy_grades[name].append(grade)


    output(academy_grades)

academy()
