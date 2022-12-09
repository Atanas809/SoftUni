class Glass:
    current_content = 0
    capacity = 250

    def __init__(self):
        self.content = self.current_content

    def fill(self, ml):
        if ml > self.space_left():
            return f"Cannot add {ml} ml"
