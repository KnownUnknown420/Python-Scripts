#python password generator
from ast import Pass
import random
import time

PasswordAdd = 1
PasswordLength = 5
AllowedSymbols = (1,2,3,4,5,6,7,8,9,10,"q","w","e","r","t","y","u","i","o",
"p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","!","@",
"#","$","%","^","&","*","(",")")

#funtions
def UpperCase(letter):
    global PasswordAdd
    Value = random.randint(0,1)
    if Value == 0:
        PasswordAdd = letter.upper()

def intPassword():
    global AllowedSymbols
    global PasswordLength
    global PasswordAdd
    PasswordFinal = ""
    print("Generating Password...:")
    for _ in range(PasswordLength):
        NumberIndex = random.randint(0,len(AllowedSymbols)-1)
        PasswordAdd = AllowedSymbols[NumberIndex]
        if type(PasswordAdd) == str:
            UpperCase(PasswordAdd)
        PasswordFinal = PasswordFinal + str(PasswordAdd)
    print("Password Generated!")
    print(PasswordFinal)
    time.sleep(3)
    
def intSettings():
    global PasswordLength
    while True:
        UserInput = input("---Settings---\n1: Password Length (" +str(PasswordLength) +")\n2: Back to menu\n")
        if UserInput == str(1):
            UserInput2 = input("Length of password:\n")
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
