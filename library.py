'''
import sqlite3 #importing this so that python can work with SQlite databases.
def connect():
    conn=sqlite3.connect("library.db") #this will automatically create library named db if not exists

    cursor=conn.cursor() #creating a cursor object to execute SQL commands in the db

    cursor.execute(""" CREATE TABLE IF NOT EXISTS books
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title text,
                   author TEXT)
                   """)
    conn.commit()


    def add_book():
        title=title_entry.get()
        author=author_entry.get()
        if title=="" or author=="":
            status_label.config(text="please enter both title and author")
            return
        cursor.execute("INSERT INTO books (title, author) VALUES (?,?)",(title,author))
        conn.commit()
        title_entry.delete(0,END)
        author_entry.delete(0,END)
        list_books()
        status_label.config(text="book added!")


def list_books():
    global listbox
    listbox.delete(0, END)
        #IT will clear the current list in the listbox
    for row in backend.get_books():
        listbox.insert(END,row)
            #insert each book from the db into the listbox

def delete_selected():
    selected=listbox.get(ACTIVE)
    if not selected:
        status_label.config(text="Select a book to delete")
        return
    cursor.execute("DELETE FROM books WHERE id=?",(selected[0],))
    conn.commit()
    list_books()
    status_label.config(text="books deleted")


    #GUI layout
    root=Tk() #creating the main window
    root.title("Library management system")
    Label(root,text="Title").grid(row=0,column=0)
    #creating a label that says Title and placing it in row 0 and column 0

    title_entry=Entry(root)
    title_entry.grid(row=0,column=1)
    #creating the input box for the title and placing it next to the label
    Label(root,text="Author").grid(row=1,column=0)
    author_entry=Entry(root)
    author_entry.grid(row=1,column=1)

    Button(root,text="Add Book",command=add_book).grid(row=2,column=0)
    Button(root,text="Show Books",command=list_books).grid(row=2,column=1)
    Button(root,text="Delete Book",command=delete_selected).grid(row=3,column=0)


    listbox=Listbox(root,width=40)
    listbox.grid(row=4,column=0,columnspan=2)
    #it means create a listbox to display all books and stretch it across 2 columns
    
    root.mainloop()
    #start the GUI event loop, keeps the window open

'''