from six import print_
import os
import pandas as pd 

import tkinter as tk
from tkinter import filedialog

def load_file(file_path):
    if file_path.endswitch(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswitch(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format Please upload a CSV or Excel file")

data = load_file("data.csv")
def update_dropdowns(coloumns):
    x_dropdown.set("")
    y_dropdown.set("")
    x_menu['menu'].delete(0, 'end')
    y_menu['menu'].delete(0, 'end')

    for col in coloumns:
        x_menu['menu'].add_command(label=col, command=lambda c=col: x_dropdown.set(c))
        y_menu['menu'].add_command(label=col, command=lambda c=col: y_dropdown.set(c))


root = tk.Tk()
root.title("Data Visual App")
root.geometry("400x300")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=["CSV Files", "Excel Files"])
    print(f"File selected: {file_path}")

upload_button = tk.Button(root, text="Upload File", command=handle_file_upload)
upload_button.pack(pady=10)

def handle_file_upload():
    file_path = filedialog.askopenfilename(filetypes=["CSV Files", "Excel Files"])
    try:
        df = load_file(file_path)
        update_dropdowns(df.columns)
        print(f"Coloumns Available : {df.columns}")
    except Exception as e:
        print(f"Error Loading Data : {e}")

# Dropdown for selecting coloumns
x_label = tk.Label(root, text="Select X-axis:")
x_label.pack(pady=10)
x_dropdown = tk.StringVar(root)
x_menu = tk.OptionMenu(root, x_dropdown, [])
x_menu.pack(pady=10)

y_label = tk.Label(root, text="Select Y-axis:")
y_label.pack(pady=10)
y_dropdown = tk.StringVar(root)
y_menu = tk.OptionMenu(root, y_dropdown, [])
y_menu.pack(pady=10)

def handle_plot_button():
    try:
        x_axis = x_dropdown.get()
        y_axis = y_dropdown.get()
        if not x_axis or not y_axis:
            print("Please select both X and Y axes")
        else:
            plot_data(df, x_axis, y_axis)
    except Exception as e:
        print(f"Error plotting data : {e}")

plot_button = tk.Button(root, text="Plot Data", command=handle_plot_button)
plot_button.pack(pady=10)


root.mainloop()


from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
import numpy as np

def plot_data(df, coloumn_x, coloumn_y):
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(df[coloumn_x].[coloumn_y], marker="o")
    ax.set_title(f"{coloumn_x} vs {coloumn_y}")
    ax.set_xlabel(coloumn_x)
    ax.set_ylabel(coloumn_y)
    
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

           


        