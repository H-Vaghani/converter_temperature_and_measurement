def vaild(text,amount):
    while True:
        x = input(text)
        length = len(x)
        try:
            nums = int(x)
            if length != 1  : # check the the length of input 1
                print("Choose only one digit") 
                x
            elif nums < 1 or nums > amount:
                print("Choose 1 or " , amount)
                x
            else:
               break        
        except ValueError: # check for other input like string symbol
            print("Input Invalid")
    return nums

def onlyfloat(text):
    while True:
        x = input(text)
        try:
            nums = float(x)   
            if nums == str:
                print("Only Integer")
            else:
                break
        except ValueError: # check for other input like string and symbol
            print("Input Invalid")
    return nums
    
