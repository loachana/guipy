from Tkinter import *

root = Tk()
logo = PhotoImage(file="python.png")
w1 = Label(root,bg="lightgray", image=logo).pack(side="right")

explanation = """ python is a general purpose language developed by a scientist.
Today it is widely used for many reasons by open source community. Python has a 
bright future as C language today."""

w2 = Label(root, justify=CENTER,fg="black", padx=10, font=('ubuntu',15), text=explanation).pack(side="left")

root.mainloop()


