import datetime
from TIMESHEET.timesheet_db import Database
import tkinter as tk

def mandays_validation2(md_entry):
    new_mandays=""
    for letter in md_entry:
        if letter==",":
            letter="."
            new_mandays+=letter
        else:
            new_mandays += letter
    try:
        mandays=float(new_mandays)
        print(mandays)
        mod = mandays % 0.5
        if mod != 0:
            return 0
        else:
            return 1
    except ValueError:
        pass


def mandays_validation(md_entry):
    mandays=float(md_entry)
    print(mandays)
    mod = mandays % 0.5
    if mod != 0:
        return 0
    else:
        return 1



def month_choice():
    choice = []
    for i in range(1, 13):
        choice.append(str(datetime.date(2008, i, 1).strftime('%B')))
    return choice

NORM_FONT = ("Helvetica", 10)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()



# def get_selected(event):
#     global selected_tuple
#     if len(Listbox.curselection()) != 0:
#         index = Listbox.curselection()[0]
#         selected_tuple = Listbox.get(index)
#     else:
#         pass
#
# def update_dropdown_user(hub_choice):
#      dependant_choice=Database.get_all_users_depend(hub_choice)
#      variable_b.set=dependant_choice[0]


