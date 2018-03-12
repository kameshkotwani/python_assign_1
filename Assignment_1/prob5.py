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
    area = (0.25 * n * (side ** 2)) / (math.tan((math.pi / n))) #Formula
    perimeter = n * n    #Perimeter
    sum = area + (perimeter ** 2)   #Sum of both with square of perimeter
    return (round(sum,4))           #returning sum 

#Main Program

def main():
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

if(__name__) == "__main__":
    main()