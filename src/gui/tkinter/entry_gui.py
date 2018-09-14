from tkinter import *


def callback(sv):
    print(sv)


window = Tk()
l1 = Label(window, text="User Name")
l1.pack(side=LEFT)
e1 = Entry(window, bd=1)
e1.pack(side=RIGHT)
window.mainloop()
