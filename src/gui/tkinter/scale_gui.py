import tkinter
from tkinter import *


def get_value():
    selection = f"Value: {var.get()}"
    label.config(text=selection)


window = Tk()

var = DoubleVar()
scale = Scale(window, variable=var, orient=HORIZONTAL)

scale.pack()

button = Button(window, text="Retrieve value", command=get_value)
button.pack()

label = Label(window)
label.pack()

window.mainloop()
