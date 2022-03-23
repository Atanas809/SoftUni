# Задача 2:
points = int(input())

bonus_points = 0

if points <= 100:
    bonus_points += 5
elif 100 < points <= 1000:
    bonus_points += points * 0.2
else:
    bonus_points += points * 0.1

if points % 2 == 0:
    bonus_points += 1
if points % 10 == 5:
    bonus_points += 2

total_points = points + bonus_points

print(bonus_points)
print(total_points)