from Tkinter import *

master = Tk()
text = "This is a test sentence"
msg = Message(master, text=text)
msg.config(bg="lightgreen", font=("time", 24, "italic"))
msg.pack()
mainloop()

