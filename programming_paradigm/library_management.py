# library_management.py

class Book:
    def __init__(self, title, author):
        """Initialize the Book with a title, author, and a default status of not checked out."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if self._is_checked_out:
            return f"'{self.title}' is already checked out."
        self._is_checked_out = True
        return f"'{self.title}' has been checked out."

    def return_book(self):
        """Mark the book as returned."""
        if not self._is_checked_out:
            return f"'{self.title}' was not checked out."
        self._is_checked_out = False
        return f"'{self.title}' has been returned."

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the Book."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise ValueError("Only instances of Book can be added to the library.")

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    return book.check_out()
                else:
                    return f"'{title}' is already checked out."
        return f"'{title}' is not found in the library."

    def return_book(self, title):
        """Return a checked-out book by its title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return f"'{title}' is not found in the library."

    def list_available_books(self):
        """List all books that are available for checkout."""
        available_books = [str(book) for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(book)
