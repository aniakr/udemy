# A program that stores below information on books:
# Title, Author, Year, ISBN
#
# year - how to allow years B.C.

# User can:
# view all records,
# Search an entry
# Add an entry
# Update an entry
# Delete an entry
# Close the program

# not yet completed

from tkinter import *
from bookstore_db_OOP import Database

database=Database("AK_bookstore.db")

class Window(object):

    def __init__(self,window):
        self.window=window
        self.window.wm_title("Bookstore")
        self.window.configure(background="black")
        self.photo = PhotoImage(file="reg_book.gif")
        Label(window, image=self.photo, bg="black").grid(row=0, column=0, columnspan=4)

        # Labels
        Title = Label(window, text="Title", bg="black", fg="white", font="Arial 12 italic")
        Title.grid(row=1, column=0, sticky=E)
        Year = Label(window, text="Year", bg="black", fg="white", font="Arial 12 italic")
        Year.grid(row=2, column=0, sticky=E)
        Author = Label(window, text="Author", bg="black", fg="white", font="Arial 12 italic")
        Author.grid(row=1, column=2, sticky=W)
        ISBN = Label(window, text="ISBN", bg="black", fg="white", font="Arial 12 italic")
        ISBN.grid(row=2, column=2, sticky=W)

        # Listbox
        self.Listbox1 = Listbox(window, height=6, width=35)
        self.Listbox1.grid(row=3, column=0, rowspan=6, columnspan=2, sticky=N + S)

        yscroll = Scrollbar(window)
        yscroll.grid(row=3, column=2, rowspan=6, sticky=N + S + W)
        self.Listbox1.configure(yscrollcommand=yscroll.set)
        yscroll.configure(command=self.Listbox1.yview)

        self.Listbox1.bind('<<ListboxSelect>>', self.get_selected_row)

        # Entry box
        self.Title_entry_value = StringVar()
        self.Title_entry = Entry(window, textvariable=self.Title_entry_value)
        self.Title_entry.grid(row=1, column=1)
        self.Author_entry_value = StringVar()
        self.Author_entry = Entry(window, textvariable=self.Author_entry_value)
        self.Author_entry.grid(row=1, column=3)
        self.Year_entry_value = StringVar()
        self.Year_entry = Entry(window, textvariable=self.Year_entry_value)
        self.Year_entry.grid(row=2, column=1)
        self.ISBN_entry_value = StringVar()
        self.ISBN_entry = Entry(window, textvariable=self.ISBN_entry_value)
        self.ISBN_entry.grid(row=2, column=3)

        # Buttons
        button_view_all = Button(window, text="View all", width=12, command=self.view_command)
        button_view_all.grid(row=3, column=3)
        button_search_entry = Button(window, text="Search entry", width=12, command=self.search_command)
        button_search_entry.grid(row=4, column=3)
        button_add_entry = Button(window, text="Add entry", width=12, command=self.add_command)
        button_add_entry.grid(row=5, column=3)
        button_update = Button(window, text="Update", width=12, command=self.update_command)
        button_update.grid(row=6, column=3)
        button_delete = Button(window, text="Delete", width=12, command=self.delete_command)
        button_delete.grid(row=7, column=3)
        button_close = Button(window, text="Close", width=12, command=window.destroy)
        button_close.grid(row=8, column=3)




    def get_selected_row(self,event):
        if len(self.Listbox1.curselection()) != 0:
            index = self.Listbox1.curselection()[0]
            self.selected_tuple=self.Listbox1.get(index)
            self.Title_entry.delete(0,END)
            self.Author_entry.delete(0,END)
            self.Year_entry.delete(0,END)
            self.ISBN_entry.delete(0,END)
            self.Title_entry.insert(END,self.selected_tuple[1])
            self.Author_entry.insert(END, self.selected_tuple[2])
            self.Year_entry.insert(END,self.selected_tuple[3])
            self.ISBN_entry.insert(END,self.selected_tuple[4])
        else:
            pass


    def view_command(self):
        self.Listbox1.delete(0,END)
        for book in database.view():
            self.Listbox1.insert(END, book)
    #
    def search_command(self):
        self.Listbox1.delete(0, END)
        for book in database.search(self.Title_entry_value.get(),self.Author_entry_value.get(), self.Year_entry_value.get(),self.ISBN_entry_value.get()):
            self.Listbox1.insert(END, book)

    def add_command(self):
        self.Listbox1.delete(0, END)
        database.insert(self.Title_entry_value.get(),self.Author_entry_value.get(), self.Year_entry_value.get(),self.ISBN_entry_value.get())
        self.Listbox1.insert(END,(self.Title_entry_value.get(),self.Author_entry_value.get(), self.Year_entry_value.get(),self.ISBN_entry_value.get()))

    def delete_command(self):
        database.deletion(self.selected_tuple[0])
        self.Listbox1.delete(0, END)
        for book in database.view():
            self.Listbox1.insert(END, book)

    def update_command(self):
        database.update(self.selected_tuple[0],self.Title_entry_value.get(),self.Author_entry_value.get(), self.Year_entry_value.get(),self.ISBN_entry_value.get())
        self.Listbox1.delete(0, END)
        for book in database.view():
            self.Listbox1.insert(END, book)



window=Tk()
Window(window)
window.mainloop()




