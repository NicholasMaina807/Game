import tkinter as tk
from tkinter import messagebox
import random


class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        # Game variables
        self.secret_number = 0
        self.attempts = 0
        self.max_attempts = 5

        # Create UI
        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="Number Guessing Game",
            font=("Arial", 20, "bold"),
            pady=20
        )
        title_label.pack()

        # Instructions
        self.instruction_label = tk.Label(
            self.root,
            text="I'm thinking of a number between 1 and 50.\nCan you guess it?",
            font=("Arial", 12),
            pady=10
        )
        self.instruction_label.pack()

        # Attempts counter
        self.attempts_label = tk.Label(
            self.root,
            text=f"Attempts: 0/{self.max_attempts}",
            font=("Arial", 11),
            pady=10
        )
        self.attempts_label.pack()

        # Input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Your guess:", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)

        self.guess_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
        self.guess_entry.pack(side=tk.LEFT, padx=5)
        self.guess_entry.bind('<Return>', lambda e: self.check_guess())

        # Guess button
        self.guess_button = tk.Button(
            self.root,
            text="Guess!",
            font=("Arial", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            width=15,
            height=2,
            command=self.check_guess,
            cursor="hand2"
        )
        self.guess_button.pack(pady=10)

        # Feedback label
        self.feedback_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 13, "bold"),
            pady=20,
            height=3
        )
        self.feedback_label.pack()

        # New game button
        self.new_game_button = tk.Button(
            self.root,
            text="New Game",
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            width=15,
            height=2,
            command=self.new_game,
            cursor="hand2"
        )
        self.new_game_button.pack(pady=10)

    def new_game(self):
        self.secret_number = random.randint(1, 50)
        self.attempts = 0
        self.attempts_label.config(text=f"Attempts: 0/{self.max_attempts}")
        self.feedback_label.config(text="", fg="black")
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()
        self.guess_button.config(state=tk.NORMAL)

    def check_guess(self):
        if self.attempts >= self.max_attempts:
            return

        try:
            guess = int(self.guess_entry.get())

            if guess < 1 or guess > 50:
                self.feedback_label.config(
                    text="Please enter a number\nbetween 1 and 50!",
                    fg="red"
                )
                return

            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")

            if guess < self.secret_number:
                self.feedback_label.config(text="Too low! Try again.", fg="blue")
            elif guess > self.secret_number:
                self.feedback_label.config(text="Too high! Try again.", fg="orange")
            else:
                self.root.config(bg="#FFD700")
                self.feedback_label.config(
                    text=f"🎉🎊 WINNER! 🎊🎉\nYou guessed it in {self.attempts} attempts!\n⭐ AMAZING! ⭐",
                    fg="#FF1493",
                    font=("Arial", 14, "bold")
                )
                self.guess_button.config(state=tk.DISABLED)
                messagebox.showinfo("🎉 WINNER! 🎉",
                                    f"🎊 CONGRATULATIONS! 🎊\n\nYou guessed the number {self.secret_number}\nin only {self.attempts} attempts!\n\nYou're a guessing champion! 🏆")
                self.root.after(3000, lambda: self.root.config(bg="SystemButtonFace"))
                return

            if self.attempts >= self.max_attempts:
                self.feedback_label.config(
                    text=f"Game Over!\nThe number was {self.secret_number}",
                    fg="red"
                )
                self.guess_button.config(state=tk.DISABLED)
                messagebox.showinfo("Game Over", f"You've used all attempts. The number was {self.secret_number}.")

            self.guess_entry.delete(0, tk.END)
            self.guess_entry.focus()

        except ValueError:
            self.feedback_label.config(text="Please enter a valid number!", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()