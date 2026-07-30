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



# %% Kasus 5 D-32 Drawing Pad App

from tkinter import colorchooser

# Main Window
root5 = tk.Tk()
root5.title("Drawing Pad App")
root5.geometry("600x600")
root5.configure(bg="#f0f0f0")

# Global Variables
current_color = "black"
current_thickness = 2

# Create Canvas
canvas5 = tk.Canvas(root5, width=500, height=400, bg="white", relief="ridge", bd=2)
canvas5.pack(pady=20)

# Drawing Function
def draw(event):
    x, y = event.x, event.y
    canvas5.create_oval(
        x - current_thickness, y - current_thickness,
        x + current_thickness, y + current_thickness,
        fill=current_color, outline=current_color 
    )

# Clear Canvas
def clear_canvas():
    canvas5.delete("all")

# Change Color
def change_color():
    global current_color
    # Open color chooser and set the selected color as current
    color = colorchooser.askcolor(title="Choose Color")
    # askcolor returns ( (r,g,b), '#rrggbb' ) or (None, None) if cancelled
    if color and color[1]:
        current_color = color[1]
        # If the button exists, update its background to reflect the chosen color
        try:
            color_btn.config(bg=current_color)
        except NameError:
            pass

# Change Thickness
def change_thickness(value):
    global current_thickness
    current_thickness = int(value)

# Bind Drawing
canvas5.bind("<B1-Motion>", draw)

# Control Panel
control_frame = tk.Frame(root5, bg="#f0f0f0")
control_frame.pack(pady=20)

color_btn = tk.Button(control_frame, text="Choose Color", command=change_color, bg="#4CAF50", fg="black", font=("Arial", 10))
color_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(control_frame, text="Clear Canvas", command=clear_canvas, bg="#f44336", fg="black", font=("Arial", 10))
clear_btn.grid(row=0, column=1, padx=10)

thickness_label = tk.Label(control_frame, text="Thickness:", bg="#f0f0f0", font=("Arial", 10))
thickness_label.grid(row=0, column=2, padx=10)

thickness_slider = tk.Scale(control_frame, from_=1, to=10, orient="horizontal", command=change_thickness, bg="#f0f0f0")
thickness_slider.set(2)
thickness_slider.grid(row=0, column=3, padx=10)

# Run Application
root5.mainloop()
