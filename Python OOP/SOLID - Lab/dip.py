"""
DIP stands for - Dependency inversion Principle
"""


class Book:
    def __init__(self, content: str):
        self.content = content


class OtherFormatter:
    def format(self, book: Book):
        return book.content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def __init__(self, formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        formatted_book = self.formatter.format(book)
        return formatted_book
    
