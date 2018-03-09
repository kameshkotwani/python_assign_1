'''
Python Assignment 1 Reboot Academy 
Factorial of a number!

Created using Python 3.6.4 
CAUTION: MAY NOT WORK IN OLDER 

Solved by: Kamesh Kotwani
'''
print("Welcome to the Factorial of the number!")

#To take input from user for a number
num = int(input("Enter the number : "))

#To check if the user typing positvive number or not, a replacement for do while loop
while(num<0):   #To check is user input is positive or not
    num = int(input("Please enter a positive number : "))

#To store the factorial of the number
fact = 1

#Loop to calculate the Factorial
for i in range(1,num+1):
    fact *=i

#To print the factorial of the number           
print(f"Factorial of {num} is: {fact}")
