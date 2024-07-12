from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images")
root.geometry('500x500')
root.iconbitmap('error')

img = PhotoImage(file="on.png")
img2 = PhotoImage(file="off.png")
img3 = PhotoImage(file="bitmap.png")

img_list = [img, img2, img3]

status = Label(root, text="Image 1 of " + str(len(img_list)))

label = Label(image=img)
label.grid(row=0, column=0, columnspan=3)

def forward(image_num):
    global label
    global btn_nxt
    global btn_back

    label.grid_forget()
    label.config(image=img_list[image_num-1])
    btn_nxt.config(command=lambda : forward(image_num+1))
    btn_nxt.grid(row=1, column=2)

    if image_num == len(img_list):
        btn_nxt.config(state=DISABLED)
        btn_back.config(state=ACTIVE)
    btn_back.config(command=lambda : backward(image_num-1))
    btn_exit.grid(row=1, column=1)

    label.grid(row=0, column=0, columnspan=3)

def backward(image_num):
    global label
    global btn_nxt
    global btn_back

    label.grid_forget()
    label.config(image=img_list[image_num - 1])
    btn_nxt.config(command=lambda: forward(image_num + 1))

    if image_num == 1:
        btn_back.config(state=DISABLED)
        btn_nxt.config(state=ACTIVE)
    btn_back.config(command=lambda: backward(image_num - 1))

    label.grid(row=0, column=0, columnspan=3)
    btn_nxt.grid(row=1, column=2)
    btn_exit.grid(row=1, column=1)

btn_back = Button(root, text="<<", command=backward, state=DISABLED)
btn_nxt = Button(root, text=">>", command=lambda : forward(2))
btn_exit = Button(root, text="Exit Viewer", command=root.quit)

btn_back.grid(row=1, column=0)
btn_nxt.grid(row=1, column=2)
btn_exit.grid(row=1, column=1)
status.grid(row=2, column=0, pady=10, columnspan=3)

root.mainloop()
