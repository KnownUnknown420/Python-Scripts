#Each Function Takes 2 arguments: 1. Number to convert 2.if is passed as a value(False), or a console output(True)
#Second Argument isnt required if you dont want 
def InchToMile(Number,output=False):
    if not output: return Number/63360
    print(Number/63360)
    
def MileToInch(Number,output=False):
    if output != True: return Number*63360
    print(Number*63360)
    
def InchToFoot(Number,output=False):
    if output != True: return Number/12
    print(Number/12)
    
def FootToInch(Number, output=False):
    if output != True: return Number*12
    print(Number*12)


    

