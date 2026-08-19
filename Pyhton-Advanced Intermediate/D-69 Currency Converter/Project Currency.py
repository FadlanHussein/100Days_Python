import os
import json
import tkinter as tk
from tkinter import ttk, messagebox

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "exchange_rate.json")

def load_exchange_rates(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data.get("rates", {}) if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def convert_currency(amount: float, from_currency: str, to_currency: str, rates: dict):
    if not rates or from_currency not in rates or to_currency not in rates:
        return None
    base_amount = amount / rates[from_currency]
    return base_amount * rates[to_currency]

def handle_conversion():
    try:
        amount_text = amount_entry.get().strip()
        if not amount_text:
            messagebox.showwarning("Input Error", "Please enter an amount.")
            return

        amount = float(amount_text)
        from_curr = from_currency_combobox.get().strip()
        to_curr = to_currency_combobox.get().strip()

        if not from_curr or not to_curr:
            messagebox.showwarning("Input Error", "Please select both currencies.")
            return

        result = convert_currency(amount, from_curr, to_curr, rates)
        if result is not None:
            result_label.config(text=f"{amount:,.2f} {from_curr} = {result:,.4f} {to_curr}")
        else:
            messagebox.showerror("Error", "Conversion not possible. Check exchange rates!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric amount!")

# Load initial exchange rates
rates = load_exchange_rates(FILE_PATH)
currency_list = sorted(list(rates.keys()))

# Tkinter Setup
root = tk.Tk()
root.title("Project Currency Converter")
root.geometry("450x380")
root.resizable(False, False)

# Amount Entry
amount_label = tk.Label(root, text="Amount:", font=("Arial", 10, "bold"))
amount_label.pack(pady=(15, 2))
amount_entry = tk.Entry(root, font=("Arial", 11), justify="center")
amount_entry.pack(pady=5, ipadx=10, ipady=3)

# From Currency Dropdown
from_currency_label = tk.Label(root, text="From Currency:", font=("Arial", 10))
from_currency_label.pack(pady=(10, 2))
from_currency_combobox = ttk.Combobox(root, values=currency_list, state="readonly", justify="center")
from_currency_combobox.pack(pady=5)
if "IDR" in currency_list:
    from_currency_combobox.set("IDR")
elif currency_list:
    from_currency_combobox.set(currency_list[0])

# To Currency Dropdown
to_currency_label = tk.Label(root, text="To Currency:", font=("Arial", 10))
to_currency_label.pack(pady=(10, 2))
to_currency_combobox = ttk.Combobox(root, values=currency_list, state="readonly", justify="center")
to_currency_combobox.pack(pady=5)
if "USD" in currency_list:
    to_currency_combobox.set("USD")
elif currency_list:
    to_currency_combobox.set(currency_list[0])

# Convert Button
convert_button = tk.Button(
    root, 
    text="Convert", 
    font=("Arial", 11, "bold"), 
    bg="#4CAF50", 
    fg="white", 
    padx=10, 
    pady=2, 
    command=handle_conversion
)
convert_button.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="#1E88E5")
result_label.pack(pady=10)

root.mainloop()