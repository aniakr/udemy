import sqlite3

def create_table():
    connection = sqlite3.connect("lite_exercises.db")
    curs = connection.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = sqlite3.connect("lite_exercises.db")
    curs = connection.cursor()
    curs.execute("INSERT INTO store VALUES(?,?,?)",(item, quantity, price))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("lite_exercises.db")
    curs = connection.cursor()
    curs.execute("SELECT * FROM store")
    rows=curs.fetchall()
    connection.close()
    return rows

def deletion(item):
    connection = sqlite3.connect("lite_exercises.db")
    curs = connection.cursor()
    curs.execute("DELETE FROM store WHERE item=?",(item,))
    connection.commit()
    connection.close()

def update(quantity, price, item):
    connection = sqlite3.connect("lite_exercises.db")
    curs = connection.cursor()
    curs.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
    connection.commit()
    connection.close()

# create_table()
# insert("Water Glass",10,7)
# insert("Coffe Cup",12,5.6)
# update(11,6,"Water Glass")
# deletion("Water Glass")
print(view())