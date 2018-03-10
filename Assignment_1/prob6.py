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
if(time >= 3600):
    hours = time/3600
    
    print(f"Number of hours in {time} seconds is : {round(hours)} hours.")
if(time<3600):
    minutes = time / 60
    print(f"{time} seconds have approx : {round(minutes)} minutes.")