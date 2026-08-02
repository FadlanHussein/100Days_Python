# Objective: Build a GUI-based Expense Tracker App that allows users to :

# 1. Add expenses with details like amount, category, and date.
# 2. View a list of all expenses.   
# 3. Delete expenses from the list.
# 4. Save and load expenses from a file for persistence.
# 5. Calculate total expenses and display them in the GUI.

# Core Features:
# 1. User-friendly interface for adding, viewing, and deleting expenses.
# 2. Validation fo numerical input for amount and proper date format.
# 3. Persistent storage of expenses in a file (e.g., CSV or JSON).
# 4. Total expenses calculation and display in the GUI.
# 5. Ablitiy to delete individual expenses from the list.

# Key GUI Components:
# 1. Entry widgets for amount, category, and date input.
# 2. Buttons for adding, deleting, and saving expenses.
# 3. Listbox or Treeview for displaying the list of expenses.
# 4. Labels for displaying total expenses and other relevant information.
# 5. Message boxes for user feedback and error handling.

import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

# Expense Tracker App

# File for storing expenses
EXPENSES_FILE = "expenses.csv"

# Create the main application window
root = tk.Tk()
root.title("Expense Tracker App")
root.geometry("700x520")
root.configure(bg="#d38787")

# Expense Data List
expenses = []

# Load Existing Expenses from CSV
def load_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return

    with open(EXPENSES_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            expenses.append(row)
            expenses_listbox.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]}")

    calculate_total()

# Save Expenses to CSV
def save_expenses():
    with open(EXPENSES_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for expense in expenses:
            writer.writerow(expense)
    messagebox.showinfo("Success", "Expenses saved successfully!")

# Add Expense Function
def add_expense():
    category = category_var.get()
    amount = amount_entry.get().strip()
    description = description_entry.get().strip()

    try:
        amount_value = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric amount.")
        return

    if category == "Select Category" or not description:
        messagebox.showerror("Error", "Please enter valid details.")
        return

    expenses.append([category, str(amount_value), description])
    expenses_listbox.insert(tk.END, f"{category} | {amount_value:.2f} | {description}")
    calculate_total()
    clear_input()
    save_expenses()

# Delete Selected Expense Function
def delete_expense():
    selected = expenses_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select an expense to delete.")
        return

    index = selected[0]
    del expenses[index]
    expenses_listbox.delete(index)
    calculate_total()
    save_expenses()

# Clear All Inputs
def clear_input():
    category_var.set("Select Category")
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

# Calculate Total Expenses
def calculate_total():
    total = sum(float(expense[1]) for expense in expenses)
    total_label.config(text=f"Total Expenses: ${total:.2f}")

# Clear All Expenses Function
def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all expenses?"):
        expenses.clear()
        expenses_listbox.delete(0, tk.END)
        calculate_total()
        save_expenses()

# ---- GUI Layout ----

# Title Label
title_label = tk.Label(root, text="Expense Tracker", font=("Arial", 24), bg="#f0f0f0")
title_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#b84f4f")
input_frame.pack(pady=10)

# Category Input
category_label = tk.Label(input_frame, text="Category:", font=("Arial", 12), bg="#f0f0f0")
category_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
category_var = tk.StringVar(value="Select Category")
category_dropdown = tk.OptionMenu(input_frame, category_var, "Food", "Transportation", "Entertainment", "Utilities")
category_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Amount Input
amount_label = tk.Label(input_frame, text="Amount:", font=("Arial", 12), bg="#f0f0f0")
amount_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
amount_entry = tk.Entry(input_frame, font=("Arial", 12))
amount_entry.grid(row=1, column=1, padx=5, pady=5)

# Description Input
description_label = tk.Label(input_frame, text="Description:", font=("Arial", 12), bg="#f0f0f0")
description_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
description_entry = tk.Entry(input_frame, font=("Arial", 12))
description_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

add_button = tk.Button(btn_frame, text="Add Expense", command=add_expense, font=("Arial", 12), bg="#4caf50", fg="white")
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(btn_frame, text="Delete Expense", command=delete_expense, font=("Arial", 12), bg="#f44336", fg="white")
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(btn_frame, text="Clear All", command=clear_all, font=("Arial", 12), bg="#1e88e5", fg="white")
clear_button.grid(row=0, column=2, padx=5)

# Expenses Listbox with Scrollbar
frame_listbox = tk.Frame(root, bg="#f0f0f0")
frame_listbox.pack(pady=10)

scrollbar = tk.Scrollbar(frame_listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

expenses_listbox = tk.Listbox(frame_listbox, height=10, width=50, yscrollcommand=scrollbar.set)
expenses_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=expenses_listbox.yview)

# Total Expenses Label
total_label = tk.Label(root, text="Total Expenses: $0.00", font=("Arial", 14, "bold"), bg="#f0f0f0")
total_label.pack(pady=10)

# Load existing expenses on startup
expenses_listbox.delete(0, tk.END)
load_expenses()
calculate_total()

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="#9e9e9e", fg="white")
exit_button.pack(pady=10)

# Start the main event loop
root.mainloop()
