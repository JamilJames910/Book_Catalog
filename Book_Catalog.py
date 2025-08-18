import json
import os 

BOOKS_FILE = 'books.json'

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, 'r') as file:
        try:  
            return json.load(file)
        except json.JSONDecodeError:
            return []
    
def save_books(books):
    with open(BOOKS_FILE, 'w') as file: 
        json.dump(books,file, indent=4)

def add_book(): 
    book = {
        'Title': input("Enter book title: "),
        'Author': input("Enter author: "),
        'Genre': input("Enter genre: "),
        'Year': input("Enter year: "),
        'ISBN': input("Enter ISBN: "),
        'Status': input("Enter status (Read, Want to Read, etc.): ")
    }
    books = load_books()
    books.append(book)
    save_books(books)
    print("Book added successfully!\n")

def view_books(): 
    books = load_books()
    if not books: 
        print("No books in catalog.\n")
        return 
    print("\n--- Book Catalog ---")
    for idx, book in enumerate(books, 1):
        print(f"{idx}. {book['Title']} by {book ['Author']} ({book['Year']})")
        print(f"    Genre: {book['Genre']}, ISBN:  {book['ISBN']}, Status:  {book['Status']}")
    print()

def search_books(): 
    keyword = input("Enter keyword to search by Title, Author, or Genre: ").lower()
    books = load_books()
    matches = [b for b in books if keyword in b['Title'].lower() 
               or keyword in b['Author'].lower()
               or keyword in b['Genre'].lower()]
    if not matches: 
        print("No matchers found. \n")
    else: 
        print(f"\nFound {len(matches)} match(es):")
        for book in matches: 
            print(f"- {book['Title']} by {book['Author']} ({book['Year']})")
        print()

def update_book(): 
    books = load_books()
    view_books()
    try: 
        idx = int(input("Enter the book number to update: ")) - 1
        if 0 <= idx < len(books): 
            print("Leave field blank to keep current value.\n")
            for field in ['Title', 'Author', 'Genre', 'Year', 'ISBN', 'Status']:
                new_val = input(f"{field} [{books[idx][field]}]: ")
                if new_val: 
                    books[idx][field] = new_val
                save_books(books)
                print("Book updated successfully!\n")
            else: 
                print("Invalid book number.\n")
    except ValueError: 
        print("Invalid input. Please enter a number. \n")

def delete_book(): 
    books = load_books()
    view_books()
    try: 
        idx = int(input("Enter the book number to delete: ")) - 1 
        if 0 <= idx < len(books): 
            deleted = books.pop(idx)
            save_books(books)
            print(f"Deleted '{deleted['Title']}' successfully !\n")
        else:
            print("Invalid book number.\n")
    except ValueError: 
        print("Invalid input. Please enter a number. \n")

def main_menu(): 
    while True: 
        print("\n--- Book Catalog Menu ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")
    
        choice = input("Choose an option (1-6): ")
        if choice == '1': 
            add_book()
        elif choice == '2': 
            view_books()
        elif choice == '3': 
            search_books()
        elif choice == '4': 
            update_book()
        elif choice == '5': 
            delete_book()
        elif choice == '6': 
            print("Goodbye!")
            break 
        else: 
            print("Invalid choice. Please try again.\n")

if __name__ == '__main__': 
    main_menu()
