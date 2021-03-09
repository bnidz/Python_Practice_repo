#task8 Guess number 1-9 game

import random

computerPick = random.range(10)

yourGuess = input("Guess which number I have in mind ;) ")
yourGuess = int(yourGuess)

if yourGuess == computerPick:
    print("Whoah! You Guessed it!")
    break

while computerPick < yourGuess:
    print("Little bit lower ;)")
    yourGuess = input("Guess which number I have in mind ;) ")
    yourGuess = int(yourGuess)
while computerPick > yourGuess:
    print("Little bit higher ;)")
    yourGuess = input("Guess which number I have in mind ;) ")
    yourGuess = int(yourGuess)
