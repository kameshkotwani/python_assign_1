'''
Assignment 3: 
Password Checker and Generator
Reboot Academy

This solution is created in python 3.6.4
CAUTION: MAY NOT WORK IN OLDER VERSION

Crafted by: Kamesh Kotwani
'''
import string

POINTS = 0

#Making a input check function, prompts user until he/she gives required input
def input_check():
    con = True
    
    #Continiously Running the loop until user gives correct input
    while(con):
        try:
            inp =int(input("YOUR Choice : "))
            con = False
            return inp
        except:
            print("Wrong Input Please input again")
        

#Defining Options Function 
def options():
    print("1. to Check strength of your password")
    print("2. to create a strong password for you")
    print("3. to quit from program")


#A function to check the strength of the password
def passkey_checker(user_passkey):
    
    #Creating a set of allowed symbols
    allowed_symbols = set("!#$%^&*()_-+=")
    
    global POINTS
    POINTS = user_passkey.__len__()
    
    #Checking if the user input is between 8-20 characters
    if(POINTS > 8 and POINTS < 20):
        POINTS+=5
    else:
        POINTS -= 5
    
    #Using any function to check if at least one characer is lowercase or not
    con  = any(c.islower() for c in user_passkey)
    
    #If it contains increase the POINTS
    if(con):
        POINTS += 5
    #If it does not contain the decrease POINTS
    else:
        POINTS -= 5

    #Checking if all the characters are lower    
    if(user_passkey.islower()):
        POINTS -= 5

    #Using any function to check if at least one characer is UPPERCASE or not
    con  = any(c.isupper() for c in user_passkey)
    
    #If it contains increase the POINTS
    if(con):
        POINTS += 5
    
    #If it does not contain the decrease POINTS
    else:
        POINTS -= 5
    
    #Checking if all the characters are UPPER    
    if(user_passkey.isupper()):
        POINTS -= 5

    #Using any function to check if at least one characer is DIGIT or not
    con  = any(c.isdigit() for c in user_passkey)
    
    #If it contains increase the POINTS
    if(con):
        POINTS += 5
        
    #If it does not contain the decrease POINTS
    else: 
        POINTS -= 5
    
    #Checking if all the characters are DIGITS    
    if(user_passkey.isdigit()):
        POINTS -= 5
    
    con = any((c in allowed_symbols) for c in user_passkey)
    if(con):
        POINTS += 5
    else:
        print(f"YOU SHOULD USE THESE SYMBOLS AS WELL : {allowed_symbols}")
        POINTS -= 5
        
    #Checking for any consicutive input by user
    qwerty="qwertyuiopasdfghjklzxcvbnm"
    for i in range(0,user_passkey.__len__()-2):
        t = user_passkey[i:i+3]
        if (t.lower() in qwerty):
            POINTS -= 5
    
    #Returning back the POINTS to main function to check the score 
    return POINTS        

#Main function of the program
def main():
    global POINTS
    while(True):
        options()
        #Catching any exception in input using input_check function
        ch =input_check()
        
        if(ch == 1):
            user_passkey = str(input("Enter your password : "))
            score = passkey_checker(user_passkey)
            if(score <= 15):
                print("Password too weak")
            else:
                print(f"GREAT PASSWORD : YOU CAN USE IT {user_passkey}")
                
        elif(ch == 2):
            print("__UNDER CONSTRUCTION__")
        
        elif(ch == 3):
            print("bye.")
            exit()
        else:
            print("ERROR. INPUT AGAIN")


if(__name__) == "__main__":
    main()

