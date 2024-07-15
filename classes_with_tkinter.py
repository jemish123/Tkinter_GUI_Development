from tkinter import *
import sqlite3


root = Tk()
root.title("Frames Demo")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry("%dx%d"%(w, h))


class FirstTkinterClass:
    def __init__(self, main):
        frame = Frame(main)
        frame.pack()

        self.btn = Button(main, text="Click me!", command=self.clicker)
        self.btn.pack(pady=20)

    def clicker(self):
        print("Button is clicked.")


e = FirstTkinterClass(root)
root.mainloop()