def quicksort(start, end, nums):
    if start >= end:
        return
    pivot = start
    left = pivot + 1
    right = end

    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] <= nums[pivot]:
            left += 1
        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]
    quicksort(pivot, right - 1, nums)
    quicksort(left, end, nums)
    return nums


numbers = list(map(int, input().split(" ")))
print(*quicksort(0, len(numbers) - 1, numbers), sep=" ")
