class reverse_iter:
    def __init__(self, nums):
        self.nums = list(reversed(nums))
        self.index = 0

    def __iter__(self):
        return self
