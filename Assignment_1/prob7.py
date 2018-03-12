'''
Python Assignment 1 Reboot Academy 
Stair Step Question

Created using Python 3.6.4 
CAUTION: MAY NOT WORK IN OLDER 

Solved by: Kamesh Kotwani
'''

#Creating First Loop for i 
for i in range(0, 5):

    #Creating another loop for j in range of i
    for j in range(i+1):
        
        #Checking if the row of i matches the coloumn of j
        if(j==i):
            
            #Printing HASH if equal
            print("#")
        else:
            #Printing space if not equal
            print(" ",end=" ")
