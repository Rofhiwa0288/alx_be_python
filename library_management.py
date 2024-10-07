class Book:
    """
    Represents a book with title, author, and checkout status.
    """

    def __init__(self, title, author):
        """
        Initialize book with title, author, and availability.

        Args:
            title (str): Book title
            author (str): Book author
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """
        Mark book as checked out.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Mark book as returned (available).
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Check if book is available.

        Returns:
            bool: True if available, False otherwise
        """
        return not self._is_checked_out


class Library:
    """
    Manages a collection of books.
    """

    def __init__(self):
        """
        Initialize library with an empty book list.
        """
        self._books = []

    def add_book(self, book):
        """
        Add a book to the library.

        Args:
            book (Book): Book instance to add
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by title.

        Args:
            title (str): Title of book to check out

        Returns:
            bool: True if checkout successful, False otherwise
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """
        Return a book by title.

        Args:
            title (str): Title of book to return

        Returns:
            bool: True if return successful, False otherwise
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """
        Print available books.
        """
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")


