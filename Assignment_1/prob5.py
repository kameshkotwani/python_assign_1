'''
Assignment_1:Question_5 Reboot Academy
Polygon Problem Statement

This solution is created in python 3.6.4
CAUTION: MAY NOT WORK IN OLDER VERSION

Solved by: Kamesh Kotwani
'''
import math

#Defining Function
def polysum(side, n):
    side = s
    n = no
    area = (0.25 * no * (s ** 2)) / (math.tan((math.pi / n))) #Formula
    perimeter = no * no     #Perimeter
    sum = area + (perimeter ** 2)   #Sum of both with square of perimeter
    return (round(sum,4))           #returning sum 

#Main Program
print("******Welcome to Polygon Surface Information****")

#To take length and number of polygon
no = int(input("Please enter number of sides : "))
s = int(input("Please enter the length of side : "))
while(s < 0 or no < 0):
    print("You are not allowed to input negative value of either of them --> ")
    s = int(input("Please enter the length of side : "))
    no = int(input("Please enter number of sides : "))

#returning value from polysum and storing in variable
total_sum = float(polysum(s, no))

#Printing value of sum
print(f"Total sum of Area and Perimeter is : {total_sum}")

