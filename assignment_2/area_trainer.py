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

#Making a input check function, prompts user until he/she gives required input
def input_check():
    con = True
    
    #Continiously Running the loop until user gives correct input
    while(con):
        try:
            inp = int(input("Please Enter your Choice : "))
            con = False
            return inp
        except ValueError as err:
            print(err, "Wrong Input Please input again")


#A check Function to see if user has given correct answer
def check(user_choice,ans):
    if(user_choice==ans and user_choice in range(1,5)):
        print(" \n__You are correct, +1 point__\n")
        increment()  #increment score if the choice is correct
    elif(user_choice not in range(1,5)):
        user_choice = input_check()
        #Recursively Calling check function 
        check(user_choice,ans)
    else:
        print("\n__WRONG__\n")

#Defining the Function for circle
def circle():
    #Using Random function to stimulate integers from 1 to 20
    radius = random.randint(1, 21)
    area = math.pi*(radius**2)
    #Printing Options
    print(f"Radius is  : {radius}")
    print("\nOnly one of them is correct, Please enter your option")
    print("Option 1 : ", round(area,4))
    print("Option 2 : ", round(area+4,4))
    print("Option 3 : ", round(area+6,4))
    print("Option 4 : ", round(area + 10, 4))
    ans = 1
    #Asking the user to input his/her choice
    user_choice = input_check()
    #Calling check function to see if user has input a correct option
    check(user_choice,ans)

#Defining rectangle Function
def rectangle():
    #Using Random function to stimulate integers from 1 to 20
    length = random.randint(1, 21)
    breadth = random.randint(1, 21)
    area = length*breadth
    #Printing Options
    print(f"length is :  {length}, breadth is : {breadth}")
    print("\nOnly one of them is correct, Please enter your option")
    print("Option 1 : ", round(area+6,4))
    print("Option 2 : ", round(area+4,4))
    print("Option 3 : ", round(area,4))
    print("Option 4 : ", round(area + 10, 4))
    ans = 3
    #Asking the user to input his/her choice
    user_choice = input_check()
    #Calling check function to see if user has input a correct option
    check(user_choice,ans)

def triangle():
    #Using Random function to stimulate integers from 1 to 20
    height = random.randint(1, 21)
    base = random.randint(1, 21)
    area = 0.5*base*height
    #Printing Options
    print(f"height is :  {height}, base is : {base}")
    print("\nOnly one of them is correct, Please enter your option")
    print("Option 1 : ", round(area+7,4))
    print("Option 2 : ", round(area+4,4))
    print("Option 3 : ", round(area+6,4))
    print("Option 4 : ", round(area,4))
    ans = 4
    #Asking the user to input his/her choice
    user_choice = input_check()
    #Calling check function to see if user has input a correct option
    check(user_choice,ans)


#Defined a login function 
def login(name,passkey):
   
    #Checking for any whitespace and using strip function
    name = name.strip()
    passkey = passkey.strip()
    
    if(name == "user" and passkey == "root"):
        print(f"ACCESS GRANTED! \nHello {name} ")
        pass
    else:
        print("ACCESS DENIED Try again : ")
        name = str(input("Please enter your name : "))
        passkey = str(input("Please enter your password : "))
        
        #Recursively Calling Login Function 
        login(name,passkey)


#Made an options function for simplicity of Main function
def options():
    print("Press 1 for Circle")
    print("Press 2 for Triangle")
    print("Press 3 for Rectangle")
    print("Press 4 to see your score")
    print("Press 5 to exit")


def main():
    print("******Hello to Area Trainer******") 
    #Calling LOGIN FUNCTION to GRANT ACCESS
    name = str(input("Please enter your name : "))
    passkey = str(input("Please enter your password : "))
    login(name, passkey)
    
    #Creating an infinite Loop until user inputs to exit
    while(True):
        
        #Asking user to input a choice among given options
        options()
        ch = input_check()
    
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