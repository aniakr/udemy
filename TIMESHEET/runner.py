import tkinter as tk
import getpass
from TIMESHEET.timesheet_frame import Timesheet
from TIMESHEET.timesheet_db import Database


db=Database()

# db.add_user("Karolina","Nowak","KNowak","EU")

root=tk.Tk()
timesheet = Timesheet(root,db)
timesheet.mainloop()


