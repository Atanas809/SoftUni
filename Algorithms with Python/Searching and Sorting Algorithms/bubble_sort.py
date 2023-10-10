def buble_sort(nums):
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        count = 0
        for i in range(1, len(nums) - count):
            if nums[i] <= nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                is_sorted = False
        count += 1
    return nums


numbers = list(map(int, input().split(" ")))
print(*buble_sort(numbers), sep=" ")
