#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import sys

class SimpleApp_tk(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0, sticky="EW")
        self.entry.bind("<Return>", self.OnPressEnter)

        button = Tkinter.Button(self,text=u"exit",
                                command=self.OnButtonClick)
        button.grid(column=1, row=0)

        self.labelVariable = Tkinter.StringVar()

        label = Tkinter.Label(self,textvariable=self.labelVariable, anchor="w", fg="white", bg="blue")
        label.grid(column=0, row=1, columnspan=2, sticky="EW")

        self.grid_columnconfigure(0,weight=1)

        self.resizable(True, False)

    def OnButtonClick(self):
        sys.exit(1)

    def OnPressEnter(self, event):
        self.labelVariable.set("You pressed enter!")



if __name__ == "__main__":
    app = SimpleApp_tk(None)
    app.title("my application")
    app.mainloop()
