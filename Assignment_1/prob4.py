'''
Assignment_1:Question_4 Reboot Academy
Stock Transaction Program

This solution is created in python 3.6.4
CAUTION: MAY NOT WORK IN OLDER VERSION

Solved by: Kamesh Kotwani
'''
print("******Welcome to Stock Transction*****")

shares = 2000                    # No of shares Joe purchased
price_one_share = 40.00        # Price of one share

#Buying the stocks!
t_pur = shares*price_one_share   # Total amount of money paid
comm0 = t_pur*0.03              # Commision paid after first purchase
left_b = t_pur+comm0              #Total money he is left with    

#After two weeks
price_one_share = 42.75         #Price of one share updated

#Selling the Stocks
t_recieved = shares*price_one_share  # total amount recieved
comm1 = t_recieved*0.03             # Commision paid after selling
left_s = t_recieved-(comm1+comm0)    #Total money he is left with
profit = left_s-t_pur               #Total Profit made

# Displaying information
print(f"The amount of money Joe paid for the stock is  : $ {t_pur}")
print(f"The amount of commision paid when bought stock : $ {comm0}")
print(f"The amount that Joe got after selling stocks : $ {t_recieved}")
print(f"The amount of money commision Joe paid when he sold the stock : $ {comm1}")
print(f"The amount of money Joe has left is : $ {left_s}")
if(profit>0):
    print(f"Joe has made a profit of :$ {profit}")
else:
    print("Joe is in loss.")

