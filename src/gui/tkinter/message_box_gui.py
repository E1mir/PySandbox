import tkinter
from tkinter import *
from tkinter import messagebox

window = Tk()


def func():
    messagebox.showinfo("Title", "Message")


btn = Button(window, text="Open Message", command=func)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()
