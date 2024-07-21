def add_book(title, author, genre):
    return (title, author, genre)  # Return the book details as a tuple

def add_to_library(library, book_set, book):
    if book in book_set:
        print("Book already exists in the library.")  # Check for duplicates
        return
    library.append(book)  # Add book to the library list
    book_set.add(book)  # Add book to the set for duplicate checking
    print("Book added successfully.")  # Confirm book addition

def remove_from_library(library, book_set, title):
    for book in library:
        if book[0] == title:  # Check if the book title matches
            library.remove(book)  # Remove book from the library list
            book_set.remove(book)  # Remove book from the set
            print("Book removed successfully.")  # Confirm book removal
            return
    print("Book not found.")  # Inform if the book was not found

def search_books(library, search_term):
    found_books = [book for book in library if search_term.lower() in book[0].lower() or search_term.lower() in book[1].lower()]
    if found_books:
        print("Books found:")  # List of books matching the search term
        for book in found_books:
            print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")
    else:
        print("No books found.")  # Inform if no books matched the search term

def list_books(library):
    if not library:
        print("Library is empty.")  # Inform if the library is empty
    else:
        print("Current library:")  # List all books in the library
        for book in library:
            print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")

def categorize_books(library):
    categories = {}
    for book in library:
        genre = book[2]  # Get the genre of the book
        if genre not in categories:
            categories[genre] = []  # Create a new list for the genre if it doesn't exist
        categories[genre].append(book)  # Add the book to the appropriate genre list
    
    if not categories:
        print("No books to categorize.")  # Inform if there are no books to categorize
    else:
        for genre, books in categories.items():
            print(f"Genre: {genre}")  # Print each genre and the books under it
            for book in books:
                print(f"  Title: {book[0]}, Author: {book[1]}")

def main():
    library = []  # List to store books as tuples
    book_set = set()  # Set to store unique books
    while True:
        # Main menu
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for books")
        print("4. List all books")
        print("5. Categorize books")
        print("6. Exit")
        choice = input("Enter a choice: ")
        
        if choice == '1':
            # Add a new book
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            book = add_book(title, author, genre)  # Create the book tuple
            add_to_library(library, book_set, book)  # Add the book to the library
        elif choice == '2':
            # Remove a book
            title = input("Enter book title to remove: ")
            remove_from_library(library, book_set, title)  # Remove the book from the library
        elif choice == '3':
            # Search for books
            search_term = input("Enter title or author to search: ")
            search_books(library, search_term)  # Search for books matching the term
        elif choice == '4':
            # List all books
            list_books(library)  # Display all books in the library
        elif choice == '5':
            # Categorize and display books by genre
            categorize_books(library)  # Categorize and display books by genre
        elif choice == '6':
            # Exit the system
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice.")  # Inform if the user enters an invalid choice

if __name__ == "__main__":
    main()  # Run the main function if the script is executed
