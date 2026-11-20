# Hangman Game — CodeAlpha Python Internship (Task 1)

A beginner-friendly **text-based Hangman game** written in Python. The player guesses a hidden word one letter at a time, with a maximum of **6 incorrect guesses**.

## Requirements
- Python 3.10 or newer
- No external libraries or API keys are required.

## Features
- Exactly five predefined words: `python`, `computer`, `program`, `science`, `internet`
- Randomly picks one word each round
- Six incorrect guesses allowed
- Displays correctly guessed letters and remaining attempts
- Rejects invalid, repeated, and multi-letter guesses without using an attempt
- Allows the player to replay
- Runs entirely in the console (no graphics or audio)

## Run on macOS / Linux

```bash
cd CodeAlpha_HangmanGame
python3 main.py
```

On Windows, use `python main.py` instead if needed.

## Run tests

From the project folder:

```bash
python3 -m unittest discover -s tests -v
```

## Project structure

```text
CodeAlpha_HangmanGame/
├── main.py
├── README.md
└── tests/
    └── test_game.py
```

## Sample interaction

```text
=== CodeAlpha Hangman Game ===
Guess the hidden word, one letter at a time.
You can make 6 incorrect guesses.

Word: _ _ _ _ _ _
Incorrect guesses: 0/6
Guessed letters: None
Enter one letter: p
Correct!
```

## Concepts demonstrated
Python lists, strings, `random`, `while` loops, `if` / `else` logic, functions, sets, and console input/output.

## Internship submission
This project implements CodeAlpha's **Python Programming Task 1: Hangman Game**. Add the repository link to the official submission form and follow the current internship instructions for LinkedIn/video requirements.
