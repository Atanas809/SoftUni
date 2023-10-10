# NOTE: In practice, this recursion should not be used here (instead use an iterative solution)

def sum_nums(i, nums):
    if i == len(nums) - 1:
        return nums[i]
    return nums[i] + sum_nums(i + 1, nums)


nums = [int(x) for x in input().split()]
print(sum_nums(0, nums))
