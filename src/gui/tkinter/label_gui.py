from tkinter import *

window = Tk()

sv = StringVar()
lbl = Label(window, textvariable=sv)
sv.set('Awesome label text')

print(sv.get())
lbl.pack(anchor=CENTER)

window.mainloop()
