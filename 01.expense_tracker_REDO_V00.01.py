# IMPORT LIBRARIES
import numpy as np
import pandas as pd
from datetime import date
import csv
import os
from pathlib import Path # https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/#:~:text=How%20to%20Check%20if%20a%20File%20Exists%20Using%20the%20Path,the%20file%20doesn't%20exist.&text=Since%20the%20example.txt%20file,is_file()%20method%20returns%20True%20.
import expense_tracker_utils


"""
    Open the file if it exists, else create one filled with column names. --> DONE
    Ask for input to the user and create a list to add to a new row to the DF and save the file
    Show the new dataframe
    Close the program.
"""

# create a Path object with the path to the file
path_to_expense_file = Path('expense_report.csv')

# Check if the file exists, otherwise create one with the right columns
expense_tracker_utils.expense_file(path_to_expense_file)

# Read the file
df_expenses = pd.read_csv("expense_report.csv")
print(df_expenses)

# Ask the user about the items purchased
option = -1 # User option or choice or input. Initialize to -1.

# Create an expense list that holds all the information about the purchase.
expense_list = []

while(option != 0):

    # Create the option menu
    print("Welcome to the Expense Tracker:")
    print()
    print("1. Add Expense")
    print("0. Exit the program")

    option = int(input('Choose an option:\n')) # The user has to insert an integer

    # Print a new line
    print()

    if option == 0:
        print("Closing the Expense Tracker...")
        break
    if option == 1:
        expense_date =          input("Enter the purchase date:\n")
        expense_category =      str(input("Enter the expense type (e.g.: Food, Transportation, etc.):\n"))
        expense_item =          str(input("Enter the good or service for the expense type " + expense_category + ":\n"))
        expense_price =         float(input("Enter the price of the good or service:\n"))
        expense_store =         str(input("Enter the store name:\n"))

        if expense_date == "":
            expense_date = date.today() # date type
        else:
            expense_date = date(expense_date)
                
        expense_list.append(expense_date)
        expense_list.append(expense_category)
        expense_list.append(expense_item)
        expense_list.append(expense_price)
        expense_list.append(expense_store)
        print(expense_list)

        # Add the expense row to end of the DataFrame
        df_expenses.loc[len(df_expenses.index)] = expense_list

        print(df_expenses)

        add_more_expenses = input("Would you like to add more expenses? Enter N to QUIT, Enter Y to continue.\n")

        if add_more_expenses == "N":
            print("Thanks for using the Expense Tracker. Have a nice day!")
            df_expenses.to_csv("expense_report.csv", index = False)  
            break
        else:
            continue
