# Date
# Category
# Amount
# Description

import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

file_path = os.path.join(os.path.dirname(__file__), "expenses2.csv")

def log_expense2(date, category, amount, description):
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

def load_expenses2():
    if not os.path.exists(file_path):
        return pd.DataFrame(columns=["date", "category", "amount", "description"])
    return pd.read_csv(file_path, names=["date", "category", "amount", "description"])

def summarize_expenses2(df):
    if df.empty:
        print("\nBelum ada data pengeluaran.")
        return
    summary = df.groupby("category")["amount"].sum()
    print("\n--- Expense Summary ---")
    print(summary)
    
# Contoh menambahkan pengeluaran baru (opsional):
# log_expense2("2026-08-14", "Food", 150, "Lunch")
# log_expense2("2026-08-14", "Transport", 50, "Taxi")

def plot_expenses2_by_category(df):
    if df.empty:
        return
    output_path = os.path.join(os.path.dirname(__file__), "expenses2_chart.png")
    summary = df.groupby("category")["amount"].sum()
    summary.plot(kind="pie", autopct="%1.1f%%", figsize=(10,10), title="Expenses by Category")
    plt.ylabel("")
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    print(f"Chart saved to: {output_path}")

# plot_expenses2_by_category(df)

def main():
    print("Welcome to The Expenses Tracker")
    while True:
        print("\nMenu:")
        print("1. Log Expense")
        print("2. View Summary")
        print("3. View Chart")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            log_expense2(date, category, amount, description)
            print("Expense logged successfully!")
        elif choice == "2":
            df = load_expenses2()  # reload agar data selalu terbaru
            summarize_expenses2(df)
        elif choice == "3":
            df = load_expenses2()  # reload agar chart selalu terbaru
            plot_expenses2_by_category(df)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
    print("Thank you for using The Expenses Tracker")

if __name__ == "__main__":
    main()