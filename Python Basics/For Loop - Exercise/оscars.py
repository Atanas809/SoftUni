actor_name = input()
academy_points = float(input())
number_of_jury = int(input())

is_nominated = False

for current_grade in range(number_of_jury):
    name = input()
    jury_points = float(input())
    current_total_points = len(name) * jury_points / 2
    academy_points += current_total_points
    if academy_points > 1250.5:
        is_nominated = True
        break
if is_nominated:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
else:
    difference = 1250.5 - academy_points
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")
