'''
Assignment Question: Reboot Academy
To print the table of given number

This solution is created in python 3.6.4
CAUTION: MAY NOT WORK IN OLDER VERSION

Solved by: Kamesh Kotwani
'''

#To ask the user a number to print the table of
n = int(input("Please enter a number to print the table of : "))

#To ask user upto how many terms he or she wants the table to be printed
d = int(input("Enter upto what term you want the table to be printed : "))

#Loop to print the table
for i in range(1,d+1):
    print(f"{n} X {i} : {n*i}")


