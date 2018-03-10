'''
Exercise 1 Test Score Grades Problem Statement 
Reboot Academy

This solution is created in python 3.6.4
CAUTION: MAY NOT WORK IN OLDER VERSION

Solved by: Kamesh Kotwani
'''

print("Welcome to Test Score Grade System! This System will help you find out your grade!")

#To take input from user about his test score
score =int(input("Please Enter your Test Score : "))

#To check if the score is above 90.
#No check is being is made if input is above 100 as not given in problem statement
if(score >=90):
    print("Your grade is A! Congratulations!")

#To check if score is between 80 and 89 
elif(score >=80 and score<=89):
    print("You have got a B grade! Very Good!")

#To check if score is between 70 and 79
elif(score >=70 and score<=79):
    print("You have got a C grade! Not so good....")

#To check if score is between 60 and 69
elif(score >=60 and score<=69):
    print("You have got a D grade! you need to work hard....")

#To check if score is below 60
elif(score<60):
    print("You have got an F, you are fail!")

#If input is not defined or any system error
else:
    print("SYSTEM ERROR or INPUT ERROR!! Please TRY again.")
