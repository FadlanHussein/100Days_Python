import tkinter as tk


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