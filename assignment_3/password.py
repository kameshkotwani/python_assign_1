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

#Increment fucntion to plus the score
def increment():
    global POINTS
    POINTS += 1

#decrement fucntion to deduct the score
def decrement():
    global POINTS
    POINTS -= 1

#Making a input check function, prompts user until he/she gives required input
def input_check():
    con = True
    
    #Continiously Running the loop until user gives correct input
    while(con):
        try:
            inp =str(input("Please Enter your Choice : "))
            con = False
            return inp
        except :
            print("Wrong Input Please input again")
        


def options():
    print("Press a to Check strength of your password")
    print("Press b to create a strong password for you")
    print("Press c to quit from program")


#A function to check the strength of the password
def passkey_checker(user_passkey):
    global POINTS
    POINTS = user_passkey.__len__()

#Main function of the program
def main():
    while(True):
        options()
        ch = (input("YOUR CHOICE : "))
        
        if(ch == chr(97)):
            user_passkey = str(input("Enter your password : "))
            passkey_checker(user_passkey)
            print(user_passkey)

        elif(ch == chr(99)):
            print("bye.")
            exit()


if(__name__) == "__main__":
    main()

    