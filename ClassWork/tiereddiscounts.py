
"""DESIGN A PROGRAM THAT APPLIES TIERED DISCOUNTS BASED ON A CUSTOMER'S TOTAL SPENDING IN A STORE. THE GREATER THE PURCHASE AMOUNT, THE HIGHER THE DISCOUNT OFFERED.

PSEUDOCODE:

Step 1: Ask for user_input
Step 2: 
"""

purchase_amount = float(input('Enter purchase amount: '))

discount = 0
discounted_price = 0

if (purchase_amount >= 1000 and purchase_amount <= 10000):
    discount = 5 / 100
    discounted_rate = purchase_amount * discount
    
    discounted_price = purchase_amount -  discounted_rate
    
    print(f"The Discount rate is {discounted_rate:.2f}")
    
    print(f"The Discounted Price is {discounted_price:.2f}")
    
elif (purchase_amount > 10000 and purchase_amount <= 50000):
    discount = 10 / 100
    discounted_rate = purchase_amount * discount
    
    discounted_price = purchase_amount -  discounted_rate
    
    print(f"The Discount rate is {discounted_rate:.2f}")
    
    print(f"The Discounted Price is {discounted_price:.2f}")      
    
elif (purchase_amount > 50000):
    discount = 20 / 100
    discounted_rate = purchase_amount * discount
    
    discounted_price = purchase_amount -  discounted_rate
    
    print(f"The Discount rate is {discounted_rate:.2f}")
    
    print(f"The Discounted Price is {discounted_price:.2f}")   
    
else:
    print("Invalid input")
    
