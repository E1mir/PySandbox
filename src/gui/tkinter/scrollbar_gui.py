import tkinter
from tkinter import *

window = Tk()

var = DoubleVar()
sc = Scrollbar(window)
sc.pack(side=RIGHT, fill=Y)

my_list = Listbox(window, yscrollcommand=sc.set)

for l in range(200):
    my_list.insert(END, f"Row: {l+1}")

my_list.pack()
sc.config(command=my_list.yview)
window.mainloop()
