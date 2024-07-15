from tkinter import *
from tkinter import filedialog
import sqlite3

root = Tk()
root.title("Frames Demo")
root.geometry("500x500")


# create a table
# cur.execute("""CREATE TABLE addresses(
#     first_name text,
#     last_name text,
#     address text,
#     state text,
#     zipcode integer
# )"""


def submit():
    # create a database or connect to one
    conn = sqlite3.connect("mydb.db")

    # create a cursor
    cur = conn.cursor()
    cur.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :state, :zipcode)",
                {
                    'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'state': state.get(),
                    'zipcode': zipcode.get()
                })

    # commit changes
    conn.commit()
    cur.close()
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    conn = sqlite3.connect("mydb.db")
    # create a cursor
    cur = conn.cursor()
    cur.execute("SELECT *, oid FROM addresses")
    records = cur.fetchall()
    print(records)  # commit changes

    print_records = ""
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=9, column=0, columnspan=2)

    # commit changes
    conn.commit()
    cur.close()
    conn.close()


def delete():
    conn = sqlite3.connect("mydb.db")
    # create a cursor
    cur = conn.cursor()
    cur.execute("DELETE from addresses WHERE oid=" + delete_record.get())

    # commit changes
    conn.commit()
    cur.close()
    conn.close()


def update():
    conn = sqlite3.connect("mydb.db")
    # create a cursor
    cur = conn.cursor()

    record_id = delete_record.get()

    cur.execute(
        """
        UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        state = :state,
        zipcode = :zip
        
        WHERE oid = :oid""",

        {
            'first' : f_name_editor.get(),
            'last': l_name_editor.get(),
            'address': address_editor.get(),
            'state': state_editor.get(),
            'zip': zipcode_editor.get(),

            'oid': record_id
        }
    )

    # commit changes
    conn.commit()
    cur.close()
    conn.close()

    editor.destroy()


def edit():
    global editor
    editor = Tk()
    editor.title("Update a Record")
    editor.geometry("500x500")

    global f_name_editor
    global l_name_editor
    global address_editor
    global state_editor
    global zipcode_editor

    f_label_editor = Label(editor, text="First Name")
    f_label_editor.grid(row=0, column=0, pady=(10, 0))
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_label_editor = Label(editor, text="Last Name")
    l_label_editor.grid(row=1, column=0)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    add_label_editor = Label(editor, text="Address")
    add_label_editor.grid(row=2, column=0)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=3, column=0)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=3, column=1, padx=20)

    zip_label_editor = Label(editor, text="Zipcode")
    zip_label_editor.grid(row=4, column=0)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=4, column=1, padx=20)

    conn = sqlite3.connect("mydb.db")
    # create a cursor
    cur = conn.cursor()

    record_id = delete_record.get()
    cur.execute("SELECT * FROM addresses WHERE oid=" + record_id)
    records = cur.fetchall()

    # loop through result
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        state_editor.insert(0, record[3])
        zipcode_editor.insert(0, record[4])

    save_btn = Button(editor, text="Save Changes",
                        font=("Helvetica", 16),
                        padx=30, command=update)
    save_btn.grid(row=5, column=0, columnspan=2,
                    padx=20, ipadx=100)

    # commit changes
    conn.commit()
    cur.close()
    conn.close()


f_label = Label(root, text="First Name")
f_label.grid(row=0, column=0, pady=(10, 0))
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_label = Label(root, text="Last Name")
l_label.grid(row=1, column=0)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

add_label = Label(root, text="Address")
add_label.grid(row=2, column=0)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

state_label = Label(root, text="State")
state_label.grid(row=3, column=0)
state = Entry(root, width=30)
state.grid(row=3, column=1, padx=20)

zip_label = Label(root, text="Zipcode")
zip_label.grid(row=4, column=0)
zipcode = Entry(root, width=30)
zipcode.grid(row=4, column=1, padx=20)

delete_label = Label(root, text="ID")
delete_label.grid(row=7, column=0, pady=(20, 5))
delete_record = Entry(root, width=30)
delete_record.grid(row=7, column=1, pady=(20, 5))

submit_btn = Button(root, text="SUBMIT",
                    font=("Helvetica", 16),
                    padx=30, command=submit)
submit_btn.grid(row=5, column=0, columnspan=2,
                padx=20, ipadx=100)

query_btn = Button(root, text="Show Records",
                   font=("Helvetica", 16),
                   padx=30, command=query)
query_btn.grid(row=6, column=0, columnspan=2,
               padx=20, ipadx=100)

delete_btn = Button(root, text="Delete Record",
                    font=("Helvetica", 16),
                    padx=30, command=delete)
delete_btn.grid(row=8, column=0, columnspan=2,
                padx=20, ipadx=100)

edit_btn = Button(root, text="Update Record",
                    font=("Helvetica", 16),
                    padx=30, command=edit)
edit_btn.grid(row=10, column=0, columnspan=2,
                padx=20, ipadx=100)

root.mainloop()
