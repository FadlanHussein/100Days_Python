from tkinter import messagebox
# %% Kasus 1 Message Box
messagebox.showinfo("Title","This is an information message")

# %% Kasus 2 Types Of Message Boxes
import tkinter as tk

root = tk.Tk()
root.withdraw() # Hides the main window

# Show different message boxes
messagebox.showinfo("Info", "This is an information")
messagebox.showwarning("Warning", "This is a warning meessage")
messagebox.showerror("Error", "This is an error message")

response = messagebox.askyesno("Question", "Do you want to continue")
print("Response:", response)
