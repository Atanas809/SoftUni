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
