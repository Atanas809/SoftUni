from collections import deque

# Test input:
"""
5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22
"""


def enough_fireworks(fireworks):
    if fireworks["Palm firework"] >= 3 and fireworks["Willow firework"] >= 3 and fireworks["Crossette firework"] >= 3:
        return True

    return False

def firework_made(sum_values, fireworks):
    if sum_values % 3 == 0 and sum_values % 5 != 0:
        fireworks["Palm firework"] += 1
        return True
    elif sum_values % 3 != 0 and sum_values % 5 == 0:
        fireworks["Willow firework"] += 1
        return True
    elif sum_values % 3 == 0 and sum_values % 5 == 0:
        fireworks["Crossette firework"] += 1
        return True

    return False


def is_valid_value(power, effect):
    if power > 0 and effect > 0:
        return True


firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

fireworks = {
    "Palm firework": 0,
    "Willow firework": 0,
    "Crossette firework": 0
}

while True:

    if not firework_effects:
        break
    elif not explosive_power:
        break
    elif enough_fireworks(fireworks):
        break

    current_effect = firework_effects.popleft()
    current_power = explosive_power.pop()

    if is_valid_value(current_power, current_effect):
        sum_values = current_power + current_effect
        if not firework_made(sum_values, fireworks):
            current_effect -= 1
            firework_effects.append(current_effect)
            explosive_power.append(current_power)
    else:
        if current_power > 0:
            explosive_power.append(current_power)
        elif current_effect > 0:
            firework_effects.appendleft(current_effect)

if enough_fireworks(fireworks):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

print(f'Palm Fireworks: {fireworks["Palm firework"]}')
print(f'Willow Fireworks: {fireworks["Willow firework"]}')
print(f'Crossette Fireworks: {fireworks["Crossette firework"]}')
