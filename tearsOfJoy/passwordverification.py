secret_password = "semicolon123"

for count in range(3):
    password = input("Enter Password: ")
    
    if password == secret_password:
        print("Access granted")
        break
        
else: 
    print("Incorrect password. Locked out")
