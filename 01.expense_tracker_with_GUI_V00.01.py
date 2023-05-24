"""
    Expense Tracker: this is a very simple Expense Tracker made in Python with a GUI in Tkinter.
    The goal was to understand how the tkinter library works and to learn about it.

"""

# IMPORT THE NECESSARY PACKAGES
from tkinter import *
from tkinter import ttk # is a submodule of tkinter. It implements Python's binding to the newer "themed widgets" that were added to Tk in 8.5.
import customtkinter as ctk
from datetime import date

# IMPORT THE expense_tracker_utils MODULE
from expense_tracker_utils import get_date
from expense_tracker_utils import get_category
from expense_tracker_utils import get_item_name
from expense_tracker_utils import get_item_price
from expense_tracker_utils import get_store
from expense_tracker_utils import save_file
from expense_tracker_utils import close_window

###########################################
######### CUSTOM VARIABLE #################

border_frame_width = 2
hover_button_color = "#f79256"
text_button_color = "#000000"
foreground_button_color = "#1ed69f"
foreground_color = "#59a1ff"
border_color = "#2b476b"

label_font = ("Gill Sans MT", 13)


###########################################
###########################################


# Sets up the main application window, giving it the title "Feet to Meters."
# This is the main outer window
# Create a window
# root = Tk() # with tkinter
root = ctk.CTk()

# Define the grid construction: in this case just two rows
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)

# Set the title
root.title("Expense Tracker")

# Set dimensions: width, heigth, x, y
root.geometry("360x860+800+80") # the +50 means where the window will be displayed on the screen

# Add the icon .ico (.icon)
# root.iconbitmap("budget.ico")
# root.iconphoto(False, PhotoImage(file='C:/Users/a_mac/Documents/solutions/learning_python/budget.png'))
root.wm_iconbitmap(('C:/Users/a_mac/Documents/solutions/learning_python/budget.ico'))

# Avoid resizing window: width, height (boolean)
root.resizable(False, False)

# Set the minimum/maximum dimensions
# root.minsize(600,600)
# root.maxsize(600,1000)

# CREATE EMPTY LIST TO STORE ALL THE ENTRIES
entry_list = []


###########################################
############# Create frames ###############

# ITEM DATE
frame_date = ctk.CTkFrame(master = root, 
                          fg_color = foreground_color,
                          border_width = border_frame_width,
                          border_color = (border_color))

# frame_date.pack(ipadx = 3, ipady=3, padx=15, pady=15, expand=True, fill=X, side=LEFT)
frame_date.grid(column = 0, 
                row = 1, 
                padx = 3, 
                pady = 3, 
                sticky = W + E + N + S)

# ITEM CATEGORY
frame_category = ctk.CTkFrame(master = root, 
                              fg_color = foreground_color,
                              border_width = border_frame_width,
                              border_color = (border_color))

# frame_category.pack(ipadx = 15, ipady=15, padx=15, pady=10, expand=True, fill=X, side=LEFT)
frame_category.grid(column = 0, 
                    row = 2, 
                    padx = 3, 
                    pady = 3, 
                    sticky = W + E + N + S)

# ITEM NAME
frame_item_name = ctk.CTkFrame(master = root, 
                               fg_color = foreground_color,
                               border_width = border_frame_width,
                               border_color = (border_color))

# frame_item_name.pack(ipadx = 15, ipady=15, padx=15, pady=10, expand=True, fill=X, side=LEFT)
frame_item_name.grid(column = 0, 
                     row = 3, 
                     padx = 3,
                     pady = 3,
                     sticky = W + E + N + S)

# ITEM PRICE
frame_item_price = ctk.CTkFrame(master = root, 
                                fg_color = foreground_color,
                                border_width = border_frame_width,
                                border_color = (border_color))

# frame_item_price.pack(ipadx = 15, ipady=15, padx=15, pady=10, expand=True, fill=X, side=LEFT)
frame_item_price.grid(column = 0, 
                      row = 4, 
                      padx = 3,
                      pady = 3,
                      sticky = W + E + N + S)

# ITEM STORE
frame_item_store = ctk.CTkFrame(master = root, 
                                fg_color = foreground_color,
                                border_width = border_frame_width,
                                border_color = (border_color))

# frame_item_store.pack(ipadx = 15, ipady=15, padx=15, pady=10, expand=True, fill=X, side=LEFT)
frame_item_store.grid(column = 0, 
                      row = 5,  
                      padx = 3, 
                      pady = 3, 
                      sticky = W + E + N + S)

# SAVE THE FINAL FILE
frame_save_file = ctk.CTkFrame(master = root, 
                               fg_color = "transparent",
                               border_color = (border_color))

# frame_item_store.pack(ipadx = 15, ipady=15, padx=15, pady=10, expand=True, fill=X, side=LEFT)
frame_save_file.grid(column = 0, 
                     row = 6, 
                     padx = 3, 
                     pady = 3, 
                     sticky = W + E + N + S)

# SAVE THE FINAL FILE
frame_close_window = ctk.CTkFrame(master = root, 
                                  fg_color = "transparent",
                                  border_color = (border_color))

# frame_item_store.pack(ipadx = 15, ipady=15, padx=15, pady=10, expand=True, fill=X, side=LEFT)
frame_close_window.grid(column = 0, 
                        row = 7, 
                        padx = 3, 
                        pady = 3, 
                        sticky = W + E + N + S)

###########################################
################ MAIN #####################

# Label date, variable, entry
label_date = ctk.CTkLabel(frame_date, 
                          text = "Enter the purchase date: (Format: YYYY-MM-DD)".upper(),
                          font = label_font)
purchase_date = StringVar()
purchase_date_entry = ctk.CTkEntry(frame_date, textvariable=purchase_date)
purchase_date_entry.insert(0, date.today())
purchase_date_entry.focus() # specify where the cursor starts when you start the program
button_date = ctk.CTkButton(frame_date, 
                            text = "Insert the date", 
                            command = lambda : get_date(entry_list, purchase_date_entry),
                            fg_color = foreground_button_color,
                            text_color = text_button_color,
                            hover_color = hover_button_color)

label_date.pack(ipadx = 10,
                ipady = 10, 
                padx = 10, 
                pady = 10)
purchase_date_entry.pack()
button_date.pack(padx = 10, 
                 pady = 10)

# HIT RETURN ON THE KEYBOARD AFTER INSERTING A VALUE, THE VALUES IS ADDED TO THE LIST
purchase_date_entry.bind('<Return>', lambda x: get_date(entry_list, purchase_date_entry))

# Label category, variable entry
label_category = ctk.CTkLabel(frame_category, 
                              text = "Enter the expense type (e.g.: Food, etc.):".upper(),
                              font = label_font)
purchase_category = StringVar()
purchase_category_entry = ctk.CTkEntry(frame_category, textvariable=purchase_category)
button_category = ctk.CTkButton(frame_category, 
                                text = "Insert the expense type", 
                                command= lambda :  get_category(entry_list, purchase_category_entry),
                                fg_color = foreground_button_color,
                                text_color = text_button_color,
                                hover_color = hover_button_color)

label_category.pack(ipadx = 10, 
                    ipady = 10, 
                    padx = 10, 
                    pady = 10)
purchase_category_entry.pack()
button_category.pack(padx = 10, 
                     pady = 10)

# HIT RETURN ON THE KEYBOARD AFTER INSERTING A VALUE, THE VALUES IS ADDED TO THE LIST
purchase_category_entry.bind('<Return>', lambda x: get_category(entry_list, purchase_category_entry))

# Label name, variable entry
label_item_name = ctk.CTkLabel(frame_item_name, 
                               text = "Enter the item/service name purchased:".upper(),
                               font = label_font)
purchase_item_name = StringVar()
purchase_item_name_entry = ctk.CTkEntry(frame_item_name, 
                                        textvariable = purchase_item_name)
button_item_name = ctk.CTkButton(frame_item_name, 
                                 text = "Insert the item name", 
                                 command= lambda :  get_item_name(entry_list, purchase_item_name_entry),
                                 fg_color = foreground_button_color,
                                 text_color = text_button_color,
                                 hover_color = hover_button_color)
label_item_name.pack(ipadx = 10, 
                     ipady = 10, 
                     padx = 10, 
                     pady = 10)
purchase_item_name_entry.pack()
button_item_name.pack(padx = 10, 
                      pady = 10)

# HIT RETURN ON THE KEYBOARD AFTER INSERTING A VALUE, THE VALUES IS ADDED TO THE LIST
purchase_item_name_entry.bind('<Return>', lambda x: get_item_name(entry_list, purchase_item_name_entry))

# Label price, variable entry
label_item_price = ctk.CTkLabel(frame_item_price, 
                                text = "Enter the item/service price".upper(),
                                font = label_font)
purchase_item_price = DoubleVar()
purchase_item_price_entry = ctk.CTkEntry(frame_item_price, 
                                         textvariable = purchase_item_price)
button_item_price = ctk.CTkButton(frame_item_price, 
                                  text = "Insert the item/service price", 
                                  command = lambda : get_item_price(entry_list, purchase_item_price),
                                  fg_color = foreground_button_color,
                                  text_color = text_button_color,
                                  hover_color = hover_button_color)
label_item_price.pack(ipadx = 10, 
                      ipady = 10, 
                      padx = 10, 
                      pady = 10)
purchase_item_price_entry.pack()
button_item_price.pack(padx = 10, 
                       pady = 10)

# HIT RETURN ON THE KEYBOARD AFTER INSERTING A VALUE, THE VALUES IS ADDED TO THE LIST
purchase_item_price_entry.bind('<Return>', lambda x: get_item_price(entry_list, purchase_item_price))

# Label store, variable entry
label_item_store = ctk.CTkLabel(frame_item_store, 
                                text = "Enter the store name:".upper(),
                                font = label_font)
purchase_store = StringVar()
purchase_store_entry = ctk.CTkEntry(frame_item_store, 
                                    textvariable = purchase_store)
button_store = ctk.CTkButton(frame_item_store, 
                             text="Insert the store name", 
                             command= lambda : get_store(entry_list, purchase_store),
                             fg_color = foreground_button_color,
                             text_color = text_button_color,
                             hover_color = hover_button_color)
label_item_store.pack(ipadx = 10, 
                      ipady = 10, 
                      padx = 10, 
                      pady = 10)
purchase_store_entry.pack()
button_store.pack(padx = 10, 
                  pady = 10)

# HIT RETURN ON THE KEYBOARD AFTER INSERTING A VALUE, THE VALUES IS ADDED TO THE LIST
purchase_store_entry.bind('<Return>', lambda x: get_store(entry_list, purchase_store))


# SAVE THE FILE, CLOSE THE WINDOW
# Label save file, variable, entry
button_save_file = ctk.CTkButton(frame_save_file, 
                                 text = "Save file", 
                                 command = lambda : save_file(entry_list),
                                 fg_color = foreground_button_color,
                                 text_color = text_button_color,
                                 font = label_font)
button_save_file.pack(padx = 10, 
                      pady = 10)

# Label save file, variable, entry
button_close_program = ctk.CTkButton(frame_close_window, 
                                     text = "Close the window", 
                                     command = lambda : close_window(root),
                                     fg_color = "#d66066",
                                     text_color = text_button_color,
                                     font = label_font)
button_close_program.pack(padx = 10, 
                          pady = 10)


# KEEP THE WINDOW OF THE PROGRAM ALWAYS OPEN
root.mainloop()