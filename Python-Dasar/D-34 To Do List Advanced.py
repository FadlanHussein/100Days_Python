import tkinter as tk

# %% Kasus 1: Using Listbox for Dynamic Lists
root = tk.Tk()
root.title("Lisbox Example")
root.geometry("300x300")

# Listbox Widget
listbox = tk.Listbox(root)
listbox.pack(pady=10)

# Add Items to Listbox
listbox.insert(tk.END, "Task 1")
listbox.insert(tk.END, "Task 2")

# Get Selected Item
def get_selected():
    selected = listbox.get(tk.ACTIVE)
    print("Selected:", selected)

button = tk.Button(root, text="Get Selected", command=get_selected)
button.pack(pady=10)

root.mainloop()

# %% Kasus 2: Scrollbal Integration

root2 = tk.Tk()
root2.title("Listbox with Scrollbar")
root2.geometry("300x300")

# Frame for Listbox and Scrollbar
frame = tk.Frame(root2)
frame.pack(pady=10)

# Scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(slide=tk.RIGHT, fill=tk.Y)

# Listbox
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, height=10)
listbox.pack()

# Configure Scrollbar
scrollbar.config(command=listbox.yview)

# Add Items
for i in range(1, 21):
    listbox.insert(tk.END, f"Item {i}")

root.mainloop()

# %% Kasus 3: Handling User Actions (Add, Delete, Clear)

root3 = tk.Tk()
root3.title("Listbox Management")
root.geometry("300x300")

# Listbox
listbox = tk.Listbox(root3)
listbox.pack(pady=10)

# Add Items
def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

# Delete Item
def delete_item():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

# Entry Field
entry = tk.Entry(root3)
entry.pack(pady=5)

# Buttons
add_button = tk.Button(root4, text="Add Item", command=add_item)
add_button.pack(pady=5)

delete_button = tk.Button(root3, text="Delete Item", command=delete_item)
delete_button.pack(pady=5)

root.mainloop()




