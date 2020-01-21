import random
import string
import requests


class Game:

    DICO_URL = 'https://wagon-dictionary.herokuapp.com/'

    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False
        copy_grid = self.grid.copy()
        tmp_finalword = []
        for letter in word:
            if letter in copy_grid:
                copy_grid.remove(letter)
                tmp_finalword.append(letter)
            else:
                return False

        if not self._is_real_word(word):
            return False

        return True

    def _is_real_word(self, word):
        #url = 'https://wagon-dictionary.herokuapp.com/CAR'
        url = self.DICO_URL+''.join(word)
        res = requests.get(self.DICO_URL+''.join(word))
        #res = requests.get(url)

        dico_res = res.json()
        if res.status_code != 200:
            return False

        return dico_res['found']
