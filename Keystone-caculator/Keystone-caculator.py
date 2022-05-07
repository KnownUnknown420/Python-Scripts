#This Script takes a number and does one of two things:
#If Even, Divides number by 2 
#If odd, Multiply number by 3 and add 1
#More Info here: https://www.youtube.com/watch?v=094y1Z2wpJg
ActiveNumber = 1
Output = True
def Main():
    global Output
    global ActiveNumber
    MathNumber = ActiveNumber
    KeyStoneCount = 0
    File = open("Keystone-caculator/Keystone History.txt", "a")
    print("Running Process...")
    while True:
        if MathNumber % 2 == 0:
            MathNumber = MathNumber / 2
        else:
            MathNumber = MathNumber * 3 + 1
        if Output:
            print(MathNumber)
        KeyStoneCount = KeyStoneCount + 1
        if MathNumber == 1:
            if Output:
                print("Loop Found!\nRaising ActiveNumber by 1...")
                print(f"Total Steps: {KeyStoneCount}")
                print(f"Active number: {ActiveNumber}")
                print("Restarting loop...\n---")
            ActiveNumber = ActiveNumber + 1
            File.write(f"\n---\nActive Number: {ActiveNumber}\nKeystones: {KeyStoneCount}\n---\n")
            MathNumber = ActiveNumber
            KeyStoneCount = 0
            #TODO: Add a file system that saves total amount of keystones
Main()
        
        
