class Stack:
    def __init__(self):
        self.values = list()

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[-1]

    def count(self):
        return len(self.values)


s = Stack()

for x in range(2, 8):  # 2, 3, 4, 5, 6, 7
    s.push(x)
