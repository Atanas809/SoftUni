max_bad_grades = int(input())
average_grade = 0
last_problem = ""
total_problems = 0
bad_grade = 0
is_ejected = False

current_problem = input()
while current_problem != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        bad_grade += 1
        if bad_grade == max_bad_grades:
            is_ejected = True
            break
    average_grade += current_grade
    total_problems += 1
    last_problem = current_problem
    current_problem = input()
if is_ejected:
    print(f"You need a break, {max_bad_grades} poor grades.")
else:
    average_grade /= total_problems
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {total_problems}")
    print(f"Last problem: {last_problem}")
