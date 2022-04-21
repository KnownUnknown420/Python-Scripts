#This Script takes a number and does one of two things:
#If Even, Divides number by 2 
#If odd, Multiply number by 3 and add 1
#More Info here: https://www.youtube.com/watch?v=094y1Z2wpJg
ActiveNumber = 1
def Main():
    global ActiveNumber
    MathNumber = ActiveNumber
    KeyStoneCount = 0
    while True:
        if MathNumber % 2 == 0:
            MathNumber = MathNumber / 2
        else:
            MathNumber = MathNumber * 3 + 1
        print(MathNumber)
        KeyStoneCount = KeyStoneCount + 1
        if MathNumber == 1:
            print("Loop Found!\nRaising ActiveNumber by 1...")
            print(f"Total Steps: {KeyStoneCount}")
            ActiveNumber = ActiveNumber + 1
            print(f"Active number: {ActiveNumber}")
            print("Restarting loop...\n---")
            MathNumber = ActiveNumber
            KeyStoneCount = 0
            #TODO: Add a file system that saves total amount of keystones
            
Main()
        
        
