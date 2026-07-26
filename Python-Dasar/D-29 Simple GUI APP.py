# %% Kasus 1 Tkinter (creating a basic tkinter window)

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First GUI App")
root.geometry("300x200")

# Start the GUI event loop
root.mainloop()


# %% Kasus 2: Adding Widgets (Labels, Buttons, Entry Fields)

import tkinter as tk

# Main Window
root - tk.Tk()
root.title("Simple GUI Example")
root.geometry("300x200")

# Add Label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=10)

# Add Entry
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Add Button
def on_click():
    text = entry.get()
    label.config(text=f"Hello, {text}!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=10)

# Run the application
root.mainloop()
# %% Kasus 3 Pratice
import tkinter as tk

root = tk.Tk()
root.title("Event Handling Example")
root.geometry("300x200")

# Add Widgets
label = tk.Label(root, text="Enter Your Name: ")
label.pack()

entry = tk.Entry(root)
entry.pack()

def greet():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

button = tk.Button(root, text="Greet", command=greet)
button.pack()

root.mainloop()
