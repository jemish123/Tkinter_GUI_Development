from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Frames Demo")
root.geometry("500x500")


# def open_window():
#     top = Toplevel()
#     top.title("Second Window")
#     Label(top, text="Hello World!").pack()
#     Button(top, text="Close Window",
#            padx=20, pady=20,
#            command=top.destroy).pack()
#
#
# Button(frame, text="Open Second Window",
#        padx=20, pady=20,
#        command=open_window).pack()


# r = IntVar()
# r.get()
#
# MODES = [
#     ("Pepperoni", "Pepperoni"), ("Cheese", "Cheese"),
#     ("Mushroom", "Mushroom"), ("Onion", "Onion")
# ]
#
# pizza = StringVar()
# pizza.set("Pepperoni")
#
# for text, mode in MODES:
#     Radiobutton(frame, text=text,
#                 variable=pizza,
#                 command=lambda : clicked(pizza.get()),
#                 value=mode).pack(anchor=W)
#
#
# def clicked(value):
#     label.config(text= "Your Topping is: "+ value)
#     label.pack()
# #
# # Radiobutton(frame, text="Option 1", variable=r, value=1,
# #             command=lambda : clicked(r.get())).pack()
# # Radiobutton(frame, text="Option 2", variable=r, value=2,
# #             command=lambda : clicked(r.get())).pack()
#
#
# label = Label(root, text="Your Topping is: ")
# label.pack(),


# def popup():
#     response = messagebox.askretrycancel("This is my Pop Up!", "Hello World!")
#     if response == "yes":
#         Label(root, text=response).pack()
#     else:
#         Label(root, text=response).pack()
#
#
# Button(frame, text="Popup", command=popup).pack()

# root.filename = filedialog.askopenfilename(
#                     initialdir="/test_dir",
#                     title="Select a File",
#                     filetypes=(("png files", "*.png"),
#                                ("All Files", "*.*"))
#                 )
#
# Label(root, image=PhotoImage(file=root.filename)).pack()

# vertical = Scale(frame, from_=0, to=200)
# vertical.pack()
#
# horizontal = Scale(frame, from_=0, to=200, orient=HORIZONTAL)
# horizontal.pack()
# var = StringVar()
# c = Checkbutton(root, text="Check this box, I Dare you!",
#                 variable=var,
#                 onvalue="On", offvalue="Off")
# c.deselect()
# c.pack()
#
# frame = LabelFrame(root, text="Selected Item.", padx=50, pady=50)
# frame.pack(padx=10, pady=10)
#
#
# def show():
#     label = Label(frame, text=var.get())
#     label.pack()
#
#
# btn = Button(frame, text="Show Selection", command=show)
# btn.pack()
# def show():
#     Label(root, text=clicked.get()).pack()
#
#
# OPTIONS = ["Monday", "Tuesday",
#            "Wednesday", "Thursday",
#            "Friday", "Saturday", "Sunday"]
#
# clicked = StringVar()
# clicked.set(OPTIONS[0])
#
# drop = OptionMenu(root, clicked, *OPTIONS)
# drop.pack()
#
# btn = Button(root, text="Show Selection", command=show)
# btn.pack()

root.mainloop()