class Book:
    def __init__(self, title, author, year):
        """
        Constructor method to initialize a Book instance.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method that is called when an object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the Book instance for users.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation of the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
