def get_number():
    while True:
        num=input("enter your number")
        if num.replace(".","",1).isdigit():
            return float(num)
        else:
            print("please enter a number")

def inches_to_centimeters(value):
    return value * 2.54
def centimeters_to_inches(value):
    return value * 0.3937
def miles_to_kilometers(value):
    return value * 1.61
def kilometers_to_miles(value):
    return value * 0.62
def ounces_to_grams(value):
    return value * 28.35
def grams_to_ounces(value):
    return value * 0.035

def convert_to_centi(value):
    return value * 10**2
def convert_to_mili(value):
    return value * 10**3
def convert_to_kilo(value):
    return value * 10**-3

def main_menu():
    while True:
        print("-------- MAIN MENU --------")
        print("1 = METRIC CONVERSION ")
        print("2 = UNIT PREFIX CONVERSION ")
        print("3 = EXIT ")
        choose=input("choose your menu number please ")
        if choose.isdigit():
            choose=int(choose)
            if choose in (1,2,3):
                return choose
            else:
                print("wrong choose try again please ")
        else:
            print("please enter a number ")

def metric_menu():
    while True:
        print("-------- METRIC CONVERSION --------")
        print("1 = INCHES TO CENTIMETERS ")
        print("2 = CENTIMETERS TO INCHES ")
        print("3 = MILES TO KILOMETERS ")
        print("4 = KILOMETERS TO MILES ")
        print("5 = OUNCES TO GRAMS ")
        print("6 = GRAMS TO OUNCES")
        print("7 = BACK TO MAIN MENU ")
        print("SELECT CONVERSION (1-7) ")
        choose=input("choose your number ")
        if choose.isdigit():
            choose=int(choose)
            if choose in (1,2,3,4,5,6,7):
                return choose
            else:
                print("wrong choose try again please ")
        else:
            print("please enter a number")

def unit_menu():
    while True:
        print("-------- UNIT PREFIX CONVERSION --------")
        print("1 = CONVERT TO CENTI ")
        print("2 = CONVERT TO MILI")
        print("3 = CONVERT TO KILO")
        print("4 = BACK TO MAIN MENU")
        print("SELECT CONVERSION (1-4) ")
        choose=input("choose your number ")
        if choose.isdigit():
            choose=int(choose)
            if choose in (1,2,3,4):
                return choose
            else:
                print("wrong choose try again please ")
        else:
            print("please enter a number")

def metric_operations():  
    while True:
            choose=metric_menu()
            if choose==1:
                number=get_number()
                print(inches_to_centimeters(number))
            elif choose==2:
                number=get_number()
                print(centimeters_to_inches(number))
            elif choose==3:
                number=get_number()
                print(miles_to_kilometers(number))
            elif choose==4:
                number=get_number()
                print(kilometers_to_miles(number))
            elif choose==5:
                number=get_number()
                print(ounces_to_grams(number))
            elif choose==6:
                number=get_number()
                print(grams_to_ounces(number))
            elif choose==7:
                 print("returning to main menu")
                 break
            else:
                print("wrong choose try again")
                
def unit_operations():   
    while True:
         choose=unit_menu()
         if choose==1:
              number=get_number()
              print(convert_to_centi(number))
         elif choose==2:
              number=get_number()
              print(convert_to_mili(number))
         elif choose==3:
              number=get_number()
              print(convert_to_kilo(number))
         elif choose==4:
              print("returning to main menu")
              break
         else:
              print("wrong choose try again please ")


while True:
    choose=main_menu()
    if choose==1:
        metric_operations()
    elif choose==2:
        unit_operations()
    elif choose==3:
        print(" GOODBYE :) ")
        break
    else:
        print("wrong choose try again please ")