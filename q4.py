import re

books = {}        git add file name

book_ids = set() 

def add_book():
    book_id = input("Enter Book ID: ")

    if book_id in book_ids:
        print("Duplicate ID! Book already exists.")
        return
    
    name = input("Book Name: ")
    author = input("Author: ")
    category = input("Category: ")

    books[book_id] = {"name": name, "author": author, "category": category}
    book_ids.add(book_id)

    with open("library.txt", "a") as f:
        f.write(f"{book_id},{name},{author},{category}\n")

    print("Book added successfully!\n")


def search_book():
    keyword = input("Enter keyword to search: ")
    pattern = re.compile(keyword, re.IGNORECASE)

    print("\nSearch Results:")
    for bid, info in books.items():
        if (pattern.search(info["name"]) or 
            pattern.search(info["author"]) or
            pattern.search(info["category"])):
            print(bid, info)


def update_book():
    book_id = input("Enter Book ID to update: ")
    if book_id not in books:
        print("Book not found!")
        return
    
    name = input("New Name: ")
    author = input("New Author: ")
    category = input("New Category: ")

    books[book_id] = {"name": name, "author": author, "category": category}
    print("Book updated!\n")


def delete_book():
    book_id = input("Enter Book ID to delete: ")
    if book_id in books:
        del books[book_id]
        print("Book deleted!\n")
    else:
        print("Book not found!")


while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        add_book()
    elif ch == '2':
        search_book()
    elif ch == '3':
        update_book()
    elif ch == '4':
        delete_book()
    else:
        break
