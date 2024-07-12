from tkinter import *


root = Tk()
root.title("Calculator")

input_field = Entry(root, width=50,  borderwidth=5)
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_clicked(number):
    current = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, str(current) + str(number))


def button_clear():
    input_field.delete(0, END)


def button_add():
    first_number = input_field.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    input_field.delete(0, END)


def button_subtract():
    first_number = input_field.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    input_field.delete(0, END)


def button_multiply():
    first_number = input_field.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    input_field.delete(0, END)


def button_division():
    first_number = input_field.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    input_field.delete(0, END)


def button_equal():
    second_number = input_field.get()
    input_field.delete(0, END)

    if math == "addition":
        input_field.insert(0, str(f_num + int(second_number)))
    if math == "subtraction":
        input_field.insert(0, str(f_num - int(second_number)))
    if math == "multiplication":
        input_field.insert(0, str(f_num * int(second_number)))
    if math == "division":
        input_field.insert(0, str(f_num / int(second_number)))

btn_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_clicked(1))
btn_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_clicked(2))
btn_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_clicked(3))
btn_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_clicked(4))
btn_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_clicked(5))
btn_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_clicked(6))
btn_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_clicked(7))
btn_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_clicked(8))
btn_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_clicked(9))
btn_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_clicked(0))
btn_dot = Button(root, text=".", padx=40, pady=20)
btn_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
btn_clear = Button(root, text="CLEAR", padx=20, pady=20, command=button_clear)
btn_add = Button(root, text="+", padx=105, pady=20, command=button_add)
btn_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
btn_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
btn_division = Button(root, text="/", padx=40, pady=20, command=button_division)


btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_dot.grid(row=4, column=0)
btn_0.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)

btn_subtract.grid(row=5, column=2)
btn_multiply.grid(row=5, column=1)
btn_division.grid(row=5, column=0)

btn_clear.grid(row=6, column=0)
btn_add.grid(row=6, column=1, columnspan=2)
root.mainloop()
