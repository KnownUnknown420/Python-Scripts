#Imports
import random
TotalAmount = 0
#functions
def main():
    while True:
        option = input("Amount of dice to roll: ")
        print("\n---Dice---")
        wantedOutput = int(option)
        
        try:
           type(wantedOutput) == int
           RollDice(wantedOutput)
        except Exception:
            print("How did we get here...")
            
def RollDice(amount):
    global TotalAmount
    TotalAmount = 0
    for x in range(amount):
        GeneratedNumber = random.randrange(1,6)
        print(GeneratedNumber)
        TotalAmount = TotalAmount + GeneratedNumber
    print("---Total Amount---")
    print(TotalAmount)
    
#Run SCript
main()
