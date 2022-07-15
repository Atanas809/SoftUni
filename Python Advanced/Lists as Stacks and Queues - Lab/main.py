class Stack:
    def __init__(self):
        self.values = list()

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[-1]
