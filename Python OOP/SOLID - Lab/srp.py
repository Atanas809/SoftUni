"""
SRP stands for - Single-Responsibility Principle
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.current_page = 0

    def turn_page(self, page):
        self.current_page = page


class Library:
    def __init__(self):
        self.books = dict()

    def add_book(self, book):
        if book not in self.books.keys():
            self.books[book.title] = book.author
            return f"{book.title} added to the library"
        return f"{book.title} already in the library"

    def remove_book(self, book_name):
        for book, author in self.books.items():
            if book == book_name:
                del self.books[book]
                return f"{book} successfully removed!"
        return f"Book {book_name} not found!"

    def find_book(self, title):
        for book, author in self.books.items():
            if book == title:
                return f"{book} from author {author}"
        return f"{title} not present in the library"


lb = Library()

for index in range(1, 21):
    current_book = Book(f"Book{index}", f"Author{index}")
    lb.add_book(current_book)

print(lb.find_book("Book3"))
print(lb.remove_book("Book3"))
print(lb.find_book("Book3"))