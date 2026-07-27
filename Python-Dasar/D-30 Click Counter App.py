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

# %% Kasus 3: Dynamic Updates
import tkinter as tk

root = tk.Tk()
root.title("Dynamic Center Button")
root.geometry("300x200")

# Counter Variable
counter = 0

def increment_counter():
    global center
    counter += 1
    label.config(text=f"Count: {counter}")

# Label and Button
label = tk.Label(root, text="Count: 0", font=("Arial", 14))
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=increment_counter)
button.pack(pady=10)

root.mainloop()


# %% Kasus 4: Button States

import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Button Events")
root.geometry("300x200")

def toogle_button():
    if button['state'] == 'normal':
        button.config(state='disabled')
        toggle_btn.config(text="Enable Button")
    else:
        button.config(state='normal')
        toggle_btn.config(text="Disable Button")

# Buttons
button = tk.Button(root, text="I am Active")
button.pack(pady=10)

toggle_btn = tk.Button(root, text="Disable Button", command=toggle_button)
toggle_btn.pack(pady=10)

root.mainloop()


