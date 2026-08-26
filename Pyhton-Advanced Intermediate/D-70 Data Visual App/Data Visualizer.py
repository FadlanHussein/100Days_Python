import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def load_file(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")


def update_dropdowns(columns):
    x_dropdown.set("")
    y_dropdown.set("")
    x_menu["menu"].delete(0, "end")
    y_menu["menu"].delete(0, "end")

    for col in columns:
        x_menu["menu"].add_command(label=col, command=lambda c=col: x_dropdown.set(c))
        y_menu["menu"].add_command(label=col, command=lambda c=col: y_dropdown.set(c))


def handle_file_upload():
    global data
    file_path = filedialog.askopenfilename(
        filetypes=[("Data Files", "*.csv;*.xlsx"), ("CSV Files", "*.csv"), ("Excel Files", "*.xlsx"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    try:
        data = load_file(file_path)
        update_dropdowns(data.columns)
        print(f"Columns Available: {list(data.columns)}")
    except Exception as e:
        messagebox.showerror("Error", f"Error loading file: {e}")


def plot_data(df, column_x, column_y):
    global canvas
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(df[column_x], df[column_y], marker="o")
    ax.set_title(f"{column_x} vs {column_y}")
    ax.set_xlabel(column_x)
    ax.set_ylabel(column_y)
    fig.tight_layout()

    if canvas is not None:
        canvas.get_tk_widget().destroy()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def handle_plot_button():
    if data is None:
        messagebox.showwarning("Warning", "Please upload a data file first.")
        return

    x_axis = x_dropdown.get()
    y_axis = y_dropdown.get()
    if not x_axis or not y_axis:
        messagebox.showwarning("Warning", "Please select both X and Y axes.")
        return

    try:
        plot_data(data, x_axis, y_axis)
    except Exception as e:
        messagebox.showerror("Error", f"Error plotting data: {e}")


# Root window setup
root = tk.Tk()
root.title("Data Visual App")
root.geometry("650x550")

data = None
canvas = None

upload_button = tk.Button(root, text="Upload File", command=handle_file_upload)
upload_button.pack(pady=5)

x_label = tk.Label(root, text="Select X-axis:")
x_label.pack(pady=2)
x_dropdown = tk.StringVar(root)
x_menu = tk.OptionMenu(root, x_dropdown, "")
x_menu.pack(pady=2)

y_label = tk.Label(root, text="Select Y-axis:")
y_label.pack(pady=2)
y_dropdown = tk.StringVar(root)
y_menu = tk.OptionMenu(root, y_dropdown, "")
y_menu.pack(pady=2)

plot_button = tk.Button(root, text="Plot Data", command=handle_plot_button)
plot_button.pack(pady=5)

# Load default data.csv if available next to the script
default_csv = os.path.join(os.path.dirname(__file__), "data.csv")
if os.path.exists(default_csv):
    try:
        data = load_file(default_csv)
        update_dropdowns(data.columns)
    except Exception:
        pass

if __name__ == "__main__":
    root.mainloop()