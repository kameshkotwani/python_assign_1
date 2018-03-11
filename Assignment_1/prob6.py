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
    time = int(input("Please Enter number of seconds [time cannot be negative] : "))

#To count number of days 
days = time // 86400

#To seperate the remaining hours
time%=86400             

#To count number of hours
hours = time//3600      

#To seperate out remaining minutes
time%=3600

#To count number of minutes
minutes = time // 60

#Finally to seperate remaining seconds
seconds = time%60

#Printing values
print(f"{time} seconds has approx: {days} days, {hours} hours, {minutes} minutes and {seconds} seconds.")
