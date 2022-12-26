class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if not isinstance(element, str):
            raise TypeError("Only string types are allowed!")

        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        reversed_list = reversed(self.data)
        return f"[{', '.join(x for x in reversed_list)}]"


s = Stack()
s.push("5")
s.push("3")
s.push("2")
print(s)
print(s.pop())
print(s)
print(s.top())
print(s.is_empty())
