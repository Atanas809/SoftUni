"""
DIP stands for - Dependency inversion Principle
"""


class Book:
    def __init__(self, content: str):
        self.content = content


class OtherFormatter:
    def format(self, book: Book):
        return book.content
