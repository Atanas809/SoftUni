from math import floor

number_of_tournaments = int(input())
starting_points = int(input())

tournaments = 0
total_points = starting_points
starting_average_points = 0
tournaments_won = 0

for position in range(1, number_of_tournaments + 1):
    current_position = input()
    if current_position == "W":
        total_points += 2000
        starting_average_points += 2000
        tournaments_won += 1
        tournaments += 1
    if current_position == "F":
        tournaments += 1
        starting_average_points += 1200
        total_points += 1200
    if current_position == "SF":
        tournaments += 1
        starting_average_points += 720
        total_points += 720

average_points = floor(starting_average_points / tournaments)
percent_won = (tournaments_won / tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_won:.2f}%")
