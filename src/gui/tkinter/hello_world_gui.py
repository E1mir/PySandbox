import tkinter

window = tkinter.Tk()

window.winfo_toplevel().title('Hello world!')

window.geometry("100x100")  # You want the size of the app to be 100x100
window.resizable(0, 0)  # Don't allow resizing in the x or y direction

lbl = tkinter.Label(window, text="Hello world!")
lbl.pack()

window.mainloop()
