import tkinter
from tkinter import messagebox
from tkinter import Button

window = tkinter.Tk()
HEIGHT = window.winfo_height()
WIDTH = window.winfo_width()
print(f'Height: {HEIGHT}, Width: {WIDTH}')


def click_button():
    msg = messagebox.showinfo("Hello!", "You clicked a button!")


button_widget = Button(window, text='Click me!', command=click_button)
button_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

window.mainloop()
