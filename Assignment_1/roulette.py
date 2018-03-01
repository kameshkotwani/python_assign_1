'''
Exercise 3 Roulette Wheel Colors Problem Statement 
Reboot Academy

This solution is created in python 3.6.4
CAUTION: MAY NOT WORK IN OLDER VERSION

Solved by: Kamesh Kotwani

'''
print("Welcome to Roulette Wheel!")

#To ask user input
n = int(input("Enter a number from 0 through 36  : "))
while(n<0 or n>36):
    n = int(input("ERROR!!!! Please enter a number from 0 through 36 : "))

#To check if n is 0
if(n==0):
    print("You have chosen GREEN!")

#To check if n i between 1 and 10
if(n>=1 and n<=10):
    if(n%2==0):
        print("You have Chosen BLACK!!")
    else:
        print("You have chosen RED!!")

#To check if n i between 11 and 18
if(n>=11 and n<=18):
    if(n%2==0):
        print("You have chosen RED!!")
    else:
        print("You have chosen BLACK!!")

#To check if n i between 9 and 28
if(n>=19 and n<=28):
    if(n%2==0):
        print("You have chosen BLACK!!")
    else:
        print("You have chosen RED!!")

#To check if n i between 29 and 36
if(n>=29 and n<=36):
    if(n%2==0):
        print("You have chosen RED!!")
    else:
        print("You have chosen BLACK!!")



