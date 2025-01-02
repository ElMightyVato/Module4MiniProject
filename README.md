Library Mangagment Computer System

Overview

The Library Management Computer System (LMCS) is a simple Python application that allows users to manage books, users, and authors. The system provides operations such as adding, borrowing, returning, and searching for books, as well as dealing with user and author details. This system is built using Object-Oriented Programming (OOP) principles with three primary classes: `Book`, `User`, and `Author`.

Features

Book Operations:
  - Add a new book
  - Borrow a book
  - Return a book
  - Search for a book by title
  - Display details of all books in the system

User Operations:
  - Add a new user
  - View user details
  - Display details of all users in the system

Author Operations:
  - Add a new author
  - View author details
  - Display details of all authors in the system

Classes

Book

This class represents a book in the library. It contains the following attributes and methods:

Attributes:
- `__title` : The title of the book.
- `__author` : The author of the book.
- `__genre` : The genre of the book.
- `__publication_date` : The publication date of the book.
- `__availability_status` : The current status of the book (either "Available" or "Borrowed").

Methods:
- `get_title()`: Returns the title of the book.
- `get_author()`: Returns the author of the book.
- `get_genre()`: Returns the genre of the book.
- `get_publication_date()`: Returns the publication date of the book.
- `get_availability_status()`: Returns the status of the book.
- `borrow()`: Changes the book's status to "Borrowed" if it's currently available.
- `return_book()`: Changes the book's status to "Available" if it's currently borrowed.
- `display_book_details()`: Returns a string containing all details of the book.

User

This class represents a user of the library. It contains the following attributes and methods:

Attributes:
- `__name` : The name of the user.
- `__library_id` : The unique library ID for the user.
- `__borrowed_books` : A list of books borrowed by the user.

Methods:
- `get_name()`: Returns the name of the user.
- `get_library_id()`: Returns the library ID of the user.
- `get_borrowed_books()`: Returns the list of borrowed books.
- `borrow_book(book)`: Borrows a book for the user.
- `return_book(book)`: Returns a borrowed book.
- `display_user_details()`: Returns a string containing the user's details and their borrowed books.

Author

This class represents an author of a book. It contains the following attributes and methods:

Attributes:
- `__name` : The name of the author.
- `__biography` : A brief biography of the author.

Methods:
- `get_name()`: Returns the name of the author.
- `get_biography()`: Returns the biography of the author.
- `display_author_details()`: Returns a string containing the author's details.

Functions

    show_main_menu()

Displays the main menu of the system, allowing the user to choose between book, user, or author.
"""
show_book_menu()
"""
Displays the book-related menu.

    show_user_menu()

Displays the user-related menu.

    show_author_menu()

Displays the author-related menu.

    main()

The main loop of the system that interacts with the user. It displays menus and calls the correct functions based on the user's choices.

    find_book_by_title(title)

Searches for a book in the system by its title and returns the `Book` object if found.

    find_user_by_id(library_id)

Searches for a user in the system by their unique library ID and returns the `User` object if found.

    find_author_by_name(name)

Searches for an author in the system by their name and returns the `Author` object if found.

How to Run

1. Clone the repostitory or download the script.
2. Run the `main.py` script in a Python environment.
3. Follow the on-screen instructions to perform various operations like adding books, borrowing books, adding users, etc.

```
python main.py
```

Example

```
Welcome to the Library Management System!
Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit
Enter your choice: 1

Book Operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
Enter your choice: 1
Enter book title: "The Great Gatsby"
Enter author name: "F. Scott Fitzgerald"
Enter genre: "Fiction"
Enter publication date: "1925"
Book added successfully!
```
