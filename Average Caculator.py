def Main():
    while True:
        UserInput = input("Input Numbers seperated with a space: ")
        List_Index = UserInput.split()
        for Num in range(len(List_Index)):
            List_Index[Num] = int(List_Index[Num])
        AverageAmount = sum(List_Index) / len(List_Index)
        print(f"---\nNumbers Used {List_Index}\nAverage: {AverageAmount}\n---")
Main()