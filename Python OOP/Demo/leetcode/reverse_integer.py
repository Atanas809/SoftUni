from collections import deque


class Solution:
    @staticmethod
    def __reversing_integer(x):
        reversed_num = 0

        while x > 0:
            a = x % 10
            reversed_num = reversed_num * 10 + a
            x = x // 10

        return reversed_num

    @staticmethod
    def __int_is_32bit(x):
        if x.bit_length() < 32:
            return True
        return False

    def reverse(self, x):
        if x < 0:
            x = abs(x)
            reversed_num = -abs(self.__reversing_integer(x))
        else:
            reversed_num = self.__reversing_integer(x)

        if not self.__int_is_32bit(reversed_num):
            return 0

        return reversed_num


s = Solution()
print(s.reverse(-123))
