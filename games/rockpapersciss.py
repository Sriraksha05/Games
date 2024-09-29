import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Function to decide the winner and update score
def determine_winner():
    global score_player1, score_player2, target_score

    if player1_choice.get() == player2_choice.get():
        result_label.config(text="It's a Tie!")
    elif (player1_choice.get() == "Rock" and player2_choice.get() == "Scissors") or \
         (player1_choice.get() == "Scissors" and player2_choice.get() == "Paper") or \
         (player1_choice.get() == "Paper" and player2_choice.get() == "Rock"):
        score_player1 += 1
        update_score()
        result_label.config(text=f"{player1_name.get()} wins this round!")
    else:
        score_player2 += 1
        update_score()
        result_label.config(text=f"{player2_name.get()} wins this round!")

    # Check if any player has reached the target score
    if score_player1 >= target_score:
        messagebox.showinfo("Game Over", f"{player1_name.get()} wins the game!")
        reset_game()
    elif score_player2 >= target_score:
        messagebox.showinfo("Game Over", f"{player2_name.get()} wins the game!")
        reset_game()

# Function to update the score display
def update_score():
    score_label.config(text=f"{player1_name.get()} Score: {score_player1}  |  {player2_name.get()} Score: {score_player2}")

# Function to start the game by initializing names, resetting scores, and getting target score
def start_game():
    global score_player1, score_player2, target_score
    if player1_name.get() == "" or player2_name.get() == "":
        messagebox.showerror("Input Error", "Please enter both player names.")
        return

    try:
        target_score = int(target_score_entry.get())
        if target_score <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid target score (positive integer).")
        return

    score_player1 = 0
    score_player2 = 0
    update_score()
    result_label.config(text="Let the game begin!")

# Function to automate the choices of both players
def automate_choices():
    options = ["Rock", "Paper", "Scissors"]
    player1_choice.set(random.choice(options))
    player2_choice.set(random.choice(options))

    # Update images based on choices
    player1_image_label.config(image=player1_images[player1_choice.get()])
    player2_image_label.config(image=player2_images[player2_choice.get()])

    determine_winner()

# Function to reset the game
def reset_game():
    global score_player1, score_player2
    score_player1 = 0
    score_player2 = 0
    player1_choice.set("")
    player2_choice.set("")
    update_score()
    result_label.config(text="Game reset! Enter target score and start again.")
    # Reset the images to show empty hands
    player1_image_label.config(image=empty_img)
    player2_image_label.config(image=empty_img)

# Initialize the window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Initialize the game variables
score_player1 = 0
score_player2 = 0
target_score = 5

player1_choice = tk.StringVar()
player2_choice = tk.StringVar()

# Player names
player1_name = tk.StringVar()
player2_name = tk.StringVar()

# Background color
window.configure(bg="#4db6ac")

# Load images for Rock, Paper, and Scissors
# For Player 1 (left hand)
rock_img_player1 = Image.open("left_rock.jpeg").resize((150, 150))
paper_img_player1 = Image.open("left_paper.jpeg").resize((150, 150))
scissors_img_player1 = Image.open("left_scissors.jpeg").resize((150, 150))

# For Player 2 (right hand)
rock_img_player2 = Image.open("right_rock.jpeg").resize((150, 150))
paper_img_player2 = Image.open("right_paper.jpeg").resize((150, 150))
scissors_img_player2 = Image.open("right_scissors.jpeg").resize((150, 150))

# Convert to ImageTk format
rock_img_player1 = ImageTk.PhotoImage(rock_img_player1)
paper_img_player1 = ImageTk.PhotoImage(paper_img_player1)
scissors_img_player1 = ImageTk.PhotoImage(scissors_img_player1)

rock_img_player2 = ImageTk.PhotoImage(rock_img_player2)
paper_img_player2 = ImageTk.PhotoImage(paper_img_player2)
scissors_img_player2 = ImageTk.PhotoImage(scissors_img_player2)

# Empty hand image
empty_img = ImageTk.PhotoImage(Image.new('RGBA', (150, 150), (255, 255, 255, 0)))

# Dictionary to map choices to images
player1_images = {
    "Rock": rock_img_player1,
    "Paper": paper_img_player1,
    "Scissors": scissors_img_player1
}

player2_images = {
    "Rock": rock_img_player2,
    "Paper": paper_img_player2,
    "Scissors": scissors_img_player2
}

# Title label
title_label = tk.Label(window, text="Rock, Paper, Scissors Game", font=('Arial', 24, 'bold'), bg="#4db6ac", fg="white")
title_label.pack(pady=10)

# Player name input
player1_label = tk.Label(window, text="Player 1 Name:", font=('Arial', 14), bg="#4db6ac", fg="white")
player1_label.pack()
player1_entry = tk.Entry(window, textvariable=player1_name, font=('Arial', 14))
player1_entry.pack()

player2_label = tk.Label(window, text="Player 2 Name:", font=('Arial', 14), bg="#4db6ac", fg="white")
player2_label.pack()
player2_entry = tk.Entry(window, textvariable=player2_name, font=('Arial', 14))
player2_entry.pack()

# Target score input
target_score_label = tk.Label(window, text="Target Score to Win:", font=('Arial', 14), bg="#4db6ac", fg="white")
target_score_label.pack()
target_score_entry = tk.Entry(window, font=('Arial', 14))
target_score_entry.pack()

# Start button
start_button = tk.Button(window, text="Start Game", font=('Arial', 14, 'bold'), bg="#8bc34a", fg="white", command=start_game)
start_button.pack(pady=10)

# Player 1 and Player 2 images for hands (show gesture)
player1_image_label = tk.Label(window, bg="#4db6ac", image=empty_img)
player1_image_label.pack(side=tk.LEFT, padx=50)

player2_image_label = tk.Label(window, bg="#4db6ac", image=empty_img)
player2_image_label.pack(side=tk.RIGHT, padx=50)

# Automate button for making random choices
automate_button = tk.Button(window, text="Play", font=('Arial', 14, 'bold'), bg="#f57f17", fg="white", command=automate_choices)
automate_button.pack(pady=20)

# Score label
score_label = tk.Label(window, text="Score", font=('Arial', 16), bg="#4db6ac", fg="white")
score_label.pack(pady=10)

# Result label
result_label = tk.Label(window, text="", font=('Arial', 14), bg="#4db6ac", fg="white")
result_label.pack(pady=10)

# Restart button to reset the game
restart_button = tk.Button(window, text="Restart Game", font=('Arial', 14, 'bold'), bg="#d32f2f", fg="white", command=reset_game)
restart_button.pack(pady=10)

# Start the Tkinter main loop
window.mainloop()
