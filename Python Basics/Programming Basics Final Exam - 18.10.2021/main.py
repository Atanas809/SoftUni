number_of_locations = int(input())

for location in range(1, number_of_locations + 1):
    total_average_yield = 0
    final_average_yield = 0
    average_yield = float(input())
    number_of_days = int(input())
    for days in range(1, number_of_days + 1):
        gold_mined = float(input())
        total_average_yield += gold_mined
    final_average_yield = total_average_yield / number_of_days
    if final_average_yield >= average_yield:
        is_achieved = True
        print(f"Good job! Average gold per day: {final_average_yield:.2f}.")
    else:
        difference = abs(final_average_yield - average_yield)
