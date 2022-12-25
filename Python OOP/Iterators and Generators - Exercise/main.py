class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.index = 0
        self.value = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.count:
            raise StopIteration
        self.value += 1
        self.index += 1
