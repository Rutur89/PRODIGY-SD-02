import tkinter as tk
from tkinter import messagebox
import random

class GuessingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")

        self.difficulty_label = tk.Label(root, text="Select Difficulty:", font=("Helvetica", 12))
        self.difficulty_label.pack()

        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("Easy")

        self.difficulty_options = ["Easy", "Medium", "Hard"]
        self.difficulty_menu = tk.OptionMenu(root, self.difficulty_var, *self.difficulty_options)
        self.difficulty_menu.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game, font=("Helvetica", 12))
        self.start_button.pack()

        self.number_to_guess = 0
        self.attempts = 0

    def start_game(self):
        difficulty = self.difficulty_var.get()
        if difficulty == "Easy":
            self.number_to_guess = random.randint(1, 10)
        elif difficulty == "Medium":
            self.number_to_guess = random.randint(1, 50)
        elif difficulty == "Hard":
            self.number_to_guess = random.randint(1, 100)

        self.attempts = 0

        game_window = tk.Toplevel(self.root)
        game_window.title("Guessing Game - Good Luck!")

        self.guess_label = tk.Label(game_window, text="Enter your guess:", font=("Helvetica", 12))
        self.guess_label.pack()

        self.guess_entry = tk.Entry(game_window, font=("Helvetica", 12))
        self.guess_entry.pack(pady=10)

        self.submit_button = tk.Button(game_window, text="Submit Guess", command=self.check_guess, font=("Helvetica", 12))
        self.submit_button.pack()

        self.result_label = tk.Label(game_window, text="", font=("Helvetica", 12))
        self.result_label.pack()

    def check_guess(self):
        try:
            user_guess = int(self.guess_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a numerical value.")
            return

        self.attempts += 1

        if user_guess == self.number_to_guess:
            result_message = f"Congratulations! You guessed the number in {self.attempts} attempts."
            self.result_label.config(text=result_message)
            self.root.destroy()  # Close the main window when the game is over
        else:
            result_message = "Incorrect! Try again."
            self.result_label.config(text=result_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameApp(root)
    root.mainloop()
