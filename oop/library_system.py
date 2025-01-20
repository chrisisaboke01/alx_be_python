class Book:
    def __init__(self, title, author):
        """
        Base class for a book with common attributes.
        """
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Derived class for an EBook with an additional file_size attribute.
        """
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Derived class for a PrintBook with an additional page_count attribute.
        """
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """
        A library that manages a collection of books.
        """
        self.books = []  # List to store books

    def add_book(self, book):
        """
        Add a book to the library collection.
        """
        self.books.append(book)

    def list_books(self):
        """
        List all books in the library.
        """
        for book in self.books:
            print(book)
