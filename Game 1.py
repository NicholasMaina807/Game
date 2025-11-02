import random


def play_game():
    print("=== Welcome to the Number Guessing Game! ===")
    print("I'm thinking of a number between 1 and 50.")
    print("Can you guess it?\n")

    # Generate random number
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1

        try:
            guess = int(input(f"Attempt {attempts}/{max_attempts} - Enter your guess: "))

            if guess < 1 or guess > 50:
                print("Please enter a number between 1 and 50!")
                attempts -= 1  # Don't count invalid guesses
                continue

            if guess < secret_number:
                print(f"Too low! {remaining - 1} attempts remaining.\n")
            elif guess > secret_number:
                print(f"Too high! {remaining - 1} attempts remaining.\n")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                print(f"The number was {secret_number}!")
                break

        except ValueError:
            print("Invalid input! Please enter a number.")
            attempts -= 1  # Don't count invalid input
            continue
    else:
        print(f"\n😔 Game Over! You've used all {max_attempts} attempts.")
        print(f"The secret number was {secret_number}.")

    # Ask to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again in ['yes', 'y']:
        print("\n" + "=" * 50 + "\n")
        play_game()
    else:
        print("Thanks for playing! Goodbye!")


if __name__ == "__main__":
    play_game()