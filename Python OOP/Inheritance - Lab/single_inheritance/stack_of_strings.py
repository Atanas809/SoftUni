

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
