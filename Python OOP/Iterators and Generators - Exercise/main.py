class dictionary_iter:
    def __init__(self, obj: dict):
        self.obj = list(obj.items())
        self.start = 0
        self.stop = len(self.obj)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.stop:
            raise StopIteration

        current_value = self.obj[self.start]

        self.start += 1
        return current_value


result = dictionary_iter({1: "1", 2: "2"})
