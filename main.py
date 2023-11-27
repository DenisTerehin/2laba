# book.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_available = True

    def borrow_book(self):
        if self._is_available:
            print(f"The book '{self.title}' by {self.author} is borrowed.")
            self._is_available = False
        else:
            print(f"Sorry, the book '{self.title}' is already borrowed.")

    def return_book(self):
        if not self._is_available:
            print(f"The book '{self.title}' has been returned.")
            self._is_available = True
        else:
            print(f"Error: The book '{self.title}' is not borrowed.")
