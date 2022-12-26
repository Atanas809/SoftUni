class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if not isinstance(element, str):
            raise TypeError("Only string types are allowed!")

        self.data.append(element)

    def pop(self):
