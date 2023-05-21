"""
    Continue from episode 11:
    https://www.youtube.com/watch?v=0eltxbvFy30&list=PLP5MAKLy8lP8nJcyISKe3t78rSRVYPxid&index=11

    Useful links:
    - https://stackoverflow.com/questions/39547768/how-do-i-get-an-entry-widget-to-save-what-i-input-python-tkinter
"""


from tkinter import *
# Import theme tkinter: add some widget to tkinter
from tkinter import ttk # is a submodule of tkinter. It implements Python's binding to the newer "themed widgets" that were added to Tk in 8.5.
from tkinter import filedialog # Needed to select the file to open
from datetime import date
from datetime import datetime
import csv
import os


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
root.iconbitmap("budget.ico")

# Avoid resizing window: width, height (boolean)
root.resizable(False, False)

# Set the minimum/maximum dimensions
# root.minsize(600,600)
# root.maxsize(600,1000)

# CREATE EMPTY LIST TO STORE ALL THE ENTRIES
entry_list = []


# FUNCTIONS TO SAVE THE VALUES
def get_date():
    result = str(purchase_date_entry.get())

    if result == "":
        result = date.today() # date type
        print(result)
        date_format =  "%Y-%m-%d"
        result = datetime.strptime(result, date_format).date() # get only the date without the time
        result = result.strftime('%Y-%m-%d')
        # expense_date = date(expense_date)
    else:
        # expense_date = date(expense_date)
        date_format =  "%Y-%m-%d"
        result = datetime.strptime(result, date_format).date() # get only the date without the time
        result = result.strftime('%Y-%m-%d')

    entry_list.append(result)
    print(entry_list)
    return result

def get_category(event=None): # Why adding event=None? https://stackoverflow.com/questions/47475783/how-to-bind-enter-key-to-a-tkinter-button
    result = purchase_category_entry.get()
    entry_list.append(result)
    print(entry_list)
    return result

def get_item_name(event=None):
    result = purchase_item_name_entry.get()
    entry_list.append(result)
    print(entry_list)
    return result

def get_item_price(event=None):
    result = purchase_item_price_entry.get()
    entry_list.append(result)
    print(entry_list)
    return result

def get_store(event=None):
    result = purchase_store_entry.get()
    entry_list.append(result)
    print("COMPLETE LIST:", entry_list)
    return result

def save_file():

    # OPEN A FILE DIALOG TO CHOOSE THE DESTINATION FILE
    file_path = filedialog.asksaveasfilename(defaultextension=".csv")

    # OPEN THE FILE IN APPEND MODE
    with open(file_path, mode='a+', newline='') as file:
        # WRITE THE FILE
        writer_row = csv.writer(file)
        
        
        # IF THE FILE HAS A SIZE OF 0, THEN IT MEANS THAT IS EMPTY
        if os.stat(file_path).st_size == 0:
            print('File is empty!')
            print('Creating a new file and inserting the header and the data...')
    
            # OPEN THE FILE IN APPEND MODE
            with open(file_path, mode='a+', newline='') as file:
                writer = csv.DictWriter(file, fieldnames = ["date", "category", "itemName", "itemPrice", "store"])
                writer.writeheader()

                # SAVE THE FINAL LIST OF ELEMENTS
                writer_row.writerow(entry_list)
                print("The new expense has been recorded!")

                # CLEAR THE LIST TO ADD OTHER ITEMS
                entry_list.clear()

        else:
            # IF THE FILE DOES EXISTS, THEN OPEN IT AND INSERT THE DATA
            # OPEN THE FILE IN APPEND MODE
            with open(file_path, mode='a+', newline='') as file:

                # SAVE THE FINAL LIST OF ELEMENTS
                writer_row.writerow(entry_list)
                print("The new expense has been recorded!")

                # CLEAR THE LIST TO ADD OTHER ITEMS
                entry_list.clear()

    return


# DEFINE A FUNCTION TO CLOSE THE WINDOW
def close_window():
    root.quit()


###########################################
############# Create frames ###############
# frame_open_file = Frame(root, background="#c4c4be")
# # frame_item_store.pack(ipadx = 15, ipady=15, padx=15, pady=10, expand=True, fill=X, side=LEFT)
# frame_open_file.grid(column=0, row=0, columnspan=2, padx = 3, pady = 3, sticky=N + W + E)

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
###### Create labels, entry, buttons ######

# # Label open file, variable, entry
# purchase_open_file = StringVar()
# button_open_file = Button(frame_open_file, text="Open file", command=expense_tracker_utils.expense_file)
# button_open_file.pack(padx=10, pady=10)


# Label date, variable, entry
label_date = Label(frame_date, text="Enter the purchase date: (Format: YYYY-MM-DD)")
purchase_date = StringVar()
purchase_date_entry = ttk.Entry(frame_date, textvariable=purchase_date)
purchase_date_entry.insert(0, date.today())
purchase_date_entry.focus() # specify where the cursor starts when you start the program
button_date = Button(frame_date, text="Insert the date", command= get_date)
label_date.pack(ipadx = 10, ipady=10, padx=10, pady=10)
purchase_date_entry.pack()
button_date.pack(padx=10, pady=10)

# Label category, variable entry
label_category = Label(frame_category, text="Enter the expense type (e.g.: Food, Transportation, etc.):")
purchase_category = StringVar()
purchase_category_entry = ttk.Entry(frame_category, textvariable=purchase_category)
button_category = Button(frame_category, text="Insert the expense type", command= get_category)
label_category.pack(ipadx = 10, ipady=10, padx=10, pady=10)
purchase_category_entry.pack()
button_category.pack(padx=10, pady=10)

# WHENEVER YOU HIT RETURN ON THE KEYBOARD AFTER INSERTING A VALUE, THE VALUES IS ADDED TO THE LIST
purchase_category_entry.bind('<Return>', get_category)

# Label name, variable entry
label_item_name = Label(frame_item_name, text="Enter the good or service for the expense type:")
purchase_item_name = StringVar()
purchase_item_name_entry = ttk.Entry(frame_item_name, textvariable=purchase_item_name)
button_item_name = Button(frame_item_name, text="Insert the item", command= get_item_name)
label_item_name.pack(ipadx = 10, ipady=10, padx=10, pady=10)
purchase_item_name_entry.pack()
button_item_name.pack(padx=10, pady=10)

# WHENEVER YOU HIT RETURN ON THE KEYBOARD AFTER INSERTING A VALUE, THE VALUES IS ADDED TO THE LIST
purchase_item_name_entry.bind('<Return>', get_item_name)

# Label price, variable entry
label_item_price = Label(frame_item_price, text="Enter the price of the good or service:")
purchase_item_price = DoubleVar()
purchase_item_price_entry = ttk.Entry(frame_item_price, textvariable=purchase_item_price)
button_item_price = Button(frame_item_price, text="Enter the price of the good or service:", command= get_item_price)
label_item_price.pack(ipadx = 10, ipady=10, padx=10, pady=10)
purchase_item_price_entry.pack()
button_item_price.pack(padx=10, pady=10)

# WHENEVER YOU HIT RETURN ON THE KEYBOARD AFTER INSERTING A VALUE, THE VALUES IS ADDED TO THE LIST
purchase_item_price_entry.bind('<Return>', get_item_price)

# Label store, variable entry
label_item_store = Label(frame_item_store, text="Enter the store name:")
purchase_store = StringVar()
purchase_store_entry = ttk.Entry(frame_item_store, textvariable=purchase_store)
button_store = Button(frame_item_store, text="Insert the store name", command= get_store)
label_item_store.pack(ipadx = 10, ipady=10, padx=10, pady=10)
purchase_store_entry.pack()
button_store.pack(padx=10, pady=10)

# WHENEVER YOU HIT RETURN ON THE KEYBOARD AFTER INSERTING A VALUE, THE VALUES IS ADDED TO THE LIST
purchase_store_entry.bind('<Return>', get_store)

# Label save file, variable, entry
button_save_file = Button(frame_save_file, text="Save file", command = save_file)
button_save_file.pack(padx=10, pady=10)

# Label save file, variable, entry
button_close_program = Button(frame_close_window, text="Close the window", command = close_window)
button_close_program.pack(padx=10, pady=10)

####################################

# This is the way the window of the program will stay continously open
root.mainloop()

