#task8 Guess number 1-9 game
#%%
import random

guessnumber = int(0)
computerPick = random.randrange(10)

yourGuess = input("Guess which number I have in mind ;) ")
yourGuess = int(yourGuess)
guessnumber += 1

while computerPick != yourGuess:
    while computerPick < yourGuess:
        print("Little bit lower ;)")
        yourGuess = input("Guess which number I have in mind ;) ")
        yourGuess = int(yourGuess)
        guessnumber += 1

    while computerPick > yourGuess:
        print("Little bit higher ;)")
        yourGuess = input("Guess which number I have in mind ;) ")
        yourGuess = int(yourGuess)
        guessnumber += 1

if yourGuess == computerPick:
    print('Whoah! You Guessed it! it was your:', int(guessnumber), 'guess!')
    exit = input("type exit to quit: ")
    while exit != "exit":
        exit = input("type exit to quit: ")
        break
