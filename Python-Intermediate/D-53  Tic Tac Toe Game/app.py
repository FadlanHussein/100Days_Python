import tkinter as tk
from tkinter import messagebox

# --- Global State ---
current_player = "X"
board = [[" "] * 3 for _ in range(3)]

# --- Window ---
window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

# --- Game Logic ---

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def disable_all():
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(state="disabled")

def on_click(row, col):
    global current_player
    if board[row][col] != " ":
        return
    board[row][col] = current_player
    buttons[row][col].config(text=current_player)

    winner = check_winner(board)
    if winner:
        result_label.config(text=f"Player {winner} Wins! 🎉")
        disable_all()
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        return
    if check_draw(board):
        result_label.config(text="It's a Draw! 🤝")
        messagebox.showinfo("Game Over", "It's a draw!")
        return

    current_player = "O" if current_player == "X" else "X"
    result_label.config(text=f"Player {current_player}'s Turn")

def reset_game():
    global current_player, board
    current_player = "X"
    board = [[" "] * 3 for _ in range(3)]
    result_label.config(text=f"Player {current_player}'s Turn")
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text=" ", state="normal")

# --- UI Layout ---

result_label = tk.Label(window, text="Player X's Turn", font=("Arial", 14))
result_label.grid(row=0, column=0, columnspan=3, pady=10)

buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        btn = tk.Button(
            window, text=" ", font=("Arial", 24), width=5, height=2,
            command=lambda r=i, c=j: on_click(r, c)
        )
        btn.grid(row=i + 1, column=j, padx=5, pady=5)
        row_buttons.append(btn)
    buttons.append(row_buttons)

reset_button = tk.Button(window, text="Reset Game", font=("Arial", 12), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3, pady=10)

window.mainloop()