'''
Assignment_1:Question_3 Reboot Academy
Cookies Program

This solution is created in python 3.6.4
CAUTION: MAY NOT WORK IN OLDER VERSION

Solved by: Kamesh Kotwani
'''

print("Welcome to Ingredients Counter!!")

#Given quantity for 48 cookies
cup_s = 1.5/48
cup_b = 1/48
cup_f = 2.75/48

#To ask the user for number of cookies required
num = int(input("Please enter the number of Cookies required to make : "))
print("Calculating the ingerdients required.........")

#Calculating the ingredients needed
cups_r = cup_s*num
cupb_r = cup_b*num
cupf_r = cup_f*num

#Displaying the number of cups needed for cookies entered by user
print(f"You need {cups_r} of Sugar")
print(f"You need {cupb_r} of Butter")
print(f"You need {cupf_r} of Flour to make {num} cookies")

