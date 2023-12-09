from tkinter import * 

from tkinter.ttk import *

window = Tk()

window.title("Owen Dev")

window.geometry('350x200')

combo = Combobox(window)

combo['values'] = (1, 2, 3, 4, 5, "Text")

combo.current(1) #set the selected item

combo.grid(column=0, row=0)

def clicked():
    print(combo.get())

btn = Button(window, text="Click Me" ,command=clicked)

btn.grid(column=2, row=0)

window.mainloop()