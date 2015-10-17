#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter

class SimpleApp_tk(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0, sticky="EW")

        button = Tkinter.Button(self,text=u"click me !")
        button.grid(column=1, row=0)


if __name__ == "__main__":
    app = SimpleApp_tk(None)
    app.title("my application")
    app.mainloop()
