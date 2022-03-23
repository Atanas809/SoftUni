# Задача 1:
time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

time_in_minutes = total_time // 60
time_in_seconds = total_time % 60

if time_in_seconds < 10:
    print(f"{time_in_minutes}:0{time_in_seconds}")
else:
    print(f"{time_in_minutes}:{time_in_seconds}")