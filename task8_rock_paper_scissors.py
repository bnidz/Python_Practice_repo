#task 8 rock papaer scissors
import random
import sys
#LIST FOR CHOICES
choises = ['Q', 'Rock', 'Paper', 'Scissors']
cWins = int(0)
pWins = int(0)

def PlayGame():
    global cWins, pWins
    #CHECK FOR INPUT
    pick = input("Pick 1. Rock 2. Paper 3. Scissors \nPress Q to Quit\n")
    pick = str(pick)
    while pick not in ("1","2","3","Q"):
        print("No!")
        pick = input("Pick 1. Rock 2. Paper 3. Scissors \nPress Q to Quit\n")
    #IF USER WANTS TO QUIT
    if str(pick) == "Q":
        sys.exit(0)
    #PICK FOR COMPUTER
    computerPick = random.randrange(1,4)
    #LOSE SCENARIOS
    while int(pick) == 1 and computerPick == 2:
        cWins+=1
        print("YOU LOST! \nScore: " + str(pWins) + " Player vs " + str(cWins) + " Computer \nRock vs. Paper! - Computer Wins ;)")
        PlayGame()
        break
    while int(pick) == 2 and computerPick == 3:
        cWins+=1
        print("YOU LOST! \nScore: " + str(pWins) + " Player vs " + str(cWins) + " Computer \nPaper vs. Scissors! - Computer Wins ;)")
        PlayGame()
        break
    while int(pick) == 3 and computerPick == 1:
        cWins+=1
        print("YOU LOST! \nScore: " + str(pWins) + " Player vs " + str(cWins) + " Computer \nScissors vs. Rock! Computer Wins ;)")
        PlayGame()
        break
    #TIE SCENARIO
    while int(pick) == computerPick:
        print("ITS A TIE!!\nScore: " + str(pWins) + " Player vs " + str(cWins) + " Computer \n" + choises[int(pick)] + " vs. " + choises[computerPick])
        PlayGame()
        break
    #WIN SCENARIOS
    while int(pick) == 1 and computerPick == 3:
        pWins+=1
        print ("YOU WIN!!!\nScore: " + str(pWins) + " Player vs " + str(cWins) + " Computer \nRock vs. " + str("Scissors"))
        PlayGame()
        break
    while int(pick) == 2 and computerPick == 1:
        pWins+=1
        print ("YOU WIN!!!\nScore: " + str(pWins) + " Player vs " + str(cWins) + " Computer \nPaper vs. " +  str("Rock"))
        PlayGame()
        break
    while int(pick) == 3 and computerPick == 2:
        pWins+=1
        print ("YOU WIN!!!\nScore: " + str(pWins) + " Player vs " + str(cWins) + " Computer \nScissors vs. " +  str("Paper"))
        PlayGame()
        break

PlayGame()
