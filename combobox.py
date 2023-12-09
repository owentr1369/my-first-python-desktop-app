from tkinter import * 

from tkinter.ttk import *

window = Tk()

window.title("Owen Dev")

window.geometry('350x200')

combo = Combobox(window)

combo['values'] = (1, 2, 3, 4, 5, "Text")

combo.current(1) #set the selected item

combo.grid(column=0, row=0)

label = Label(window, text="Hello", font=("Arial Bold", 20))
label.grid(column=1, row=4)

def clicked():
    if combo.get() == '1':
        label.configure(text="You picked 1")
    elif combo.get() == '2':
        label.configure(text="You picked 2")
    else: label.configure(text="You picked other")

btn = Button(window, text="Click Me" ,command=clicked)

btn.grid(column=2, row=0)

window.mainloop()