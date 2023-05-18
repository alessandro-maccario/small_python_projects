# IMPORT LIBRARIES
import numpy as np
import pandas as pd
from datetime import date
import csv
import os
from pathlib import Path # https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/#:~:text=How%20to%20Check%20if%20a%20File%20Exists%20Using%20the%20Path,the%20file%20doesn't%20exist.&text=Since%20the%20example.txt%20file,is_file()%20method%20returns%20True%20.


def expense_file(path_to_expense_file):
    if not os.path.exists(path_to_expense_file):
        with open('expense_report.csv', 'a+', newline='') as outcsv:
            writer = csv.DictWriter(outcsv, fieldnames = ["date", "category", "itemName", "itemPrice", "store"])
            writer.writeheader()
        # path_to_expense_file("expense_report.csv", 'w').close()
    else:
        print("The file already exists.")
