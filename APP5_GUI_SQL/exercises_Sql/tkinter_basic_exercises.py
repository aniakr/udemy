from tkinter import *

practice_window=Tk()
Kg=Label(practice_window,text="Kg")
Kg.grid(row=0,column=0)

def conversion():
    gr=float(button_entry_kg_value.get())*1000
    text_window_gr.insert(END, gr)
    pound=float(button_entry_kg_value.get())*2.20462
    text_window_pou.insert(END, pound)
    ounce=float(button_entry_kg_value.get())*35.274
    text_window_oun.insert(END, ounce)


button_convert=Button(practice_window, text="Convert",command=conversion)
# button1.pack() - button can be put this way, but grid is better
button_convert.grid(row=0, column=2)

button_entry_kg_value=StringVar()
button_entry_kg=Entry(practice_window, textvariable=button_entry_kg_value)
button_entry_kg.grid(row=0,column=1)

text_window_gr=Text(practice_window, height=1, width=10)
text_window_gr.grid(row=1, column=0)

text_window_pou=Text(practice_window, height=1, width=10)
text_window_pou.grid(row=1, column=1)

text_window_oun=Text(practice_window, height=1, width=10)
text_window_oun.grid(row=1, column=2)

practice_window.mainloop()