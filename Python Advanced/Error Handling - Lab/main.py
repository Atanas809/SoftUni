# Test inputs:
"""
1: 1, 4, 5

# Correct code:
numbers_list = [int(x) for x in input().split(", ")]
result = 1
2: 4, 5, 6, 1, 3

3: 2, 5, 10
"""


# Expected output:
"""
1: 20
2: 10
3: 1
"""

# Wrong code:
# numbers_list = input().split(", ")
# result = 0
#
# for i in range(numbers_list):
#     number = numbers_list[i + 1]
#     if number < 5:
#         result *= number
#     elif number > 5 and number > 10:
#         result /= number
#
# print(result)

# Correct code:
numbers_list = [int(x) for x in input().split(", ")]
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
