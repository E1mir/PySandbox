from tkinter import *
from tkinter import messagebox

window = Tk()


def add_new():
    msg = messagebox.showinfo("New", "ADD NEW FILE")


def undo_comm():
    msg = messagebox.showinfo("Undo", "UNDO COMMAND")


def redo_comm():
    msg = messagebox.showinfo("Redo", "REDO COMMAND")


def clear_hist():
    msg = messagebox.showinfo("Clear history", "CLEAR HISTORY COMMAND")


menu_bar = Menu(window)

menu_1 = Menu(menu_bar)
menu_1.add_command(label="New", command=add_new)
menu_1.add_separator()
menu_1.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label='File', menu=menu_1)

menu_2 = Menu(menu_bar)
menu_2.add_command(label="Undo", command=undo_comm)
menu_2.add_command(label="Redo", command=redo_comm)
menu_2.add_separator()
menu_2.add_command(label='Clear history', command=clear_hist)
menu_bar.add_cascade(label='Edit', menu=menu_2)

window.config(menu=menu_bar)
window.mainloop()
