"""CodeAlpha Python Internship - Task 1: Text-based Hangman Game."""

import random

WORDS = ["python", "computer", "program", "science", "internet"]
MAX_WRONG_GUESSES = 6


def masked_word(secret_word: str, guessed_letters: set[str]) -> str:
    """Show correctly guessed letters and hide the others with underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)


def play_game(secret_word: str | None = None) -> bool:
    """Play a single round; return True on a win and False on a loss."""
    if secret_word is None:
        secret_word = random.choice(WORDS)

    guessed_letters: set[str] = set()
    wrong_guesses = 0

    print("\n=== CodeAlpha Hangman Game ===")
    print("Guess the hidden word, one letter at a time.")
    print(f"You can make {MAX_WRONG_GUESSES} incorrect guesses.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(f"Word: {masked_word(secret_word, guessed_letters)}")
        print(f"Incorrect guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "None")

        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isascii() or not guess.isalpha():
            print("Please enter exactly one English letter (a-z).\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct!\n")
            if all(letter in guessed_letters for letter in secret_word):
                print(f"You win! The word was '{secret_word}'.")
                return True
        else:
            wrong_guesses += 1
            print("Incorrect guess.\n")

    print(f"Game over! The word was '{secret_word}'.")
    return False


def main() -> None:
    try:
        while True:
            play_game()
            again = input("\nPlay again? (y/n): ").strip().lower()
            if again not in ("y", "yes"):
                print("Thanks for playing!")
                break
    except (EOFError, KeyboardInterrupt):
        print("\nGame ended. Goodbye!")


if __name__ == "__main__":
    main()
