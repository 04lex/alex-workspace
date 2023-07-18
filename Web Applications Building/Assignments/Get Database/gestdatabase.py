import sqlite3

def create_table():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Books
                 (id INTEGER PRIMARY KEY,
                  title TEXT,
                  year INTEGER)''')
    conn.commit()
    conn.close()

def insert_book():
    title = input("Insert book title: ")
    year = int(input("Insert book year: "))

    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute("INSERT INTO Books (title, year) VALUES (?, ?)", (title, year))
    conn.commit()
    conn.close()

def read_books():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Books")
    books = c.fetchall()
    conn.close()

    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Year: {book[2]}")

create_table()

while True:
    print("\n1. Add book")
    print("2. Show books")
    print("3. Exit")

    choice = input("Insert choice: ")

    if choice == '1':
        insert_book()
    elif choice == '2':
        read_books()
    elif choice == '3':
        break
    else:
        print("Invalid, please insert again.")
