from tkinter import *

window = Tk()

cv = IntVar()
cb = Checkbutton(
    window,
    text='Checkbox',
    variable=cv,
    onvalue=1,
    offvalue=0,
)

check_var_1 = IntVar()
check_var_2 = IntVar()

c1 = Checkbutton(
    window,
    text="Movie",
    variable=check_var_1,
    onvalue=1,
    offvalue=0,
    height=5,
    width=20
)
c2 = Checkbutton(
    window,
    text="Games",
    variable=check_var_2,
    onvalue=1,
    offvalue=0,
    height=5,
    width=20
)
cb.pack()
c1.pack()
c2.pack()
window.mainloop()
