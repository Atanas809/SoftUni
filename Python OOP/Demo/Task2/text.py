from Task2.get_text_result import OutputText


class Text(OutputText):
    def __init__(self, data):
        super().__init__(data)

    def get_result(self):
        return len(self.data)
