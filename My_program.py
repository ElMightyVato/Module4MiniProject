# library_system.py

from My_classes import Book, User, Author

# Initialize data stores
books = []
users = []
authors = []

def show_main_menu():
    print("Welcome to the Library Management System!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")

def show_book_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")

def show_user_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")

def show_author_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")

def main():
    while True:
        show_main_menu()
        try:
            choice = input("Enter your choice: ")
            if choice == "1":
                show_book_menu()
                book_choice = input("Enter your choice: ")
                if book_choice == "1":
                    # Add a new book
                    title = input("Enter book title: ")
                    author = input("Enter author name: ")
                    genre = input("Enter genre: ")
                    publication_date = input("Enter publication date: ")
                    books.append(Book(title, author, genre, publication_date))
                    print("Book added successfully!")
                elif book_choice == "2":
                    # Borrow a book
                    title = input("Enter book title to borrow: ")
                    book = find_book_by_title(title)
                    if book:
                        user_id = input("Enter user library ID: ")
                        user = find_user_by_id(user_id)
                        if user:
                            user.borrow_book(book)
                            print("Book borrowed successfully!")
                        else:
                            print("User not found.")
                    else:
                        print("Book not found.")
                elif book_choice == "3":
                    # Return a book
                    title = input("Enter book title to return: ")
                    book = find_book_by_title(title)
                    if book:
                        user_id = input("Enter user library ID: ")
                        user = find_user_by_id(user_id)
                        if user:
                            user.return_book(book)
                            print("Book returned successfully!")
                        else:
                            print("User not found.")
                    else:
                        print("Book not found.")
                elif book_choice == "4":
                    # Search for a book
                    title = input("Enter book title to search: ")
                    book = find_book_by_title(title)
                    if book:
                        print(book.display_book_details())
                    else:
                        print("Book not found.")
                elif book_choice == "5":
                    # Display all books
                    for book in books:
                        print(book.display_book_details())
                else:
                    print("Invalid choice, please try again.")
        
            elif choice == "2":
                show_user_menu()
                user_choice = input("Enter your choice: ")
                if user_choice == "1":
                    # Add a new user
                    name = input("Enter user name: ")
                    library_id = input("Enter user library ID: ")
                    users.append(User(name, library_id))
                    print("User added successfully!")
                elif user_choice == "2":
                    # View user details
                    user_id = input("Enter user library ID to view details: ")
                    user = find_user_by_id(user_id)
                    if user:
                        print(user.display_user_details())
                    else:
                        print("User not found.")
                elif user_choice == "3":
                    # Display all users
                    for user in users:
                        print(user.display_user_details())
                else:
                    print("Invalid choice, please try again.")
        
            elif choice == "3":
                show_author_menu()
                author_choice = input("Enter your choice: ")
                if author_choice == "1":
                    # Add a new author
                    name = input("Enter author name: ")
                    biography = input("Enter biography: ")
                    authors.append(Author(name, biography))
                    print("Author added successfully!")
                elif author_choice == "2":
                    # View author details
                    author_name = input("Enter author name to view details: ")
                    author = find_author_by_name(author_name)
                    if author:
                        print(author.display_author_details())
                    else:
                        print("Author not found.")
                elif author_choice == "3":
                    # Display all authors
                    for author in authors:
                        print(author.display_author_details())
                else:
                    print("Invalid choice, please try again.")
        
            elif choice == "4":
                print("Thank you for using the Library Management System. Goodbye!")
                break
            else:
                print("Invalid main menu choice, please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")
            continue

def find_book_by_title(title):
    try:
        for book in books:
            if book.get_title() == title:
                return book
        return None
    except Exception as e:
        print(f"Error searching for book by title: {e}")
        return None


def find_user_by_id(library_id):
    try:
        for user in users:
            if user.get_library_id() == library_id:
                return user
        return None
    except Exception as e:
        print(f"Error looking for user by their ID: {e}")

def find_author_by_name(name):
    try:
        for author in authors:
            if author.get_name() == name:
                return author
        return None
    except Exception as e:
        print(f"Error searching for author by name: {e}")
        return None

if __name__ == "__main__":
    main()
