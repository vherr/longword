import random
import string

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False
        copy_grid = self.grid.copy()
        for letter in word:
            if letter in copy_grid:
                copy_grid.remove(letter)
            else:
                return False
        return True
