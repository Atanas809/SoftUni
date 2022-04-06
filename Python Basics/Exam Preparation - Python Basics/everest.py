current_metres = 5364
goal = 8848
current_day = 1
command = input()
goal_is_reached = False
while command != "END":
    will_sleep = command
    more_metres = int(input())
    if current_day >= 5:
        break
    if will_sleep == "Yes":
        current_day += 1
        current_metres += more_metres
    elif will_sleep == "No":
        current_metres += more_metres
    if goal <= current_metres:
        goal_is_reached = True
        break
    command = input()
if goal_is_reached:
    print(f"Goal reached for {current_day} days!")
else:
    print("Failed!")
    print(f"{current_metres}")
