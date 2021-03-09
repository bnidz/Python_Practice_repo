#task18 bull game ;)
import random

def Guess():
    guess = int(input("Give a 4 digit number to guess the cows \n"))
    while guess not in range(10000):
        print("WARNING ;) guess not in range!")
        guess = int(input("Give a 4 digit number to guess the cows \n"))
    return(str(guess))
print(Guess())

def Answer_Gen():
    answer = []
    for x in range(4):
        n = random.randint(0,9)
        answer.append(n)
    ans = ""
    for ele in answer:
        ans +=str(ele)
    return(ans)
print(Answer_Gen())
cows = int()
bulls = int()
def Compare_Results():
    for ele in Guess() and ele in Answer_Gen():
        cows+=1
    print(cows)