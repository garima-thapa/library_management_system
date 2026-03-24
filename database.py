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
    conn.close()
    
connect() #calling the connect function to actually create the database and table
    
    