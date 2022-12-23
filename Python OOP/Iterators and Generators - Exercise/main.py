class sequence_repeat:
    def __init__(self, text, number):
        self.text = text
        self.number = number
        self.start = -1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.number:
            raise StopIteration
