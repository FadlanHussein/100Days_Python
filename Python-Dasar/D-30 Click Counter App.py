# %% Kasus 1: How Buttons Work

import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Basic Button Example")
root.geometry("300x200")

# Button Click Handler
def on_click():
    print("Button clicked")

# Create Button
button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=20)

# Run the application
root.mainloop()

# %% Kasus 2: Binding Events

import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Button Events")
root.geometry("300x200")

# Event Handlers
def on_enter(event):
    button.config(text="Mouse Over")

def on_leave(event):
    button.config(text="Mouse Out")

# Create Button
button = tk.Button(root, text="Hover Me")
button.pack(pady=20)

# Bind Events
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()

# %%
