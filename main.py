from tkinter import *

window = Tk()

window.title("Hello Uyen Beo")

window.geometry('350x200')

lbl = Label(window, text="Hello Uyen Beo hihi", font=("Arial Bold", 20))

lbl.grid(column=0, row=0)

txt = Entry(window, width=10)

txt.grid(column=1, row=0)

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)

btn = Button(window, text="Click Me", bg="orange", fg="red", command=clicked)
btn.grid(column=2, row=0)

btn2 = Button(window, text="Click Me", bg="orange", fg="red", state=DISABLED)

btn2.grid(column=0, row=1)


window.mainloop()