import datetime
from TIMESHEET.timesheet_db import Database


def month_choice():
    choice = []
    for i in range(1, 13):
        choice.append(str(datetime.date(2008, i, 1).strftime('%B')))
    return choice


def get_selected(event):
    global selected_tuple
    if len(Listbox.curselection()) != 0:
        index = Listbox.curselection()[0]
        selected_tuple = Listbox.get(index)
    else:
        pass


