from Tkinter import *

root = Tk()

v = IntVar()

Label(root,
        text="""Choose a 
        programming Language:""",
        justify = LEFT,
        font=(15),
        padx = 20).pack()
Radiobutton(root,
        text="python",
        padx = 20,
        font=(15),
        variable = v,
        value = 1).pack(anchor=W)
Radiobutton(root,
        text="Perl",
        padx= 20,
        font=(15),
        variable=v,
        value=2).pack(anchor=W)
mainloop()
