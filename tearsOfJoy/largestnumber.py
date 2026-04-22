largest = None

while True:
    user_input = input("Enter integers (Enter done to stop): ")
    
    if user_input.lower() == 'done':
        break
        
    number = int(user_input)
    
    if largest is None or number > largest:
        largest = number
        
print(f"The largest is {largest}")
