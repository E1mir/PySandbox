from tkinter import *

window = Tk()

m_btn = Menubutton(window, text="Click me!")
m_btn.grid()
m_btn.menu = Menu(m_btn)
m_btn["menu"] = m_btn.menu

for i in range(10):
    m_btn.menu.add_checkbutton(label=f"Item {i}")

m_btn.pack()

window.mainloop()
