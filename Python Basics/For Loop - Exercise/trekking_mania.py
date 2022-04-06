count_groups = int(input())

for_musala = 0
for_monblan = 0
for_kilimanjaro = 0
for_k2 = 0
for_everest = 0


for climbers in range(1, count_groups + 1):
    alpinists = int(input())
    if alpinists <= 5:
        for_musala += alpinists
    if 6 <= alpinists <= 12:
        for_monblan += alpinists
    if 13 <= alpinists <= 25:
        for_kilimanjaro += alpinists
    if 26 <= alpinists <= 40:
        for_k2 += alpinists
    if alpinists >= 41:
        for_everest += alpinists

total_alpinists = for_musala + for_monblan + for_kilimanjaro + for_k2 + for_everest
percentage_climbers_musala = (for_musala / total_alpinists) * 100
percentage_climbers_monblan = (for_monblan / total_alpinists) * 100
percentage_climbers_kilimanjaro = (for_kilimanjaro / total_alpinists) * 100
percentage_climbers_k2 = (for_k2 / total_alpinists) * 100
percentage_climbers_everest = (for_everest / total_alpinists) * 100


print(f"{percentage_climbers_musala:.2f}%")
print(f"{percentage_climbers_monblan:.2f}%")
print(f"{percentage_climbers_kilimanjaro:.2f}%")
print(f"{percentage_climbers_k2:.2f}%")
# print(f"{percentage_climbers_everest:.2f}%")
