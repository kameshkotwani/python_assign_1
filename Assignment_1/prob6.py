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
days = time // 86400
time%=86400
hours = time//3600
time%=3600
minutes = time // 60
seconds = time%60
print(f"{time} seconds has approx: {days} days, {hours} hours, {minutes} minutes and {seconds} seconds.")
