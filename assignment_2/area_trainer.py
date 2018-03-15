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

SCORE =0   #Global Score Variable

#Function to keep track of score
def increment():
    global SCORE
    SCORE+=1

#A check Function to see if user has given correct answer
def check(choice):
    if(choice == 1 or choice ==2 or choice ==3 or choice ==4):
        if(choice == 1):
            print(" \n__You are correct, +1 point__\n")
            increment()  #increment score if the choice is correct
        else:
            print("\n__WRONG__\n")
    else:
        choice = int(input("Please Enter 1 or 2 or 3 or 4 \nYOUR CHOICE : "))
        
        #Recursively Calling check function 
        check(choice)

#Defining Options function to print the options
def options(area):
    print("\nOnly one of them is correct, Please enter your option")
    print("Option 1 : ", round(area,4))
    print("Option 2 : ", round(area+4,4))
    print("Option 3 : ", round(area+6,4))
    print("Option 4 : ", round(area + 10, 4))

#Defining the Function for circle
def circle():
    #Using Random function to stimulate integers from 1 to 20
    radius = random.randint(1, 21)
    area = math.pi*(radius**2)
    #Printing Options
    print(f"Radius is  : {radius}")
    options(area)
    #Asking the user to input his/her choice
    choice = int(input("Please Enter 1 or 2 or 3 or 4 \nYOUR CHOICE : "))
    #Calling check function to see if user has input a correct option
    check(choice)

#Defining rectangle Function
def rectangle():
    #Using Random function to stimulate integers from 1 to 20
    length = random.randint(1, 21)
    breadth = random.randint(1, 21)
    area = length*breadth
    #Printing Options
    print(f"length is :  {length}, breadth is : {breadth}")
    options(area)
    #Asking the user to input his/her choice
    choice = int(input("Please Enter 1 or 2 or 3 or 4 \nYOUR CHOICE : "))
    #Calling check function to see if user has input a correct option
    check(choice)

def triangle():
    #Using Random function to stimulate integers from 1 to 20
    height = random.randint(1, 21)
    base = random.randint(1, 21)
    area = 0.5*base*height
    #Printing Options
    print(f"height is :  {height}, base is : {base}")
    options(area)
    #Asking the user to input his/her choice
    choice = int(input("Please Enter 1 or 2 or 3 or 4 \nYOUR CHOICE : "))
    #Calling check function to see if user has input a correct option
    check(choice)



#Defined a login function 
def login(name,passkey):
   
    if(name == "kamesh" and passkey == "kamesh@123"):
        print(f"ACCESS GRANTED! \nHello {name} ")
        pass
    else:
        print("ACCESS DENIED Try again : ")
        name = str(input("Please enter your name : "))
        passkey = str(input("Please enter your password : "))
        login(name,passkey)

def main():
    print("******Hello to Area Trainer******") 
    #Calling LOGIN FUNCTION to GRANT ACCESS
    name = str(input("Please enter your name : "))
    passkey = str(input("Please enter your password : "))
    login(name, passkey)
    
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
            print(f"{name}, your current score is : {SCORE} ")
        
        #Calling exit function to exit from program
        elif(ch ==5):
            print("\nGoodbye,thanks for training! Have a nice day.")
            print(f"{name}, your Final score is : {SCORE} \n")
            exit()       
            
        #If user inputs something else
        else:
            print("__Please select something else__ \n")


#Calling main function
if(__name__) == "__main__":
    main()