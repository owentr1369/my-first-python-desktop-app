from tkinter import *

window = Tk()

window.title("Hello Uyen Beo")

window.geometry('350x200')

lbl = Label(window, text="Hello Uyen Beo hihi", font=("Arial Bold", 20))

lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me", bg="orange", fg="red")
btn.grid(column=1, row=0)

window.mainloop()