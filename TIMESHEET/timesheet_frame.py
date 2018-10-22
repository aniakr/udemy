import getpass
import tkinter as tk
from TIMESHEET.timesheet_service import month_choice
import datetime
from TIMESHEET.timesheet_db import Database


class Timesheet(tk.Frame):
    Name_L = 1
    now = datetime.datetime.now()
    current_month = now.strftime("%B")
    current_year = now.year

    def __init__(self,master,database,*args,**kwargs):
        self.db=database
        current_user = self.db.user_from_login(getpass.getuser())
        users_list= self.db.get_all_users()
        hub_list=self.db.get_all_items('hub_name','hubs')
        hub_default=self.db.hub_default(current_user)

        tk.Frame.__init__(self,*args,**kwargs)
        master.wm_title("Timesheet")
        master.geometry("400x600")
        self.photo = tk.PhotoImage(file="kalender_2.gif")
        tk.Label(master, image=self.photo, bg="white").grid(row=0, column=0, columnspan=4)
        Name_L = tk.Label(master, text="Name")
        Name_L.grid(row=1, column=0, sticky=tk.W)
        # buttons

        Name_L = tk.Label(master, text="Name")
        Name_L.grid(row=1, column=0, sticky=tk.W)
        Hub_L = tk.Label(master, text="Hub")
        Hub_L.grid(row=1, column=2, sticky=tk.W)
        Month_L = tk.Label(master, text="Month")
        Month_L.grid(row=2, column=0, sticky=tk.W)
        Year_L = tk.Label(master, text="Year")
        Year_L.grid(row=2, column=2, sticky=tk.W)
        Activity_L = tk.Label(master, text="Activity")
        Activity_L.grid(row=3, column=0, sticky=tk.W)
        Comment_L = tk.Label(master, text="Comment")
        Comment_L.grid(row=4, column=0, sticky=tk.W)
        Entry_box_L = tk.Label(master, text="Your input for: ")
        Entry_box_L.grid(row=5, column=0, sticky=tk.W)

        self.Entry_box = tk.Listbox(master, height=6, width=35)
        self.Entry_box.grid(row=8, column=0, rowspan=6, columnspan=3, sticky=tk.N + tk.S +tk.W + tk.E)

        yscroll = tk.Scrollbar(master)
        yscroll.grid(row=8, column=3, rowspan=6, sticky=tk.N + tk.S + tk.W)
        self.Entry_box.configure(yscrollcommand=yscroll.set)
        yscroll.configure(command=self.Entry_box.yview)

        self.Name_entry_val = tk.StringVar()
        self.Name_entry_val.set(*current_user)
        Name_entry=tk.OptionMenu(master, self.Name_entry_val,*users_list)
        Name_entry.grid(row=1, column=1, sticky=tk.W)

        self.Month_entry_val=tk.StringVar()
        self.Month_entry_val.set(Timesheet.current_month)
        Month_entry=tk.OptionMenu(master, self.Month_entry_val,*month_choice())
        Month_entry.grid(row=2, column=1,sticky=tk.W)

        self.Hub_entry_val=tk.StringVar()
        self.Hub_entry_val.set(hub_default)
        Hub_entry=tk.OptionMenu(master, self.Hub_entry_val,*hub_list)
        Hub_entry.grid(row=1, column=3,sticky=tk.W)

        self.Year_entry_val=tk.StringVar()
        self.Year_entry_val.set(self.current_year)
        Year_entry = tk.OptionMenu(master, self.Year_entry_val, self.current_year-1,self.current_year, self.current_year+1)
        Year_entry.grid(row=2, column=3,sticky=tk.W)

        self.Activity_entry_val=tk.StringVar()
        Activity_entry = tk.OptionMenu(master, self.Activity_entry_val, "SOX", "PWC", "Audit")
        Activity_entry.grid(row=3, column=1,sticky=tk.W)

        self.Comment_entry_value=tk.StringVar()
        Comment_entry=tk.Entry(master, textvariable=self.Comment_entry_value)
        Comment_entry.grid(row=4, column=1,sticky=tk.W)

        button_submit = tk.Button(master, text="Submit", bg="green", width=15, command=self.submit)
        button_submit.grid(row=6, column=1)

        button_delete=tk.Button(master, text="Delete selected",bg="red", width=15, command=self.delete_command)
        button_delete.grid(row=7, column=1)

    def delete_command(self):
        print('deleting')

    def submit(self):
        self.db.insert_entry(self.Name_entry_val.get(),self.Activity_entry_val.get(),self.Month_entry_val.get(),self.Year_entry_val.get())
        print('inserting')
        self.view_command()

    def view_command(self):
        self.Entry_box.delete(0, tk.END)
        month_entry = self.db.display_month(self.Month_entry_val.get(),self.Year_entry_val.get())
        for entry in month_entry:
             self.Entry_box.insert(tk.END, entry)

