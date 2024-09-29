import tkinter as tk
from tkinter import messagebox

# Function to check for a win
def check_winner():
    global game_over
    # Define winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]

    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] and board[combination[0]] != "":
            messagebox.showinfo("Game Over", f"Player {turn.get()} wins!")
            game_over = True
            return

    # Check if the board is full (draw)
    if "" not in board:
        messagebox.showinfo("Game Over", "It's a Draw!")
        game_over = True

# Function to handle player moves
def on_click(button, index):
    global current_turn
    if button["text"] == "" and not game_over:
        # Update the board with the current player's symbol
        board[index] = current_turn
        button["text"] = current_turn

        # Check for a winner
        check_winner()

        # Toggle between players
        if not game_over:
            current_turn = "O" if current_turn == "X" else "X"
            turn.set(current_turn)

# Function to reset the game
def reset_game():
    global board, current_turn, game_over
    board = [""] * 9
    current_turn = "X"
    turn.set(current_turn)
    game_over = False

    # Reset all the buttons to be blank
    for button in buttons:
        button.config(text="")

# Initialize the window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Initialize the game variables
board = [""] * 9
current_turn = "X"
turn = tk.StringVar()
turn.set(current_turn)
game_over = False

# Create a label to display which player's turn it is
turn_label = tk.Label(window, text="Player Turn: ", font=('Arial', 14))
turn_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
current_turn_label = tk.Label(window, textvariable=turn, font=('Arial', 14, 'bold'))
current_turn_label.grid(row=0, column=2, padx=10, pady=10)

# Create the buttons for the Tic-Tac-Toe board
buttons = []
for i in range(9):
    button = tk.Button(window, text="", font=('Arial', 20), width=5, height=2,
                       command=lambda i=i: on_click(buttons[i], i))
    button.grid(row=(i//3)+1, column=i%3, padx=5, pady=5)
    buttons.append(button)

# Add a restart button to reset the game
restart_button = tk.Button(window, text="Restart Game", font=('Arial', 14), bg="#d32f2f", fg="white", command=reset_game)
restart_button.grid(row=4, column=0, columnspan=3, pady=10)

# Start the Tkinter main loop
window.mainloop()
