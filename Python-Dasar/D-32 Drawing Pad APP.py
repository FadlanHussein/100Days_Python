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

# %% Mouse Drawing on Cancas

root3 = tk.Tk()
root3.title("Mouse Drawing")
root3.geometry("400x400")

canvas3 = tk.Canvas(root3, width=400, height=400, bg="white")
canvas3.pack()

# Draw on Mouse Drag
def draw(event):
    x, y = event.x, event.y
    canvas3.create_oval(x, y, x+2, y+2, fill="black", outline="black")

canvas3.bind("<B1-Motion>", draw)

root3.mainloop()

# %% Clearing and Resetting Canvas

root4 = tk.Tk()
root4.title("Clear Canvas")
root4.geometry("400x450")

canvas4 = tk.Canvas(root4, width=400, height=350, bg="white")
canvas4.pack()

# Drawing Function
def draw(event):
    x, y = event.x, event.y
    canvas4.create_oval(x, y, x+2, y+2, fill="black", outline="black")

# Clear Function
def clear_canvas():
    canvas4.delete("all")

# Bind Drawing
canvas4.bind("<B1-Motion>", draw)

# Clear Button
clear_btn = tk.Button(root4, text="Clear", command=clear_canvas)
clear_btn.pack(side="bottom", pady=10)

root4.mainloop()



# %%
