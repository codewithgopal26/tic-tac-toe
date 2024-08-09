import tkinter as tk
from tkinter import messagebox
import random

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def get_available_moves(board):
    moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return moves

def ai_move(board):
    available_moves = get_available_moves(board)
    return random.choice(available_moves)

def click(row, col):
    global game_over
    if board[row][col] == " " and not game_over:
        board[row][col] = "X"
        buttons[row][col].config(text="X", state=tk.DISABLED)
        if check_win(board, "X"):
            game_over = True
            show_message("Congratulations! You win!")
            reset_game()
        elif len(get_available_moves(board)) == 0:
            game_over = True
            show_message("It's a draw!")
            reset_game()
        else:
            ai_row, ai_col = ai_move(board)
            board[ai_row][ai_col] = "O"
            buttons[ai_row][ai_col].config(text="O", state=tk.DISABLED)
            if check_win(board, "O"):
                game_over = True
                show_message("AI wins! Better luck next time.")
                reset_game()

def show_message(message):
    messagebox.showinfo("Tic Tac Toe", f"\n\n{message}\n\n", icon='info')

def reset_game():
    global board, buttons, game_over
    board = [[" " for _ in range(3)] for _ in range(3)]
    game_over = False
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tk.NORMAL)

app = tk.Tk()
app.title("Tic Tac Toe")

buttons = [[None for _ in range(3)] for _ in range(3)]
board = [[" " for _ in range(3)] for _ in range(3)]
game_over = False

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(app, text="", width=10, height=3, font=('Helvetica', 20), command=lambda row=i, col=j: click(row, col))
        buttons[i][j].grid(row=i, column=j)

reset_button = tk.Button(app, text="Reset", font=('Helvetica', 15), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

app.mainloop()
