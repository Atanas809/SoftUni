from math import floor
current_record = float(input())
distance_in_metres = float(input())
time_for_one_meter = float(input())
break_the_record = False

need_to_swim = distance_in_metres * time_for_one_meter
resistance = floor(distance_in_metres / 15) * 12.5

total_time = need_to_swim + resistance

if total_time < current_record:
    break_the_record = True

if break_the_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    difference = abs(current_record - total_time)
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
