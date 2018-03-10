'''
Python Assignment 1 : Reboot Academy 
To print the prime numbers in given range 

Created using Python 3.6.4 
CAUTION: MAY NOT WORK IN OLDER 

Solved by: Kamesh Kotwani
'''
print("***Welcome to prime series!***")
n = int(input("Please enter upto which number primes should be displayed : "))
#Making sure if the user has entered a positive number or not
while(n<0):
    n = int(input("Please enter upto which number primes should be displayed : "))


print(f"**List of prime numbers from 2 to {n}***")
for i in range(2,n + 1):              #Counting from 2 through number
   if(i > 1):
       for j in range(2,i):           #Another loop to find out divisibility
           if (i%j== 0):              #If divisible then breaking out of loop  
               break
       else:                            #If not, then printing the number
           print(f"{i}",end=" ")
