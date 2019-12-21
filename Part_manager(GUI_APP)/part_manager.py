from tkinter import *
from tkinter import messagebox
from db import Database


db = Database('store.db')


def populate_list():
    part_list.delete(0, END)  # to remove the redundancy when displaying
    for row in db.fetch():
        part_list.insert(END, row)


def add_item():
    if part_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'please include all fields')
        return
    db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    part_list.delete(0, END)
    part_list.insert(END, (part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
    clear_item()
    populate_list()


def select_item(event):
    global selected_item
    index = part_list.curselection()[0]
    selected_item = part_list.get(index)
    print(selected_item)

    part_entry.delete(0, END)
    part_entry.insert(END, selected_item[1])
    customer_entry.delete(0, END)
    customer_entry.insert(END, selected_item[2])
    retailer_entry.delete(0, END)
    retailer_entry.insert(END, selected_item[3])
    price_entry.delete(0, END)
    price_entry.insert(END, selected_item[4])


def remove_item():
   db.remove(selected_item[0])
   clear_item()
   populate_list()


def update_item():
 db.update(selected_item[0],part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
 populate_list()


def clear_item():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)


# To create window object
app = Tk()
part_text = StringVar()
# creating part label
part_label = Label(app, text="Part Name ", font=('bold', 10), pady=20, padx=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# creating customer label
customer_text = StringVar()
customer_label = Label(app, text="Customer Name ", font=('bold', 10), padx=20)
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# creating retailer label
retailer_text = StringVar()
retailer_label = Label(app, text="Retailer", font=('bold', 10), padx=20)
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

# creating price label
price_text = StringVar()
price_label = Label(app, text="Price ", font=('bold', 10), padx=20)
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

# creating parts list (Listbox)
part_list = Listbox(app, height=8, width=50, border=0)
part_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# creating scrollbar
scroll_bar = Scrollbar(app)
scroll_bar.grid(row=3, column=3)
# set scroll to listbox
part_list.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=part_list.yview)

# bind select
part_list.bind("<<ListboxSelect>>", select_item)
# buttons
add_btn = Button(app, text="Add Parts",  width=12, bg='gray', command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text="Remove Parts",  width=12, bg='gray',  command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text="Update Parts",  width=12, bg='gray', command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text="Clear Input",  width=12, bg='gray', command=clear_item)
clear_btn.grid(row=2, column=3)

# to change the title
app.title("Part Manager")
app.geometry('520x350')
# populate data
populate_list()

# To start  the program
app.mainloop()

