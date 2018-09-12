# not yet completed script

import sqlite3

class Database:


    # constructor. when calling a class, only this one is executed
    def __init__(self,db):
        self.connection = sqlite3.connect(db)
        self.curs = self.connection.cursor()
        self.curs.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT,Year INTEGER, Isbn INTEGER)")
        self.connection.commit()

    def insert(self,Title,Author,Year,Isbn):
        self.curs.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(Title, Author, Year,Isbn))
        self.connection.commit()

    def view(self):
        self.curs.execute("SELECT * FROM books")
        rows=self.curs.fetchall()
        return rows

    # or empty strings " " as default values
    def search(self,Title=None,Author=None,Year=None,Isbn=None):
        self.curs.execute("SELECT * FROM books WHERE Title =? OR Author=? OR Year=? OR Isbn=?",(Title,Author,Year,Isbn))
        rows=self.curs.fetchall()
        return rows

    def deletion(self,id):
        self.curs.execute("DELETE FROM books WHERE id=?",(id,))
        self.connection.commit()

    def update(self,id,Title,Author,Year,Isbn):
        self.curs.execute("UPDATE books SET Title=?, Author=?, Year=?, Isbn=? WHERE id=?",(Title,Author,Year,Isbn,id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
