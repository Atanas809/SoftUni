# Задача 7:

def min_max_sum():

    numbers = list(map(int, input().split()))

    min_number = min(numbers)
    max_number = max(numbers)
    sum_numbers = sum(numbers)

    return f"The minimum number is {min_number}" \
           f"\nThe maximum number is {max_number}" \
           f"\nThe sum number is: {sum_numbers}"

print(min_max_sum())
