# Book Catalog 📚

A simple, intuitive Python command-line program to manage a personal book catalog.
Perfect for adding, viewing, searching, updating, and deleting books stored in a JSON file.

## Features ✨

✅ Add new books with details: Title, Author, Genre, Year, ISBN, and Status.
✅ View all books in the catalog.
✅ Search books by Title, Author, or Genre.
✅ Update existing book information.
✅ Delete books from the catalog.
✅ Stores data locally in a `books.json` file.
✅ Works across different operating systems (Windows, macOS, Linux).

## Table of Contents

* Installation
* Usage
* Example
* Project Structure
* Contributing
* Contact

## Installation 🛠️

Clone this repository:

```bash
git clone https://github.com/JamilJames910/Book_Catalog.git
cd Book_Catalog
```

Make sure you have Python 3.x installed.

(Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

No additional dependencies are required—Python's built-in `json` module handles everything.

## Usage 💻

Run the script:

```bash
python Book_Catalog.py
```

You will be prompted to:

* Enter book details (Title, Author, Genre, Year, ISBN, Status).
* Search books by Title, Author, or Genre.
* Update or delete books.

The program will store all data in `books.json` and provide clear feedback for every action.

## Example

Add a new book:

```bash
Enter Title: The Great Gatsby
Enter Author: F. Scott Fitzgerald
Enter Genre: Fiction
Enter Year: 1925
Enter ISBN: 9780743273565
Enter Status: Read
```

View all books:

```bash
python Book_Catalog.py list
```

Output:

```
1. The Great Gatsby | F. Scott Fitzgerald | Fiction | 1925 | 9780743273565 | Read
```

Update a book:

```bash
python Book_Catalog.py update 1
```

Delete a book:

```bash
python Book_Catalog.py delete 1
```

Output:

```
🗑️ Book deleted: The Great Gatsby
```

## Project Structure 🗂️

Book_Catalog
├── Book_Catalog.py       # Main script
├── books.json            # Local book storage (created automatically)
├── README.md             # Project documentation
└── .gitignore            # Git ignore file

## Contributing 🤝

Contributions, suggestions, and improvements are welcome!

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a Pull Request.

## Contact ✉️

Created with ❤️ by Jamil James

GitHub: [JamilJames910](https://github.com/JamilJames910)
Email: [Jamil.i.James1@gmail.com](mailto:Jamil.i.James1@gmail.com)
