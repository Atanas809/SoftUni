import time


# Correct but very slow operation with bigger list
# class Solution:
#     @staticmethod
#     def two_sum(nums, target):
#         indices = []
#
#         # start = time.time()
#
#         for i in range(0, len(nums)):
#             if not indices:
#                 for j in range(i + 1, len(nums)):
#                     result = nums[i] + nums[j]
#
#                     if result == target:
#                         indices.extend([i, j])
#                         break
#             else:
#                 break
#
#         #
#         # end = time.time()
#         # print(end - start)
#
#         return indices


# Best solution with very fast execution time!!!
class Solution:
    @staticmethod
    def two_sum(nums, target):
        cache = {}

        for i, n in enumerate(nums):
            difference = target - n

            if difference not in cache:
                cache[n] = i
            else:
                return [cache[difference], i]


s = Solution()
print(s.two_sum([2, 7, 11, 15], 9))
