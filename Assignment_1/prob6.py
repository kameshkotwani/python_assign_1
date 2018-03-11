'''
Assignment_1:Question_6 Reboot Academy
Time Calculator

This solution is created in python 3.6.4
CAUTION: MAY NOT WORK IN OLDER VERSION

Solved by: Kamesh Kotwani
'''

print("****Welcome to Time Calculator****")
time = int(input("Please Enter number of seconds : "))
while(time < 0):
    time = int(input("Please Enter number of seconds : "))
minutes = time / 60
hours = time/3600
days = time / 86400
if(time >= 3600):
    print(f"Number of hours in {time} seconds is approx: {round(hours)} hours.")
if(time<3600):
    print(f"{time} seconds have approx : {round(minutes)} minutes.")
if(time >= 86400):
    print("some useful information!")
    print(f"{time} seconds has approx: {round(days)} days, approx:  {round(hours)} hours, approx : {round(minutes)} minutes.")