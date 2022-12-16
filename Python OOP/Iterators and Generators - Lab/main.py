class reverse_iter:
    def __init__(self, nums):
        self.nums = list(reversed(nums))
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.nums):
            raise StopIteration

        value = self.nums[self.index]

        self.index += 1
        return value


reversed_list = reverse_iter([1, 2, 3, 4])
