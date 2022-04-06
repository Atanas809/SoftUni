current_meters = 5364
goal = 8848
current_day = 1
command = input()
goal_is_reached = False

while command != "END":
    will_sleep = command
    more_meters = int(input())
    if current_day >= 5:
        break
    if will_sleep == "Yes":
        current_day += 1
        current_meters += more_meters
    elif will_sleep == "No":
        current_meters += more_meters
    if goal <= current_meters:
        goal_is_reached = True
        break
    command = input()
    
if goal_is_reached:
    print(f"Goal reached for {current_day} days!")
    
else:
    print("Failed!")
    print(f"{current_meters}")
