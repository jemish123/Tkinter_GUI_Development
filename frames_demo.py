from tkinter import *

root = Tk()
root.title("Frames Demo")

frame = LabelFrame(root, text="This is my Frame.", padx=50, pady=50)
frame.pack(padx=10, pady=10)

r = IntVar()
r.get()
r.set(2)

MODES = [
    ("Pepperoni", "Pepperoni"), ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"), ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(frame, text=text, variable=pizza, value=mode).pack()
def clicked(value):
    label.config(text=value)
    label.pack()
#
# Radiobutton(frame, text="Option 1", variable=r, value=1,
#             command=lambda : clicked(r.get())).pack()
# Radiobutton(frame, text="Option 2", variable=r, value=2,
#             command=lambda : clicked(r.get())).pack()

label = Label(root, text=pizza.get())
label.pack()
root.mainloop()