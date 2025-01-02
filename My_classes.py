class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability_status = "Available"
    
    # Getters and Setters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def get_availability_status(self):
        return self.__availability_status
    
    def borrow(self):
        if self.__availability_status == "Available":
            self.__availability_status = "Borrowed"
        else:
            raise Exception("Book is already borrowed.")
    
    def return_book(self):
        if self.__availability_status == "Borrowed":
            self.__availability_status = "Available"
        else:
            raise Exception("Book is already available.")

    def display_book_details(self):
        return f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Publication Date: {self.__publication_date}, Status: {self.__availability_status}"


class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books
    
    def borrow_book(self, book):
        self.__borrowed_books.append(book.get_title())
        book.borrow()

    def return_book(self, book):
        if book.get_title() in self.__borrowed_books:
            self.__borrowed_books.remove(book.get_title())
            book.return_book()
        else:
            raise Exception("This user has not borrowed this book.")

    def display_user_details(self):
        borrowed_books = ', '.join(self.__borrowed_books) if self.__borrowed_books else "None"
        return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {borrowed_books}"


class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def display_author_details(self):
        return f"Name: {self.__name}, Biography: {self.__biography}"
