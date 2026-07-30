import tkinter as tk

# %% Kasus 1 Canvas Widget
root1 = tk.Tk()
canvas1 = tk.Canvas(root1, width=100, height=300, bg="white")
canvas1.pack()

# %% Kasus 2 Drawing shapes and lines
root2 = tk.Tk()
root2.title("Canvas Example")
root2.geometry("400x400")

canvas2 = tk.Canvas(root2, width=400, height=300, bg="white")
canvas2.pack()

# Draw Shape
canvas2.create_line(10, 10, 200, 200, fill="blue", width=3)
canvas2.create_rectangle(50, 50, 150, 150, outline="red", width=2)
canvas2.create_oval(200, 50, 350, 200, outline="green", width=2)

root1.mainloop()
root2.mainloop()

# %%
