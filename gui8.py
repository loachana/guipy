from Tkinter import *

root = Tk()

v = IntVar()
v.set(1)

languages = [
        ("python",1),
        ("perl",2),
        ("java",3),
        ("c++",4),
        ("c",5)
    ]

def ShowChoice():
    print v.get()

Label(root,
        text="""choose your favourite 
programming Language: """,
        justify=LEFT,
        padx=20).pack()

for txt, val in languages:
    Radiobutton(root,
            text=txt,
            padx=20,
            variable=v,
            command=ShowChoice,
            value=val).pack(anchor=W)
mainloop()


