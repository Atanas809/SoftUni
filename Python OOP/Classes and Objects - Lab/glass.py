class Glass:
    current_content = 0
    capacity = 250

    def __init__(self):
        self.content = self.current_content

    def fill(self, ml):
        if ml > self.space_left():
            return f"Cannot add {ml} ml"

        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{self.space_left()} ml left"

    def space_left(self):
        return self.capacity - self.content


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
