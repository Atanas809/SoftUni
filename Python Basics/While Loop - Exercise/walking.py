goal = 10000
final_steps = 0
is_reached = False

command = input()
while command != "Going home":
    current_steps = int(command)
    final_steps += current_steps
    if final_steps >= goal:
        is_reached = True
        break
    command = input()
if is_reached:
    difference = abs(final_steps - goal)
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
if command == "Going home":
    current_steps = int(input())
    final_steps += current_steps
    if final_steps < goal:
        difference = abs(final_steps - goal)
        print(f"{difference} more steps to reach goal.")
    else:
        difference = abs(final_steps - goal)
        print("Goal reached! Good job!")
        print(f"{difference} steps over the goal!")
