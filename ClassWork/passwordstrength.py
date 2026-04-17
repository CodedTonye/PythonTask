"""
PSEUDOCODE

Step 1: Prompt a user to enter a password
step 2: Set length of password ***
Step 3: Categorize the length: less than 8 for very weak
Step 4: Categorize the length: 8 for weak
Step 5: Categorize the length: between 8 & 16 for strong
Step 6: Categorize the length: 16 and above for very strong
Step 7: print()



"""

password = input('Enter Password: ')

password_length = len(password)

if password_length < 8:
    print("Password is very weak")

elif password_length == 8:
    print("Password is weak")   
    
elif password_length > 8 and password_length <= 16:
    print("Password is strong") 
    
else: 
    print("Password is very strong") 
