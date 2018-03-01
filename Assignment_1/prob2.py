'''
Assignment_1:Question_2 Reboot Academy
To Ask the User about the price of total food and display the taxes applied
This solution is created in python 3.6.4
CAUTION: MAY NOT WORK IN OLDER VERSION

Solved by: Kamesh Kotwani

'''
#To input the name and the total amount paid
name = input ("Please Enter your name : ")
t_amount  = input(f"Enter the total amount you have paid, {name} : Rs. ")

#To calculate the taxes
tip = float(t_amount)*0.18
s_tax = float(t_amount)*0.07
s_tax=round(s_tax,3)

#To print all the prices
print(f"The 18% tip you have paid      : Rs. {tip}")
print(f"The 7% sales tax you have paid : Rs. {s_tax}")
print(f"The total amount you have paid : Rs. {t_amount}")

