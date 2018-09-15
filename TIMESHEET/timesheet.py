from tkinter import *
import datetime
import getpass

now=datetime.datetime.now()
current_month=now.strftime("%B")
current_year=now.year
current_user=getpass.getuser()

def month_choice():
    choice=[]
    for i in range(1,13):
        choice.append(str(datetime.date(2008, i, 1).strftime('%B')))
    return choice


def get_selected_row(event):
    global selected_tuple
    if len(Listbox.curselection()) != 0:
        index = Listbox.curselection()[0]
        selected_tuple=Listbox.get(index)
    else:
        pass

def submit():
    Listbox.insert(END,Name_entry_val.get(),
                   Activity_entry_val.get())

def delete_command():
    Listbox.delete(0, END)



timesheet=Tk()
timesheet.wm_title("IS IC Timesheet Form")

photo=PhotoImage(file="kalender_2.gif")
Label(timesheet,image=photo,bg="white").grid(row=0,column=0, columnspan=4)

# https://stackoverflow.com/questions/28518072/play-animations-in-gif-with-tkinter

# Labels
Name_L=Label(timesheet,text="Name")
Name_L.grid(row=1, column=0, sticky=W)

Hub_L=Label(timesheet,text="Hub")
Hub_L.grid(row=1, column=2,sticky=W)

Month_L=Label(timesheet,text="Month")
Month_L.grid(row=2, column=0,sticky=W)

Year_L=Label(timesheet,text="Year")
Year_L.grid(row=2, column=2,sticky=W)

Activity_L=Label(timesheet,text="Activity")
Activity_L.grid(row=3, column=0,sticky=W)

Comment_L=Label(timesheet,text="Comment")
Comment_L.grid(row=4, column=0,sticky=W)

Listbox_L=Label(timesheet,text="Your input for: ")
Listbox_L.grid(row=5, column=0,sticky=W)


# Listbox
Listbox=Listbox(timesheet, height=6, width=35)
Listbox.grid(row=8, column=0, rowspan=6, columnspan=3, sticky=N + S + W + E)

yscroll=Scrollbar(timesheet)
yscroll.grid(row=8, column=3, rowspan=6, sticky=N+S+W)
Listbox.configure(yscrollcommand=yscroll.set)
yscroll.configure(command=Listbox.yview)

# Listbox1.bind('<<ListboxSelect>>',get_selected_row)

# Entry box
Name_entry_val=StringVar()
Name_entry_val.set(current_user)
Name_entry=OptionMenu(timesheet, Name_entry_val,"Ania","Karola")
Name_entry.grid(row=1, column=1, sticky=W)

Month_entry_val=StringVar()
Month_entry_val.set(current_month)
Month_entry=OptionMenu(timesheet, Month_entry_val,*month_choice())
Month_entry.grid(row=2, column=1,sticky=W)

Hub_entry_val=StringVar()
Hub_entry_val.set("Krakow")
Hub_entry=OptionMenu(timesheet, Hub_entry_val,"Asia","Krakow", "Buenos", "HQ")
Hub_entry.grid(row=1, column=3,sticky=W)

Year_entry_val=StringVar()
Year_entry_val.set(current_year)
Year_entry = OptionMenu(timesheet, Year_entry_val, current_year-1,current_year, current_year+1)
Year_entry.grid(row=2, column=3,sticky=W)

Activity_entry_val=StringVar()
Activity_entry = OptionMenu(timesheet, Activity_entry_val, "SOX", "PWC", "Audit")
Activity_entry.grid(row=3, column=1,sticky=W)

Comment_entry_value=StringVar()
Comment_entry=Entry(timesheet, textvariable=Comment_entry_value)
Comment_entry.grid(row=4, column=1,sticky=W)

# buttons
button_submit=Button(timesheet, text="Submit", bg="green", width=15, command=submit)
button_submit.grid(row=6, column=1)

button_delete=Button(timesheet, text="Delete selected",bg="red", width=15, command=delete_command)
button_delete.grid(row=7, column=1)
# https://stackoverflow.com/questions/40504864/graded-combobox-menu-python-tkinter/41181375#41181375


timesheet.mainloop()