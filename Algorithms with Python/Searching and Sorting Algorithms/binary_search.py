def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid_index = (right + left) // 2
        mid_el = nums[mid_index]

        if mid_el == target:
            return mid_index
        if mid_el < target:
            left = mid_index + 1
        else:
            right = mid_index - 1

    return -1


numbers = list(map(int, input().split(" ")))
target = int(input())
print(binary_search(numbers, target))
