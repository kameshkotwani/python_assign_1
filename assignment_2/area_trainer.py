'''
Assignment 2: Area Trainer Program::Reboot Academy

This solution is created in python 3.6.4
CAUTION: MAY NOT WORK IN OLDER VERSION

Solved by: Kamesh Kotwani
'''
import math
import random
import string
def circle():
    radius = random.randint(1, 50)
    area = math.pi*(radius**2)
    print("Option 1 : ", area+2)
    print("Option 2 : ", round(area+0.8,4))
    print("Option 3 : ", round(area+1,4))
    print("Option 4 : ", round(area+3,4))
    choice = int(input("Please Enter 1 or 2 or 3 or 4 : "))
    if(choice == 1 or choice == 2 or choice == 3 or choice == 4):
        pass
    elif(choice<0):
        choice = int(input("Please Enter 1 or 2 or 3 or 4 : "))
    else:
        choice = int(input("Please Enter 1 or 2 or 3 or 4 : "))    
    
        
        

def main():
    print("******Hello to Area Trainer******")
    circle()

if(__name__) == "__main__":
    main()