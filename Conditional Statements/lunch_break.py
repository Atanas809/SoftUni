# Задача 8:
from math import ceil
type_of_series = input()
episode_duration = int(input())
break_duration = int(input())
enough_time = False

lunch_duration = (1 / 8) * break_duration
rest_duration = (1 / 4) * break_duration

time_left = break_duration - (lunch_duration + rest_duration)

if time_left >= episode_duration:
    enough_time = True

difference = ceil(abs(time_left - episode_duration))

if enough_time:
    print(f"You have enough time to watch {type_of_series} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {type_of_series}, you need {difference} more minutes.")
