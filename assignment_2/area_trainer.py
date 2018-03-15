'''
Assignment 2: 
Area Trainer Program:
Reboot Academy

This solution is created in python 3.6.4
CAUTION: MAY NOT WORK IN OLDER VERSION

Solved by: Kamesh Kotwani
'''
import math
import random

#Defining the Function for circle
def circle():
    
    #Using Random function to stimulate integers from 1 to 50
    radius = random.randint(1, 50)
    
    #Calculating Area
    area = math.pi*(radius**2)
    
    #Printing Options
    print(f"Radius is  : {radius}")
    print("Only one of them is correct, Please enter your option")
    print("Option 1 : ", round(area,4))
    print("Option 2 : ", round(area+0.8,4))
    print("Option 3 : ", round(area+1,4))
    print("Option 4 : ", round(area + 3, 4))
    
    #Asking the user to input his/her choice
    choice = int(input("Please Enter 1 or 2 or 3 or 4 : "))
    
    #Checking if the input is among the following options
    if(choice == 1 or choice == 2 or choice == 3 or choice == 4):
        
        #If choice is the correct answer printing correct
        if(choice == 1):
            print("you are right")
        else:
            print("Wrong.")
    
    #Giving conditions if the user tries to input something else
    elif(choice<0):
        choice = int(input("Please Enter 1 or 2 or 3 or 4 : "))
    else:
        choice = int(input("Please Enter 1 or 2 or 3 or 4 : "))    
    

def main():
    print("******Hello to Area Trainer******")
    while(True):
        ch = int(input(" Press 1 for Circle.\n Press 2 for Triangle.\n Press 3 for Rectangle.\n Press 4 for Square\n Press 5 to exit.\n YOUR CHOICE : "))
        if(ch == 1):
            circle()
        elif(ch ==5):
            print("Goodbye,thanks for training! Have a nice day.")
            exit()       
        else:
            print("\n__Under construction__ Please select something else \n")
            
if(__name__) == "__main__":
    main()