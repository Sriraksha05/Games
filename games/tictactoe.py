import tkinter as tk
from tkinter import messagebox

# Function to check if a player has won
def check_winner():
    global board

    # Winning combinations: rows, columns, diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]

    for condition in win_conditions:
        if condition[0] == condition[1] == condition[2] and condition[0] != "":
            return True

    return False

# Function to handle a player's move
def player_move(r, c):
    global player_turn, board, buttons, turn_label

    # Check if the cell is already clicked
    if board[r][c] == "":
        # Update the board with current player's symbol
        board[r][c] = player_turn
        buttons[r][c]["text"] = player_turn
        buttons[r][c]["bg"] = "#d1c4e9" if player_turn == "X" else "#ffe0b2"

        # Check if there's a winner
        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {player_turn} wins!")
            reset_board()
            return

        # Check for a tie
        if all(cell != "" for row in board for cell in row):
            messagebox.showinfo("Tic-Tac-Toe", "It's a Tie!")
            reset_board()
            return

        # Switch turns
        player_turn = "O" if player_turn == "X" else "X"
        turn_label.config(text=f"Player {player_turn}'s Turn")

# Function to reset the board
def reset_board():
    global board, buttons, player_turn, turn_label
    board = [["" for _ in range(3)] for _ in range(3)]
    for r in range(3):
        for c in range(3):
            buttons[r][c]["text"] = ""
            buttons[r][c]["bg"] = "#b2dfdb"
    player_turn = "X"
    turn_label.config(text=f"Player {player_turn}'s Turn")

# Function to restart the game
def restart_game():
    reset_board()  # Call reset function to clear the board

# Initialize the window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Beautify the window background
window.configure(bg="#4db6ac")

# Initialize the game variables
player_turn = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Label to show which player's turn it is
turn_label = tk.Label(window, text=f"Player {player_turn}'s Turn", font=('Arial', 18, 'bold'), 
                      bg="#4db6ac", fg="white", pady=10)
turn_label.grid(row=0, column=0, columnspan=3)

# Create the 3x3 grid of buttons with a consistent button style
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(window, text="", width=10, height=3, font=('Arial', 24, 'bold'), 
                                  bg="#b2dfdb", fg="black", activebackground="#80cbc4",
                                  command=lambda r=r, c=c: player_move(r, c))
        buttons[r][c].grid(row=r+1, column=c, padx=5, pady=5)

# Add a Restart button
restart_button = tk.Button(window, text="Restart Game", font=('Arial', 14, 'bold'), bg="#f44336", 
                           fg="white", command=restart_game)
restart_button.grid(row=4, column=0, columnspan=3, pady=10)

# Start the Tkinter main loop
window.mainloop()
