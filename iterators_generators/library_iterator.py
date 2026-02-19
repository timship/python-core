"""
Для класса Book реализуем класс Library, который будет обладать свойствами итератора,
однако итерирование возможно в библиотеке только по тем книгам,
которые не находятся в пользовании у читателей (book.is_use = False).
"""
class Book:
    def __init__(self, title, is_use):
        self.title = title
        self.is_use = is_use

    def __repr__(self):
        return f"Book('{self.title}', {self.is_use})"

"""
class Library:

    def __init__(self, books):
        self.books = books

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        while self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1

            if not book.is_use:
                return book
        raise StopIteration
"""

class Library:
    def __init__(self, books):
        self.books = books

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.books):
            raise StopIteration
        if self.books[self.index].is_use:
            return self.__next__()
        return self.books[self.index]


books = [
    Book("Python for Beginners", True),
    Book("Python in Action", False),
    Book("Hands-On Machine Learning", False),
    Book("Introduction to Machine Learning with Python", True),
    Book("The Hundred-page Machine Learning Book", False),
]

library = Library(books)
for b in library:
    print(f"{b.title}")
# Python in Action
# Hands-On Machine Learning
# The Hundred-page Machine Learning Book

