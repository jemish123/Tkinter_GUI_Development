from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Frames Demo")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry("%dx%d"%(w, h))

# def clicker(event):
#     label = Label(root, text="Button is clicked.")
#     label.pack()
#
#
# btn = Button(root, text="Click Me")
# btn.bind("<Button-2>", clicker)
# btn.pack()

# def selected(event):
#     label = Label(root, text=clicked.get())
#     label.pack()
#
# def comboclick(event):
#     label = Label(root, text=my_combo.get())
#     label.pack()
#
# OPTION = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# clicked = StringVar()
# clicked.set(OPTION[0])
#
# drop = OptionMenu(root, clicked, *OPTION,
#                   command=selected)
# drop.pack(pady=20)
#
# # btn = Button(root, text="Select from list", command=selected)
# # btn.pack()
#
# my_combo = ttk.Combobox(root, values=OPTION)
# my_combo.current(0)
# my_combo.bind("<<ComboboxSelected>>", comboclick)
# my_combo.pack()
my_menu = Menu(root)
root.config(menu=my_menu)


def our_command():
    pass


# creating menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=our_command)
edit_menu.add_command(label="Copy", command=our_command)

root.mainloop()
