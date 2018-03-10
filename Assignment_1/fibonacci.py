'''
Fibonacci Series : Reboot Academy

This solution is created in python 3.6.4
CAUTION: MAY NOT WORK IN OLDER VERSION

Solved by: Kamesh Kotwani
'''
print("****Welcome to Fibonacci Series****")
n = int(input("Please enter until how many terms you want to print : "))
while(n<0):
    n = int(input("Please enter until how many terms you want to print : "))

#First two terms of Fibonnaci Series
t_one= 0        
t_two = 1

#The fibonacci Series Loop
for i in range(1,n+1):
    print(f"{t_one} ",end=" ")      #Printing the terms
    next_term = t_one+t_two
    t_one = t_two
    t_two = next_term
    