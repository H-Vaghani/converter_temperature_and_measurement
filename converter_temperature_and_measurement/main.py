import Input
def selection():
    choose = Input.vaild("Press 1: For Temperature: \npress 2: For Measurement: ",2)
    if choose == 1:
        temp()
    elif choose == 2:
        Measurement()

def temp():
    temp = Input.vaild("Press 1:convert Fahrenheit to Celcius : \npress 2: convert Celcius to Fahrenheit  ",2)
    x = Input.onlyfloat("Enter the Temperature: ")
    if temp == 1:
        celcius = (x -32) / 1.8
        print("In Celcius: ", celcius)
    else:
        fahrenheit = (x *1.8) + 32
        print("In Fahrenheit: " , fahrenheit)
    re()

def Measurement():
    convert= {
        1:"Meter", 2:"Kilometer", 3:"Centimeter", 
        4:"Millimeter", 5:"Micrometer", 6:"Nanometre", 
        7:"Mile", 8:"Yard", 9:"Feet", 10:"Inch", 
    }
    print (convert)
    fromm = Input.vaild("From: ",10)
    to = Input.vaild("TO: ",10)
    y = Input.onlyfloat("Enter the number: ")

    if fromm == 1:
        meter = y
    elif fromm == 2:
        meter = y * 1000
    elif fromm == 3:
        meter = y / 100
    elif fromm == 4:
        meter= y / 1000
    elif fromm == 5:
        meter= y / 1000000
    elif fromm == 6:
        meter = y / 1000000000
    elif fromm == 7:
        meter = y * 1069.344
    elif fromm == 8:
        meter = y / 1.0936
    elif fromm == 9:
        meter = y / 3.28084
    elif fromm == 10:
        meter = y / 39.370079

    print("convert from ", convert[fromm], " to", convert[to])
    print(measurments(meter,to) , convert[to])
    re()


def measurments(meter, too):
    if too == 1:
        return meter
    elif too == 2:
        return meter / 1000
    elif too ==  3:
        return meter * 100
    elif too == 4:
        return meter * 1000
    elif too == 5:
        return meter * 1000000
    elif too == 6:
        return meter * 1000000000
    elif too == 7:
        return meter / 1069.344
    elif too == 8:
        return meter * 1.0936
    elif too == 9:
        return meter * 3.28084
    elif too == 10:
        return meter * 39.370079

def re():
    while True:
        re: str = str(input("To Run Calculator (y/n): "))
        if len(re) <= 0 or len(re) > 1:
            print("only (y/n)")
        elif re == "y":
            selection()
        elif re == "n":
            exit()
selection()



