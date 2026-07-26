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
root = tk.Tk()
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

# %% Kasus 4 Project GUI
import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Simple GUI app")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Welcome to my GUI App!!", font=("Arial", 18), bg="#f0f0f0")
title_label.pack(pady=20)

# Name Entry
name_label = tk.Label(root, text="Enter your name:", font=("Arial", 12), bg="#f0f0f0")
name_label.pack()

name_entry = tk.Entry(root, font=("Arial", 12), width=30)
name_entry.pack(pady=10)

# Greeting Label
greeting_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
greeting_label.pack(pady=10)

# Greeting Function
def greet_user():
    name = name_entry.get()
    if name:
        greeting_label.config(text=f"Hello, {name}!", fg="green")
    else:
        greeting_label.config(text="Please enter your name!", fg="red")

# Reset Function
def reset():
    name_entry.delete(0, tk.END)
    greeting_label.config(text="", fg="black")

# Greet Button
greet_button = tk.Button(root, text="Greet", font=("Arial", 12), command=greet_user)
greet_button.pack(pady=10)

# Reset Button
reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=reset)
reset_button.pack(pady=10)

root.mainloop()