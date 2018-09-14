from tkinter import *

window = Tk()

canvas_widget = Canvas(window, bg="red", height=512, width=512)

coord_1 = (10, 50, 512, 512)
coord_2 = (75, 10, 20, 150)

# Create arc shaped object, Pac-man in our case
arc_obj = canvas_widget.create_arc(coord_1, start=0, extent=270, fill='white')

# Simple line in canvas
line_obj = canvas_widget.create_line(coord_2, fill='magenta', width=10)

canvas_widget.pack()

window.mainloop()
