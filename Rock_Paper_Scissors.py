import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    outcomes = {'rock': {'rock': 'tie', 'paper': 'lose', 'scissors': 'win'},
                'paper': {'rock': 'win', 'paper': 'tie', 'scissors': 'lose'},
                'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'tie'}}
    return outcomes[user_choice][computer_choice]

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"Computer's choice: {computer_choice}\n{result}")

def main():
    root = tk.Tk()
    root.title("Rock, Paper, Scissors")

    def on_button_click(user_choice):
        play_game(user_choice)

    rock_button = tk.Button(root, text="Rock", command=lambda: on_button_click('rock'))
    rock_button.pack(pady=5)

    paper_button = tk.Button(root, text="Paper", command=lambda: on_button_click('paper'))
    paper_button.pack(pady=5)

    scissors_button = tk.Button(root, text="Scissors", command=lambda: on_button_click('scissors'))
    scissors_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()