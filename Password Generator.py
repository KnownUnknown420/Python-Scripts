#python password generator
import random
import time

PasswordLength = 5
AllowedSymbols = (1,2,3,4,5,6,7,8,9,10,"q","w","e","r","t","y","u","i","o",
"p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","!","@",
"#","$","%","^","&","*","(",")")

#funtions


def intPassword():
    global AllowedSymbols
    global PasswordLength
    PasswordFinal = ""
    print("Generating Password...:")
    for _ in range(PasswordLength):
        NumberIndex = random.randint(0,len(AllowedSymbols)-1)
        PasswordFinal = PasswordFinal + str(AllowedSymbols[NumberIndex])
    print("Password Generated!")
    print(PasswordFinal)
    time.sleep(3)
    
def intSettings():
    global PasswordLength
    while True:
        UserInput = input("---Settings---\n1: Password Length (" +str(PasswordLength) +")\n2: Back to menu")
        if UserInput == str(1):
            UserInput2 = input("Length of password: ")
            PasswordLength = int(UserInput2)
        elif UserInput == str(2):
            intMain()
        else:
            print("Error: Sorry thats not an option")
            time.sleep(1)

def intMain():
    while True:
        UserInput = input("---Password generator---\n1: Generate Password\n2: Settings\n")
        if UserInput == str(1):
           intPassword()
        elif UserInput == str(2):
           intSettings()
        else:
            print("Sorry, THats not an option.\n\n\n")
            time.sleep(1)
    
    
#intMain
intMain()
