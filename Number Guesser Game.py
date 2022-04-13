#import
import random
import time

#Veriables
SmallNumber = 1
BigNumber = 5
Hints = True

#Functions
def GameLoop():
    global BigNumber
    global SmallNumber
    global Hints
    KeyStones = 0
    SelectedNumber = random.randrange(SmallNumber,BigNumber)
    while True: 
        UserInput = input("Guess: ")
        KeyStones = KeyStones + 1
        if str(UserInput) == str(SelectedNumber):
            print("Correct! You Guessed in " +str(KeyStones) +" trys.\n\n\n")
            time.sleep(3)
            MainMenu()
            break
        else:
            print("Incorrect!")
            if Hints == True:
                Amountaway = int(SelectedNumber) - int(UserInput)
                print("Your Guess was " +str(Amountaway) +" away from the number. ")
            
def SettingsMenu():
    global SmallNumber
    global BigNumber
    global Hints
    while True:
        print("---Settings---")
        print("1: Range of numbers (" +str(SmallNumber) +"," +str(BigNumber) +")")
        print("2: Hints: " +str(Hints))
        print("3: Back to menu")
        UserInput = input("")
        if UserInput == str("1"): 
            UserInput = input("Pick smallest Possible number: ")
            SmallNumber = int(UserInput)
            UserInput2 = input("Pick largest Possible number: ")
            BigNumber = int(UserInput2)
        elif UserInput == str("2"):
            Hints = not Hints
        elif UserInput == str("3"):
            MainMenu()
            break
        else:
            print("---Error: Not an option---\n\n\n")
def MainMenu():
    while True:
        print("--Number guesser!--\n1. Play Game\n2. Settings")
        UserInput = input("")
        if UserInput == str("1"):
            GameLoop()
            break
        elif UserInput == str("2"):
            SettingsMenu()
            break
        else:
            print("---Error: Not an option---\n\n\n")
#Main Loop
MainMenu()
