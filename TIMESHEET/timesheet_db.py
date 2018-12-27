import psycopg2

# https://www.youtube.com/watch?v=8gd1DlXwzlY
from psycopg2 import sql


class Database:
    init_test_data = True

    def __init__(self, db_name):
        self.connection = psycopg2.connect("dbname="+ db_name + " user=postgres password=adminsql host=localhost port=5432")
        self.curs = self.connection.cursor()
        self.curs.execute(
            "CREATE TABLE IF NOT EXISTS Users (id SERIAL, F_Name VARCHAR(20), Login VARCHAR(8), Hub INTEGER)")
        self.curs.execute("CREATE TABLE IF NOT EXISTS Hubs (id INTEGER, Hub_Name VARCHAR(3))")
        self.curs.execute(
            "CREATE TABLE IF NOT EXISTS Activities (id SERIAL, Activity TEXT, Hub INTEGER, Icap INTEGER)")
        self.curs.execute("CREATE TABLE IF NOT EXISTS ICAP (id INTEGER, ICAP_Name TEXT)")
        self.curs.execute(
            "CREATE TABLE IF NOT EXISTS Timesheet_entries (id SERIAL PRIMARY KEY, F_Name VARCHAR(20), Activity TEXT, Month TEXT, Year TEXT, "
            "Mandays REAL, Icap INTEGER, Comment VARCHAR(50))")
        self.connection.commit()
        if(self.init_test_data):
            self.populate_test_data()

    def populate_test_data(self):
        self.curs.execute("INSERT INTO users(F_Name, Login, Hub)  SELECT 'Anna Krach','Ania',1 WHERE NOT EXISTS (SELECT * FROM users)")
        self.curs.execute(
            "INSERT INTO users(F_Name, Login, Hub)  SELECT 'Tommy Tommy','TTom',2 WHERE NOT EXISTS (SELECT * FROM users WHERE users.Login='TTom')")
        self.curs.execute("INSERT INTO Hubs(id,Hub_name)  SELECT 2,'AP' WHERE NOT EXISTS (SELECT * FROM hubs)")
        self.curs.execute("INSERT INTO Hubs(id,Hub_name)  SELECT 1,'EU' WHERE NOT EXISTS (SELECT * FROM hubs WHERE Hubs.id=1)")
        self.curs.execute("INSERT INTO Activities (Activity,Hub,ICAP)  SELECT 'SOX',1,1 WHERE NOT EXISTS (SELECT * FROM Activities)")
        self.curs.execute(
            "INSERT INTO  Timesheet_entries (F_Name, Activity, Month,Year, Mandays) SELECT 'Tommy Tommy','SOX','October','2018','5' WHERE NOT EXISTS (SELECT * FROM Timesheet_entries)")
        self.connection.commit()

    def insert_entry(self, F_Name, Activity, Month,Year, Mandays, Comment):
        self.curs.execute("INSERT INTO  Timesheet_entries (F_Name, Activity, Month,Year, Mandays, Comment) VALUES(%s,%s,%s,%s,%s,%s)", (F_Name, Activity, Month,Year, Mandays,Comment))
        self.connection.commit()

    def add_user(self, F_Name, Login, Hub):
        self.curs.execute("INSERT INTO Users (F_Name, Login, Hub) VALUES(%s,%s,%s)",
                          (F_Name, Login, Hub))
        self.connection.commit()

    def user_from_login(self, current_user):
        self.curs.execute("SELECT F_Name FROM Users WHERE Login=%s", (current_user,))
        user = self.curs.fetchone()
        return user

    def get_all_users(self):
        self.curs.execute("SELECT F_Name FROM Users")
        users = self.curs.fetchall()
        all_users=[]
        for item in users:
            all_users.append(item[0])
        return all_users

    def get_all_users_depend(self,key):
        self.curs.execute("SELECT u.F_Name FROM Users u INNER JOIN hubs h ON h.id=u.hub WHERE h.hub_name = %s",(key,))
        users = self.curs.fetchall()
        all_users=[]
        for item in users:
            all_users.append(item[0])
        return all_users


    def hub_default(self,user):
        self.curs.execute("SELECT Hub_Name FROM Hubs h INNER JOIN users u ON h.id = u.hub WHERE u.F_Name = %s",(user,))
        hub = self.curs.fetchone()
        return hub

    def get_all_items(self,column,table):
        self.curs.execute(sql.SQL("SELECT {} FROM {}").format(sql.Identifier(column),sql.Identifier(table)))
        items = self.curs.fetchall()
        # all_items=[]
        # for item in items:
        #     all_items.append(item)
        # return all_items
        return items

    def display_month(self, month, year, user):
        self.curs.execute("SELECT * FROM Timesheet_entries WHERE month=%s AND year=%s AND F_Name=%s",(month,year,user))
        month_entry = self.curs.fetchall()
        all_items=[]
        for item in month_entry:
            all_items.append(item)
        return all_items

    def get_all(self):
        self.curs.execute("SELECT * FROM Users")
        users = self.curs.fetchall()
        return users

    def delete_selected(self,ID_number):
        self.curs.execute("DELETE FROM Timesheet_entries WHERE id=%s",(ID_number,))
        self.connection.commit()

