import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_is_not_empty(self):
        new_game = Game()
        new_game.grid = list("OQUWRBAZE")
        user_input = ""
        self.assertIs(new_game.is_valid(user_input), False)

    def test_is_valid(self):
        new_game = Game()
        new_game.grid = list("OQUWRBAZE")
        user_input = "BAROQUE"
        self.assertIs(new_game.is_valid(user_input), True)
        self.assertEqual(new_game.grid, list("OQUWRBAZE"))

    def test_is_not_valid(self):
        new_game = Game()
        new_game.grid = list("OQUWRBAZE")
        user_input = "BARIQUE"
        self.assertIs(new_game.is_valid(user_input), False)
        self.assertEqual(new_game.grid, list("OQUWRBAZE"))

    def test_unknown_word_is_invalid(self):
      new_game = Game()
      new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
      self.assertIs(new_game.is_valid('FEUN'), False)
