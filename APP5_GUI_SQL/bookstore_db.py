import sqlite3

def connect():
    connection = sqlite3.connect("AK_bookstore.db")
    curs = connection.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT,Year INTEGER, Isbn INTEGER)")
    connection.commit()
    connection.close()

def insert(Title,Author,Year,Isbn):
    connection = sqlite3.connect("AK_bookstore.db")
    curs = connection.cursor()
    curs.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(Title, Author, Year,Isbn))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("AK_bookstore.db")
    curs = connection.cursor()
    curs.execute("SELECT Title, Author, Year,Isbn FROM books")
    rows=curs.fetchall()
    connection.close()
    return rows


# or empty strings " " as default values
def search(Title=None,Author=None,Year=None,Isbn=None):
    connection = sqlite3.connect("AK_bookstore.db")
    curs = connection.cursor()
    curs.execute("SELECT Title, Author, Year,Isbn FROM books WHERE Title =? OR Author=? OR Year=? OR Isbn=?",(Title,Author,Year,Isbn))
    rows=curs.fetchall()
    connection.close()
    return rows


def deletion(id):
    connection = sqlite3.connect("AK_bookstore.db")
    curs = connection.cursor()
    curs.execute("DELETE FROM books WHERE id=?",(id,))
    connection.commit()
    connection.close()

def update(id,Title,Author,Year,Isbn):
    connection = sqlite3.connect("AK_bookstore.db")
    curs = connection.cursor()
    curs.execute("UPDATE books SET Title=?, Author=?, Year=?, Isbn=? WHERE id=?",(Title,Author,Year,Isbn,id))
    connection.commit()
    connection.close()

# call function so that it is always executed when gui is run
connect()
# insert("Shogun","James Clavell",1980,11345678)
deletion(6)
# update(1,"King Rats","James Clavell",1980,11345678)
print(view())
# print(search(Author="James Clavell"))