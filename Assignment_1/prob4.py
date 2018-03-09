'''
Assignment_1:Question_4 Reboot Academy
Stock Transaction Program

This solution is created in python 3.6.4
CAUTION: MAY NOT WORK IN OLDER VERSION

Solved by: Kamesh Kotwani

'''
print("Welcome to Stock Transction!")

#Buying the stocks!
pur0 = 2000                    # No of shares Joe purchased
price_one_share = 40.00        # Price of one share
t_pur = pur0*price_one_share   # Total amount of money paid
comm0 = t_pur*0.03              # Commision paid after first purchase

#Selling the Stocks
sell0 = 2000                        # No of shares Joe sold
price_one_share = 42.75             # price of one share
t_recieved = sell0*price_one_share  # total amount recieved
comm1 = t_recieved*0.03             # Commision paid after selling

commision = comm0+comm1             #Total money paid to broker


# Displaying information
print(f"The amount of money Joe paid for the stock is  : $ {t_pur}")
print(f"The amount of commision paid when bought stock : ${comm0}")
print(f"The amount that Joe got after selling stocks : ${t_recieved}")
print(f"The amount of money commision Joe paid when he sold the stock : ${comm1}")

