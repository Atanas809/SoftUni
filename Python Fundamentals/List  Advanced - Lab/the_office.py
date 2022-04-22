# Задача 7:

employees = list(map(int, input().split()))

improvement = int(input())

new_happiness = list(map(lambda x: x * improvement, employees))

average = sum(new_happiness) / len(new_happiness)

happy_count = 0

for j in new_happiness:
    if j >= average:
        happy_count += 1

if happy_count >= len(employees) // 2:
    print(f"Score: {happy_count}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{len(employees)}. Employees are not happy!")


