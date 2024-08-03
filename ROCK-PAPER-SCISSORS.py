import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")

        self.choice_label = tk.Label(root, text="Choose your move:")
        self.choice_label.pack()

        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play_game('rock'))
        self.rock_button.pack()

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play_game('paper'))
        self.paper_button.pack()

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play_game('scissors'))
        self.scissors_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def play_game(self, user_choice):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            result = "You win!"
        else:
            result = "You lose!"

        self.result_label.config(text=f"Computer chose: {computer_choice}\nResult: {result}")

# Usage
root = tk.Tk()
app = RockPaperScissorsApp(root)
root.mainloop()
