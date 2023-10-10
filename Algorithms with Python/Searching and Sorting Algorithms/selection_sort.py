def selection_sort(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] <= nums[i]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


numbers = list(map(int, input().split(" ")))
print(*selection_sort(numbers), sep=" ")