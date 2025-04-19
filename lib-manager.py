import json  # to save and load data
import os    # to check if file exists

data_file = 'library.json'  # changed to json for clarity

def load_library():
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Warning: Library file is corrupted or empty. Starting fresh.")
            return []
    return []

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input("Have you read the book? (yes/no): ").lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(new_book)
    save_library(library)
    print(f"\n✅ Book '{title}' by {author} added to the library successfully!\n")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").lower()
    initial_length = len(library)
    updated_library = [book for book in library if book['title'].lower() != title]
    
    if len(updated_library) < initial_length:
        save_library(updated_library)
        print(f"\n✅ Book '{title}' removed from the library successfully.\n")
    else:
        print(f"\n❌ Book '{title}' not found in the library.\n")
    
    return updated_library

def search_library(library):
    search_by = input("Search by title or author: ").lower()
    if search_by not in ['title', 'author']:
        print("❌ Invalid search criteria. Use 'title' or 'author'.")
        return

    search_term = input(f"Enter the {search_by} to search for: ").lower()

    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        print("\n🔍 Search Results:")
        for book in results:
            status = "Read" if book['read'] else "Unread"
            print(f"- {book['title']} by {book['author']} ({book['year']}) - {status}")
    else:
        print(f"\n❌ No books found matching '{search_term}' in {search_by}.")

def display_books(library):
    if library:
        print("\n📚 All Books in Library:")
        for book in library:
            status = "Read" if book['read'] else "Unread"
            print(f"- {book['title']} by {book['author']} ({book['year']}) - {status}")
    else:
        print("📭 The library is empty.")

def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    per_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print("\n📊 Library Statistics:")
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {per_read:.2f}%")

def main():
    library = load_library()
    while True:
        print("\n====== 📖 Library Menu ======")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search the library")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            library = remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("\n👋 Have a good day!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

