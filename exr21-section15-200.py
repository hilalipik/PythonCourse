import unittest
import random_game

class TestGame(unittest.TestCase):
    def test_correct(self):
        result = random_game.check_guess(4, 4, 1, 10)
        self.assertTrue(result)

    def test_incorrect(self):
        result = random_game.check_guess(5, 8, 1, 10)
        self.assertFalse(result)

    def test_incorrect_input(self):
        result = random_game.check_guess(20, 8, 1, 10)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()