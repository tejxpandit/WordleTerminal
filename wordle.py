# Project : Wordle
# Author : Tej Pandit

import random
import string

won = False
alphabets = list(string.ascii_lowercase)

def checkletters(g, w):
    global won
    letter_flag = 0 #flag: 0=not_in_word, 1=in_word, 2=correct_position
    guess = list(g)
    word = list(w)
    result = ""
    for l in range(len(word)):
        if word[l] == guess[l]:
            letter = guess[l].upper()
            letter_flag = 2
            numbercorrect += 1
        

ww1 = open("wordle-words.txt", "r")
wordlewords = ww1.read().splitlines()
ww2 = open("valid-wordle-words.txt", "r")
allwords = ww2.read().splitlines()

print("WORDLE GAME: ")
print("_ _ _ _ _ _ _ _")

n = len(wordlewords)
w = random.randint(0,n-1)
selectedword = wordlewords[w]

numberofguesses = 0
while numberofguesses < 6:
    guess = input()
    if len(guess) <= 5:
        if guess in allwords:
            print(checkletters(guess, selectedword))
            numberofguesses += 1
        else:
            print("not a word!")
    else:
        print("word too long!")

    if won:
        break

if won:
    print("WORDLE COMPLETE:")
else:
    print("WORDLE FAILED: Correct Word => " + selectedword)
print("_ _ _ _ _ _ _ _")