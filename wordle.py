# Project : Wordle
# Author : Tej Pandit

import random
import string

won = False
alphabets = list(string.ascii_lowercase)

ww1 = open("wordle-words.txt", "r")
wordlewords = ww1.read().splitlines()
ww2 = open("valid-wordle-words.txt", "r")
allwords = ww2.read().splitlines()

print("WORDLE GAME: ")
print("_ _ _ _ _ _ _ _")

if won:
    print("WORDLE COMPLETE:")
else:
    print("WORDLE FAILED: Correct Word => " + selectedword)
print("_ _ _ _ _ _ _ _")