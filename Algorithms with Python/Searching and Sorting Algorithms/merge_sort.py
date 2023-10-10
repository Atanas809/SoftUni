def apply_sort(left, right):
    output = [None] * (len(left) + len(right))
    left_idx = 0
    right_idx = 0
    output_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            output[output_idx] = left[left_idx]
            left_idx += 1
        else:
            output[output_idx] = right[right_idx]
            right_idx += 1
        output_idx += 1

    while left_idx < len(left):
        output[output_idx] = left[left_idx]
        left_idx += 1
        output_idx += 1

    while right_idx < len(right):
        output[output_idx] = right[right_idx]
        right_idx += 1
        output_idx += 1

    return output


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    mid_index = len(nums) // 2
    left = nums[:mid_index]
    right = nums[mid_index:]
    return apply_sort(merge_sort(left), merge_sort(right))


numbers = list(map(int, input().split(" ")))
print(*merge_sort(numbers), sep=" ")
