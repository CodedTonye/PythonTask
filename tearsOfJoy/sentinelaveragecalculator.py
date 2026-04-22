total = 0
count = 0

while True:
    number = int(input("Enter integers (-1 to stop): "))
    
    if number == -1:
        break
        
    total += number
    count += 1
    
if count > 0:
    average = total / count
    print(f"Average = {average:.2f}")
else:
    print("No numbers were entered.")
