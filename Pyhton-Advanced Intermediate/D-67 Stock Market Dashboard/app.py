import os
import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def load_data(file_path):
    return pd.read_csv(file_path)


# Load dataset
csv_path = os.path.join(os.path.dirname(__file__), 'stock_data.csv')
stock_data = load_data(csv_path)

# Main window
root = tk.Tk()
root.title('Stock Market Dashboard')
root.geometry('800x650')

# Global reference to hold canvas widget so we can update it
current_canvas = None


def plot_stock_data(stock):
    global current_canvas

    if not stock:
        return

    filtered_data = stock_data[stock_data['Ticker'] == stock]

    # Remove previous canvas if exists
    if current_canvas is not None:
        current_canvas.get_tk_widget().destroy()

    fig = Figure(figsize=(7, 4.5), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(filtered_data['Date'], filtered_data['Close'], marker='o', color='#1f77b4')
    ax.set_xlabel('Date')
    ax.set_ylabel('Close Price ($)')
    ax.set_title(f'{stock} Stock Price')
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()

    current_canvas = FigureCanvasTkAgg(fig, master=root)
    current_canvas.draw()
    current_canvas.get_tk_widget().pack(pady=10)


# Dropdown for selecting stock
stock_label = tk.Label(root, text='Select Stock:', font=('Arial', 11))
stock_label.pack(pady=(15, 5))

tickers = list(stock_data['Ticker'].unique())
selected_stock = tk.StringVar(value=tickers[0] if tickers else '')

stock_dropdown = ttk.Combobox(root, values=tickers, textvariable=selected_stock, state='readonly')
stock_dropdown.pack(pady=5)

# Button to plot data
plot_button = ttk.Button(root, text='Plot Stock Data', command=lambda: plot_stock_data(selected_stock.get()))
plot_button.pack(pady=10)

# Initial plot with default stock
if tickers:
    plot_stock_data(selected_stock.get())

root.mainloop()