#functions
def Add(x,y):
    return x + y

def Subtract(x,y):
    return x - y

def Multiply(x,y):
    return x * y

def Divide(x,y):
    return x / y

def Main():
    while True:
        EquationType = input("Select Math process\n1: Add\n2: Subtract\n3: Multiply\n4: Divide\n")
        UserNumber1 = int(input("Select First Number\n"))
        UserNumber2 = int(input("Select Second Number\n"))
        print("---")
        if EquationType == str(1):
            print(Add(UserNumber1,UserNumber2))
        elif EquationType == str(2):
            print(Subtract(UserNumber1,UserNumber2))
        elif EquationType == str(3):
            print(Multiply(UserNumber1,UserNumber2))
        elif EquationType == str(4):
            print(Divide(UserNumber1,UserNumber2))
        else:
            print(f"Error: '{EquationType}' is not an option.")
        print("---\n")

#main
Main()


