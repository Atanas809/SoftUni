class dictionary_iter:
    def __init__(self, obj: dict):
        self.obj = list(obj.items())
        self.start = 0
        self.stop = len(self.obj)
