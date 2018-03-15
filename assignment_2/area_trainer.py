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

#A check Function to see if user has given correct answer
def check(choice):
    if(choice == 1):
        print(" \n__You are correct, +1 point__\n")
    else:
        print("\n__WRONG__\n")

#Defining an options area
def options(area):
    print("Only one of them is correct, Please enter your option")
    print("Option 1 : ", round(area,4))
    print("Option 2 : ", round(area+4,4))
    print("Option 3 : ", round(area+6,4))
    print("Option 4 : ", round(area + 10, 4))

#Defining the Function for circle
def circle():
    #Using Random function to stimulate integers from 1 to 50
    radius = random.randint(1, 20)
    area = math.pi*(radius**2)
    #Printing Options
    print(f"Radius is  : {radius}")
    options(area)
    #Asking the user to input his/her choice
    choice = int(input("Please Enter 1 or 2 or 3 or 4 : \nYOUR CHOICE : "))
    #Calling check function to see if user has input a correct option
    check(choice)

#Defining rectangle Function
def rectangle():
    #Using Random function to stimulate integers from 1 to 50
    length = random.randint(1, 20)
    breadth = random.randint(1, 20)
    area = length*breadth
    #Printing Options
    print(f"length is :  {length}, breadth is : {breadth}")
    options(area)
    #Asking the user to input his/her choice
    choice = int(input("Please Enter 1 or 2 or 3 or 4 : "))
    #Calling check function to see if user has input a correct option
    check(choice)

def triangle():
    #Using Random function to stimulate integers from 1 to 50
    height = random.randint(1, 20)
    base = random.randint(1, 20)
    area = 0.5*base*height
    #Printing Options
    print(f"height is :  {height}, base is : {base}")
    options(area)
    #Asking the user to input his/her choice
    choice = int(input("Please Enter 1 or 2 or 3 or 4 : "))
    #Calling check function to see if user has input a correct option
    check(choice)


def main():
    print("******Hello to Area Trainer******")   
    #Creating an infinite Loop until user inputs to exit
    while(True):
        
        #Asking user to input a choice among given options
        ch = int(input(" Press 1 for Circle.\n Press 2 for Triangle.\n Press 3 for Rectangle.\n Press 4 to see your score.\n Press 5 to exit. \n YOUR CHOICE : "))
        
        #Calling circle function if user inputs 1
        if(ch == 1):
            circle()

        #Calling Triangle Function if user inputs 2
        elif(ch == 2):
            triangle()

        #Calling Rectangle Function if user inputs 3
        elif(ch ==3):
            rectangle()            
        
        elif(ch == 4):
            print(f"Your current score is : __Under Construction__ ")
        
        #Calling exit function to exit from program
        elif(ch ==5):
            print("Goodbye,thanks for training! Have a nice day.")
            print(f"Your Final score is : __Under Construction__ ")
            exit()       
            
        #If user inputs something else
        else:
            print("__Please select something else__ \n")
            


#Calling main function
if(__name__) == "__main__":
    main()