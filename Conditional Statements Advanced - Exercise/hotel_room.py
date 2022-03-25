month = input()
nights_count = int(input())

studio_prize = 0
apartment_prize = 0

if month == "May" or month == "October":
    studio_prize += 50 * nights_count
    apartment_prize += 65 * nights_count
    if 7 < nights_count < 14:
        studio_prize -= studio_prize * 0.05
    if nights_count > 14:
        studio_prize -= studio_prize * 0.3
elif month == "June" or month == "September":
    studio_prize = 75.2 * nights_count
    apartment_prize = 68.7 * nights_count
    if nights_count > 14:
        studio_prize -= studio_prize * 0.2
elif month == "July" or month == "August":
    studio_prize = 76 * nights_count
    apartment_prize = 77 * nights_count

if nights_count > 14:
    apartment_prize -= apartment_prize * 0.1

print(f"Apartment: {apartment_prize:.2f} lv.")
print(f"Studio: {studio_prize:.2f} lv.")
