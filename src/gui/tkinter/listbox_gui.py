from tkinter import *

window = Tk()

list_box = Listbox(window)
for i in range(10):
    list_box.insert(i, f"Item {i+1}")
list_box.pack()

window.mainloop()
