from tkinter import *
from tkinter import font
# tkinter is a module which will import everything to creater
#GUI windows, buttons, labels etc
import backend
#here i have imported the backend.py file that handles db operations
 
'''
  #fn to list all the books in the GUI
def list_books():
    listbox.delete(0, END)
        #IT will clear the current list in the listbox
    for row in backend.get_books():
        listbox.insert(END,row)
            #insert each book from the db into the listbox


'''
 #fn to list all the books in the GUI
def list_books():
    global listbox,current_books
    listbox.delete(0, END)
    current_books=backend.get_books()
        #IT will clear the current list in the listbox
    for i,row in enumerate(backend.get_books(),start=1):
        display_text=f"{i}. {row[1]} by {row[2]}"
        listbox.insert(END,display_text)
            #insert each book from the db into the listbox



 #function to add a book using the GUI input
def add_book():
    global title_entry,author_entry
    title=title_entry.get() #get the text form the title input box
    author=author_entry.get() 
    backend.add_book(title,author)
    #here i am calling the backend fn to add the book
    list_books()
    #refresh the list of books in the GUI to show the new book

'''
    #fn to list all the books in the GUI
    def list_books():
        listbox.delete(0, END)
        #IT will clear the current list in the listbox
        for row in backend.get_books():
            listbox.insert(END,row)
            #insert each book from the db into the listbox
'''

#function to delete the selected book from the databse and GUI
'''
def delete_selected():
    selected=listbox.get(ACTIVE)
    book_id=selected
    #getting the currently selected item in the listbox
    backend.delete_book(selected[0])
    #here i am passing the book's id to the backend delete fn
    list_books()
    #refreshing the listbox to show the updated list
'''

def delete_selected():
    try:
        index = listbox.curselection()[0]
        book_id = current_books[index][0]  # real DB id
        backend.delete_book(book_id)
        list_books()
        status_label.config(text="Book deleted successfully!")
    except IndexError:
        status_label.config(text="No book selected.")



    #GUI layout
root=Tk() #creating the main window
root.title("Library management system")
root.geometry("600x400")
root.configure(bg="#f0f0f0")
#custom font
my_font=font.Font(family="Helvetica",size=12,weight="bold")
Label(root,text="Title",font=my_font,bg="pink").grid(row=0,column=0,padx=10,pady=10)
    #creating a label that says Title and placing it in row 0 and column 0

title_entry=Entry(root,width=30)
title_entry.grid(row=0,column=1,padx=10,pady=10)
    #creating the input box for the title and placing it next to the label
Label(root,text="Author",font=my_font,bg="pink").grid(row=1,column=0,padx=10,pady=10)
author_entry=Entry(root,width=30)
author_entry.grid(row=1,column=1,padx=10,pady=10)

Button(root,text="Add Book",command=add_book,bg="lightblue",font=my_font).grid(row=2,column=0,padx=10,pady=10)
Button(root,text="Show Books",command=list_books,bg="lightgreen",font=my_font).grid(row=2,column=1,padx=10,pady=10)
Button(root,text="Delete Book",command=delete_selected,bg="salmon",font=my_font).grid(row=3,column=0,padx=10,pady=10)


listbox=Listbox(root,width=50,height=10)
listbox.grid(row=4,column=0,columnspan=2,sticky="nsew", padx=10, pady=10)
    #it means create a listbox to display all books and stretch it across 2 columns

    # Make listbox expandable
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(1, weight=1)

scrollbar = Scrollbar(root)
scrollbar.grid(row=4, column=2, sticky="ns")
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Status bar
status_label = Label(root, text="", bg="#f0f0f0", fg="blue", anchor="w")
status_label.grid(row=5, column=0, columnspan=3, sticky="we", padx=10, pady=5)


root.mainloop()
    #start the GUI event loop, keeps the window open


