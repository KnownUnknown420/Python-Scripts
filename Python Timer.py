import time
def Wait(Amount):
    return time.sleep(Amount)
def CountDown(Start):
    i = int(Start)
    while i != 0:
        i -= 1 
        Wait(1)
        print(i)
    else:
        print("Timer Finished!")
        
    
while True:
    UserInput = input("Count down time: ")
    CountDown(UserInput)
    
