#task16 password generator
import random
import string

print("1 LOW 2 MED 3 HIGH")

security_level = int(input("Give new password security level:\n 1 - 2 - 3: "))
while security_level not in range(1,4):
    security_level = int(input("Give new password security level:\n 1 - 2 - 3: "))

def Generate_Password(security_level):
    password = []
    for x in range(0,security_level*8*security_level):
        if random.randint(1,2) == 1:
            n = random.randint(0,9)
            password.append(n)
        else:
            n = random.choice(string.ascii_letters)
            password.append(n)
    print("your password lenght is: " + str(len(password)))
    psw = ""
    # traverse in the string
    for ele in password:
        psw += str(ele)
    return(psw)

print("New Password: \n" + Generate_Password(security_level))
