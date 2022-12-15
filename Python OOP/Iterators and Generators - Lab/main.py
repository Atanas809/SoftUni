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
