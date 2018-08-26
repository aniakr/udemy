# not yet completed script

import sqlite3

class Database:


    # constructor. when calling a class, only this one is executed
    def __init__(self,db):
        connection = sqlite3.connect(db)
        curs = connection.cursor()
        curs.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT,Year INTEGER, Isbn INTEGER)")
        connection.commit()
        connection.close()

    def insert(self,Title,Author,Year,Isbn):
        connection = sqlite3.connect("AK_bookstore.db")
        curs = connection.cursor()
        curs.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(Title, Author, Year,Isbn))
        connection.commit()
        connection.close()

    def view(self):
        connection = sqlite3.connect("AK_bookstore.db")
        curs = connection.cursor()
        curs.execute("SELECT * FROM books")
        rows=curs.fetchall()
        connection.close()
        return rows

    # or empty strings " " as default values
    def search(self,Title=None,Author=None,Year=None,Isbn=None):
        connection = sqlite3.connect("AK_bookstore.db")
        curs = connection.cursor()
        curs.execute("SELECT * FROM books WHERE Title =? OR Author=? OR Year=? OR Isbn=?",(Title,Author,Year,Isbn))
        rows=curs.fetchall()
        connection.close()
        return rows

    def deletion(self,id):
        connection = sqlite3.connect("AK_bookstore.db")
        curs = connection.cursor()
        curs.execute("DELETE FROM books WHERE id=?",(id,))
        connection.commit()
        connection.close()

    def update(self,id,Title,Author,Year,Isbn):
        connection = sqlite3.connect("AK_bookstore.db")
        curs = connection.cursor()
        curs.execute("UPDATE books SET Title=?, Author=?, Year=?, Isbn=? WHERE id=?",(Title,Author,Year,Isbn,id))
        connection.commit()
        connection.close()


