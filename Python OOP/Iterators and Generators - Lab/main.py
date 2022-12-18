class vowels:
    def __init__(self, text):
        self.text = text
        self.all_vowels = 'auoyei'
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            value = self.text[self.index]
