'''
Python Assignment 1 Reboot Academy 
Exercise Payroll Question

Created using Python 3.6.4 
CAUTION: MAY NOT WORK IN OLDER 

Question : Chris owns an auto repair shop.
Hey pays regular pay for 40 hours, he pays them 1.5 times regular
hourly rate if the working hours are more than 40.
Design a simple payroll to determine total gross pay.

Crafted by: Kamesh Kotwani
'''
def main():
    print("**__Payroll Determiner__**")
    
    #While Loop to continiously ask user to input correct datatype 
    while(True):
        try:
            #ASking user to input the total WEEKS and total WORK HOURS
            weeks = int(input("Please enter the TOTAL WORKING WEEKS : "))
            work_hours = int(input("Please enter the TOTAL WORKING in HOURS : "))
            
            #Cross checking if the input hours is valid as a week only has 168 hours
            while(work_hours > weeks*168):
                print(f"{weeks} weeks has only has {weeks*168} hours, your employee cannot work more than that.")
                work_hours = int(input("Please enter the TOTAL WORKING in HOURS : "))
            
            #Asking for HOURLY rate only if the entered working hours is valid
            hourly_pay = int(input("Please Ente the HOURLY PAYRATE of Employee : Rs."))
            break

        #Catching any exception ERROR.
        except:
            print("INPUT ERROR. Please input again : ")
    
    
    #If working hours is under 40 hours displaying normal payrate
    if(work_hours <= 40):
        
        #Calculating Regular Pay for hours
        regular_pay = work_hours*hourly_pay
        print(f"Total Pay is  : Rs. {regular_pay}")
    
    #If the working hours is more than 40 calculating ovetime wages
    elif(work_hours > 40):
        regular_pay = 40*hourly_pay
        
        #Calculating working hours more than 40
        overtime_hours = work_hours - 40
        
        #Gross Pay will be regular pay of 40 HOURS then 1.5 times the regular hourly rate
        gross_pay = (regular_pay)+overtime_hours*hourly_pay*1.5
        print(f"Gross pay is : Rs. {gross_pay} inclusive of overtime wages.")
    else:
        print("SOMETHING WENT WRONG.")
    
    #ASking user if s/he wants to continue or not
    print("WANT TO continue? PRESS Y")
    print("To exit press anything else.")
    while(True):
        try:
            ch = str(input("YOUR CHOICE : "))
            break
        except:
            print("Please ENTER YOUR CHOICE again.")
        
    if(ch == 'y' or ch == 'Y'):
        main()
    else:
        print("bye.")
        exit()

if(__name__ == "__main__"):
    main()