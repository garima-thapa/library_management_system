import sqlite3
#function to add a book to our db
def add_book(title, author):
    conn=sqlite3.connect("library.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (?,?)",(title,author))
    #the ? are the placeholders and title, author fills then safely i.e prevents errors and attacks
    conn.commit()
    conn.close()

    #fn to get all books from the db
def get_books():
        conn=sqlite3.connect("library.db")
        cursor=conn.cursor() #creating a cursor object to run the sql commands
        cursor.execute("SELECT * FROM books")
        rows=cursor.fetchall()
        #this will fetch all rows from the result of query and store then in 'rows'
        conn.close()
        return rows #this will return the list of books to the part of the program that called this fn
    

    #fn to delete a book from the db
def delete_book(book_id):
        conn=sqlite3.connect("library.db")
        cursor=conn.cursor()
        cursor.execute("DELETE FROM books where id=?",(book_id,))
        #the book_id is a tuple which will fills the 
        #placeholder '?' safely and sql code will execute if both matches
        conn.commit()
        conn.close()
        