class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self
