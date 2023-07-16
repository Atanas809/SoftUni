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


book = Book("Content1")
book1 = Book("Content2")
book2 = Book("Content3")

f1 = Formatter()
f2 = OtherFormatter()

p1 = Printer(f1)
p2 = Printer(f2)

print(p1.get_book(book))
print(p1.get_book(book1))
print(p1.get_book(book2))
print('-' * 10)
print(p2.get_book(book))
print(p2.get_book(book1))
print(p2.get_book(book2))
