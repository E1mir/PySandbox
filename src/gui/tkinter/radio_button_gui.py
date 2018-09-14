import tkinter
from tkinter import *


def select():
    selection = f"Awesome option: {var.get()}"
    label.config(text=selection)


window = tkinter.Tk()

var = IntVar()

radio_1 = Radiobutton(
    window,
    text="Music",
    variable=var,
    value=1,
    command=select
)
radio_1.pack(anchor=W)

radio_2 = Radiobutton(
    window,
    text="Video",
    variable=var,
    value=2,
    command=select
)
radio_2.pack(anchor=W)

radio_3 = Radiobutton(
    window,
    text="Movie",
    variable=var,
    value=3,
    command=select
)
radio_3.pack(anchor=W)

radio_4 = Radiobutton(
    window,
    text="Cartoon",
    variable=var,
    value=4,
    command=select
)
radio_4.pack(anchor=W)

label = Label(window)
label.pack()

window.mainloop()
