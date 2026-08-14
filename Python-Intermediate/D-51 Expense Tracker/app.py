# Date
# Category
# Amount
# Description

import csv
import os
from datetime import datetime

def log_expense(date, category, amount, description):
    file_path = os.path.join(os.path.dirname(__file__), "expenses.csv")
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

# Example
log_expense(datetime.now().strftime("%Y-%m-%d"), "Food", 150, "Lunch")
print("Expense logged successfully!")
