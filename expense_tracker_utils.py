# IMPORT LIBRARIES
import numpy as np
import pandas as pd
from datetime import date
from datetime import datetime
import csv
import os
from pathlib import Path # https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/#:~:text=How%20to%20Check%20if%20a%20File%20Exists%20Using%20the%20Path,the%20file%20doesn't%20exist.&text=Since%20the%20example.txt%20file,is_file()%20method%20returns%20True%20.
from tkinter import filedialog # Needed to select the file to open


# FUNCTIONS
def expense_file():
    path_to_expense_file = "C:/Users/a_mac/Documents/solutions/learning_python/expense_report.csv"
    
    filetypes = (
        ("CSV File", "*.csv"),
        ("ALL File", "*.*")
    )

    # If the file does not exists, first create it, then open it.
    if not os.path.exists(path_to_expense_file):
        with open('C:/Users/a_mac/Documents/solutions/learning_python/expense_report.csv', 'a+', newline='') as outcsv:
            writer = csv.DictWriter(outcsv, fieldnames = ["date", "category", "itemName", "itemPrice", "store"])
            writer.writeheader()
        # path_to_expense_file("expense_report.csv", 'w').close()
    else:
        filename = filedialog.askopenfilenames(initialdir="C:/Users/a_mac/Documents/solutions/learning_python/", filetypes=filetypes)
        read_file = pd.read_csv(filename[0])
        print("The file already exists.")

    return read_file

###########################

def get_date(entry_list, purchase_date_entry):
    result = str(purchase_date_entry.get())

    if result == "":
        result = date.today() # date type
        print(result)
        date_format =  "%Y-%m-%d"
        result = datetime.strptime(result, date_format).date() # get only the date without the time
        result = result.strftime('%Y-%m-%d')
    else:
        date_format =  "%Y-%m-%d"
        result = datetime.strptime(result, date_format).date() # get only the date without the time
        result = result.strftime('%Y-%m-%d')

    entry_list.append(result)
    print(entry_list)
    return result


def get_category(entry_list, purchase_category_entry): # Why adding event=None? https://stackoverflow.com/questions/47475783/how-to-bind-enter-key-to-a-tkinter-button
    result = purchase_category_entry.get()
    entry_list.append(result)
    print(entry_list)
    return result

def get_item_name(entry_list, purchase_item_name_entry):
    result = purchase_item_name_entry.get()
    entry_list.append(result)
    print(entry_list)
    return result

def get_item_price(entry_list, purchase_item_price_entry):
    result = purchase_item_price_entry.get()
    entry_list.append(result)
    print(entry_list)
    return result

def get_store(entry_list, purchase_store_entry):
    result = purchase_store_entry.get()
    entry_list.append(result)
    print("COMPLETE LIST:", entry_list)
    return result


def save_file(entry_list):

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
def close_window(root):
    root.quit()