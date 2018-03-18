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
            inp =str(input("Please Enter your Choice : "))
            con = False
            return inp
        except:
            print("Wrong Input Please input again")
        

#Defining Options Function 
def options():
    print("Press a to Check strength of your password")
    print("Press b to create a strong password for you")
    print("Press c to quit from program")


#A function to check the strength of the password
def passkey_checker(user_passkey):
    global POINTS
    POINTS = user_passkey.__len__()
    if(POINTS < 8 or POINTS > 20):
        user_passkey = str(input("Please Enter your password again 8-20 characters : "))
        passkey_checker(user_passkey)
    print("initial POINTS is now",POINTS)
    for c in user_passkey:
        if(c.islower()):
            POINTS += 5
            print("after islower POINTS is now",POINTS)
            break
    for c in user_passkey:
        if(c.isupper()):
            POINTS += 5
            print("after isupper POINTS is now",POINTS)
            break
    for c in user_passkey:
        if(c.isdigit()):
            POINTS += 5
            print("after is digit POINTS is now",POINTS)
            break


#Main function of the program
def main():
    global POINTS
    while(True):
        options()
        ch = (input("YOUR CHOICE : "))
        
        if(ch == chr(97)):
            user_passkey = str(input("Enter your password : "))
            passkey_checker(user_passkey)

        elif(ch == chr(98)):
            print("__UNDER CONSTRUCTION__")
        
        elif(ch == chr(99)):
            print("bye.")
            exit()
        else:
            print("ERROR.")


if(__name__) == "__main__":
    main()

    