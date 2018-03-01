'''
Python Assignment 1 Reboot Academy 
Sales Price Question 1 
Solved by: Kamesh Kotwani
'''

#To input the user name 
name = input("Please Enter your name : ")
print(f"Hello {name}, Welcome to sales price!")

#To take the input from user for the amount
amount = input("Please Enter the total amount in Rupees : ")
print("Calculating amount after 20% discount.......")

#To store the discounted price into another variable
dis =float(amount)*0.80

#To print the discounted price
print(f"The Total amount you have to pay after 20% discount is : {dis} Rupees")
