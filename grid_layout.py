from tkinter import *


def button_clicked():
    print("Good Morning, " + ip1.get() + "!")


root = Tk()
root.title("First Grid Layout")

# Grid System

# Labels
# label1 = Label(root, text="Hello")
# label2 = Label(root, text="World!")
# label1.grid(row=0, column=0)
# label2.grid(row=1, column=0)

# Input Fields
ip1 = Entry(root, width=50, bg="black", fg="red")
ip1.pack()

# Button in Pack Layout
btn = Button(root, text="Greet",
             padx=20, command=button_clicked,
             fg="blue", bg="red")
btn.pack()

root.mainloop()