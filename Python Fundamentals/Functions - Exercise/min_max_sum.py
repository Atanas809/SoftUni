def min_max_sum():

    numbers = list(map(int, input().split()))

    min_number = min(numbers)
    max_number = max(numbers)
    sum_numbers = sum(numbers)

    return f"The minimum number is {min_number}" \
           f"\nThe maximum number is {max_number}" \
           f"\nThe sum of all numbers is: {sum_numbers}"

print(min_max_sum())
