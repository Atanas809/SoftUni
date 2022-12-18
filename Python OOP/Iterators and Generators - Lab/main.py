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
            self.index += 1
            if value.lower() in self.all_vowels:
                return value
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
