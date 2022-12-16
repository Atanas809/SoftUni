class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        value = self.start

        if value > self.end:
            raise StopIteration

        self.start += 1
        return value


one_to_ten = CustomRange(1, 10)
for num in one_to_ten:
    print(num)
