import tkinter
from tkinter import *

window = Tk()

label_frame = LabelFrame(window, text="This is awesome")
label_frame.pack(fill=BOTH, expand=YES)

left = Label(label_frame, text="Inside the label frame")
left.pack(side=LEFT)

window.mainloop()
