# A program that stores below information on books:
# Title, Author, Year, ISBN
#
# User can:
# view all records,
# Search an entry
# Add an entry
# Update an entry
# Delete an entry
# Close the program

from tkinter import *

bookstore_window=Tk()
bookstore_window.title("Bookstore")
bookstore_window.configure(background="black")


photo=PhotoImage(file="reg_book.gif")
Label(bookstore_window,image=photo,bg="black").grid(row=0,column=0, columnspan=4)

# Labels
Title=Label(bookstore_window, text="Title",bg="black",fg="white",font="Arial 12 italic")
Title.grid(row=1,column=0,sticky=E)
Year=Label(bookstore_window, text="Year",bg="black",fg="white",font="Arial 12 italic")
Year.grid(row=2,column=0,sticky=E)
Author=Label(bookstore_window, text="Author",bg="black",fg="white",font="Arial 12 italic")
Author.grid(row=1,column=2, sticky=W)
ISBN=Label(bookstore_window, text="ISBN",bg="black",fg="white",font="Arial 12 italic")
ISBN.grid(row=2,column=2, sticky=W)

# Listbox
Listbox1=Listbox(bookstore_window, height=6, width=30)
Listbox1.grid(row=3, column=0, rowspan=6, columnspan=2, sticky=N+S)

yscroll=Scrollbar(bookstore_window)
yscroll.grid(row=3, column=2, rowspan=6, sticky=N+S+W)
Listbox1.configure(yscrollcommand=yscroll.set)
yscroll.configure(command=Listbox1.yview)



# Entry box
Title_entry_value=StringVar()
Title_entry=Entry(bookstore_window, textvariable=Title_entry_value)
Title_entry.grid(row=1, column=1)
Author_entry_value=StringVar()
Author_entry=Entry(bookstore_window, textvariable=Author_entry_value)
Author_entry.grid(row=1, column=3)
Year_entry_value=StringVar()
Year_entry=Entry(bookstore_window, textvariable=Year_entry_value)
Year_entry.grid(row=2, column=1)
ISBN_entry_value=StringVar()
ISBN_entry=Entry(bookstore_window, textvariable=ISBN_entry_value)
ISBN_entry.grid(row=2, column=3)

# Buttons
button_view_all=Button(bookstore_window, text="View all", width=12)
button_view_all.grid(row=3, column=3)
button_search_entry=Button(bookstore_window, text="Search entry", width=12)
button_search_entry.grid(row=4, column=3)
button_add_entry=Button(bookstore_window, text="Add entry", width=12)
button_add_entry.grid(row=5, column=3)
button_update=Button(bookstore_window,text="Update", width=12)
button_update.grid(row=6, column=3)
button_delete=Button(bookstore_window,text="Delete", width=12)
button_delete.grid(row=7, column=3)
button_close=Button(bookstore_window,text="Close", width=12)
button_close.grid(row=8,column=3)


bookstore_window.mainloop()





