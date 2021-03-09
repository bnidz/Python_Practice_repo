#task11 - Lets check if a given number is a prime
import math
number = int(input("Give a number to check if Prime ;) "))
divisorlist = list()

for x in range(1, int(math.sqrt(number) + 2)):
    if number % x == 0:
        divisorlist.append(x)
        if len(divisorlist) > 1:
            print("number is not a prime!")
            break

if int(len(divisorlist)) == 1 and number != 4:
    print("number is a prime")
