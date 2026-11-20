"""Tests for the CodeAlpha Hangman game (no external dependencies)."""

import unittest
from unittest.mock import patch

from main import masked_word, play_game


class HangmanTests(unittest.TestCase):
    def test_masked_word(self):
        self.assertEqual(masked_word("python", {"p", "h"}), "p _ _ h _ _")

    def test_winning_game(self):
        with patch("builtins.input", side_effect=["p", "y", "t", "h", "o", "n"]):
            self.assertTrue(play_game("python"))

    def test_six_incorrect_guesses_ends_game(self):
        with patch("builtins.input", side_effect=["a", "b", "c", "d", "e", "f"]):
            self.assertFalse(play_game("python"))

    def test_invalid_and_repeated_guesses_do_not_count(self):
        # Six different wrong letters end the game; invalid/repeated entries do not.
        with patch("builtins.input", side_effect=["12", "a", "a", "b", "c", "d", "e", "f"]):
            self.assertFalse(play_game("python"))


if __name__ == "__main__":
    unittest.main()
