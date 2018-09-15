from tkinter import *
import datetime

now=datetime.datetime.now()
current_month=now.strftime("%B")
current_year=now.year

timesheet=Tk()
timesheet.wm_title("IS IC Timesheet Form")

photo=PhotoImage(file="kalender.gif")
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
Listbox1=Listbox(timesheet, height=6, width=35)
Listbox1.grid(row=6, column=0, rowspan=6, columnspan=3, sticky=N+S+W+E)

yscroll=Scrollbar(timesheet)
yscroll.grid(row=6, column=3, rowspan=6, sticky=N+S+W)
Listbox1.configure(yscrollcommand=yscroll.set)
yscroll.configure(command=Listbox1.yview)

# Listbox1.bind('<<ListboxSelect>>',get_selected_row)

# Entry box
Name_entry_val=StringVar()
Name_entry=Entry(timesheet, textvariable=Name_entry_val)
Name_entry.grid(row=1, column=1)
Name_entry.insert(END, 'Ania')

Month_entry_val=StringVar()
Month_entry=Entry(timesheet, textvariable=Month_entry_val)
Month_entry.grid(row=2, column=1)
Month_entry.insert(END, current_month)

Year_entry_val=StringVar(timesheet)
Year_entry_val.set(current_year)
Year_entry = OptionMenu(timesheet, Year_entry_val, "2018", "2019")
Year_entry.grid(row=2, column=3)

# https://stackoverflow.com/questions/40504864/graded-combobox-menu-python-tkinter/41181375#41181375


timesheet.mainloop()