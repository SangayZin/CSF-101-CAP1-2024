# Refrence

# https://docs.python.org/3/tutorial/classes.html
# https://realpython.com/python3-object-oriented-programming/


# Step 1: Create the Book class
class Book:
    def __init__(self, title, author):
        # Initialize the Book object with title and author
        self.title = title
        self.author = author
        self.is_available = True  # By default, the book is available when added

    def __str__(self):
        # To print a readable version of a book showing title, author, and availability status
        return f"{self.title} by {self.author} - {'Available' if self.is_available else 'Borrowed'}"


# Step 2: Create the Library class
    
# This class will manage the collection of books and handle borrowing and returning.
class Library:
    def __init__(self):
        # Initialize the Library with a list to store all books and a dictionary to track borrowed books
        self.books = []  # List to store
        self.borrowed_books = {}  # To track which user borrowed which book
        # Adding dummy data
        self.add_book(Book("Book A", "Author A"), show_message=False)
        self.add_book(Book("Book B", "Author B"), show_message=False)
        self.add_book(Book("Book C", "Author C"), show_message=False)

    def add_book(self, book, show_message=True):
        self.books.append(book)
        if show_message:
            print(f"Book '{book.title}' added to the library.")

    def view_all_books(self):
        # Display all the books in the library
        if len(self.books) == 0:
            print("No books available in the library.")
        else:
            print("All books in the library:")
            for book in self.books:
                print(book)

    def borrow_book(self, book_title, user):
        # Allow a user to borrow a book if it's available
        for book in self.books:
            if book.title == book_title and book.is_available:
                book.is_available = False # Mark the book as borrowed
                self.borrowed_books[book_title] = user # Track which user borrowed the book
                print(f"Book '{book_title}' borrowed by {user}.")
                return
        print(f"Book '{book_title}' is not available or already borrowed.")

    def return_book(self, book_title, user):
        # Allow a user to return a borrowed book
        if book_title in self.borrowed_books and self.borrowed_books[book_title] == user:
            for book in self.books:
                if book.title == book_title:
                    book.is_available = True # Maek the book as available again
                    del self.borrowed_books[book_title]
                    print(f"Book '{book_title}' returned by {user}.")
                    return
        print(f"Book '{book_title}' is not borrowed by {user}.") # Inform if the book wasn't borrowed by the user.


# Step 3: Create the User class
        
# This class represent a user which each has a name and can perform actions related to borrowing and returning Books.      
class User:
    def __init__(self, name):
        self.name = name  # User's name

    def borrow_book(self, library, book_title):
        library.borrow_book(book_title, self.name)  # Borrow a book

    def return_book(self, library, book_title):
        library.return_book(book_title, self.name)  # Return a book


# Step 4: Create the Admin class (inherits from User)
        
# This class represents an administrator in the library system
class Admin(User):
    def add_book(self, library, title, author):
        new_book = Book(title, author)  # Create a new book
        library.add_book(new_book)  # Add the book to the library

    def track_borrowed_books(self, library):
        if library.borrowed_books:
            print("Currently borrowed books:")
            for book, user in library.borrowed_books.items():
                print(f"'{book}' is borrowed by {user}.")
        else:
            print("No books are currently borrowed.")


# Step 5: Create the Main program Loop
            
# This function manages the flow of the system by handling user inputs, directing them to the appropriate menu, and executing the corresponding function.
def main():
    # Create a library instance that will store the collection of books and manage borrowed books.
    library = Library()  

    while True:
        print("\nWelcome to the Library Management System!")
        user_type = input("Are you an Admin or a User? (admin/user) : ").strip().lower()

        if user_type == "admin":
            password = input("Enter Admin password: ")
            if password == "admin123":
                admin = Admin("Admin")  # Instantiate admin here
                while True:
                    print("\nAdmin Menu:")
                    print("1. View all books")
                    print("2. Add a book")
                    print("3. View borrowed books with user details")
                    print("4. Exit Admin Menu")
                    print("5. Exit System")

                    choice = input("Choose an option: ")

                    if choice == "1":
                        library.view_all_books()
                    elif choice == "2":
                        title = input("Enter book title: ")
                        author = input("Enter book author: ")
                        admin.add_book(library, title, author)
                    elif choice == "3":
                        admin.track_borrowed_books(library)
                    elif choice == "4":
                        print("Exiting Admin Menu.")
                        break
                    elif choice == "5":
                        print("Thank you for using our library system.")
                        return  # Exit the entire system
                    else:
                        print("Invalid option. Try again.")
            else:
                print("Incorrect password. Access denied.")

        elif user_type == "user":
            user_name = input("Enter your name: ")
            user = User(user_name)
            while True:
                print("\nUser Menu:")
                print("1. View all books")
                print("2. Borrow a book")
                print("3. Return a book")
                print("4. Exit User Menu")
                print("5. Exit System")

                choice = input("Choose an option: ")

                if choice == "1":
                    library.view_all_books()
                elif choice == "2":
                    book_title = input("Enter the book title to borrow: ")
                    user.borrow_book(library, book_title)
                elif choice == "3":
                    book_title = input("Enter the book title to return: ")
                    user.return_book(library, book_title)
                elif choice == "4":
                    print("Exiting User Menu.")
                    break
                elif choice == "5":
                    print("Thank you for using our library system.")
                    return  # Exit the entire system
                else:
                    print("Invalid option. Try again.")
        else:
            print("Invalid input. Please specify 'admin' or 'user'.")

if __name__ == "__main__":
    main()
