from tkinter import *
from random import randint

import grid_layout

# def button_clicked():
#     print("Good Morning, " + ip1.get() + "!")


root = Tk()
root.geometry('400x400')
root.title("First Grid Layout")

# Grid System


# Labels
# label1 = Label(root, text="Hello")
# label2 = Label(root, text="World!")
# label1.grid(row=0, column=0)
# label2.grid(row=1, column=0)

# Input Fields
# ip1 = Entry(root, width=50, bg="black", fg="green")
# ip1.insert(0, "The switch is on.")
# ip1.pack()
#
# # Button position
# btn = Button(root, text="Greet",
#              padx=20, fg="blue", bg="red")
# # Method 1
# # btn.place(x=100, y=20)
# # Method 2
# btn.pack(padx=15, pady=20)
#
#
# # Method 3 is using grid layout
# # Random Positioning
#
# def clicked(event):
#     print("Clicked")
#     x = randint(50, 250)
#     y = randint(50, 250)
#     btn.place(x=x, y=y)
#
#
# btn.bind("<Enter>", clicked)
# btn.pack()
#
# # Switch Button
# is_on = True
#
#
# def switch():
#     global is_on
#     if is_on:
#         ip1.delete(0, END)
#         ip1.config(fg="red")
#         ip1.insert(0, "The switch is off.")
#         on_button.config(image=off)
#
#         is_on = False
#     else:
#         on_button.config(image=on)
#         ip1.delete(0, END)
#         ip1.config(fg="green")
#         ip1.insert(0, "The switch is on.")
#
#         is_on = True
#
# on = PhotoImage(file="on.png")
# off = PhotoImage(file="off.png")
# on_button = Button(root, image=on, bd=0, command=switch)
# on_button.pack(pady=50)
root.columnconfigure(index=0, weight=1)
root.rowconfigure(index=0, weight=1)

btn2 = Button(root, text="Button 1")
btn2.grid(row=0, column=0, sticky="NSEW")


def resize(e):
    # get window width
    size = e.width/10

#     Define text size on different condition
    if e.height <=400 and e.height > 300:
        btn2.config(font=("Helvetica", 40))
    elif e.height < 300 and e.height > 200:
        btn2.config(font=("Arial", 30))
    elif e.height < 200:
        btn2.config(font=("Helvetica", 40))


root.bind("<Configure>", resize)

root.mainloop()
