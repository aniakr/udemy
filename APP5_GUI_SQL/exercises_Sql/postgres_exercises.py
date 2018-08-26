import psycopg2

def create_table():
    connection = psycopg2.connect("dbname='database_python' user='postgres' "
                                  "password='adminsql' host='localhost' port='5432'")
    curs = connection.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = psycopg2.connect("dbname='database_python' user='postgres' "
                                  "password='adminsql' host='localhost' port='5432'")
    curs = connection.cursor()
    #not recommended
    # curs.execute("INSERT INTO store VALUES('%s','%s','%s')"%(item, quantity, price))
    curs.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    connection.commit()
    connection.close()

def view():
    connection = psycopg2.connect("dbname='database_python' user='postgres' "
                                  "password='adminsql' host='localhost' port='5432'")
    curs = connection.cursor()
    curs.execute("SELECT * FROM store")
    rows=curs.fetchall()
    connection.close()
    return rows

def deletion(item):
    connection = psycopg2.connect("dbname='database_python' user='postgres' "
                                  "password='adminsql' host='localhost' port='5432'")
    curs = connection.cursor()
    curs.execute("DELETE FROM store WHERE item=%s",(item,))
    connection.commit()
    connection.close()

def update(quantity, price, item):
    connection = psycopg2.connect("dbname='database_python' user='postgres' "
                                  "password='adminsql' host='localhost' port='5432'")
    curs = connection.cursor()
    curs.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
    connection.commit()
    connection.close()

#create_table()
# insert("Apple",10,15)
# insert("Coffe Cup",12,5.6)
update(11,6,"Apple")
# deletion("Coffe Cup")
print(view())