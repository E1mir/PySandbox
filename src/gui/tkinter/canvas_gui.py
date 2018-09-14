from tkinter import *

window = Tk()

canvas_widget = Canvas(window, bg="red", height=512, width=512)

coord = (10, 50, 512, 512)
arc_obj = canvas_widget.create_arc(coord, start=0, extent=270, fill='white')
line_obj = canvas_widget.create_line((75, 10, 20, 150), fill='magenta',width=10)

canvas_widget.pack()

window.mainloop()
