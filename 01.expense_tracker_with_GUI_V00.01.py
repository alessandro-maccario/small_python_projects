"""
    Expense Tracker: this is a very simple Expense Tracker made in Python with a GUI in Tkinter.
    The goal was to understand how the tkinter library works and to learn about it.

"""

# IMPORT THE NECESSARY PACKAGES
from tkinter import *
from tkinter import ttk # is a submodule of tkinter. It implements Python's binding to the newer "themed widgets" that were added to Tk in 8.5.
from datetime import date

# IMPORT THE expense_tracker_utils MODULE
from expense_tracker_utils import get_date
from expense_tracker_utils import get_category
from expense_tracker_utils import get_item_name
from expense_tracker_utils import get_item_price
from expense_tracker_utils import get_store
from expense_tracker_utils import save_file
from expense_tracker_utils import close_window


# Sets up the main application window, giving it the title "Feet to Meters."
# This is the main outer window
# Create a window
root = Tk()

# Define the grid construction: in this case just two rows
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# Set the title
root.title("Expense Tracker")

# Set dimensions: width, heigth, x, y
root.geometry("660x500+650+50") # the +50 means where the windowd will be displayed

# Add the icon .ico (.icon)
# root.iconbitmap("budget.ico")
root.iconphoto(False, PhotoImage(file='C:/Users/a_mac/Documents/solutions/learning_python/budget.png'))

# Avoid resizing window: width, height (boolean)
root.resizable(False, False)

# Set the minimum/maximum dimensions
# root.minsize(600,600)
# root.maxsize(600,1000)

# CREATE EMPTY LIST TO STORE ALL THE ENTRIES
entry_list = []


###########################################
############# Create frames ###############

frame_date = Frame(root, background="#e39d12")
# frame_date.pack(ipadx = 3, ipady=3, padx=15, pady=15, expand=True, fill=X, side=LEFT)
frame_date.grid(column=0, row=1, padx = 3, pady = 3, sticky=N + W + E)

frame_category = Frame(root, background="#32a852")
# frame_category.pack(ipadx = 15, ipady=15, padx=15, pady=10, expand=True, fill=X, side=LEFT)
frame_category.grid(column=1, row=1, padx = 3, pady = 3, sticky=N + W + E)

frame_item_name = Frame(root, background="#32a875")
# frame_item_name.pack(ipadx = 15, ipady=15, padx=15, pady=10, expand=True, fill=X, side=LEFT)
frame_item_name.grid(column=0, row=2, padx = 3, sticky=N + W + E)

frame_item_price = Frame(root, background="#32a8a2")
# frame_item_price.pack(ipadx = 15, ipady=15, padx=15, pady=10, expand=True, fill=X, side=LEFT)
frame_item_price.grid(column=1, row=2, padx = 3, sticky=N + W + E)

frame_item_store = Frame(root, background="#3283a8")
# frame_item_store.pack(ipadx = 15, ipady=15, padx=15, pady=10, expand=True, fill=X, side=LEFT)
frame_item_store.grid(column=0, row=3, columnspan=2, padx = 3, pady = 3, sticky=N + W + E)

# SAVE THE FINAL FILE
frame_save_file = Frame(root, background="#2c21c4")
# frame_item_store.pack(ipadx = 15, ipady=15, padx=15, pady=10, expand=True, fill=X, side=LEFT)
frame_save_file.grid(column=0, row=4, columnspan=2, padx = 3, pady = 3, sticky=N + W + E)

# SAVE THE FINAL FILE
frame_close_window = Frame(root, background="#e32222")
# frame_item_store.pack(ipadx = 15, ipady=15, padx=15, pady=10, expand=True, fill=X, side=LEFT)
frame_close_window.grid(column=0, row=6, columnspan=2, padx = 3, pady = 3, sticky=N + W + E)

###########################################
################ MAIN #####################

# Label date, variable, entry
label_date = Label(frame_date, text="Enter the purchase date: (Format: YYYY-MM-DD)")
purchase_date = StringVar()
purchase_date_entry = ttk.Entry(frame_date, textvariable=purchase_date)
purchase_date_entry.insert(0, date.today())
purchase_date_entry.focus() # specify where the cursor starts when you start the program
button_date = Button(frame_date, text="Insert the date", command= lambda : get_date(entry_list, purchase_date_entry)) # The Lambda function is
label_date.pack(ipadx = 10, ipady=10, padx=10, pady=10)
purchase_date_entry.pack()
button_date.pack(padx=10, pady=10)

# HIT RETURN ON THE KEYBOARD AFTER INSERTING A VALUE, THE VALUES IS ADDED TO THE LIST
purchase_date_entry.bind('<Return>', lambda x: get_date(entry_list, purchase_date_entry))

# Label category, variable entry
label_category = Label(frame_category, text="Enter the expense type (e.g.: Food, Transportation, etc.):")
purchase_category = StringVar()
purchase_category_entry = ttk.Entry(frame_category, textvariable=purchase_category)
button_category = Button(frame_category, text="Insert the expense type", command= lambda :  get_category(entry_list, purchase_category_entry))
label_category.pack(ipadx = 10, ipady=10, padx=10, pady=10)
purchase_category_entry.pack()
button_category.pack(padx=10, pady=10)

# HIT RETURN ON THE KEYBOARD AFTER INSERTING A VALUE, THE VALUES IS ADDED TO THE LIST
purchase_category_entry.bind('<Return>', lambda x: get_category(entry_list, purchase_category_entry))

# Label name, variable entry
label_item_name = Label(frame_item_name, text="Enter the good or service for the expense type:")
purchase_item_name = StringVar()
purchase_item_name_entry = ttk.Entry(frame_item_name, textvariable=purchase_item_name)
button_item_name = Button(frame_item_name, text="Insert the item", command= lambda :  get_item_name(entry_list, purchase_item_name_entry))
label_item_name.pack(ipadx = 10, ipady=10, padx=10, pady=10)
purchase_item_name_entry.pack()
button_item_name.pack(padx=10, pady=10)

# HIT RETURN ON THE KEYBOARD AFTER INSERTING A VALUE, THE VALUES IS ADDED TO THE LIST
purchase_item_name_entry.bind('<Return>', lambda x: get_item_name(entry_list, purchase_item_name_entry))

# Label price, variable entry
label_item_price = Label(frame_item_price, text="Enter the price of the good or service:")
purchase_item_price = DoubleVar()
purchase_item_price_entry = ttk.Entry(frame_item_price, textvariable=purchase_item_price)
button_item_price = Button(frame_item_price, text="Enter the price of the good or service:", command = lambda : get_item_price(entry_list, purchase_item_price))
label_item_price.pack(ipadx = 10, ipady=10, padx=10, pady=10)
purchase_item_price_entry.pack()
button_item_price.pack(padx=10, pady=10)

# HIT RETURN ON THE KEYBOARD AFTER INSERTING A VALUE, THE VALUES IS ADDED TO THE LIST
purchase_item_price_entry.bind('<Return>', lambda x: get_item_price(entry_list, purchase_item_price))

# Label store, variable entry
label_item_store = Label(frame_item_store, text="Enter the store name:")
purchase_store = StringVar()
purchase_store_entry = ttk.Entry(frame_item_store, textvariable=purchase_store)
button_store = Button(frame_item_store, text="Insert the store name", command= lambda : get_store(entry_list, purchase_store))
label_item_store.pack(ipadx = 10, ipady=10, padx=10, pady=10)
purchase_store_entry.pack()
button_store.pack(padx=10, pady=10)

# HIT RETURN ON THE KEYBOARD AFTER INSERTING A VALUE, THE VALUES IS ADDED TO THE LIST
purchase_store_entry.bind('<Return>', lambda x: get_store(entry_list, purchase_store))


# SAVE THE FILE, CLOSE THE WINDOW
# Label save file, variable, entry
button_save_file = Button(frame_save_file, text="Save file", command = lambda : save_file(entry_list))
button_save_file.pack(padx=10, pady=10)

# Label save file, variable, entry
button_close_program = Button(frame_close_window, text="Close the window", command = lambda : close_window(root))
button_close_program.pack(padx=10, pady=10)


# KEEP THE WINDOW OF THE PROGRAM ALWAYS OPEN
root.mainloop()